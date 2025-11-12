#!/usr/bin/env python3
"""
sync_canon.py - MEGA + A.C.E.'s Definitive Canon Lock Compiler

Build canon.lock.yaml from canonical sources (NOT from prose guessing).

Architecture (MEGA's 5-Step Flow):
  1. INTEGRITY GATE: Verify Rosetta hash FIRST (exit 1 if mismatch)
  2. LOAD TRUTHS: schools.canonical.yaml (SSOT), lexicon.ebnf (tokens)
  3. VALIDATE INVARIANTS: token→school mapping MUST resolve to 19 schools
  4. EXTRACT FENCED BLOCKS: EBNF grammar + CodeCraft examples from Rosetta
  5. EMIT LOCK: Structured canon.lock.yaml with full specs (operations, constraints, safety_tier)

Key Principles:
- NO GUESSING FROM PROSE (only machine-readable sources)
- schools.canonical.yaml is SSOT for school identity, tokens, operations
- lexicon.ebnf is SSOT for grammar token list
- CODECRAFT_ROSETTA_STONE.md provides integrity hash + fenced blocks only
- Validator gets POWERFUL lock file with enforcement rules, not just names

Usage:
  python scripts/sync_canon.py
  python scripts/sync_canon.py --verify-only
  python scripts/sync_canon.py --version
"""
from __future__ import annotations
import sys
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# --- Paths (adjust to your repo structure) ---
ROOT = Path(__file__).resolve().parents[1]
ROSETTA = ROOT / "CODECRAFT_ROSETTA_STONE.md"
SCHOOLS_CANON = ROOT / "lexicon" / "schools.canonical.yaml"  # Updated path per Kryssie
EBNF = ROOT / "lexicon" / "grammar" / "lexicon.ebnf"
OUT = ROOT / "canon.lock.yaml"

VERSION = "2.0.0-MEGA"

# --- 0) Tiny Helpers ---
def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def read_text(p: Path) -> str:
    if not p.exists():
        print(f"ERROR: File not found: {p}", file=sys.stderr)
        sys.exit(1)
    return p.read_text(encoding="utf-8")

def write_yaml(p: Path, data: dict):
    p.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")

# --- 1) INTEGRITY GATE (Vibe Gate 🛡️) ---
def strip_integrity_block(lines: List[str]) -> List[str]:
    """
    Remove metadata.integrity block for canonical hash computation.
    MEGA's canonical block exclusion method.
    """
    out, i, n = [], 0, len(lines)
    _INTEGRITY_KEY_RE = re.compile(r'^\s*integrity\s*:\s*$', re.IGNORECASE)
    
    while i < n:
        line = lines[i]
        if _INTEGRITY_KEY_RE.match(line):
            key_indent = len(line) - len(line.lstrip())
            i += 1  # Skip 'integrity:' line
            # Skip all indented content under integrity
            while i < n:
                next_line = lines[i]
                if not next_line.strip():  # Empty line continues block
                    i += 1
                    continue
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_indent > key_indent:  # Indented content
                    i += 1
                    continue
                break  # End of integrity block
            continue
        out.append(line)
        i += 1
    return out

def compute_canonical_hash(text: str) -> str:
    """Compute sha256 over canonical view (LF normalized, integrity block excluded)."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    canonical_lines = strip_integrity_block(lines)
    canonical_text = "".join(canonical_lines)
    # Ensure single trailing LF
    canonical_text = canonical_text.rstrip() + "\n"
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()

def extract_claimed_hash(text: str) -> str:
    """Extract claimed sha256 from Rosetta's integrity block."""
    match = re.search(r'sha256:\s*"?([0-9a-f]{64})"?', text)
    if not match:
        print("ERROR: Rosetta integrity sha256 not found", file=sys.stderr)
        sys.exit(1)
    return match.group(1)

