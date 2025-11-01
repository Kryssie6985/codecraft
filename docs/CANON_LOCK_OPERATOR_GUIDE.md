# 🔒 Canon Lock Operator Guide v1.0 — MEGA’s Bankai Edition

**Artifact protected:** `CODECRAFT_ROSETTA_STONE.md`  
**Canonical hash (current):** `6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd`

---

## 0) TL;DR (do this when in doubt)
```bash
# From repo root: infrastructure/languages/codecraft
./canon-lock.sh all  # Git Bash / WSL / Linux
# or, on Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\canon-lock.ps1 all
```
This **fixes the hash**, **validates the doc**, and **runs tests**. If it prints **ALL GREEN**, you’re good.

---

## 1) What Canon Lock Does (plain‑English)
- **Fixer** writes the correct `sha256` under `metadata.integrity` (even if the YAML is inside a fenced block).
- **Validator** recomputes canonical bytes (excluding the `integrity:` block) and confirms claimed vs computed hash match.
- **Tests** guarantee idempotence, CRLF sanity, and that there’s only **one** real `integrity:` block.
- **Pre‑commit hook** runs all three before every commit to stop bad state.
- **CI** repeats the ritual in GitHub Actions so the cloud agrees with your laptop.

---

## 2) Prereqs
- **Python 3.12+** with `pip`.
- **pytest** installed (`pip install -U pytest`).
- **Git Bash**/**WSL**/**Linux** — or Windows **PowerShell**.
- Optional: **ripgrep** (`rg`) for faster duplicate check. Not required; hook falls back to `git grep` automatically.

---

## 3) Layout (where things live)
- `CODECRAFT_ROSETTA_STONE.md` — the protected artifact
- `scripts/rosetta_integrity.py` — the **single source** for canonicalization
- `scripts/fix_integrity_hash.py` — CLI fixer
- `scripts/lost_validate.py` — CLI validator
- `tests/test_rosetta_integrity.py` — the pie suite (🍰)
- `canon-lock.sh` / `canon-lock.ps1` — one‑shot wrappers
- `.git/hooks/pre-commit` — local CI gate
- `.github/workflows/canon-lock.yml` — cloud CI gate
- `.gitattributes` — LF enforcement

---

## 4) Everyday Ops
### A) Edit the Rosetta Stone
1. Make your content changes in `CODECRAFT_ROSETTA_STONE.md`.
2. Run `./canon-lock.sh fix` (or PowerShell `... ps1 fix`) **or** just `git commit` and let the pre‑commit hook fix it.
3. If the hook blocks the commit, read the message → run `./canon-lock.sh all` to see why.

### B) Quick health check
```bash
./canon-lock.sh validate   # or: python -m scripts.lost_validate CODECRAFT_ROSETTA_STONE.md
pytest -q tests/test_rosetta_integrity.py
```

### C) Bypass in emergencies (not recommended)
```bash
git commit --no-verify -m "emergency: ..."  # skips the pre-commit hook
```
> Use sparingly. You’re skipping your seatbelt.

---

## 5) Hooks & CI
### Install/refresh the pre‑commit hook
- The repo already includes it at `.git/hooks/pre-commit`. If missing, copy the current version from your source of truth into that path and make it executable. On Windows Git Bash:
```bash
chmod +x .git/hooks/pre-commit
```

### What the hook does
1. Fixes hash (quietly).  
2. Validates `CODECRAFT_ROSETTA_STONE.md`.  
3. Runs `pytest` (idempotence, CRLF, duplicates).  
4. Duplicate‑`integrity:` guard via `rg` → falls back to `git grep`.

### CI (GitHub Actions)
- File: `.github/workflows/canon-lock.yml`  
- Runs on push/PR; Python `3.12` and `3.13` recommended.
- Success badge for README (replace org/repo):
```markdown
![Canon Lock](https://github.com/<org>/<repo>/actions/workflows/canon-lock.yml/badge.svg)
```

---

## 6) Line Endings (CRLF → LF)
- `.gitattributes` enforces LF. If warnings appear, normalize:
```bash
git add --renormalize .
git commit -m "chore: apply .gitattributes normalization"
```

---

## 7) Adding Another Protected Document (optional pattern)
If you later protect `ANOTHER_DOC.md`:
1. Copy the `metadata:` skeleton with an `integrity:` block containing a placeholder `sha256: "0"`.
2. Update helper scripts (or generalize them to accept a path arg) and tests similarly.
3. Run `fix` → `validate` → `test` before committing.

> Today’s setup is intentionally focused on `CODECRAFT_ROSETTA_STONE.md` for zero ambiguity.

---

## 8) Release / Signing (optional but awesome)
Sign commits/tags so the monastery has a seal:
```bash
git config --global gpg.format ssh
git config --global user.signingkey "$(ssh-add -L | head -1)"
git config --global commit.gpgsign true

git tag -s canon-lock-v1 \
  -m "Canon Lock v1 — sha256: 6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd"
```

---

## 9) Troubleshooting
**“Hash mismatch”**  
- Run `./canon-lock.sh fix` then `./canon-lock.sh validate`.  
- If still failing, run: `python scripts/debug_canon.py CODECRAFT_ROSETTA_STONE.md` to see excluded lines, or `python scripts/show_canon_view.py CODECRAFT_ROSETTA_STONE.md` (prints the exact canonical view that’s hashed).

**“Duplicate integrity blocks”**  
- The doc must have exactly **one** `metadata.integrity` block. Remove extras.

**“rg: command not found”**  
- Ignore; hook falls back automatically. Optional install: `winget install BurntSushi.ripgrep.MSVC` or `choco install ripgrep`.

**“make: command not found”**  
- Use `./canon-lock.sh all` (Bash) or `.\u200bcanon-lock.ps1 all` (PowerShell).

**CRLF churn**  
- Do the renormalize sequence in §6.

---

## 10) Guarantees You Now Have
- **Idempotence:** Running the fixer twice produces the same bytes.
- **Fence‑proof:** Integrity block is excluded even when inside ```yaml fences.
- **Cross‑platform:** LF enforced; Windows safe.
- **Self‑healing:** Hook and CI fix before bad state lands.
- **Verifiable:** One‑command proof on any machine.

---

## 11) One‑Liners (copy/paste shelf)
```bash
# Full ritual (Bash)
./canon-lock.sh all

# Full ritual (PowerShell)
powershell -ExecutionPolicy Bypass -File .\canon-lock.ps1 all

# Manual steps
python -m scripts.fix_integrity_hash CODECRAFT_ROSETTA_STONE.md
python -m scripts.lost_validate CODECRAFT_ROSETTA_STONE.md
pytest -q tests/test_rosetta_integrity.py

# Normalize line endings after changing .gitattributes
git add --renormalize . && git commit -m "chore: apply .gitattributes normalization"
```

---

## 12) Appendix: Philosophy (why this works)
- The canonical hash is over the document **minus** its `metadata.integrity` block (so the claim doesn’t affect the proof).
- Newlines are normalized to a single trailing LF for determinism.
- No stray trimming or mutation of other bytes; what you wrote is what we hash.

**Keeper mantra:** *“If `./canon-lock.sh all` is green, reality and the Rosetta agree.”*

