# tests/test_rosetta_integrity.py
from __future__ import annotations
import os, sys, re, shutil, subprocess, hashlib, importlib
from pathlib import Path

# Bootstrap path for scripts/ package
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import from scripts package (unified path)
from scripts.rosetta_integrity import canonical_hash_from_text, find_sha_span

# Sanity check: verify we're importing from the right location
RI = importlib.import_module("scripts.rosetta_integrity")
assert RI.__file__.endswith("scripts/rosetta_integrity.py") or RI.__file__.endswith("scripts\\rosetta_integrity.py")

ROSETTA = ROOT / "CODECRAFT_ROSETTA_STONE.md"

def runm(mod: str, *args: str) -> subprocess.CompletedProcess:
    """Run module with -m flag, ensuring same package resolution as pytest"""
    return subprocess.run(
        [sys.executable, "-m", mod, *args],
        cwd=str(ROOT),
        text=True, capture_output=True, check=True
    )

def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def _claimed_sha(text: str) -> str:
    # Use the same locator the fixer/validator use
    lines = text.replace("\r\n","\n").replace("\r","\n").split("\n")
    span = find_sha_span(lines)
    if span is None:
        raise AssertionError("metadata.integrity.sha256 not found")
    i, _, m = span
    return m.group(3).lower()  # the 64-hex as captured

def test_no_crlf_in_repo_version():
    data = ROSETTA.read_bytes()
    assert b"\r" not in data, "CRLF detected — .gitattributes/.editorconfig not enforcing LF"

def test_fixer_idempotent_and_validator_agrees(tmp_path: Path):
    # Work on an isolated copy so we don't mutate your real Rosetta
    copy = tmp_path / "ROSETTA_COPY.md"
    shutil.copy2(ROSETTA, copy)

    # 1) First run of fixer computes + writes the sha
    r_fix = runm("scripts.fix_integrity_hash", str(copy))
    first_hex = r_fix.stdout.strip().lower()
    text1 = _read(copy)
    claim1 = _claimed_sha(text1)
    comp1 = canonical_hash_from_text(text1)
    assert claim1 == first_hex == comp1, "First run: claimed != computed"

    # 2) Second run must be a no-op (idempotent)
    before_bytes = copy.read_bytes()
    r_fix2 = runm("scripts.fix_integrity_hash", str(copy))
    second_hex = r_fix2.stdout.strip().lower()
    after_bytes = copy.read_bytes()
    assert before_bytes == after_bytes, "Fixer is not idempotent (content changed on second run)"
    assert second_hex == first_hex, "Fixer recomputed a different hash on second run"

    # 3) Validator must pass twice (consistency)
    runm("scripts.lost_validate", str(copy))
    runm("scripts.lost_validate", str(copy))

def test_only_one_real_integrity_block_under_metadata(tmp_path: Path):
    # Sanity: fixer should NEVER append a second integrity block
    copy = tmp_path / "ROSETTA_COPY2.md"
    shutil.copy2(ROSETTA, copy)
    runm("scripts.fix_integrity_hash", str(copy))
    text = _read(copy)
    # Count 'integrity:' headers that begin a block; allow the one under metadata and possibly an example in prose,
    # but there must be NO trailing, extra integrity block at EOF.
    lines = text.split("\n")
    idxs = [i for i, ln in enumerate(lines) if re.match(r"^\s*integrity:\s*$", ln)]
    # ensure no trailing integrity: block beyond the metadata section end
    assert len(idxs) >= 1, "No integrity: header found at all"
    # Heuristic: last integrity header must be *inside* metadata (i.e., not in the trailing tail)
    # If fixer ever appended, it would be the last lines of file; catch that:
    tail = "\n".join(lines[-10:])
    assert not re.search(r"^\s*integrity:\s*$", tail, re.M), "Duplicate integrity block detected near EOF"
