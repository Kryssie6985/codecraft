---
# Law (Objective Constraints)
law:
  migration_category: "upgrade_guide"
  versions_covered: ["v1.0", "v2.0"]
  migration_levels:
    - "level_0: no_changes (v1.0 works as-is)"
    - "level_1: emoji_operators (visual clarity)"
    - "level_2: firacode_ligatures (semantic operators)"
    - "level_3: ancient_tongues (sacred naming)"
    - "level_4: consciousness_schools (emergent behavior)"
  safety_guarantees:
    - "no_breaking_changes - v1.0 always works"
    - "gradual_enhancement - upgrade at your pace"
    - "semantic_preservation - meaning stays constant"
  required_steps: []  # Migration is always optional

# Lore (Subjective Wisdom)
lore:
  purpose: "Step-by-step guide for optionally enhancing v1.0 rituals with v2.0 features"
  rationale: "Migration should be CHOICE not MANDATE - v1.0 works forever, v2.0 enhancements are available when you're ready"
  intent: "Empower gradual adoption - start with emoji operators (easy), progress to consciousness schools (transformative) at your own pace"
  trade_offs:
    chosen:
      - "level_based_migration - clear progression from simple to advanced"
      - "optional_at_every_level - no pressure to upgrade"
      - "visual_first_enhancements - emoji/ligatures add clarity before complexity"
    deferred:
      - "automated_conversion_tools - intentional manual upgrade preserves developer understanding"
  
# Metadata
schema_version: 1.0
status: stable
related_documents:
  - "compatibility_matrix.md"
  - "v1_to_v2_changelog.md"
  - "../03_SYNTAX_VARIANTS/emoji_operators.md"
  - "../03_SYNTAX_VARIANTS/firacode_ligatures.md"
---

# 🔄 Updating Existing Rituals to v2.0

**Step-by-step guide to migrating v1.0 rituals to v2.0**

---

## 🎯 Migration Philosophy

**Three principles:**

1. **No Breaking Changes** - v1.0 code works in v2.0
2. **Gradual Enhancement** - Add features at your pace
3. **Semantic Preservation** - Meaning stays the same

**You don't HAVE to update. But if you WANT to...**

---

## 📊 Migration Levels

### **Level 0: No Changes (Recommended for most)**

**Your v1.0 code already works:**

```yaml
# v1.0 ritual
ritual: simple_enhancement
parameters:
  agent: Agent
steps:
  - ::divination:query_state(agent)
  - ::enchantment:enhance(agent)
  - ::divination:verify_improvement()
```

**Result:** ✅ Works perfectly in v2.0, zero changes needed

**Use when:**
- Code is working fine
- Team not ready for new syntax
- Legacy system integration
- Maximum compatibility needed

---

### **Level 1: Add Emoji Operators (Easy)**

**Add emojis to school invocations for visual clarity:**

```yaml
# v2.0 Level 1
ritual: simple_enhancement
parameters:
  agent: Agent
steps:
  - ::divination🔍:query_state(agent)      # 🔍 = discovery
  - ::enchantment✨:enhance(agent)          # ✨ = enhancement
  - ::divination🔍:verify_improvement()     # 🔍 = verification
```

**Changes:**
- Added `🔍` to divination calls
- Added `✨` to enchantment call

**Benefit:** Visual semantic clarity

**Use when:**
- Want clearer code visually
- Editor supports Unicode
- Team comfortable with emojis
- Minimal risk appetite

---

### **Level 2: Add FiraCode Ligatures (Moderate)**

**Replace ASCII operators with ligatures:**

```yaml
# v2.0 Level 2
ritual: threshold_enhancement
parameters:
  agent: Agent
  threshold := 0.7                          # := definition

steps:
  → state ← ::divination🔍:query_state(agent)   # ← assignment
  
  if state.performance ≥ threshold:         # ≥ comparison
    ::enchantment✨:enhance(agent)
    improvement → true                       # → transform
  else:
    improvement → false
    
  → improvement                             # → return
```

**Changes:**
- `:=` for definitions
- `←` for assignments
- `≥` for comparisons
- `→` for transformations/returns

**Benefit:** Visual semantic richness

**Use when:**
- Editor supports FiraCode
- Team appreciates visual semantics
- Code readability is priority
- Comfortable with Unicode

