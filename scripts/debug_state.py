#!/usr/bin/env python3
# debug_state.py - Debug state machine for canonical exclusion

import re

text = open('CODECRAFT_ROSETTA_STONE.md', 'r', encoding='utf-8', errors='ignore').read()
t = text.replace("\r\n", "\n").replace("\r", "\n")
lines = t.split("\n")

in_fence = False
in_metadata, meta_indent = False, 0
in_integrity, integ_indent = False, 0
top_kv = re.compile(r'^\s*[A-Za-z0-9_]+\s*:\s*')
FENCE = ("```", "~~~")

for i, line in enumerate(lines[5165:5190], 5165):  # Around metadata block
    ls = line.lstrip()
    ci = len(line) - len(line.lstrip(" "))
    
    # Check conditions
    is_fence = ls.startswith(FENCE[0]) or ls.startswith(FENCE[1])
    is_metadata = re.match(r'^\s*metadata:\s*$', line)
    is_integrity = re.match(r'^\s*integrity:\s*$', line)
    is_topkv = top_kv.match(line)
    
    action = "KEEP"
    if in_fence:
        action = "KEEP (fence)"
    elif in_integrity:
        if is_topkv and ci <= integ_indent:
            action = "KEEP (exit integrity)"
        else:
            action = "SKIP (in integrity)"
    elif in_metadata:
        if is_topkv and ci <= meta_indent:
            action = "KEEP (exit metadata)"
        elif is_integrity and ci > meta_indent:
            action = "SKIP (integrity header)"
        else:
            action = "KEEP (metadata content)"
    
    print(f"{i:4d} | fence={int(in_fence)} meta={int(in_metadata)}:{meta_indent} integ={int(in_integrity)}:{integ_indent} | indent={ci:2d} | {action:25s} | {repr(line[:60])}")
    
    # Update state
    if is_fence:
        in_fence = not in_fence
    elif not in_fence:
        if is_metadata and not in_metadata:
            in_metadata = True
            meta_indent = ci
        elif in_metadata:
            if is_topkv and ci <= meta_indent:
                in_metadata = False
                in_integrity = False
            elif is_integrity and not in_integrity and ci > meta_indent:
                in_integrity = True
                integ_indent = ci
            elif in_integrity and is_topkv and ci <= integ_indent:
                in_integrity = False
