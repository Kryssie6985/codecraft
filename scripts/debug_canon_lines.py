#!/usr/bin/env python3
from rosetta_integrity import _canonical_lines

text = open('CODECRAFT_ROSETTA_STONE.md', 'r', encoding='utf-8', errors='ignore').read()
canon = _canonical_lines(text)

# Print lines around where metadata.integrity should be
for i in range(5160, 5190):
    if i < len(canon):
        print(f"{i:4d}: {repr(canon[i][:70])}")
