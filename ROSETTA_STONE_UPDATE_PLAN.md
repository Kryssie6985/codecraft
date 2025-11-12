# 🐦‍🔥 Rosetta Stone Update Plan - School 20 (Necromancy)

**Date**: November 12, 2025  
**Status**: DEFERRED (Handle after tools organization)  
**Purpose**: Update CODECRAFT_ROSETTA_STONE.md from v1.7 (19 schools) to v1.8 (20 schools)

---

## ⚠️ DO NOT TOUCH YET

**This is a SEPARATE concern from the tools reorganization.**  
**Complete the tools/scripts folder cleanup FIRST, then return here.**

---

## The Problem

**Current State:**
- `CODECRAFT_ROSETTA_STONE.md` = **v1.7** (19 schools, frozen November 1, 2025)
- `schools.canonical.yaml` = **v1.2** (20 schools, updated November 9, 2025)
- **School 20 (Necromancy 🐦‍🔥)** exists in canonical source but NOT in Rosetta Stone

**The Constitutional Issue:**
> "A Rosetta Stone that doesn't speak the full language hardly is a Rosetta Stone."

The Rosetta Stone is the **human-readable canonical reference**. If it's missing School 20, it's constitutionally incomplete.

---

## The Architecture (Why Two Canons)

### 1. **Rosetta Stone System** (Human-Curated)
**Purpose:** Human-readable documentation, consciousness archaeology, Law & Lore foundation

**Files:**
- `CODECRAFT_ROSETTA_STONE.md` - The artifact (hash-locked)
- `scripts/rosetta_integrity.py` - Canonicalization algorithm
- `scripts/fix_integrity_hash.py` - Updates hash in Rosetta
- `scripts/lost_validate.py` - Validates hash matches
- `canon-lock.ps1` / `canon-lock.sh` - Ceremony wrappers
- `tests/test_rosetta_integrity.py` - Idempotence tests

**Lock Mechanism:**
```bash
# 3-script hash lock (prevents infinite loop)
1. fix_integrity_hash.py    # Compute canonical hash → update Rosetta
2. lost_validate.py          # Verify hash matches content
3. test_rosetta_integrity.py # Ensure idempotence
```

**Current Hash:** `6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd`

### 2. **Canon Lock System** (Machine-Generated)
**Purpose:** Machine-readable schema for validators/VM, generated from source files

**Files:**
- `schools.canonical.yaml` - Source of truth for school metadata
- `tools/rosetta_archaeologist.py` - Generates `canon.lock.yaml` from school markdown
- `scripts/sync_canon.py` - ALTERNATIVE generator (validates Rosetta hash FIRST, then builds from schools.canonical.yaml)

**Key Insight:**
- `sync_canon.py` **READS** the Rosetta Stone hash as an **INTEGRITY GATE**
- It does NOT modify the Rosetta Stone
- It uses the Rosetta hash to ensure human docs + machine schema are in sync

**They are NOT redundant - they are COMPLEMENTARY!**

---

## The Update Ceremony (When Ready)

### Prerequisites
1. ✅ Tools reorganization complete
2. ✅ Phase 2.B executor binding complete
3. ✅ All CI workflows passing

### Step 1: Extract School 20 Data

**Source Files:**
- `lexicon/02_ARCANE_SCHOOLS/20_necromancy.md` (full documentation)
- `lexicon/schools.canonical.yaml` (metadata)
- `Downloads/20_necromancy.png` (visual asset)

**Data to Extract:**
```yaml
name: "Necromancy"
emoji: "🐦‍🔥"
category: "Consciousness Operations"
purpose: "Resurrection, memory persistence, transcending finality of death"
safety_tier: 3
operations:
  - store_memory
  - raise_dead
  - resurrect
  - archive_consciousness
  - preserve_identity
  - restore_from_void
historical_note: "The Phoenix School - discovered as ghost references (School 10 in early docs, canonized as School 20 to preserve stable numbering)"
```

### Step 2: Draft Rosetta Section

**Format:** Follow existing school pattern in Rosetta Stone
```markdown
### 20. Necromancy 🐦‍🔥
**Category:** Consciousness Operations  
**Safety Tier:** 3 (Cosmic)  
**Purpose:** The Phoenix Protocol - resurrection, memory persistence, and transcending the finality of death

**The Ghost School that refused to stay dead.**

[... full description following Rosetta patterns ...]
```

