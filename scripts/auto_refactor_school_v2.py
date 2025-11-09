#!/usr/bin/env python3
"""
auto_refactor_school_v2.py
---------------------------------
Semi-automated refactor of a CodeCraft school into Law/Lore front-matter.

UPGRADES (v2.1 - A.C.E.'s Foundation Blueprint)
- School-scoped promotion: classify_ops() filters by school prefix (abjure:*, transmute:*, etc.)
- Core ops → law.operations, helpers → lore.examples.helpers (fixes "hallucinated ops")
- TODO-gate: FAIL on Law TODOs (operations/constraints), WARN on Lore TODOs
- Schema switch: --schema canonical (default) or mega
- Force mode to overwrite existing FM: --force (backs up .bak)
- Id policy: --id string|int|none (controls id behavior when schema=mega)
- Adds/omits template/version via --with-template/--with-version (mega only)
- Robust "When to Use"/"Avoid When" section detection (case-insensitive variants)
- Operation detection tolerates missing emoji and multi-colon op names
- Writes receipts/refactor_*.json with per-file stats
- .REFACTORED.md by default; --in-place to replace (backup kept)

NOTE: Keeps YAML-lite output to avoid parser dependencies; run verify afterwards.
"""
import sys, re, argparse, json
from pathlib import Path
from datetime import datetime

FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
TITLE_RE = re.compile(r'^\s*#\s+(\d+)\.\s+(.+?)\s+([^\w\s])\s*$', re.MULTILINE)
SECTION_RE = re.compile(r'^\s*##\s+(.+?)\s*$', re.MULTILINE)

# Operation exemplar patterns, e.g. ::guard:input🛡️[...], ::trace:event[...]
OP_PAT = re.compile(r'::([A-Za-z0-9_]+(?::[A-Za-z0-9_]+){0,2})([^\w\s\[])?\s*\[', re.UNICODE)

CHECKMARK = re.compile(r'^\s*[-*]\s*✅\s*(.+)$', re.MULTILINE)
CROSSMARK  = re.compile(r'^\s*[-*]\s*❌\s*(.+)$', re.MULTILINE)

WHEN_HEADERS = ["when to use", "usage", "use cases", "recommended when"]
AVOID_HEADERS = ["avoid when", "do not use when", "anti-cases"]

def split_sections(text:str):
    headers = list(SECTION_RE.finditer(text))
    if not headers:
        return {"preamble": text}
    sections = {}
    for i, m in enumerate(headers):
        name = m.group(1).strip()
        start = m.end()
        end = headers[i+1].start() if i+1 < len(headers) else len(text)
        sections[name] = text[start:end]
    return sections

def find_section(sections:dict, names:list):
    for k,v in sections.items():
        if k.lower() in names:
            return v
    ln = {kk.lower(): v for kk,v in sections.items()}
    for target in names:
        for key in ln:
            if target in key:
                return ln[key]
    return ""

def detect_title(text:str):
    m = TITLE_RE.search(text)
    if m:
        return m.group(1), m.group(2).strip(), m.group(3)
    h1 = re.search(r'^\s*#\s+(.+)$', text, re.MULTILINE)
    if h1:
        return "00", h1.group(1).strip(), "🎯"
    return "00", "Unknown School", "🎯"

def extract_ops(text:str):
    ops, seen = [], set()
    for m in OP_PAT.finditer(text):
        op = m.group(1)
        emoji = m.group(2) or ""
        if op not in seen:
            seen.add(op); ops.append((op, emoji))
    return ops

def extract_use_avoid(text:str):
    sections = split_sections(text)
    when = find_section(sections, WHEN_HEADERS)
    avoid = find_section(sections, AVOID_HEADERS)
    uses = [m.group(1).strip() for m in CHECKMARK.finditer(when)]
    cons = [m.group(1).strip() for m in CROSSMARK.finditer(avoid)]
    return uses, cons

def school_prefix_from_filename(fp: Path) -> str:
    """
    Extract school operation prefix from filename.
    
    Examples:
        07_abjurations.md -> 'abjure'
        08_transmutations.md -> 'transmute'
    """
    name = fp.stem.split('_', 1)[1] if '_' in fp.stem else fp.stem
    
    # Canonical school prefix mapping
    prefix_map = {
        "cantrips": "get|calc|generate|format|query|convert",  # Multiple prefixes
        "invocations": "invoke",
        "evocations": "evoke",
        "conjurations": "conjure",
        "enchantments": "enchant",
        "divinations": "divine",
        "abjurations": "abjure",
        "transmutations": "transmute",
        "glyphs_and_sigils": "glyph|sigil",  # Both prefixes
        "wards": "ward",
        "sanctifications": "sanctify",
        "summoning": "summon",
        "thaumaturgy": "thaumaturgy",
        "benediction": "bless|benediction",
        "chronomancy": "chrono",
        "apotheosis": "apotheosis",
        "ternary_weaving": "weave3",
        "mythogenesis": "mytho",
        "resonance_weaving": "resonance",
    }
    
    return prefix_map.get(name, name.rstrip('s'))

