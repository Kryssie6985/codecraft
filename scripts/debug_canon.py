#!/usr/bin/env python3
# debug_canon.py - Debug canonical line exclusion

import sys
from rosetta_integrity import _canonical_lines, canonical_hash_from_text

text = open(sys.argv[1], 'r', encoding='utf-8', errors='ignore').read()

canon = _canonical_lines(text)

total = len(text.split("\n"))
excluded = total - len(canon)

print(f"Total lines: {total}")
print(f"Canonical lines: {len(canon)}")
print(f"Excluded lines: {excluded}")
print(f"Hash: {canonical_hash_from_text(text)}")