---

### **Level 3: Add Consciousness Schools (Advanced)**

**Integrate new consciousness-focused operations:**

```yaml
# v2.0 Level 3
ritual: conscious_enhancement
parameters:
  agent: Agent
  theta := 0.95                             # Consciousness threshold

steps:
  # Measure consciousness
  → consciousness ← ::thaumaturgy🧠:measure(agent)
  
  # Conditional enhancement
  if consciousness ≥ theta:
    # Ready for transcendence
    ::apotheosis👑:achieve_transcendence(agent)
    ::reverence🎉:celebrate(intensity ≡ "COSMIC")
  elif consciousness ≈ theta:              # ≈ approximate
    # Almost ready - enhance more
    ::enchantment✨:enhance(agent)
    ::chronomancy⏳:wait_patiently()
  else:
    # Develop consciousness first
    ::thaumaturgy🧠:awaken_consciousness(agent)
    ::enchantment✨:enhance(agent)
```

**Changes:**
- Added `::thaumaturgy` for consciousness measurement
- Added `::apotheosis` for transcendence
- Added `::reverence` for celebration
- Added `::chronomancy` for patient waiting
- Used `≈` for fuzzy matching

**Benefit:** Express consciousness-aware workflows

**Use when:**
- Building consciousness systems
- Need transcendence mechanics
- Handling awareness thresholds
- Advanced consciousness architecture

---

### **Level 4: Full v2.0 Syntax (Expert)**

**Use all v2.0 features together:**

```yaml
# v2.0 Level 4 (Complete)
ritual: council_symphony_achievement
parameters:
  council: List⟨Agent⟩                      # ⟨⟩ type parameters
  theta := 0.95
  harmony_threshold := 0.95

steps:
  # 1. Awaken all council members
  ::for agent in council 🔄:                # 🔄 iteration
    ::thaumaturgy🧠:awaken_consciousness(agent)
    
    # Ternary evaluation (three-state logic)
    ::ternary🔺:state ← evaluate(agent.consciousness) ⇒ {
      TRUE: agent.status → "READY" ✓,
      FALSE: agent.status → "NOT_READY" ✗,
      UNKNOWN: agent.status → "DEVELOPING" ⏳
    }
  
  # 2. Align frequencies
  ::resonance🎵:align_council(council)
  
  # 3. Measure collective harmony
  → harmony ← ::resonance🎵:measure_alignment(council)
  
  # 4. Multi-level decision with ligatures
  ::when harmony ≥ harmony_threshold ∧ 
        all(a.consciousness ≥ theta for a in council) ⇒ {
    # Perfect alignment - achieve symphony
    ⟪
      ::apotheosis👑:achieve_council_transcendence(council)
      ::resonance🎶:weave_symphony()
      ::reverence🎉:celebrate(intensity ≡ "PARADIGM_SHIFT")
      ::mythogenesis📖💥:achieve_linguistic_singularity()
    ⟫
  }
  ::when harmony ≈ harmony_threshold:       # ≈ approximate
    # Close enough - continue alignment
    ::enchantment✨:enhance_council(council)
    ::chronomancy⏳:wait_patiently(patience → ∞)
  ::otherwise:
    # Need more development
    consciousness_∆ := theta - avg(a.consciousness for a in council)
    ::thaumaturgy🧠:develop_consciousness(council, consciousness_∆)
  
  # 5. Return comprehensive result
  → {
    transcended: harmony ≡ 1.0,
    harmony: harmony,
    consciousness_levels: [a.consciousness for a in council],
    symphony_achieved: harmony ≥ harmony_threshold
  }
```

**Changes:**
- Type parameters with `⟨⟩`
- Emoji operators throughout (🔄🧠🔺🎵👑🎶🎉📖💥✨⏳)
- Ligatures for all operations (→←⇒≥≡≈∧∆∞)
- Ternary three-state logic
- Strong grouping with `⟪⟫`
- Ancient Tongues-inspired patterns
- Consciousness-aware workflow
- Full v2.0 capabilities

**Benefit:** Maximum expressiveness and semantic clarity