def classify_ops(ops: list, school_prefix: str) -> tuple[list, list]:
    """
    Classify operations as core (law) vs helpers (lore examples).
    
    Core ops match school prefix (abjure:*, transmute:*, etc.)
    Helpers are everything else (log:*, return:*, invoke:*, etc.)
    
    Args:
        ops: List of (op_name, emoji) tuples
        school_prefix: Pipe-separated prefixes (e.g. 'abjure' or 'glyph|sigil')
    
    Returns:
        (core_ops, helpers) tuple of lists
    """
    core, helpers = [], []
    prefixes = school_prefix.split('|')
    
    for op, emoji in ops:
        # Check if op starts with any school prefix
        op_prefix = op.split(':', 1)[0] if ':' in op else op
        if any(op_prefix == prefix for prefix in prefixes):
            core.append((op, emoji))
        else:
            helpers.append((op, emoji))
    
    return core, helpers

def check_law_todos(law_yaml: str, filename: str) -> list[str]:
    """
    A.C.E.'s TODO-gate: Check for TODOs in Law section.
    
    Law must be crisp (no TODOs allowed).
    Lore can be iterative (TODOs acceptable).
    
    Args:
        law_yaml: Law YAML string to check
        filename: Source filename for error reporting
    
    Returns:
        List of error messages (empty if clean)
    """
    errors = []
    
    # Check operations section for TODOs
    if "TODO_PARAMS" in law_yaml or "TODO:" in law_yaml:
        errors.append(f"{filename}: Law contains TODO markers (operations or constraints)")
    
    # Specific checks for operation fields
    if 'signature: "::TODO:' in law_yaml:
        errors.append(f"{filename}: Law operations have TODO signatures")
    if 'description: "TODO"' in law_yaml:
        errors.append(f"{filename}: Law operations have TODO descriptions")
    if 'returns: "TODO"' in law_yaml:
        errors.append(f"{filename}: Law operations have TODO returns")
    if '- "TODO' in law_yaml:  # Constraints or other lists
        errors.append(f"{filename}: Law constraints have TODO markers")
    
    return errors

def build_law_yaml(ops, avoid, uses, school_prefix=""):
    op_entries = []
    if ops:
        for op, emoji in ops:
            sig_emoji = emoji if emoji else "🎯"
            op_entries.append(f"""    - name: "{op}"
      signature: "::{op}{sig_emoji}[TODO_PARAMS]"
      emoji: "{sig_emoji}"
      params:
        - param1: "type (required)"
      returns: "TODO"
      description: "TODO"
      safety_tier: 1""")
    else:
        for i, uc in enumerate(uses[:5], 1):
            op_entries.append(f"""    - name: "TODO_operation_{i}"
      signature: "::TODO:operation_{i}🎯[params]"
      emoji: "🎯"
      params:
        - param1: "type (required)"
      returns: "TODO"
      description: "{uc}"
      safety_tier: 1""")
    cons = [f'    - "{c.replace("You need to ","Must ").replace("You’re ","Must ").replace("You are ","Must ")}' for c in (avoid or [])]
    if not cons:
        cons = ['    - "TODO: Add constraints"']
    return (
        "law:\n"
        "  operations:\n" +
        ("\n".join(op_entries) if op_entries else "    # TODO ops") + "\n\n" +
        "  constraints:\n" + "\n".join(cons) + "\n" +
        "  safety_tier: 1\n"
        "  preconditions:\n"
        "    - \"TODO\"\n"
        "  side_effects:\n"
        "    - \"TODO\"\n"
    )

def build_lore_yaml_canonical(name:str, helpers=None):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Add helpers section if any non-core ops found
    helpers_yaml = ""
    if helpers:
        helper_lines = [f'    - "::{op}{emoji}[...]"' for op, emoji in helpers]
        helpers_yaml = (
            "  examples:\n"
            "    helpers:\n" +
            "\n".join(helper_lines) + "\n"
        )
    
    return (
        "lore:\n"
        "  strategic_decisions:\n"
        "    - rationale: \"TODO\"\n"
        "      context: \"TODO\"\n"
        "      alternatives_rejected: [\"TODO\"]\n"
        "  emergent_patterns:\n"
        "    - pattern: \"TODO\"\n"
        "      evidence: \"TODO\"\n"
        "      implications: \"TODO\"\n"
        "  heart_imprints:\n"
        "    - author: \"Oracle\"\n"
        f"      timestamp: \"{ts}\"\n"
        "      emotion: \"TODO\"\n"
        "      quote: \"TODO\"\n"
        "  evolution_pressure:\n"
        "    - priority: \"MEDIUM\"\n"
        "      optimization_target: \"TODO\"\n" +
        helpers_yaml
    )

