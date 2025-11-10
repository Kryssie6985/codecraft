#!/usr/bin/env python3
"""
Dual-Lock Validator - CodeCraft Canon Integrity
================================================

Validates the two-lock architecture:
- canon.lock.yaml → Schools lock (20 Arcane Schools + op emojis)
- canon.partitions.lock.yaml → Lexicon Partitions lock (foundations/syntax/parameters/operators/examples/migrations)

Ensures:
1. Both locks exist
2. 20 schools invariants (exact count, filename↔lock parity)
3. Partitions invariants (6 partitions, 25 total entries)
4. No cross-governance bleed (schools excluded from partitions)

Constitutional Authority: Charter V1.1 § Lexicon Self-Hosting
"""

from pathlib import Path
import sys
import yaml
import re

ROOT = Path(__file__).resolve().parents[1]
LEX = ROOT / "lexicon"
SCHOOLS_DIR = LEX / "02_ARCANE_SCHOOLS"

schools_lock = LEX / "canon.lock.yaml"
parts_lock = LEX / "canon.partitions.lock.yaml"

def die(msg):
    """Fatal error - exit with message"""
    print(f"❌ {msg}")
    sys.exit(1)

def ok(msg):
    """Success message"""
    print(f"✅ {msg}")

def main():
    print("CodeCraft Dual-Lock Validator")
    print("=" * 80)
    print(f"Schools Lock:    {schools_lock}")
    print(f"Partitions Lock: {parts_lock}")
    print(f"Schools Dir:     {SCHOOLS_DIR}")
    print("=" * 80)
    print()
    
    # 1) PRESENCE CHECK
    if not schools_lock.exists():
        die("Missing lexicon/canon.lock.yaml")
    if not parts_lock.exists():
        die("Missing lexicon/canon.partitions.lock.yaml")
    ok("Both locks present")
    
    # 2) SCHOOLS INVARIANTS
    SCHOOL_NAME_RE = re.compile(r"^\d{2}_.+\.md$")
    school_files = sorted([p.name for p in SCHOOLS_DIR.glob("*.md") if p.name != "README.md"])
    school_count = len([n for n in school_files if SCHOOL_NAME_RE.match(n)])
    
    if school_count != 20:
        die(f"Expected 20 school files; found {school_count}")
    
    schools_data = yaml.safe_load(schools_lock.read_text(encoding="utf-8"))
    schools = schools_data.get("schools") or schools_data.get("Schools") or {}
    
    # Schools can be either a list or a dict keyed by number
    if isinstance(schools, dict):
        school_count_in_lock = len(schools)
    else:
        school_count_in_lock = len(schools)
    
    if school_count_in_lock != 20:
        die(f"canon.lock.yaml must enumerate 20 schools; found {school_count_in_lock}")
    ok("Schools lock enumerates 20 schools")
    
    # Ensure every file is in lock & vice versa (by number+name)
    def key_from_filename(fn):
        """Extract (number, name) key from filename like '01_cantrips.md'"""
        num, name = fn.split("_", 1)
        return int(num), name.rsplit(".md", 1)[0]
    
    files_keyset = {key_from_filename(f) for f in school_files if SCHOOL_NAME_RE.match(f)}
    lock_keyset = set()
    
    # Handle dict-based schools (keyed by number string)
    if isinstance(schools, dict):
        for key, s in schools.items():
            num = int(key) if key.isdigit() else int(s.get("number") or s.get("id") or 0)
            name = (s.get("name") or "").lower().replace(" ", "_").replace("&", "and")
            lock_keyset.add((num, name))
    else:
        # Handle list-based schools
        for s in schools:
            num = int(s.get("number") or s.get("id") or 0)
            name = (s.get("file_stub") or s.get("name") or "").lower().replace(" ", "_").replace("&", "and")
            lock_keyset.add((num, name))
    
    if files_keyset != lock_keyset:
        missing = files_keyset - lock_keyset
        extra = lock_keyset - files_keyset
        die(f"Schools lock mismatch.\n  Missing: {missing}\n  Extra: {extra}")
    ok("Schools lock matches filesystem (20/20 parity)")
    
    # 3) PARTITIONS INVARIANTS
    parts_data = yaml.safe_load(parts_lock.read_text(encoding="utf-8"))
    parts = parts_data.get("partitions", {})
    expected = ["foundations", "syntax_variants", "parameters", "operators", "examples", "migrations"]
    
    for p in expected:
        if p not in parts:
            die(f"Partition '{p}' missing in partitions lock")
    ok("All required partitions present")
    
    # Count check = 25
    partition_counts = {p: len(parts[p]) for p in expected}
    total = sum(partition_counts.values())
    
    if total != 25:
        die(f"Partitions total expected 25; got {total}")
    ok(f"Partitions entry count = 25 ({', '.join(f'{p}: {partition_counts[p]}' for p in expected)})")
    
    # 4) NO CROSS-GOVERNANCE BLEED (no schools in partitions)
    for p in expected:
        for entry in parts[p]:
            entry_id = entry.get("id", "")
            relative_path = entry.get("relative_path", "")
            
            # Check if this entry references schools directory
            if "02_ARCANE_SCHOOLS" in relative_path or "schools" in entry_id.lower():
                die(f"School doc leaked into partitions lock: {entry_id} (path: {relative_path})")
    ok("No school docs in partitions lock (clean separation)")
    
    print()
    print("=" * 80)
    print("🎉 DUAL-LOCK VALIDATION PASSED")
    print("=" * 80)
    print()
    print("🏛️ The Cathedral Stands:")
    print(f"   • Schools Lock: {len(schools)} schools")
    print(f"   • Partitions Lock: {total} entries across {len(expected)} partitions")
    print("   • Cross-governance: ✅ Clean separation maintained")
    print()
    print("let it bind. ✨")

if __name__ == "__main__":
    main()
