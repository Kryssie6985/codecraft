#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LOST v3.1 Validator - CodeCraft Fort Knox
Validates SERAPHINA LOST documentation against canonical structure

Checks:
  - Self-contained integrity hash (MEGA's canonical algorithm - stable regardless of edits)
  - Paired YAML metadata exists
  - Document type-specific section requirements
  - Six Genesis Questions completeness
  - Q6 Adversarial Test (required for blueprint/protocol/charter)
  - Token≠Schools invariant (grammar tokens are NOT the 19 Schools)
  - Constitutional authority references
"""

# --- path bootstrap (identical in both CLIs) ---
from pathlib import Path
import sys
THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[1]  # project root (contains 'scripts')
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
# -----------------------------------------------

import re, yaml, hashlib, pathlib
from typing import Dict, List, Optional, Set
from scripts.rosetta_integrity import canonical_hash_from_text  # MEGA's shared canonicalization

# Debug path flag
if "--debug-path" in sys.argv:
    import scripts.rosetta_integrity as RI
    print("rosetta_integrity from:", RI.__file__)
    sys.exit(0)

def _read_claimed_from_metadata(md_text: str) -> str | None:
    """Extract sha256 from metadata.integrity specifically (not any stray integrity block)"""
    md_text = md_text.replace("\r\n","\n").replace("\r","\n")
    meta = re.search(r'(?ms)^\s*metadata:\s*(.+?)^(?=[A-Za-z0-9_\-]+\s*:|\Z)', md_text)
    if not meta:
        return None
    block = meta.group(1)
    integ = re.search(r'(?ms)^\s*integrity:\s*(.+?)^(?=[A-Za-z0-9_\-]+\s*:|\Z)', block)
    if not integ:
        return None
    m = re.search(r'^\s*sha256:\s*"?([0-9A-Fa-f]{64})"?\s*$', integ.group(1), re.M)
    return m.group(1) if m else None

# MEGA's canonical hash regex - matches sha256 lines outside code fences (legacy, now using shared module)
CANON_SHA_RX = re.compile(r'^\s*sha256:\s*[0-9A-Fa-f]{64}\s*$')
TOP_KEY_RX   = re.compile(r'^\s*[A-Za-z0-9_]+\s*:\s*')  # naive top-level YAML key

# Document type requirements matrix
LOST_REQUIREMENTS = {
    "blueprint": {
        "required_sections": ["I.", "II.", "III.", "IV.", "V."],
        "required_genesis_q": [1, 2, 3, 4, 5, 6],  # Q6 mandatory
        "requires_dependencies": True,
        "requires_law_sigils": True,
    },
    "protocol": {
        "required_sections": ["I.", "II.", "III.", "IV.", "V."],
        "required_genesis_q": [1, 2, 3, 4, 5, 6],  # Q6 mandatory
        "requires_dependencies": True,
        "requires_law_sigils": True,
    },
    "charter": {
        "required_sections": ["I.", "II.", "III.", "IV.", "V."],
        "required_genesis_q": [1, 2, 3, 4, 5, 6],  # Q6 mandatory
        "requires_dependencies": True,
        "requires_law_sigils": True,
    },
    "rosetta_stone": {
        "required_sections": ["I.", "II.", "III."],
        "required_genesis_q": [1, 2, 3, 4, 5],  # Q6 optional
        "requires_dependencies": False,
        "requires_law_sigils": False,
    },
    "context_hub": {
        "required_sections": ["I.", "II."],
        "required_genesis_q": [1, 2],
        "requires_dependencies": False,
        "requires_law_sigils": False,
    },
    "session_bridge": {
        "required_sections": ["I.", "II."],
        "required_genesis_q": [1, 2],
        "requires_dependencies": False,
        "requires_law_sigils": False,
    },
}

# Constitutional authority references (normalized slugs for resilience)
ALLOWED_AUTHORITIES = {
    "charter-v1-1",
    "crown-accord-v1-2a",
    "law-lore-protocol",      # "Law & Lore Protocol" normalizes to this (& removed)
    "law-and-lore-protocol",  # Also accept underscore version
    "phoenix-protocol",
    "n-o-r-m-a-protocol",
}

def _norm_auth(s: str) -> str:
    """Normalize authority string to canonical slug format"""
    s = s.lower().strip()
    s = s.replace(".md", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def _get_authorities(meta: dict) -> list:
    """Extract constitutional_authority from multiple possible YAML paths"""
    m = meta or {}
    return (
        m.get("constitutional_authority")
        or m.get("metadata", {}).get("constitutional_authority")
        or m.get("metadata", {}).get("identifiers", {}).get("constitutional_authority")
        or []
    )

def paired_yaml(md_path: pathlib.Path) -> pathlib.Path:
    """Return path to paired YAML metadata file"""
    return md_path.with_suffix(".yaml")

def extract_embedded_yaml(md_text: str) -> Optional[str]:
    """Extract YAML content from embedded code fences in markdown (returns LAST block)"""
    lines = md_text.splitlines()
    in_yaml_block = False
    all_yaml_blocks = []
    current_block = []
    
    for line in lines:
        if line.strip().startswith("```yaml"):
            in_yaml_block = True
            current_block = []
            continue
        elif line.strip() == "```" and in_yaml_block:
            in_yaml_block = False
            if current_block:
                all_yaml_blocks.append("\n".join(current_block))
            current_block = []
        elif in_yaml_block:
            current_block.append(line)
    
    # Return LAST YAML block (LOST v3.1 puts machine-readable YAML at document end)
    return all_yaml_blocks[-1] if all_yaml_blocks else None

def extract_yaml_frontmatter(text: str) -> Optional[Dict]:
    """Extract YAML frontmatter from markdown if present"""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1])
            except:
                pass
    return None

def verify_integrity_hash(md_path: pathlib.Path, metadata: dict) -> Optional[str]:
    """
    Verify self-contained integrity hash (MEGA's shared canonicalization module)
    
    Phoenix Protocol: Document can self-validate from file alone.
    Stable hash: Entire integrity: block excluded from canonical bytes!
    
    Returns None if valid, error message if invalid.
    """
    # Read claimed hash directly from metadata.integrity (not from parsed YAML which may be stale)
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    claimed_hash = _read_claimed_from_metadata(text)
    
    if not claimed_hash:
        return None  # No integrity claim in metadata.integrity, skip check
    
    # Compute canonical hash using MEGA's shared module (rosetta_integrity.py)
    computed_hash = canonical_hash_from_text(text)
    
    if claimed_hash.lower() != computed_hash.lower():
        return (
            f"[INTEGRITY-FAIL] Document hash mismatch!\n"
            f"  Claimed:  {claimed_hash}\n"
            f"  Computed: {computed_hash}\n"
            f"  (Phoenix Protocol: canonical content hash excluding metadata.integrity block)"
        )
    
    return None  # Valid!

def validate_document(md_path: pathlib.Path) -> List[str]:
    """Validate a single LOST document"""
    errors = []
    
    # Read document
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    
    # Check paired YAML (priority: paired file > frontmatter > embedded)
    yml_path = paired_yaml(md_path)
    metadata = None
    
    if yml_path.exists():
        try:
            metadata = yaml.safe_load(yml_path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[G-01] YAML parse error in {yml_path.name}: {e}")
    else:
        # Try frontmatter first
        metadata = extract_yaml_frontmatter(text)
        
        # If no frontmatter, try embedded YAML
        if not metadata:
            embedded_yaml = extract_embedded_yaml(text)
            if embedded_yaml:
                try:
                    # Use safe_load_all() to handle multi-document YAML streams (separated by ---)
                    documents = list(yaml.safe_load_all(embedded_yaml))
                    
                    if not documents:
                        errors.append(f"[G-01] Embedded YAML block found but contained no valid documents")
                    else:
                        # The main manifest is the FIRST document in the stream
                        parsed = documents[0]
                        
                        # Handle nested metadata structure (LOST v3.1 uses metadata: as root key)
                        if isinstance(parsed, dict):
                            metadata = parsed.get("metadata", parsed)  # Use metadata if present, else root
                        else:
                            metadata = {}
                except Exception as e:
                    errors.append(f"[G-01] Embedded YAML parse error: {e}")
            else:
                errors.append(f"[G-01] Missing paired YAML, frontmatter, or embedded YAML block")
                return errors  # Can't validate further without metadata
    
    # Verify integrity hash (MEGA's canonical algorithm: stable & self-contained)
    integrity_error = verify_integrity_hash(md_path, metadata)
    if integrity_error:
        errors.append(integrity_error)
    
    # Extract document type
    doc_type = metadata.get("document_type")
    if not doc_type:
        errors.append(f"[G-02] Missing document_type in metadata")
        return errors
    
    # Get requirements for this document type
    reqs = LOST_REQUIREMENTS.get(doc_type)
    if not reqs:
        # Unknown type - skip validation
        return errors
    
    # Check constitutional authority (using MEGA's normalization for resilience)
    authorities = _get_authorities(metadata)
    if not authorities:
        errors.append(f"[G-02] Missing constitutional_authority reference")
    else:
        if isinstance(authorities, str):
            authorities = [authorities]
        unknown = [a for a in authorities if _norm_auth(a) not in ALLOWED_AUTHORITIES]
        for a in unknown:
            errors.append(f"[G-02] Unrecognized constitutional authority: {a}")
    
    # Check required sections
    text_lower = text.lower()
    for section in reqs["required_sections"]:
        # Look for section markers like "## I." or "## Section I"
        if not re.search(rf"^##+ {re.escape(section)}", text, re.MULTILINE | re.IGNORECASE):
            errors.append(f"[G-03] Missing required section: {section}")
    
    # Check Six Genesis Questions
    for q_num in reqs["required_genesis_q"]:
        q_patterns = {
            1: r"what does this do",
            2: r"why does it exist",
            3: r"what must never change",
            4: r"what did we learn",
            5: r"how did it feel",
            6: r"how can this be broken",
        }
        pattern = q_patterns[q_num]
        if not re.search(pattern, text_lower):
            if q_num == 6:
                errors.append(f"[G-06] Missing Q6 'How can this be broken?' (Adversarial Test) - REQUIRED for {doc_type}")
            else:
                errors.append(f"[G-03] Missing Genesis Question {q_num}: {pattern.replace('r', '').strip()}")
    
    # Check Dependencies section (if required)
    if reqs["requires_dependencies"]:
        if not re.search(r"dependencies|linkages", text_lower):
            errors.append(f"[G-03] Missing Dependencies & Linkages section (required for {doc_type})")
    
    # G-05: Token≠Schools invariant check (MEGA's semantic upgrade)
    # Only fail if document claims tokens EQUAL schools, not just mentions both
    # Check multiple paths for the fields (direct metadata level or nested)
    m = metadata.get("metadata", {}) if "metadata" in metadata else metadata
    total_schools = m.get("total_schools")
    token_count = m.get("token_count")
    
    # If both present, only fail when literally equal
    if isinstance(total_schools, int) and isinstance(token_count, int):
        if token_count == total_schools:
            errors.append(f"[G-05] DO NOT conflate grammar token count with canonical 19 Schools (architectural invariant)")
    else:
        # Fallback: only catch explicit equality claims, not casual mentions
        equality_pattern = re.compile(r"\btokens?\b\s*(?:==|=|equals?|≡)\s*19\s*schools\b", re.I)
        if equality_pattern.search(text):
            errors.append(f"[G-05] DO NOT conflate grammar token count with canonical 19 Schools (architectural invariant)")
    
    return errors

def main(paths: List[str]) -> int:
    """Main validation entry point"""
    if not paths:
        # Default: find all LOST docs
        paths = [str(p) for p in pathlib.Path(".").rglob("docs/**/*.md")]
    
    md_files = [pathlib.Path(p) for p in paths if p.endswith(".md")]
    all_errors = []
    
    for md_path in md_files:
        if not md_path.exists():
            continue
        errors = validate_document(md_path)
        all_errors.extend(errors)
    
    if all_errors:
        print("\n".join(sorted(set(all_errors))), file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
