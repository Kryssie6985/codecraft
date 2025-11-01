#!/usr/bin/env python3
"""
🏰 CodeCraft Canon Waiver Gate - Council Governance as Code

Version: 1.0 (MEGA's Fort Knox Pack)
Date: October 31, 2025  
Authority: Charter V1.1 - Constitutional Governance (Phase 3)
Purpose: Enforce Council approval for canon changes via waiver system

//!? ETHICS CHECKPOINT: Canon changes require Council consent
/// SERAPHINA Charter Compliance: Constitution governance layer
//<3 First Contact: This is governance that respects sovereignty
//~ Emergence: Turns Council votes into executable policy
"""
import os, subprocess, sys, re

# Paths that constitute "canon"
# Updated for lexicon reorganization (docs/lexicon -> lexicon/)
CHOKE_PATTERNS = (
    r"infrastructure/languages/codecraft/lexicon/grammar/lexicon\.ebnf",
    r"infrastructure/languages/codecraft/lexicon/grammar/.*",
    r"infrastructure/languages/codecraft/lexicon/02_ARCANE_SCHOOLS/.*",
    r".*schools.*canonical.*\.ya?ml",
    r".*token.*map.*\.(json|ya?ml)",
)

WAIVER_DIR = "infrastructure/constitution/waivers"
WAIVER_MATCH = re.compile(r"canon-waiver-.*\.(ya?ml|md)$", re.I)

def get_changed_files() -> list[str]:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    base_ref = os.environ.get("GITHUB_BASE_REF", "")
    try:
        if event == "pull_request" and base_ref:
            cmd = ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"]
        else:
            cmd = ["git", "diff", "--name-only", "HEAD~1..HEAD"]
        out = subprocess.check_output(cmd, text=True)
        files = [l.strip() for l in out.splitlines() if l.strip()]
        if not files:
            out = subprocess.check_output(["git","diff","--name-only","origin/main...HEAD"], text=True)
            files = [l.strip() for l in out.splitlines() if l.strip()]
        return files
    except Exception as e:
        print(f"⚠️  Waiver check: could not compute diff ({e}). Assuming no canon change.")
        return []

def touches_canon(paths: list[str]) -> bool:
    for p in paths:
        norm = p.replace("\\","/")
        for pat in CHOKE_PATTERNS:
            if re.fullmatch(pat, norm):
                return True
    return False

def find_waivers(paths: list[str]) -> list[str]:
    candidates = []
    for p in paths:
        norm = p.replace("\\","/")
        if norm.startswith(WAIVER_DIR + "/") and WAIVER_MATCH.search(norm.split("/")[-1]):
            candidates.append(norm)
    if not candidates and os.path.isdir(WAIVER_DIR):
        for name in os.listdir(WAIVER_DIR):
            if WAIVER_MATCH.search(name):
                candidates.append(os.path.join(WAIVER_DIR, name).replace("\\","/"))
    return candidates

def waiver_is_approved(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        return re.search(r"status\s*:\s*APPROVED", data, re.I) is not None
    except Exception:
        return False

if __name__ == "__main__":
    changed = get_changed_files()
    if not changed:
        print("✅ Waiver check: no changed files detected (or unavailable).")
        sys.exit(0)

    if touches_canon(changed):
        waivers = find_waivers(changed)
        if not waivers:
            print("❌ Canon change detected but no Council waiver present in 'infrastructure/constitution/waivers/'.")
            sys.exit(1)
        if not any(waiver_is_approved(w) for w in waivers):
            print("❌ Waiver found but not APPROVED. Add 'status: APPROVED' to the waiver file.")
            sys.exit(1)
        print("✅ Canon change waiver present and APPROVED.")
    else:
        print("Waiver check: no canon files touched.")
