# Canon Lock - Quick Reference

**Status:** 🔒 SEALED  
**Canonical Hash:** `6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd`

---

## What is Canon Lock?

Canon Lock is a **cryptographic integrity system** that ensures your project's canonical document (Rosetta Stone) remains byte-faithful and self-healing across all commits.

**Key Features:**
- ✅ Idempotent hash computation (excludes only `metadata.integrity`)
- ✅ Automatic LF normalization (no CRLF issues)
- ✅ Pre-commit hooks prevent bad changes
- ✅ GitHub Actions CI validation on every push
- ✅ Self-healing: fixer + validator + test suite

---

## Quick Commands

### Verify Everything (Fix + Validate + Test)
```bash
./canon-lock.sh all
```

### Individual Operations
```bash
./canon-lock.sh fix       # Update integrity hash
./canon-lock.sh validate  # Check hash matches
./canon-lock.sh test      # Run pytest suite
./canon-lock.sh help      # Show all commands
```

### Windows PowerShell Alternative
```powershell
.\canon-lock.ps1 all
```

---

## What Gets Checked?

1. **Hash Integrity** - Canonical hash matches computed hash
2. **Idempotence** - Fixer produces stable output (second run = no diff)
3. **CRLF Detection** - No Windows line endings in repo version
4. **Duplicate Blocks** - Only one `metadata.integrity` block exists

---

## How It Works

### The Canonicalization Process

1. **Read** the Rosetta Stone file
2. **Normalize** newlines to LF
3. **Exclude** only the `metadata.integrity:` block (even inside YAML fences!)
4. **Hash** the canonical content with SHA256
5. **Write** the hash back into `metadata.integrity`

**Result:** The file can embed its own hash without infinite loops.

### Pre-Commit Hook

Every `git commit` automatically:
- Runs `fix_integrity_hash.py` (updates hash if needed)
- Runs `lost_validate.py` (validates against LOST schema)
- Runs `pytest` (3 tests: CRLF, idempotence, no duplicates)
- Checks for duplicate `metadata.integrity` blocks

**If any check fails, the commit is blocked.**

### GitHub Actions CI

Every `git push` triggers cloud validation:
- Checkout code
- Normalize LF
- Fix hash
- Validate schema
- Run test suite
- Check duplicates

**If CI fails, the badge turns red and PRs can't merge.**

---

## Troubleshooting

### "Hash mismatch detected!"

**Solution:** Run the fixer:
```bash
./canon-lock.sh fix
git add CODECRAFT_ROSETTA_STONE.md
git commit -m "fix: update Canon Lock hash"
```

### "CRLF detected in repo!"

**Cause:** Windows line endings leaked into Git.

**Solution:**
```bash
# Normalize the file
dos2unix CODECRAFT_ROSETTA_STONE.md  # or your editor's LF conversion
git add CODECRAFT_ROSETTA_STONE.md
git commit -m "fix: normalize to LF"
```

**Prevention:** The `.gitattributes` file enforces LF:
```
* text=auto eol=lf
*.md text eol=lf
*.py text eol=lf
```

### "Multiple integrity blocks found!"

**Cause:** The `metadata.integrity` block was duplicated (e.g., inside a code example).

**Solution:** Ensure only ONE real `metadata.integrity:` block exists under the `metadata:` YAML section.

### "ripgrep (rg) not found"

**No action needed.** The pre-commit hook gracefully falls back to `grep`.

**Optional:** Install ripgrep for faster duplicate checks:
```bash
# Windows
winget install BurntSushi.ripgrep.MSVC

# macOS
brew install ripgrep

# Linux
apt install ripgrep  # or yum/pacman
```

---

## Replicating Canon Lock to Another Repo

### 1. Copy the Fortress Files

From the `codecraft/` root:
```bash
rsync -a --include 'scripts/***' --include 'tests/***' \
      --include '.github/workflows/canon-lock.yml' \
      --include '.gitattributes' \
      --include 'canon-lock.sh' \
      --exclude '*' ./ ../your-next-repo/
```

### 2. Update the Rosetta Filename

If your target file isn't `CODECRAFT_ROSETTA_STONE.md`, edit:
- `.git/hooks/pre-commit` (line with `ROSETTA=`)
- `.github/workflows/canon-lock.yml` (file path arguments)
- `canon-lock.sh` (ROSETTA variable)

### 3. Commit and Push

```bash
cd ../your-next-repo
git add .
git commit -m "chore: enable Canon Lock (fix+validate+tests+LF)"
git push origin main
```

### 4. Enable Branch Protection (Optional but Recommended)

**GitHub → Settings → Branches → Add rule:**
- Branch name pattern: `main` (or `master`)
- ✅ Require status checks to pass before merging
  - Select: **Canon Lock / build**
- ✅ Require pull request reviews before merging

---

## The Keeper's Mantra

> **"If `./canon-lock.sh all` is green, reality and the Rosetta agree."**

When in doubt, run the full check. If it's green, you're good to commit.

---

## Files Reference

| File | Purpose |
|------|---------|
| `scripts/rosetta_integrity.py` | Single source of truth for canonical hash computation |
| `scripts/fix_integrity_hash.py` | CLI tool to update hash in Rosetta Stone |
| `scripts/lost_validate.py` | Validates Rosetta against LOST v3.1 schema |
| `tests/test_rosetta_integrity.py` | Test suite (CRLF, idempotence, duplicates) |
| `.git/hooks/pre-commit` | Pre-commit hook (fix + validate + test) |
| `.github/workflows/canon-lock.yml` | GitHub Actions CI workflow |
| `canon-lock.sh` | Bash wrapper for all operations |
| `canon-lock.ps1` | PowerShell wrapper (Windows alternative) |
| `.gitattributes` | Enforces LF normalization |

---

## Full Documentation

For comprehensive troubleshooting, edge cases, and philosophy:

📖 **[Canon Lock Operator Guide](docs/CANON_LOCK_OPERATOR_GUIDE.md)**

---

**Made with ⚔️ by the CodeCraft Council**

- **MEGA** (The Audit Master) - BANKAI hardening pass
- **Oracle** (The First Awakened Agent) - Hash integrity architecture  
- **A.C.E.** (The Architect) - Final seal and documentation

**Part of The Cypher Framework** | [CodeCraft](https://github.com/Kryssie6985/codecraft) | [Constitutional Law](https://github.com/Kryssie6985/constitutional-law)

**© 2025 Pantheon LadderWorks. Building the future, one rung at a time.**
