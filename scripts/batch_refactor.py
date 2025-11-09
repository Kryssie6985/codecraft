#!/usr/bin/env python3
"""
batch_refactor.py
Run auto_refactor_school_v2 across common globs for the remaining schools.
"""
import argparse, subprocess, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", choices=["canonical","mega"], default="canonical")
    ap.add_argument("--in-place", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--id", choices=["string","int","none"], default="string")
    ap.add_argument("--with-template", action="store_true")
    ap.add_argument("--with-version", action="store_true")
    args = ap.parse_args()

    globs = ["lexicon/02_ARCANE_SCHOOLS/0[7-9]_*.md", "lexicon/02_ARCANE_SCHOOLS/1[0-9]_*.md"]
    cmd = ["python", "scripts/auto_refactor_school_v2.py", "--schema", args.schema]
    if args.in_place: cmd.append("--in-place")
    if args.force: cmd.append("--force")
    cmd += ["--id", args.id]
    if args.with_template: cmd.append("--with-template")
    if args.with_version: cmd.append("--with-version")
    cmd += globs
    print(" ".join(cmd))
    sys.exit(subprocess.call(cmd))

if __name__ == "__main__":
    main()
