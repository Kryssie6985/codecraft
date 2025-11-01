# scripts/rosetta_integrity.py
# MEGA's Audit Master - Surgical integrity hash (no duplicates, LF-enforced)

import hashlib
import re
from pathlib import Path
from typing import Optional, Tuple

FENCE = ("```", "~~~")
TOP_KV = re.compile(r'^\s*[A-Za-z0-9_]+\s*:\s*$')  # yaml-ish key line (no value on same line)

def _indent(s: str) -> int:
    return len(s) - len(s.lstrip(" "))

def _canonical_lines(text: str) -> list[str]:
    """
    Canonical view for hashing:
    - Normalize newlines to LF
    - Exclude ONLY metadata.integrity: block (nested path search)
    - Ignore code fences correctly
    - Preserve everything else byte-for-byte (no rstrip!)
    """
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = t.split("\n")

    out: list[str] = []
    in_fence = False
    in_metadata = False
    meta_indent = 0
    in_integrity = False
    integ_indent = 0

    for line in lines:
        ls = line.lstrip()

        # Toggle fence state
        if ls.startswith(FENCE[0]) or ls.startswith(FENCE[1]):
            in_fence = not in_fence
            out.append(line)  # preserve exactly
            continue

        # CRITICAL: Parse metadata.integrity EVEN inside fences (Rosetta Stone has YAML inside ```yaml fence!)
        ci = _indent(line)

        # Enter metadata:
        if not in_metadata and re.match(r'^\s*metadata:\s*$', line):
            in_metadata = True
            meta_indent = ci
            out.append(line)
            continue

        if in_metadata:
            # Exit metadata if sibling/parent key
            if TOP_KV.match(ls) and ci <= meta_indent:
                in_metadata = False
                in_integrity = False
                out.append(line)
                continue

            # Enter integrity: under metadata
            if (not in_integrity and
                re.match(r'^\s*integrity:\s*$', line) and
                ci > meta_indent):
                in_integrity = True
                integ_indent = ci
                # Skip integrity: header itself
                continue

            # Inside integrity: skip until next sibling key at same/lower indent
            if in_integrity:
                if TOP_KV.match(ls) and ci <= integ_indent:
                    in_integrity = False
                    out.append(line)  # first sibling after integrity
                    continue
                # still inside integrity → skip
                continue

            # Other metadata content
            out.append(line)
            continue

        # Everything else (outside metadata, inside or outside fences)
        out.append(line)

    return out

def canonical_hash_from_text(text: str) -> str:
    canon = "\n".join(_canonical_lines(text))
    # normalize to *single* LF final newline for hashing
    if not canon.endswith("\n"):
        canon += "\n"
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()

_sha_rx = re.compile(r'^(\s*sha256:\s*)(["\']?)([0-9A-Fa-f]{64})(\2)\s*$')

def find_sha_span(lines: list[str]) -> Optional[Tuple[int, int, re.Match]]:
    """
    Find the sha256 line **under metadata.integrity** ONLY.
    Returns (line_index, column_start, regex_match) or None.
    """
    i, n = 0, len(lines)
    while i < n:
        if re.match(r'^\s*metadata:\s*$', lines[i]):
            meta_indent = _indent(lines[i])
            i += 1
            while i < n and _indent(lines[i]) > meta_indent:
                if re.match(r'^\s*integrity:\s*$', lines[i]):
                    integ_indent = _indent(lines[i])
                    i += 1
                    while i < n and _indent(lines[i]) > integ_indent:
                        m = _sha_rx.match(lines[i])
                        if m:
                            return (i, m.start(3), m)
                        i += 1
                    return None  # integrity present but no sha256
                i += 1
            return None  # metadata present but no integrity
        i += 1
    return None  # no metadata block

def replace_sha(text: str, new_hex: str) -> str:
    """
    Replace ONLY the sha256 value under metadata.integrity.
    No duplicate blocks; fail loudly if not found.
    """
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = t.split("\n")
    found = find_sha_span(lines)
    if found is None:
        raise RuntimeError(
            "metadata.integrity.sha256 not found; refusing to append elsewhere. "
            "Ensure the document has exactly ONE integrity: block under metadata:"
        )
    i, _, m = found
    prefix = m.group(1)
    quote = m.group(2) or '"'
    lines[i] = f'{prefix}{quote}{new_hex}{quote}'

    out = "\n".join(lines)
    # force a single LF at EOF for determinism
    if not out.endswith("\n"):
        out += "\n"
    return out

# Convenience CLI so fixer/validator/tests all use the *same* code path
if __name__ == "__main__":
    import sys
    p = Path(sys.argv[1])
    text = p.read_text(encoding="utf-8", errors="ignore")
    h = canonical_hash_from_text(text)
    print(h)
