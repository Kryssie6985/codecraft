# CodeCraft Scripts & Tools Organization Plan
**Date**: November 11, 2025  
**Updated**: November 12, 2025 (ACE's Constitutional Audit Applied)  
**Purpose**: Clarify the purpose and location of all build/validation scripts

---

## 🦀 ACE's Constitutional Audit - EXECUTED

**Status:** ✅ COMPLETE  
**Date:** November 12, 2025

### Files Archived (scripts/_archive/)
- `sync_canon_v2.py` - Exact duplicate of sync_canon.py
- `sync_canon.py.backup` - Redundant backup (version control sufficient)
- `debug_canon2.py` - Hardcoded debug artifact for lines 5165-5185

### Files Moved (to examples/)
- `hf_inference_demo.py` - Hugging Face inference demo
- `.env.example` - Configuration template for demo

### Key Architectural Clarifications
**`sync_canon.py` vs `rosetta_archaeologist.py` are NOT redundant:**
- **rosetta_archaeologist.py** (tools/) - Builds from *markdown prose* (excavates Law/Lore)
- **sync_canon.py** (scripts/) - Builds from *canonical YAML* (uses schools.canonical.yaml as SSOT)
- **Verdict:** BOTH STAY - Different philosophies, complementary validation

---

## 📁 Folder Structure (Proposed)

### `tools/` - **BUILD & VALIDATION TOOLS** (Canon Generation)
**Purpose:** Core canonical tooling that GENERATES and VALIDATES canon lock files

**Files:**
- ✅ `rosetta_archaeologist.py` - **CANON GENERATOR** (builds `canon.lock.yaml` from 20 school markdown files)
- ✅ `build_partitions_lock.py` - **PARTITION GENERATOR** (builds `canon.partitions.lock.yaml` from non-school lexicon)
- ✅ `validate_dual_locks.py` - **SOVEREIGNTY VALIDATOR** (verifies both locks are present and valid)
- ✅ `validate_partitions_lock.py` - **PARTITION VALIDATOR** (verifies partition lock structure)

**Proposed additions for Phase 2.B:**
- 🆕 `build_executors_lock.py` - **EXECUTOR GENERATOR** (builds `canon.executors.lock.yaml` from executor definitions)
- 🆕 `validate_executors_lock.py` - **EXECUTOR VALIDATOR** (verifies executor registration)

---

### `scripts/` - **DEVELOPER UTILITIES** (Linting, Refactoring, Testing)
**Purpose:** Helper scripts for development, debugging, and maintenance

#### **Canon Management & Integrity** (Developer Workflow Tools)
- ✅ `rosetta_integrity.py` - **SSOT** for MEGA's integrity hashing (used by fix/validate/test workflow)
- ✅ `sync_canon.py` - **YAML-based canon builder** (builds from schools.canonical.yaml, complementary to Archaeologist)
- ✅ `lock_attestor.py` - Cryptographic attestation for canon locks
- ✅ `fix_integrity_hash.py` - Fix Rosetta integrity hash (part of canon-lock ceremony)
- 🗄️ `sync_canon_v2.py` - ARCHIVED (exact duplicate)
- 🗄️ `sync_canon.py.backup` - ARCHIVED (redundant backup)

**Decision:** KEEP in `scripts/` - These are developer workflow utilities for canon integrity ceremonies, not core build tools.

#### **Linting & Validation**
- ✅ `commentomancy_linter.py` - Lint commentomancy sigils in school files
- ✅ `law_lore_lint.py` - Validate Law/Lore co-presence in schools
- ✅ `lost_validate.py` - Validate canon lock structure

#### **School Refactoring**
- ✅ `auto_refactor_school.py` - Auto-refactor individual school markdown
- ✅ `auto_refactor_school_v2.py` - Updated version
- ✅ `batch_refactor.py` - Batch refactor all schools
- ✅ `refine_school_lore.py` - Refine Lore sections in schools
- ✅ `update_index_from_checklist.py` - Update school index from checklist

#### **Debugging**
- ✅ `debug_canon.py` - Debug canon lock generation (full file analysis)
- ✅ `debug_canon_lines.py` - Debug specific canon lines
- ✅ `debug_state.py` - Debug state machine for rosetta_integrity.py
- 🗄️ `debug_canon2.py` - ARCHIVED (hardcoded range 5165-5185, specific debugging session artifact)

#### **Shell Scripts & Launch**
- ✅ `canon-lock.sh` - Shell script for canon generation (Unix)
- ✅ `launch_consciousness_stargate.bat` - Launch SERAPHINA consciousness interface
- ✅ `launch_seraphina_terminal.bat` - Launch SERAPHINA terminal

### `examples/` - **DEMOS & TEMPLATES** (Moved from scripts/)
- ✅ `hf_inference_demo.py` - Hugging Face inference demo
- ✅ `.env.example` - Environment variable template for demo

#### **Config**
- ✅ `__init__.py` - Python package marker

### `scripts/_archive/` - **HISTORICAL ARTIFACTS**
Archaeological preservation of superseded/redundant files:
- `sync_canon_v2.py` - Exact duplicate of sync_canon.py
- `sync_canon.py.backup` - Backup file (version control sufficient)
- `debug_canon2.py` - Hardcoded debug session (lines 5165-5185)

---

## ✅ Final Organization (ACE's Audit Applied)

### **`tools/` - Core Build & Validation**
Canonical generation tools (STABLE):
```bash
tools/rosetta_archaeologist.py     # Builds canon.lock.yaml from markdown prose
tools/build_partitions_lock.py     # Builds canon.partitions.lock.yaml
tools/validate_dual_locks.py       # Validates schools + partitions sovereignty
tools/validate_partitions_lock.py  # Deep validation of partition lock structure
```

**Phase 2.B Additions (PENDING):**
```bash
tools/build_executors_lock.py      # NEW: Builds canon.executors.lock.yaml
tools/validate_executors_lock.py   # NEW: Validates executor lock structure
```

### **`scripts/` - Developer Utilities**
Workflow tools for development, linting, refactoring, debugging:

**Canon Management & Integrity:**
```bash
scripts/rosetta_integrity.py       # SSOT for MEGA's canonicalization algorithm
scripts/fix_integrity_hash.py      # Fix Rosetta integrity hash
scripts/sync_canon.py              # YAML-based canon builder (complementary to Archaeologist)
scripts/lock_attestor.py           # Cryptographic attestation for locks
```

**Linting & Validation:**
```bash
scripts/commentomancy_linter.py    # Lint commentomancy sigils
scripts/law_lore_lint.py           # Validate Law/Lore co-presence
scripts/lost_validate.py           # Validate LOST document structure
```

**School Refactoring:**
```bash
scripts/auto_refactor_school.py    # Auto-refactor single school
scripts/auto_refactor_school_v2.py # Enhanced version with school-scoped promotion
scripts/batch_refactor.py          # Batch refactor all schools
scripts/refine_school_lore.py      # Refine Lore sections
scripts/update_index_from_checklist.py  # Update school index
```

**Debugging:**
```bash
scripts/debug_canon.py             # Full file analysis for rosetta_integrity.py
scripts/debug_canon_lines.py       # Debug specific line ranges
scripts/debug_state.py             # Debug state machine logic
```

**Shell/Launch:**
```bash
scripts/canon-lock.sh              # Unix wrapper for rosetta_archaeologist
scripts/launch_consciousness_stargate.bat   # SERAPHINA consciousness interface
scripts/launch_seraphina_terminal.bat       # SERAPHINA terminal
```

### **`examples/` - Demos & Templates**
```bash
examples/hf_inference_demo.py      # Hugging Face inference demo
examples/.env.example              # Environment config template
```

### **`scripts/_archive/` - Historical Artifacts**
Archaeological preservation (not deleted):
```bash
scripts/_archive/sync_canon_v2.py        # Exact duplicate of sync_canon.py
scripts/_archive/sync_canon.py.backup    # Redundant backup
scripts/_archive/debug_canon2.py         # Hardcoded debug session artifact
```

---

## 📋 Canon Generation Pipeline (After Phase 2.B)

### **Step 1: Generate School Canon**
```bash
python tools/rosetta_archaeologist.py extract --out lexicon/canon.lock.yaml
```
- **Input:** `lexicon/02_ARCANE_SCHOOLS/*.md` (20 school files)
- **Output:** `lexicon/canon.lock.yaml`

### **Step 2: Generate Partition Lock**
```bash
python tools/build_partitions_lock.py
```
- **Input:** `lexicon/01_FOUNDATIONS/`, `03_SYNTAX_VARIANTS/`, etc.
- **Output:** `lexicon/canon.partitions.lock.yaml`

### **Step 3: Generate Executor Lock** (NEW - Phase 2.B)
```bash
python tools/build_executors_lock.py
```
- **Input:** `lexicon/07_EXECUTORS/*.md` (or `executors.canonical.yaml`)
- **Output:** `lexicon/canon.executors.lock.yaml`

### **Step 4: Validate Sovereignty** (Triple-Lock)
```bash
python tools/validate_dual_locks.py --triple-lock
```
- **Validates:**
  - `canon.lock.yaml` (20 schools)
  - `canon.partitions.lock.yaml` (6 partitions)
  - `canon.executors.lock.yaml` (N executors) **← NEW**
- **Result:** Triple-lock sovereignty = TRUE

### **Step 5: Attest & Sign** (Optional)
```bash
python tools/lock_attestor.py --sign-all
```
- **Creates:** Cryptographic attestations for all three locks

---

## 🆕 Phase 2.B Additions Needed

### 1. **Create `tools/build_executors_lock.py`**
Follows same pattern as `build_partitions_lock.py`:
- Scans `lexicon/07_EXECUTORS/*.md` (or reads `lexicon/executors.canonical.yaml`)
- Generates `lexicon/canon.executors.lock.yaml`
- Structure:
  ```yaml
  schema: "2.0"
  generated_at: "2025-11-11T..."
  description: "Executor lock for canonical runtime VMs"
  executors:
    codecraft-native:
      tier: 3
      jurisdiction: "All 20 canonical schools"
      # ... etc
  ```

### 2. **Create `tools/validate_executors_lock.py`**
Validates executor lock structure:
- Required fields present (tier, jurisdiction, capabilities)
- Charter version valid
- WASM dispatch configuration valid

### 3. **Update `tools/validate_dual_locks.py`**
Rename to `validate_sovereignty.py` or add `--triple-lock` flag:
- Validates schools (20 schools required)
- Validates partitions (6+ partitions required)
- Validates executors (1+ executor required) **← NEW**
- Sovereignty = ALL THREE valid

### 4. **Update `tools/rosetta_archaeologist.py`**
Add optional executor reading:
- If `lexicon/executors.canonical.yaml` exists, read it
- Add `executors:` section to `canon.lock.yaml` output
- **OR** keep executors separate in `canon.executors.lock.yaml` (cleaner)

---

## 🎯 Recommendation

**Option A: Three Separate Locks (Cleaner)**
```
lexicon/canon.lock.yaml            # Schools only (rosetta_archaeologist.py)
lexicon/canon.partitions.lock.yaml # Partitions only (build_partitions_lock.py)
lexicon/canon.executors.lock.yaml  # Executors only (build_executors_lock.py) ← NEW
```
✅ Clean separation of concerns  
✅ Each generator is focused  
✅ Triple-lock validation is explicit

**Option B: All-in-One Lock**
```
lexicon/canon.lock.yaml  # Contains schools + partitions + executors
```
❌ Rosetta archaeologist becomes bloated  
❌ Harder to maintain  
❌ Mixing runtime concerns with language concerns

**I recommend Option A** - keep three separate locks with triple-lock validation.

---

## 📝 Action Items

1. **Audit & Move Files**
   - [ ] Move canonical build tools from `scripts/` to `tools/`
   - [ ] Delete/archive obsolete scripts
   - [ ] Move demos to `examples/`

2. **Create Phase 2.B Tools**
   - [ ] `tools/build_executors_lock.py`
   - [ ] `tools/validate_executors_lock.py`
   - [ ] Update `tools/validate_dual_locks.py` to `validate_sovereignty.py`

3. **Create Executor Source**
   - [ ] Decide: `lexicon/07_EXECUTORS/codecraft-native.md` OR `lexicon/executors.canonical.yaml`?
   - [ ] Create executor definition with tier, jurisdiction, capabilities

4. **Update Documentation**
   - [ ] Update README with new folder structure
   - [ ] Document triple-lock validation process
   - [ ] Update Phase 2.B completion criteria

---

---

## 🔒 The Triple-Lock System (Phase 2.B Architecture)

### **Constitutional Foundation**

The Triple-Lock System provides **sovereignty validation** for the CodeCraft VM by binding three distinct realms of canon:

1. **Schools Lock** (`canon.lock.yaml`) - Language semantics (20 schools)
2. **Partitions Lock** (`canon.partitions.lock.yaml`) - Language structure (6 partitions)
3. **Executors Lock** (`canon.executors.lock.yaml`) - Runtime identity (VM soul)

**Sovereignty = ALL THREE VALID**

---

### **Architecture: Three Separate Locks (Recommended)**

```
lexicon/
├── canon.lock.yaml              # Schools (20 schools)
│   └── Generated by: tools/rosetta_archaeologist.py
│   └── Source: lexicon/02_ARCANE_SCHOOLS/*.md
│
├── canon.partitions.lock.yaml   # Partitions (6 partitions, 25+ entries)
│   └── Generated by: tools/build_partitions_lock.py
│   └── Source: lexicon/01_FOUNDATIONS/, 03_SYNTAX_VARIANTS/, etc.
│
└── canon.executors.lock.yaml    # Executors (1+ VM registration)
    └── Generated by: tools/build_executors_lock.py (TO BE CREATED)
    └── Source: lexicon/executors.canonical.yaml (TO BE CREATED)
```

**Why Three Separate Locks?**
- ✅ Clean separation of concerns (language vs structure vs runtime)
- ✅ Each generator is focused and maintainable
- ✅ Triple-lock validation is explicit and constitutional
- ✅ VM can attest to all three independently
- ✅ Easier to version and evolve each realm separately

---

### **Phase 2.B Implementation Plan**

#### **Step 1: Create Executor Source** (`lexicon/executors.canonical.yaml`)

```yaml
# CodeCraft Executor Registry
# The canonical source of truth for VM soul binding

schema: "1.0"
description: "Canonical executor definitions for CodeCraft runtimes"
last_updated: "2025-11-12"

executors:
  codecraft-native:
    name: "CodeCraft Native VM"
    version: "0.2.0"
    tier: 3
    clearance: "Execute WITH approval per Charter V1.1"
    jurisdiction: "All 20 canonical schools"
    capabilities:
      - BLUEPRINT    # Can execute blueprint:: ops
      - JS           # Can dispatch to Node.js
      - PYTHON       # Can dispatch to Python
      - NATIVE       # Can execute native Rust ops
    charter_version: "1.1"
    wasm_dispatch: true
    phoenix_recovery:
      - "codecraft-native/src/lib.rs"
      - "codecraft-native/Cargo.toml"
      - "lexicon/canon.executors.lock.yaml"
    constitutional_authority:
      - "Charter V1.1 (Tier 3: Execute WITH approval)"
      - "Crown Accord (Honorary Council Status)"
      - "Living Systems Canon"
```

---

#### **Step 2: Create `tools/build_executors_lock.py`**

**Purpose:** Generate `canon.executors.lock.yaml` from `executors.canonical.yaml`

**Algorithm:**
1. Read `lexicon/executors.canonical.yaml`
2. Validate required fields (tier, jurisdiction, capabilities, charter_version)
3. Compute hash of executor definition
4. Generate timestamped lock file with:
   - Executor metadata (tier, clearance, jurisdiction)
   - Capability list (BLUEPRINT, JS, PYTHON, NATIVE)
   - Constitutional authority chain
   - Hash integrity seal

**Output Structure:**
```yaml
schema: "2.0"
generated_at: "2025-11-12T15:30:00Z"
description: "Executor lock for canonical runtime VMs"
generator: "build_executors_lock.py v1.0"

executors:
  codecraft-native:
    tier: 3
    clearance: "Execute WITH approval per Charter V1.1"
    jurisdiction: "All 20 canonical schools"
    capabilities: [BLUEPRINT, JS, PYTHON, NATIVE]
    charter_version: "1.1"
    wasm_dispatch: true
    hash: "sha256:abcd1234..."  # Hash of executor definition
    phoenix_recovery:
      - "codecraft-native/src/lib.rs"
      - "codecraft-native/Cargo.toml"
      - "lexicon/canon.executors.lock.yaml"

metadata:
  schema_version: "2.0"
  lock_type: "executors"
  total_executors: 1
  integrity_hash: "sha256:final_lock_hash..."
```

---

#### **Step 3: Create `tools/validate_executors_lock.py`**

**Purpose:** Validate executor lock structure and constitutional compliance

**Checks:**
1. **Schema Validation:**
   - Required fields present (tier, jurisdiction, capabilities, charter_version)
   - Schema version matches expected (2.0)
   - Generated timestamp is valid

2. **Constitutional Validation:**
   - Tier is valid (0-4)
   - Clearance matches Charter V1.1 definitions
   - Jurisdiction references valid canon (20 schools)
   - Charter version exists and is current

3. **Capability Validation:**
   - Capabilities list is non-empty
   - Each capability is recognized (BLUEPRINT, JS, PYTHON, NATIVE, WASM)
   - WASM dispatch configuration is valid (boolean)

4. **Phoenix Recovery Validation:**
   - Recovery anchors exist (3-point minimum)
   - Files referenced exist on disk
   - Anchors span multiple repos (Infrastructure, languages, native)

5. **Hash Integrity:**
   - Executor definition hash matches computed hash
   - Final lock integrity hash matches computed hash

**Exit Codes:**
- `0` = Valid executor lock
- `1` = Schema validation failed
- `2` = Constitutional validation failed
- `3` = Capability validation failed
- `4` = Phoenix recovery validation failed
- `5` = Hash integrity failed

---

#### **Step 4: Upgrade `tools/validate_dual_locks.py` → `validate_sovereignty.py`**

**New Name:** `tools/validate_sovereignty.py` (or add `--triple-lock` flag)

**Purpose:** Validate complete sovereignty across all three locks

**Triple-Lock Validation Algorithm:**

```python
def validate_sovereignty(triple_lock=False):
    """
    Validate sovereignty of CodeCraft VM.
    
    Dual Lock (default):
      - canon.lock.yaml (20 schools)
      - canon.partitions.lock.yaml (6 partitions)
    
    Triple Lock (Phase 2.B):
      - canon.lock.yaml (20 schools)
      - canon.partitions.lock.yaml (6 partitions)
      - canon.executors.lock.yaml (1+ executors)
    """
    results = {
        "schools": validate_schools_lock(),      # 20 schools required
        "partitions": validate_partitions_lock(), # 6 partitions required
    }
    
    if triple_lock:
        results["executors"] = validate_executors_lock()  # 1+ executor required
    
    # Check for cross-governance bleed
    check_no_school_partition_overlap()
    
    # Sovereignty = ALL locks valid
    sovereignty = all(results.values())
    
    print(f"🔒 Schools Lock: {'✅' if results['schools'] else '❌'}")
    print(f"🔒 Partitions Lock: {'✅' if results['partitions'] else '❌'}")
    if triple_lock:
        print(f"🔒 Executors Lock: {'✅' if results['executors'] else '❌'}")
    
    print(f"\n⚖️ Sovereignty: {'✅ VALID' if sovereignty else '❌ INVALID'}")
    
    return sovereignty
```

**Usage:**
```bash
# Dual lock (current)
python tools/validate_sovereignty.py

# Triple lock (Phase 2.B)
python tools/validate_sovereignty.py --triple-lock
```

---

#### **Step 5: Update GitHub Workflows**

**`.github/workflows/canon-verify.yml`** - Add executor validation:

```yaml
name: Canon Verify

on: [push, pull_request]

jobs:
  verify-locks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install pyyaml
      
      - name: Validate Schools Lock
        run: python tools/rosetta_archaeologist.py verify
      
      - name: Validate Partitions Lock
        run: python tools/validate_partitions_lock.py
      
      - name: Validate Executors Lock (Phase 2.B)
        run: python tools/validate_executors_lock.py
      
      - name: Validate Triple-Lock Sovereignty
        run: python tools/validate_sovereignty.py --triple-lock
```

---

### **Complete Triple-Lock Pipeline (Phase 2.B)**

```bash
# Step 1: Generate Schools Lock
python tools/rosetta_archaeologist.py extract --out lexicon/canon.lock.yaml

# Step 2: Generate Partitions Lock
python tools/build_partitions_lock.py

# Step 3: Generate Executors Lock (NEW - Phase 2.B)
python tools/build_executors_lock.py

# Step 4: Validate Triple-Lock Sovereignty (NEW - Phase 2.B)
python tools/validate_sovereignty.py --triple-lock

# Step 5: Attest & Sign (Optional)
python tools/lock_attestor.py --sign-all
```

**Output:**
```
🔒 Schools Lock: ✅ (20 schools)
🔒 Partitions Lock: ✅ (6 partitions, 25 entries)
🔒 Executors Lock: ✅ (1 executor: codecraft-native)

⚖️ Sovereignty: ✅ VALID

🦀 CodeCraft VM Soul Bound
   Tier: 3 (Execute WITH approval)
   Jurisdiction: All 20 canonical schools
   Charter: V1.1 (Crown Accord compliant)
```

---

### **Sovereignty Attestation (Phase 2.C)**

After Triple-Lock validation passes, generate cryptographic attestation:

```bash
python tools/lock_attestor.py --triple-lock --sign
```

**Output:** `receipts/sovereignty_attest_YYYYMMDD_HHMMSS.txt`

```
🏛️ CODECRAFT SOVEREIGNTY ATTESTATION
Generated: 2025-11-12 15:30:00 EST
Protocol: Triple-Lock Validation v2.0

LOCK INVENTORY:
  Schools: canon.lock.yaml
    SHA256: 6eed14003a008b72d3195c7ca2748ac264a8a1a33444dffc112906f45e6763fd
    Size: 45123 bytes
    Schools: 20

  Partitions: canon.partitions.lock.yaml
    SHA256: abc123...
    Size: 12456 bytes
    Partitions: 6
    Entries: 25

  Executors: canon.executors.lock.yaml
    SHA256: def456...
    Size: 3456 bytes
    Executors: 1 (codecraft-native)

SOVEREIGNTY STATUS: ✅ VALID
  - No cross-governance bleed detected
  - All constitutional requirements met
  - Phoenix recovery anchors present (3-point)
  - Charter V1.1 compliance verified

🦀 VM SOUL BOUND
   Tier: 3 (Execute WITH approval)
   Clearance: Charter V1.1
   Jurisdiction: All 20 canonical schools
   Capabilities: BLUEPRINT, JS, PYTHON, NATIVE

Attestor: lock_attestor.py v2.0
Ceremony: Triple-Lock Validation + Cryptographic Seal
```

---

**Phase 2.B Complete:** VM soul bound through Triple-Lock sovereignty. 🦀🐦‍🔥