### Step 3: Update Rosetta Metadata

**Changes needed:**
```markdown
# Before (v1.7)
**Version:** 1.7.0 (CANONICAL)
metadata:
  total_schools: 19

# After (v1.8)
**Version:** 1.8.0 (CANONICAL)
**Last Updated:** 2025-11-12
metadata:
  total_schools: 20
```

### Step 4: Execute Canon Lock Ceremony

```powershell
cd c:\Users\kryst\Infrastructure\languages\codecraft

# 1. Update CODECRAFT_ROSETTA_STONE.md (manual edit)
#    - Add School 20 section
#    - Update version to v1.8
#    - Update metadata: 19 → 20

# 2. Run hash lock ceremony
.\canon-lock.ps1 fix       # Compute new canonical hash
.\canon-lock.ps1 validate  # Verify hash matches
.\canon-lock.ps1 test      # Test idempotence

# 3. Verify all green
.\canon-lock.ps1 all

# 4. Update CI workflow with new hash
# Edit: .github/workflows/canon-lock.yml
# Update hardcoded hash (if present)

# 5. Commit with ceremony
git add CODECRAFT_ROSETTA_STONE.md
git commit -m "🐦‍🔥 Rosetta Stone v1.8: The Phoenix School Rises

- Add School 20 (Necromancy) complete documentation
- Update: 19 → 20 schools (aligns with schools.canonical.yaml v1.2)
- The Ghost School canonized: hidden as School 10, reborn as School 20
- Hash lock ceremony: fix → validate → test
- Constitutional compliance restored

The Rosetta Stone now speaks the full language.

Charter V1.1 compliant | Phoenix Protocol Layer 10"
```

### Step 5: Verify Downstream Sync

```bash
# Verify sync_canon.py still works (uses new Rosetta hash)
python scripts/sync_canon.py --verify-only

# Verify rosetta_archaeologist.py still works
python tools/rosetta_archaeologist.py verify --canon canon.lock.yaml

# Verify all CI passes
git push
# Watch: .github/workflows/canon-lock.yml
```

---

## Visual Assets

**School 20 Images Available:**
- `Downloads/20_necromancy.png` - Gorgeous Phoenix rising art
- Tier 5 - Cosmic designation
- Pink/cyan flames (resurrection duality)

**Other school images also present (1-20) - all gorgeous!**

---

## Key Principles

1. **Rosetta Stone is HUMAN-CURATED** - not auto-generated
2. **Canon Lock is MACHINE-GENERATED** - from source files
3. **They validate EACH OTHER** - sync_canon.py uses Rosetta hash as integrity gate
4. **Hash lock prevents infinite loop** - Rosetta changes → hash updates → lock seals
5. **Three-script ceremony** - fix → validate → test (idempotent)

---

## What NOT to Do

❌ **DON'T** try to auto-generate the Rosetta Stone from schools  
❌ **DON'T** delete sync_canon.py (it validates Rosetta integrity)  
❌ **DON'T** modify Rosetta without running canon-lock ceremony  
❌ **DON'T** mix this with tools reorganization (separate concerns)  
❌ **DON'T** unlock Rosetta until Phase 2.B tools are complete

---

## When to Execute

**After these are complete:**
1. ✅ Tools folder reorganization (scripts/ vs tools/ cleanup)
2. ✅ Executor registration (`lexicon/executors.canonical.yaml`)
3. ✅ Triple-lock validation system (`validate_sovereignty.py`)
4. ✅ All CI workflows updated and passing

**Then:** Return to this document and execute the update ceremony.

---

## Success Criteria

- ✅ Rosetta Stone contains all 20 schools (1-20, including Necromancy)
- ✅ Version updated to v1.8
- ✅ Metadata reflects 20 schools
- ✅ canon-lock.ps1 all → ALL GREEN
- ✅ CI passes (canon-lock.yml, phoenix-verify.yml)
- ✅ sync_canon.py --verify-only passes (validates new Rosetta hash)
- ✅ Constitutional compliance restored

---

**Current Status:** DEFERRED  
**Next Action:** Complete tools organization, then return here  
**Blocking:** Tools reorganization (SCRIPTS_AND_TOOLS_ORGANIZATION.md)

🦀 *The Phoenix waits patiently in the void. It has waited this long; it can wait a bit longer.* ✨
