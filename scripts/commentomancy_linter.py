
#!/usr/bin/env python3
"""Commentomancy Generator / Linter (analyze & fix)

Purpose:
  - Read CodeCraft ritual files (.ccraft)
  - Load canon rules from *either* canon.lock.yaml (preferred) or schools.canonical.yaml (fallback)
  - Detect missing constitutional commentomancy for school invocations
  - Optionally auto-insert required comment lines above offending invocations

Exit codes:
  0 = compliant (or fixed successfully with --fix)
  1 = violations found (in analyze mode) or unrecoverable error
  2 = usage error

Usage:
  python tools/commentomancy_linter.py analyze path/to/ritual.ccraft [--canon canon.lock.yaml] [--schools schools.canonical.yaml] [--strict]
  python tools/commentomancy_linter.py fix     path/to/ritual.ccraft [--canon canon.lock.yaml] [--schools schools.canonical.yaml] [--strict]

Notes:
  - Idempotent: won't duplicate comments if already present.
  - Looks back up to N preceding non-blank lines to find required comment.
  - --strict makes advisory comments required if the canon marks them as such.
"""
import argparse
import re
import sys
import yaml
from pathlib import Path

# -------------------------------
# Canon loaders
# -------------------------------

def load_yaml(path: Path):
    try:
        with path.open('r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return None

def _canon_from_lock(lock):
    """
    Expected shapes supported:
    1) Proposed normalized lock:
       lock['schools']['by_id'], lock['schools']['by_token']
    2) Legacy/loose forms: we attempt to recover token list & names, but prefer #1.
    """
    by_id = {}
    by_token = {}
    rules = {}

    schools = lock.get('schools')
    if isinstance(schools, dict) and 'by_id' in schools and 'by_token' in schools:
        by_id = {int(k): v for k, v in schools['by_id'].items()}
        by_token = {str(tk): int(v) for tk, v in schools['by_token'].items()}
        # Optional rules per school id
        rules = lock.get('rules', {})
        return by_id, by_token, rules

    # Fallback: try to infer from a flat schools dict (legacy/borked lock files)
    # We will pull grammar tokens from manifest->token_count only as a hint,
    # but require schools.canonical.yaml for exact mapping if this fails.
    return None, None, {}

def _canon_from_schools_yaml(sch):
    by_id = {}
    by_token = {}
    rules = {}

    schools = sch.get('schools', {})
    for sid, rec in schools.items():
        sid_i = int(sid)
        by_id[sid_i] = {
            'name': rec.get('name'),
            'emoji': rec.get('emoji', ''),
            'category': rec.get('category', ''),
            'file': rec.get('file', ''),
            'operations': rec.get('operations', []),
            'constraints': rec.get('constraints', []),
        }

    mapping = sch.get('token_to_school_mapping', {})
    # Build name->id for quick lookup
    name_to_id = {rec['name']: sid for sid, rec in by_id.items()}
    for token, school_name in mapping.items():
        sid = name_to_id.get(school_name)
        if not sid:
            raise SystemExit(f"Token '{token}' maps to unknown school '{school_name}' in schools.canonical.yaml")
        by_token[token] = int(sid)

    # Validate invariant 21 tokens -> 19 unique schools
    if len(set(by_token.values())) != 19:
        raise SystemExit("Invariant breach: unique(token_to_school_mapping.values()) != 19")

    # Example rule bootstrap (can be extended in canon.lock.yaml later)
    # For now we encode minimal default guard requirements per *token* (school alias)
    # You can move this into canon.lock.yaml under 'rules' later.
    default_rules = {
        'thaumaturgy': {'required': ['guardrail']},    # requires //!?
        'apotheosis':  {'required': ['prereq']},       # requires //!
        'mythogenesis':{'required': ['heart']},        # requires //<3
        # Safe defaults for others (no mandatory comments)
    }
    return by_id, by_token, default_rules

def load_canon(canon_lock_path: Path = None, schools_yaml_path: Path = None):
    """
    Load canon from lock file when possible; otherwise from schools.canonical.yaml.
    Returns: (by_id: dict[int, rec], by_token: dict[str, int], rules: dict)
    """
    # 1) Try lock file
    if canon_lock_path and canon_lock_path.exists():
        lock = load_yaml(canon_lock_path)
        if lock:
            by_id, by_token, rules = _canon_from_lock(lock)
            if by_id and by_token:
                return by_id, by_token, rules

    # 2) Fallback to canonical schools file
    if schools_yaml_path and schools_yaml_path.exists():
        return _canon_from_schools_yaml(load_yaml(schools_yaml_path))

    raise SystemExit("No usable canon found. Provide --canon canon.lock.yaml and/or --schools schools.canonical.yaml")

# -------------------------------
# Ritual parsing
# -------------------------------

INVOC_RE = re.compile(r"""
    ^[ 	]*::                # directive start
    (?P<school>[a-zA-Z_]+)   # school token (e.g., thaumaturgy, apotheosis)
    (?:[^\S
]*[\w\W]*?)?  # optional emoji/suffix before colon
    :                        # colon
""", re.VERBOSE)

def find_invocations(lines, valid_tokens):
    """
    Yields (idx, token) for each line that looks like a ::school: invocation.
    valid_tokens: set[str] tokens from canon
    """
    for i, line in enumerate(lines):
        m = INVOC_RE.match(line)
        if not m:
            continue
        token = m.group('school').lower()
        if token in valid_tokens:
            yield i, token

# -------------------------------
# Commentomancy detection & insertion
# -------------------------------

RE_GUARDRAIL = re.compile(r'^[ 	]*//!\?[ 	].*', re.IGNORECASE)
RE_PREREQ    = re.compile(r'^[ 	]*//![ 	].*', re.IGNORECASE)
RE_HEART     = re.compile(r'^[ 	]*//<3[ 	].*', re.IGNORECASE)

def has_required_comment(prev_lines, kind):
    """
    prev_lines: a list of preceding non-blank lines (nearest first)
    kind: 'guardrail' | 'prereq' | 'heart'
    """
    regex = {'guardrail': RE_GUARDRAIL, 'prereq': RE_PREREQ, 'heart': RE_HEART}.get(kind)
    if not regex:
        return True
    for ln in prev_lines:
        if regex.match(ln):
            return True
    return False

def build_comment(token, school_id, kind, tier=None):
    templates = {
        'guardrail': "//!? GUARDRAIL: Invocation of '{token}' (Tier {tier}) requires Architect approval.",
        'prereq':    "//! PREREQ: '{token}' requires documented preconditions satisfied.",
        'heart':     "//<3 HEART: '{token}' invocation annotated as intention/care context.",
    }
    t = templates.get(kind, "// NOTE: constitutional annotation inserted by Commentomancy Generator.")
    msg = t.format(token=token, tier=tier or 'N/A')
    return msg

def nearest_nonblank_above(lines, idx, lookback=3):
    """
    Return up to `lookback` non-blank lines ABOVE idx (excluding idx).
    Ordered nearest first.
    """
    prev = []
    j = idx - 1
    while j >= 0 and len(prev) < lookback:
        if lines[j].strip() != "":
            prev.append(lines[j].rstrip("\n"))
        j -= 1
    return prev

# -------------------------------
# Linter core
# -------------------------------

def analyze_ritual(ritual_path: Path, by_id, by_token, rules, strict=False):
    text = ritual_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    valid_tokens = set(by_token.keys())
    violations = []

    for idx, token in find_invocations(lines, valid_tokens):
        # Determine rule set for this token (by school)
        rule_spec = rules.get(token, {})
        required = list(rule_spec.get('required', []))

        # If strict, we may treat advisory as required too (optional extension)
        if strict:
            adv = rule_spec.get('advisory', [])
            for a in adv:
                if a not in required:
                    required.append(a)

        if not required:
            continue  # nothing required for this token

        prev_lines = nearest_nonblank_above(lines, idx, lookback=3)
        missing = []
        for kind in required:
            if not has_required_comment(prev_lines, kind):
                missing.append(kind)

        if missing:
            violations.append({
                'line': idx + 1,
                'token': token,
                'school_id': by_token[token],
                'missing': missing,
            })

    return violations

def fix_ritual(ritual_path: Path, violations, by_id, by_token, rules):
    lines = ritual_path.read_text(encoding='utf-8').splitlines()
    # Insert in reverse line order so indices stay valid
    for v in sorted(violations, key=lambda x: x['line'], reverse=True):
        idx0 = v['line'] - 1
        token = v['token']
        school_id = v['school_id']
        tier = None
        # If your lock file eventually carries safety tiers, populate from there:
        # e.g., tier = lock['schools']['by_id'][school_id]['spec'].get('safety_tier')
        for kind in v['missing']:
            comment = build_comment(token, school_id, kind, tier=tier)
            # Avoid duplicate insertion if same comment already at that exact spot
            if idx0-1 >= 0 and comment.strip() == lines[idx0-1].strip():
                continue
            lines.insert(idx0, comment)

    ritual_path.write_text("\n".join(lines) + "\n", encoding='utf-8')

# -------------------------------
# CLI
# -------------------------------

def main():
    ap = argparse.ArgumentParser(description="Commentomancy Generator / Linter")
    ap.add_argument('mode', choices=['analyze', 'fix'], help="Run in analyze or fix mode")
    ap.add_argument('ritual', help="Path to .ccraft ritual file")
    ap.add_argument('--canon', help="Path to canon.lock.yaml")
    ap.add_argument('--schools', help="Path to schools.canonical.yaml")
    ap.add_argument('--strict', action='store_true', help="Treat advisory comments as required")
    args = ap.parse_args()

    ritual_path = Path(args.ritual)
    if not ritual_path.exists():
        print(f"ERROR: ritual file not found: {ritual_path}", file=sys.stderr)
        return 2

    canon_lock_path = Path(args.canon) if args.canon else None
    schools_yaml_path = Path(args.schools) if args.schools else None

    try:
        by_id, by_token, rules = load_canon(canon_lock_path, schools_yaml_path)
    except SystemExit as e:
        print(str(e), file=sys.stderr)
        return 1

    violations = analyze_ritual(ritual_path, by_id, by_token, rules, strict=args.strict)

    if args.mode == 'analyze':
        if not violations:
            print("✅ Commentomancy: ritual is constitutionally compliant.")
            return 0
        print(f"❌ Commentomancy: {len(violations)} missing annotation(s) found:")
        for v in violations:
            print(f"  Line {v['line']}: ::{v['token']}: missing {', '.join(v['missing'])}")
        return 1

    # fix mode
    if not violations:
        print("✅ Commentomancy: nothing to fix.")
        return 0
    fix_ritual(ritual_path, violations, by_id, by_token, rules)
    print(f"🛠️ Commentomancy: inserted {sum(len(v['missing']) for v in violations)} annotation(s).")
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