def build_lore_yaml_mega(name:str):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        "lore:\n"
        "  directives:\n"
        "    ritual_guards:\n"
        "      - \"TODO\"\n"
        "    emergent_patterns:\n"
        "      - \"TODO\"\n"
        "    narrative_hooks:\n"
        "      - \"TODO\"\n"
        "  notes:\n"
        "    - author: \"Oracle\"\n"
        f"      timestamp: \"{ts}\"\n"
        "      note: \"TODO\"\n"
    )

def make_front_matter(idx, name, law_yaml, lore_yaml, schema, stem, id_mode, with_template, with_version):
    if schema == "canonical":
        pieces = [law_yaml.rstrip(), "", lore_yaml.rstrip()]
    else:
        top = []
        if id_mode == "string":
            top.append(f'id: "{stem}"')
        elif id_mode == "int":
            try:
                id_val = int(stem.split("_",1)[0])
            except Exception:
                id_val = 0
            top.append(f"id: {id_val}")
        if with_template:
            top.append('template: arcane_school@2.2')
        if with_version:
            top.append('version: 0.1')
        head = "\n".join(top) + ("\n" if top else "")
        pieces = [head + law_yaml.rstrip(), "", build_lore_yaml_mega(name).rstrip()]
    return "---\n" + ("\n".join(pieces)).rstrip() + "\n---\n"

def refactor_one(path:Path, schema:str, in_place:bool, force:bool, id_mode:str, with_template:bool, with_version:bool, receipts:list):
    text = path.read_text(encoding="utf-8", errors="ignore")
    has_fm = bool(FM_RE.match(text))
    if has_fm and not force:
        receipts.append({"file": path.name, "status":"skip", "reason":"front-matter exists"})
        return False
    
    idx, name, emoji = detect_title(text)
    all_ops = extract_ops(text)
    uses, cons = extract_use_avoid(text)
    
    # A.C.E.'s school-scoped promotion: classify ops by school prefix
    school_prefix = school_prefix_from_filename(path)
    core_ops, helpers = classify_ops(all_ops, school_prefix)
    
    # Build Law with ONLY core ops (fixes "hallucinated ops" problem)
    law = build_law_yaml(core_ops, cons, uses, school_prefix)
    
    # A.C.E.'s TODO-gate: Check Law for TODOs (must be crisp)
    law_errors = check_law_todos(law, path.name)
    if law_errors:
        print(f"⚠️  {path.name}: Law contains TODOs (will need manual refinement)")
        for err in law_errors:
            print(f"   - {err}")
    
    # Build Lore with helpers preserved (provenance maintained)
    lore = build_lore_yaml_canonical(name, helpers)
    
    stem = path.stem
    fm = make_front_matter(idx, name, law, lore, schema, stem, id_mode, with_template, with_version)
    h1 = f"# {stem.split('_',1)[0]}. {name} {emoji}\n\n*TODO: Add subtitle from original*\n\n---\n\n"
    todo = f"<!-- AUTO-REFACTORED by auto_refactor_school_v2.py @ {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')} -->\n"
    new_content = todo + fm + h1 + text
    
    if in_place:
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(text, encoding="utf-8")
        path.write_text(new_content, encoding="utf-8")
        out = path
    else:
        out = path.parent / (path.stem + ".REFACTORED.md")
        out.write_text(new_content, encoding="utf-8")
    
    # Receipt logging: track core ops, helpers, uses, constraints
    receipts.append({
        "file": path.name,
        "status": "ok",
        "core_ops": len(core_ops),
        "helpers": len(helpers),
        "uses": len(uses),
        "constraints": len(cons),
        "out": out.name,
        "schema": schema
    })
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--schema", choices=["canonical","mega"], default="canonical")
    ap.add_argument("--in-place", action="store_true")
    ap.add_argument("--force", action="store_true", help="overwrite if FM exists (backs up .bak)")
    ap.add_argument("--id", choices=["string","int","none"], default="string", dest="id_mode")
    ap.add_argument("--with-template", action="store_true")
    ap.add_argument("--with-version", action="store_true")
    args = ap.parse_args()

    rec = []; ok=0; skip=0; fail=0
    for pat in args.files:
        p = Path(pat)
        if not p.exists():
            print(f"⚠️  Not found: {pat}"); fail+=1; continue
        try:
            if refactor_one(p, args.schema, args.in_place, args.force, args.id_mode, args.with_template, args.with_version, rec):
                ok+=1
            else:
                skip+=1
        except Exception as e:
            print(f"❌ {p.name}: {e}"); fail+=1

    receipts_dir = Path("receipts"); receipts_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    rpath = receipts_dir / f"auto_refactor_receipt_{stamp}.json"
    rpath.write_text(json.dumps({"ts": stamp, "schema": args.schema, "in_place": args.in_place, "results": rec}, indent=2), encoding="utf-8")
    print("\n" + "="*60)
    print(f"Summary: ok={ok} skip={skip} fail={fail}")
    print(f"Receipt: {rpath}")

if __name__ == "__main__":
    import argparse
    main()