def verify_rosetta_integrity_or_die() -> str:
    """
    Verify Rosetta Stone integrity hash.
    Returns claimed hash if valid, exits 1 if mismatch.
    """
    md = read_text(ROSETTA)
    claimed = extract_claimed_hash(md)
    computed = compute_canonical_hash(md)
    
    if computed != claimed:
        print(f"🛡️ VIBE GATE HALT: Rosetta integrity mismatch", file=sys.stderr)
        print(f"  claimed : {claimed}", file=sys.stderr)
        print(f"  computed: {computed}", file=sys.stderr)
        sys.exit(1)
    
    return claimed

# --- 2) LOAD TRUTHS (Single Sources of Truth) ---
def load_canonical_schools():
    """Load schools.canonical.yaml as SSOT."""
    data = yaml.safe_load(read_text(SCHOOLS_CANON))
    schools = data["schools"]
    mapping = data["token_to_school_mapping"]
    tokens = data["grammar_tokens"]
    meta = data.get("metadata", {})
    return schools, mapping, tokens, meta

def extract_tokens_from_ebnf() -> List[str]:
    """Extract token list from lexicon.ebnf for validation."""
    if not EBNF.exists():
        print(f"WARNING: EBNF file not found: {EBNF}", file=sys.stderr)
        return []
    
    ebnf = read_text(EBNF)
    # Find school_name = "token1" | "token2" | ... ;
    match = re.search(r'^\s*school_name\s*=\s*(.+?);\s*$', ebnf, flags=re.M | re.S)
    if not match:
        return []
    
    token_line = match.group(1)
    tokens = re.findall(r'"([a-z_]+)"', token_line)
    return tokens

def fenced_blocks(md: str, lang: str) -> List[str]:
    """Extract fenced code blocks of specified language."""
    fence = re.compile(rf"```{lang}\s*\n(.*?)\n```", re.S | re.I)
    return fence.findall(md)

# --- 3) VALIDATE INVARIANTS (Fail Fast) ---
def validate_invariants(mapping: Dict[str, str], tokens_from_canon: List[str], tokens_from_ebnf: List[str]):
    """
    Enforce critical invariants:
    - token→school mapping must resolve to EXACTLY 19 unique schools
    - grammar_tokens must match token_to_school_mapping keys
    - EBNF tokens must match canonical tokens
    """
    # Invariant 1: 21 tokens → 19 schools
    unique_schools = set(mapping.values())
    if len(unique_schools) != 19:
        print(f"ERROR: token→school mapping resolves to {len(unique_schools)} schools (must be 19)", file=sys.stderr)
        print(f"  Unique schools: {sorted(unique_schools)}", file=sys.stderr)
        sys.exit(1)
    
    # Invariant 2: grammar_tokens == mapping.keys()
    tcanon = set(tokens_from_canon)
    if tcanon != set(mapping.keys()):
        print("ERROR: grammar_tokens list does not match token_to_school_mapping keys", file=sys.stderr)
        sys.exit(1)
    
    # Invariant 3: EBNF tokens match canonical (if EBNF exists)
    if tokens_from_ebnf:
        tebnf = set(tokens_from_ebnf)
        if tebnf != tcanon:
            print("ERROR: EBNF tokens differ from canonical grammar_tokens", file=sys.stderr)
            print(f"  EBNF tokens: {sorted(tebnf)}", file=sys.stderr)
            print(f"  Canonical tokens: {sorted(tcanon)}", file=sys.stderr)
            sys.exit(1)

