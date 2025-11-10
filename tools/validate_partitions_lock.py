"""
validate_partitions_lock.py
Structural validator for canon.partitions.lock.yaml
Validates:
  - Required partitions exist
  - Required fields present in each entry
  - File hashes match on-disk files
  - No duplicate IDs

Usage:
    python tools/validate_partitions_lock.py

Requirements:
    pip install pyyaml
"""
import sys
import hashlib
from pathlib import Path
from typing import Dict, Any, List, Set

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(2)

# ═══════════════════════════════════════════════════════════════════════════
# VALIDATION RULES
# ═══════════════════════════════════════════════════════════════════════════

REQUIRED_PARTITIONS = [
    "foundations",
    "syntax_variants",
    "parameters",
    "operators",
    "examples",
    "migrations"
]

REQUIRED_FIELDS = ["id", "title", "kind", "version", "status", "provenance", "hash"]

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def sha256_file(path: Path) -> str:
    """Compute SHA-256 hash of file contents."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

# ═══════════════════════════════════════════════════════════════════════════
# VALIDATORS
# ═══════════════════════════════════════════════════════════════════════════

def validate_structure(lock: Dict[str, Any]) -> List[str]:
    """Validate top-level lock structure."""
    errors = []
    
    if not isinstance(lock, dict):
        errors.append("Lock file must be a YAML mapping")
        return errors
    
    if "partitions" not in lock:
        errors.append("Missing required key: 'partitions'")
        return errors
    
    partitions = lock["partitions"]
    if not isinstance(partitions, dict):
        errors.append("'partitions' must be a mapping")
        return errors
    
    # Check required partitions exist
    for partition in REQUIRED_PARTITIONS:
        if partition not in partitions:
            errors.append(f"Missing required partition: '{partition}'")
        elif not isinstance(partitions[partition], list):
            errors.append(f"Partition '{partition}' must be a list")
    
    return errors

def validate_entry(partition_name: str, index: int, entry: Dict[str, Any], lexicon_root: Path) -> List[str]:
    """Validate a single partition entry."""
    errors = []
    entry_id = f"[{partition_name}[{index}]]"
    
    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(f"{entry_id} missing required field: '{field}'")
    
    # Provenance validation
    provenance = entry.get("provenance", {})
    if "path" not in provenance:
        errors.append(f"{entry_id} provenance missing 'path'")
    else:
        # Check file exists and hash matches
        rel_path = provenance["path"]
        file_path = lexicon_root / rel_path
        
        if not file_path.exists():
            errors.append(f"{entry_id} file not found: {rel_path}")
        else:
            # Validate hash
            expected_hash = entry.get("hash")
            if expected_hash:
                actual_hash = sha256_file(file_path)
                if actual_hash != expected_hash:
                    errors.append(f"{entry_id} hash mismatch for {rel_path}")
                    errors.append(f"  Expected: {expected_hash}")
                    errors.append(f"  Actual:   {actual_hash}")
    
    return errors

def validate_unique_ids(partitions: Dict[str, List[Dict[str, Any]]]) -> List[str]:
    """Validate that all entry IDs are unique across partitions."""
    errors = []
    seen_ids: Dict[str, str] = {}  # id -> partition name
    
    for partition_name, entries in partitions.items():
        for entry in entries:
            entry_id = entry.get("id")
            if not entry_id:
                continue
            
            if entry_id in seen_ids:
                errors.append(
                    f"Duplicate ID '{entry_id}' in partitions "
                    f"'{seen_ids[entry_id]}' and '{partition_name}'"
                )
            else:
                seen_ids[entry_id] = partition_name
    
    return errors

# ═══════════════════════════════════════════════════════════════════════════
# MAIN VALIDATOR
# ═══════════════════════════════════════════════════════════════════════════

def validate_lock(lock_path: Path, lexicon_root: Path) -> bool:
    """Validate partition lock file. Returns True if valid, False otherwise."""
    
    if not lock_path.exists():
        print(f"❌ ERROR: Lock file not found: {lock_path}")
        return False
    
    # Load lock file
    try:
        with open(lock_path, "r", encoding="utf-8") as f:
            lock = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ ERROR: Failed to parse lock file: {e}")
        return False
    
    errors = []
    
    # Structure validation
    errors.extend(validate_structure(lock))
    if errors:
        print("❌ STRUCTURAL ERRORS:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    partitions = lock["partitions"]
    
    # Entry validation
    for partition_name in REQUIRED_PARTITIONS:
        if partition_name not in partitions:
            continue
        
        entries = partitions[partition_name]
        for index, entry in enumerate(entries):
            errors.extend(validate_entry(partition_name, index, entry, lexicon_root))
    
    # ID uniqueness validation
    errors.extend(validate_unique_ids(partitions))
    
    # Report results
    if errors:
        print("❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    # Success summary
    counts = {name: len(partitions.get(name, [])) for name in REQUIRED_PARTITIONS}
    total = sum(counts.values())
    
    print("✅ VALIDATION PASSED")
    print("\nPartition Counts:")
    for name in REQUIRED_PARTITIONS:
        count = counts[name]
        print(f"  - {name:20s}: {count:3d} entries")
    print(f"\n  TOTAL: {total} entries")
    
    return True

# ═══════════════════════════════════════════════════════════════════════════
# CLI ENTRYPOINT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # Determine paths relative to script location
    script_dir = Path(__file__).parent
    lexicon_root = (script_dir / "../lexicon").resolve()
    lock_path = lexicon_root / "canon.partitions.lock.yaml"
    
    print("CodeCraft Partition Lock Validator")
    print("="*80)
    print(f"Lock File:    {lock_path}")
    print(f"Lexicon Root: {lexicon_root}")
    print("="*80 + "\n")
    
    valid = validate_lock(lock_path, lexicon_root)
    
    sys.exit(0 if valid else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