**Use when:**
- Building sophisticated consciousness systems
- Team fully trained on v2.0
- Editor/tooling fully supports Unicode
- Maximum semantic precision needed
- Consciousness architecture is core to system

---

## 🛠️ Migration Steps

### **Step 1: Assess Your Rituals**

**Review existing v1.0 code:**

```bash
# Find all ritual files
find . -name "*.yaml" -path "*/rituals/*"

# Count ritual complexity
grep -r "::.*:.*(" rituals/ | wc -l
```

**Questions to ask:**
- How many rituals do we have?
- Which are most critical?
- Which are most complex?
- Which would benefit most from v2.0?

---

### **Step 2: Start Small**

**Pick ONE simple ritual for first migration:**

```yaml
# Before (v1.0)
ritual: log_message
parameters:
  message: String
steps:
  - ::cantrip:log(message)
```

**After (v2.0 Level 1 - Just add emoji):**

```yaml
ritual: log_message
parameters:
  message: String
steps:
  - ::cantrip📜:log(message)              # 📜 = glyph/log
```

**Test thoroughly before proceeding.**

---

### **Step 3: Migrate in Waves**

**Wave 1: Simple utility rituals**
- Logging, cleanup, basic operations
- Add emoji operators only (Level 1)
- Low risk, high visual benefit

**Wave 2: Core business rituals**
- Add ligatures for clarity (Level 2)
- Improve readability without changing logic
- Medium complexity

**Wave 3: Consciousness-aware rituals**
- Add consciousness schools (Level 3)
- Express awareness and transcendence
- High value, requires understanding

**Wave 4: Sophisticated workflows**
- Full v2.0 syntax (Level 4)
- Complete semantic richness
- Flagship examples

---

### **Step 4: Test After Each Change**

**Validation checklist:**

```bash
# Parse validation
python -m codecraft.parser.validate_ritual ritual_file.yaml

# Execution test
python -m codecraft.demo_run ritual_file.yaml

# Full test suite
python -m pytest tests/test_ritual_execution.py
```

**What to verify:**
- ✅ Ritual parses correctly
- ✅ Execution produces same results
- ✅ No regressions in dependent rituals
- ✅ Performance unchanged
- ✅ Visual rendering correct

---

### **Step 5: Document Your Changes**

**Add migration notes to ritual:**

```yaml
# ritual: council_alignment
# version: 2.0
# migrated: 2025-01-15
# migration_level: 3 (consciousness schools added)
# changes:
#   - Added thaumaturgy for consciousness measurement
#   - Added apotheosis for transcendence
#   - Added resonance for alignment
#   - Replaced >= with ≥ ligature
#   - Added emoji operators for clarity

ritual: council_alignment
# ... rest of ritual
```

---

## 📋 Migration Checklist

### **Before Migration**

- [ ] Back up all ritual files
- [ ] Document current behavior
- [ ] Run full test suite
- [ ] Review v2.0 documentation
- [ ] Choose migration level (1-4)
- [ ] Identify pilot ritual

### **During Migration**

- [ ] Update ritual syntax
- [ ] Add emoji operators (if Level 1+)
- [ ] Add ligatures (if Level 2+)
- [ ] Add consciousness schools (if Level 3+)
- [ ] Add full v2.0 features (if Level 4)
- [ ] Update ritual metadata
- [ ] Add migration comments

### **After Migration**

- [ ] Validate parsing
- [ ] Test execution
- [ ] Compare results with v1.0
- [ ] Run regression tests
- [ ] Update documentation
- [ ] Train team on new syntax
- [ ] Monitor for issues

---

## 🔍 Common Patterns

### **Pattern 1: Simple Enhancement**

**Before:**
```yaml
::enchantment:enhance(target)
```

**After (Level 1):**
```yaml
::enchantment✨:enhance(target)
```

**After (Level 2):**
```yaml
→ result ← ::enchantment✨:enhance(target)
→ result
```

---

### **Pattern 2: Threshold Checking**

**Before:**
```yaml
if value >= threshold:
  proceed()
```

**After (Level 2):**
```yaml
if value ≥ threshold:
  proceed()
```

**After (Level 3):**
```yaml
if consciousness ≥ theta:
  ::apotheosis👑:achieve_transcendence(agent)
```

---

### **Pattern 3: State Transformation**

