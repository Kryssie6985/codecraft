#!/usr/bin/env python3
# fix_integrity_hash.py - Update integrity hash in CODECRAFT_ROSETTA_STONE.md
# MEGA's Audit Master - Surgical, idempotent, LF-enforced

# --- path bootstrap (identical in both CLIs) ---
from pathlib import Path
import sys
THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[1]  # project root (contains 'scripts')
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
# -----------------------------------------------

from scripts.rosetta_integrity import canonical_hash_from_text, replace_sha

# Debug path flag
if "--debug-path" in sys.argv:
    import scripts.rosetta_integrity as RI
    print("rosetta_integrity from:", RI.__file__)
    sys.exit(0)

def main():
    if len(sys.argv) != 2:
        print("usage: fix_integrity_hash.py <path-to-md>", file=sys.stderr)
        sys.exit(2)
    
    md = Path(sys.argv[1])
    text = md.read_text(encoding="utf-8", errors="ignore")
    digest = canonical_hash_from_text(text)
    new_text = replace_sha(text, digest)
    # Write deterministically (no CRLF)
    md.write_text(new_text, encoding="utf-8", newline="\n")
    print(digest)

if __name__ == "__main__":
    main()