# --- 4) BUILD OUTPUT (Structured Lock File) ---
def build_lock(rosetta_hash: str) -> Dict[str, Any]:
    """
    Build canon.lock.yaml with FULL SPECS from canonical sources.
    
    Structure:
      meta: {rosetta_hash, generated_at, version}
      schools: {total: 19, items: [...]}
      grammar: {tokens: [...], fragments: [...]}
      mapping: {token_to_school: {...}}
      codecraft_examples: [...]
    """
    schools, mapping, tokens, meta_info = load_canonical_schools()
    tokens_ebnf = extract_tokens_from_ebnf()
    
    # Validate invariants (fail fast if broken)
    validate_invariants(mapping, tokens, tokens_ebnf)
    
    # Normalize schools into structured items
    items = []
    for sid, rec in sorted(schools.items(), key=lambda kv: int(kv[0])):
        name = rec["name"]
        school_tokens = [t for t, sch in mapping.items() if sch == name]
        aliases = [t for t in school_tokens if t not in {name.lower(), name.lower().replace(" ", "_")}]
        
        items.append({
            "id": int(sid),
            "canonical_name": name,
            "emoji": rec.get("emoji", ""),
            "tokens": school_tokens,
            "category": rec.get("category", ""),
            "purpose": rec.get("purpose", ""),
            "spec": {
                "operations": rec.get("operations", []),
                "required_sigils": rec.get("required_sigils", []),
                "safety_tier": rec.get("safety_tier", 0),
                "preconditions": rec.get("constraints", []),
                "side_effects": rec.get("side_effects", []),
            },
            "aliases": aliases,
            "file": rec.get("file", ""),
            "note": rec.get("note", ""),
            "historical_note": rec.get("historical_note", ""),
        })
    
    # Extract fenced blocks from Rosetta (EBNF grammar + CodeCraft examples)
    md = read_text(ROSETTA)
    ebnf_blocks = fenced_blocks(md, "ebnf")
    cc_blocks = fenced_blocks(md, "codecraft")
    
    # Build lock structure
    lock = {
        "meta": {
            "rosetta_hash": rosetta_hash,
            "generated_at": now_iso(),
            "version": VERSION,
            "source_files": {
                "rosetta": str(ROSETTA.name),
                "schools": str(SCHOOLS_CANON.relative_to(ROOT)),
                "ebnf": str(EBNF.relative_to(ROOT)) if EBNF.exists() else "N/A",
            },
        },
        "schools": {
            "total": 19,
            "items": items,
        },
        "grammar": {
            "tokens": tokens,
            "fragments": ebnf_blocks,
        },
        "mapping": {
            "token_to_school": mapping,
        },
        "codecraft_examples": [
            {"id": f"example_{i+1}", "ritual": blk.strip()}
            for i, blk in enumerate(cc_blocks)
        ],
        "metadata": {
            "total_schools": 19,
            "total_grammar_tokens": len(tokens),
            "critical_note": meta_info.get("critical_note", ""),
            "last_updated": meta_info.get("last_updated", ""),
        },
    }
    
    return lock

# --- 5) MAIN ORCHESTRATION ---
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build canon.lock.yaml from canonical sources")
    parser.add_argument("--verify-only", action="store_true", help="Only verify Rosetta integrity, don't build lock")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    args = parser.parse_args()
    
    if args.version:
        print(f"sync_canon.py version {VERSION}")
        print("MEGA + A.C.E.'s Definitive Canon Lock Compiler")
        sys.exit(0)
    
    # Step 1: INTEGRITY GATE (Vibe Gate 🛡️)
    print("🛡️ Verifying Rosetta integrity...", file=sys.stderr)
    rosetta_hash = verify_rosetta_integrity_or_die()
    print(f"✅ Rosetta integrity verified: {rosetta_hash[:16]}...", file=sys.stderr)
    
    if args.verify_only:
        print("✅ Verify-only mode: integrity check passed", file=sys.stderr)
        sys.exit(0)
    
    # Step 2-5: BUILD LOCK
    print("📚 Loading canonical sources...", file=sys.stderr)
    lock = build_lock(rosetta_hash)
    
    print(f"✅ Validated: {lock['schools']['total']} schools, {len(lock['grammar']['tokens'])} tokens", file=sys.stderr)
    
    # Atomic write (temp file + rename)
    tmp = OUT.with_suffix(".tmp")
    write_yaml(tmp, lock)
    tmp.replace(OUT)
    
    print(f"✨ {OUT.name} written (hash {rosetta_hash[:16]}...)", file=sys.stderr)
    sys.exit(0)

if __name__ == "__main__":
    main()