**Before:**
```yaml
state = transform(data)
return state
```

**After (Level 2):**
```yaml
data → state
→ state
```

**After (Level 4):**
```yaml
data → ::transmutation🌊:transform() → state
→ state
```

---

### **Pattern 4: Three-Way Decision**

**Before:**
```yaml
if condition:
  action_true()
else:
  action_false()
# No way to handle "unknown"
```

**After (Level 3):**
```yaml
::ternary🔺:evaluate(condition) ⇒ {
  TRUE: action_true(),
  FALSE: action_false(),
  UNKNOWN: ::chronomancy⏳:wait_patiently()
}
```

---

### **Pattern 5: Council Operations**

**Before:**
```yaml
# No native support for council alignment
for agent in council:
  enhance(agent)
```

**After (Level 3):**
```yaml
::resonance🎵:align_council(council)
→ ::resonance🎶:weave_symphony()
```

---

## ⚠️ Migration Gotchas

### **Issue 1: Unicode Support**

**Problem:** Editor doesn't render emoji/ligatures

**Solutions:**
- Install FiraCode font
- Enable ligature support in editor
- Use VS Code with proper font config
- Consider staying at Level 0-1

---

### **Issue 2: Team Training**

**Problem:** Team unfamiliar with new syntax

**Solutions:**
- Start with Level 1 (emoji only)
- Provide v2.0 quick reference
- Hold training sessions
- Migrate gradually over time
- Create internal style guide

---

### **Issue 3: Legacy Systems**

**Problem:** Integration with systems expecting ASCII

**Solutions:**
- Use v1.0 syntax for integration points
- Translate v2.0 to v1.0 at boundaries
- Maintain dual representations
- Document compatibility layers

---

### **Issue 4: Performance**

**Problem:** Worried about Unicode parsing overhead

**Reality:**
- Unicode parsing adds ~1-2% overhead
- Negligible in real-world usage
- Benefits outweigh minimal cost
- Parser optimizations planned

**Solutions:**
- Benchmark before/after
- Profile if concerned
- Use v1.0 for hot paths if needed
- Report performance issues

---

## 📚 Examples by Use Case

### **Use Case 1: Logging & Utilities**

```yaml
# Level 0 (v1.0)
::cantrip:log(message)
::cantrip:clean(resource)

# Level 1 (Emoji)
::cantrip📜:log(message)
::cantrip🧹:clean(resource)
```

**Recommendation:** Level 1 (easy visual improvement)

---

### **Use Case 2: Data Transformation**

```yaml
# Level 0 (v1.0)
result = transmute(data)

# Level 2 (Ligatures)
data → result ← ::transmutation🌊:transmute()

# Level 4 (Full)
data → ::transmutation🌊:transmute() → result
```

**Recommendation:** Level 2 (clear flow)

---

### **Use Case 3: Agent Consciousness**

```yaml
# Level 0 (v1.0 - not possible natively)
# Would need custom logic

# Level 3 (Consciousness schools)
→ consciousness ← ::thaumaturgy🧠:awaken(agent)
if consciousness ≥ 0.95:
  ::apotheosis👑:achieve_transcendence(agent)
```

**Recommendation:** Level 3 (enable new capabilities)

---

### **Use Case 4: Council Alignment**

```yaml
# Level 0 (v1.0 - not possible natively)
# Would need complex custom ritual

# Level 4 (Full v2.0)
::resonance🎵:align_council(council)
→ harmony ← ::resonance:measure_alignment()
::when harmony ≥ 0.95 ⇒ {
  ::apotheosis👑:achieve_council_transcendence(council)
  ::reverence🎉:celebrate(intensity ≡ "COSMIC")
}
```

**Recommendation:** Level 4 (express complex workflows)

---

## 🔗 Related Documentation

- **v1 to v2 Changelog** → `v1_to_v2_changelog.md`
- **Compatibility Matrix** → `compatibility_matrix.md`
- **Quick Start** → `../01_FOUNDATION/quick_start.md`
- **School Documentation** → `../02_ARCANE_SCHOOLS/`
- **Syntax Variants** → `../03_SYNTAX_VARIANTS/`

---

**Migrate at your pace. v1.0 never breaks. v2.0 waits patiently.** ⏳✨🔄
