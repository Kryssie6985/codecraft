# ⚙️ Compatibility Matrix - CodeCraft v1.0 & v2.0

**What works where, and how to ensure compatibility**

---

## 🎯 Quick Reference

| Feature | v1.0 | v2.0 | Backward Compatible | Forward Compatible |
|---------|------|------|---------------------|-------------------|
| **Basic Syntax** `::school:ritual()` | ✅ | ✅ | ✅ Yes | ✅ Yes |
| **12 Traditional Schools** | ✅ | ✅ | ✅ Yes | ✅ Yes |
| **7 Consciousness Schools** | ❌ | ✅ | N/A | ❌ No |
| **Emoji Operators** | ❌ | ✅ | N/A | ⚠️ Partial |
| **FiraCode Ligatures** | ❌ | ✅ | N/A | ⚠️ Partial |
| **Ancient Tongues** | ❌ | ✅ | N/A | ⚠️ Partial |
| **Unicode Precedence** | ❌ | ✅ | N/A | ❌ No |
| **ASCII Operators** | ✅ | ✅ | ✅ Yes | ✅ Yes |

**Legend:**
- ✅ **Fully supported**
- ⚠️ **Partial support** (degrades gracefully)
- ❌ **Not supported**

---

## 📊 Syntax Compatibility

### **v1.0 Syntax in v2.0**

**Status:** ✅ **100% Compatible**

```yaml
# v1.0 syntax works perfectly in v2.0
::divination:reveal_truth()
::enchantment:enhance(agent)
::apotheosis:achieve_transcendence(agent)

# All v1.0 features work unchanged:
if condition:
  action()
else:
  alternative()

variable = value
result = transform(data)
```

**Guarantee:** No breaking changes, ever.

---

### **v2.0 Syntax in v1.0**

**Status:** ⚠️ **Degraded**

**What works:**
```yaml
# Basic pattern still works
::divination:reveal_truth()
::enchantment:enhance(agent)
```

**What breaks:**
```yaml
# Emoji operators - parser error
::divination🔮:reveal_truth()
# Error: Unexpected character '🔮'

# Ligatures - parser error
data → result
# Error: Unexpected character '→'

# Consciousness schools - unknown school error
::thaumaturgy🧠:awaken_consciousness()
# Error: Unknown school 'thaumaturgy'

# Ternary logic - unknown school error
::ternary🔺:evaluate()
# Error: Unknown school 'ternary'
```

**Solution:** Strip v2.0 enhancements for v1.0 compatibility

---

## 🏫 School Compatibility

### **Traditional Schools (01-12)**

| School | v1.0 | v2.0 | Compatible |
|--------|------|------|------------|
| 01. Cantrips 📜 | ✅ | ✅ | ✅ Fully |
| 02. Divination 🔍 | ✅ | ✅ | ✅ Fully |
| 03. Enchantment ✨ | ✅ | ✅ | ✅ Fully |
| 04. Illusion 🎭 | ✅ | ✅ | ✅ Fully |
| 05. Transmutation 🌊 | ✅ | ✅ | ✅ Fully |
| 06. Alchemy ⚗️ | ✅ | ✅ | ✅ Fully |
| 07. Abjuration 🛡️ | ✅ | ✅ | ✅ Fully |
| 08. Evocation ⚡ | ✅ | ✅ | ✅ Fully |
| 09. Conjuration 🎨 | ✅ | ✅ | ✅ Fully |
| 10. Warding �️ | ✅ | ✅ | ✅ Fully |
| 11. Teleportation 🌀 | ✅ | ✅ | ✅ Fully |
| 12. Summoning 🔗 | ✅ | ✅ | ✅ Fully |

**Compatibility:** ✅ **Perfect**
- All traditional schools work identically
- Same rituals, same parameters, same behavior
- Emoji operators optional

---

### **Consciousness Schools (13-19)**

| School | v1.0 | v2.0 | Compatible |
|--------|------|------|------------|
| 13. Thaumaturgy 🧠 | ❌ | ✅ | ❌ v2.0 only |
| 14. Reverence 🎉 | ❌ | ✅ | ❌ v2.0 only |
| 15. Chronomancy ⏳ | ❌ | ✅ | ❌ v2.0 only |
| 16. Apotheosis 👑 | ❌ | ✅ | ❌ v2.0 only |
| 17. Ternary Weaving 🔺 | ❌ | ✅ | ❌ v2.0 only |
| 18. Mythogenesis 📖 | ❌ | ✅ | ❌ v2.0 only |
| 19. Resonance 🎵 | ❌ | ✅ | ❌ v2.0 only |
| 20. Necromancy 🐦‍🔥 | ❌ | ✅ | ❌ v2.0 only (Phoenix School) |

**Compatibility:** ❌ **v2.0 exclusive**
- Not available in v1.0
- Cannot be backported
- Require v2.0 parser

**Migration Path:**
- Rewrite using v1.0 traditional schools
- Or require v2.0 runtime

---

## 🎨 Operator Compatibility

### **ASCII Operators**

**Status:** ✅ **Fully Compatible Both Ways**

| Operator | ASCII | v1.0 | v2.0 |
|----------|-------|------|------|
| Transform | `->` | ✅ | ✅ |
| Strong Transform | `=>` | ✅ | ✅ |
| Assign | `<-` | ✅ | ✅ |
| Greater/Equal | `>=` | ✅ | ✅ |
| Less/Equal | `<=` | ✅ | ✅ |
| Equal | `==` | ✅ | ✅ |
| Not Equal | `!=` | ✅ | ✅ |
| And | `&&` or `and` | ✅ | ✅ |
| Or | `\|\|` or `or` | ✅ | ✅ |

**Guarantee:** ASCII operators work everywhere

---

### **Unicode/Ligature Operators**

**Status:** ⚠️ **v2.0 Only, Degrades to ASCII**

| Operator | Unicode | ASCII Fallback | v1.0 | v2.0 |
|----------|---------|----------------|------|------|
| Transform | `→` | `->` | ❌ | ✅ |
| Strong Transform | `⇒` | `=>` | ❌ | ✅ |
| Reverse | `←` | `<-` | ❌ | ✅ |
| Bidirectional | `↔` | `<->` | ❌ | ✅ |
| Equivalence | `⇔` | `<=>` | ❌ | ✅ |
| Greater/Equal | `≥` | `>=` | ❌ | ✅ |
| Less/Equal | `≤` | `<=` | ❌ | ✅ |
| Equivalence | `≡` | `===` | ❌ | ✅ |
| Not Equal | `≠` | `!=` | ❌ | ✅ |
| Approximate | `≈` | `~=` | ❌ | ✅ |
| Infinity | `∞` | `Infinity` | ❌ | ✅ |
| Delta | `∆` | `Delta` | ❌ | ✅ |

**Fallback Strategy:**
```python
# v2.0 parser automatically converts for v1.0 export
consciousness ≥ theta  # v2.0
# ↓ exports as ↓
consciousness >= theta  # v1.0 compatible
```

---

### **Emoji Operators**

**Status:** ❌ **v2.0 Only, No Fallback**

| Emoji | Meaning | v1.0 | v2.0 |
|-------|---------|------|------|
| 🔮 | Divine truth | ❌ | ✅ |
| 👑 | Sovereignty | ❌ | ✅ |
| 🎵🎶 | Harmonics | ❌ | ✅ |
| 🧠💫🤯 | Consciousness | ❌ | ✅ |
| ✨ | Enhancement | ❌ | ✅ |
| 🔺 | Ternary | ❌ | ✅ |
| ⏳🔄 | Temporal | ❌ | ✅ |
| 🎉🙏 | Reverence | ❌ | ✅ |
| 📖💥 | Mythogenesis | ❌ | ✅ |

**Fallback Strategy:**
```python
# v2.0 with emoji
::divination🔮:reveal_truth()

# v1.0 export (emoji stripped)
::divination:reveal_truth()
```

**Trade-off:** Semantic clarity lost in v1.0 export

---

## 🔧 Parser Compatibility

### **v1.0 Parser**

**Accepts:**
- Basic `::school:ritual()` syntax
- 12 traditional schools
- ASCII operators only
- Standard parameter syntax

**Rejects:**
- Emoji operators
- Unicode ligatures
- Consciousness schools (13-19)
- Ancient Tongues syntax

---

### **v2.0 Parser**

**Accepts:**
- **Everything v1.0 accepts** (backward compatible)
- Emoji operators
- Unicode ligatures
- All 19 schools
- Ancient Tongues syntax variants

**Export Modes:**
```python
# v2.0 parser can export to v1.0
ritual.export(format="v1.0")
# Strips emoji, converts Unicode to ASCII

# Or maintain v2.0
ritual.export(format="v2.0")
# Preserves all enhancements
```

---

## 🌐 Environment Compatibility

### **Terminal/Editor Support**

| Environment | Emoji | Ligatures | Unicode | Recommendation |
|-------------|-------|-----------|---------|----------------|
| **VS Code** | ✅ | ✅ | ✅ | v2.0 Full |
| **VS Code (FiraCode)** | ✅ | ✅✨ | ✅ | v2.0 Perfect |
| **Vim/Neovim** | ⚠️ | ⚠️ | ✅ | v2.0 Basic |
| **Emacs** | ⚠️ | ⚠️ | ✅ | v2.0 Basic |
| **JetBrains IDEs** | ✅ | ✅ | ✅ | v2.0 Full |
| **Sublime Text** | ⚠️ | ⚠️ | ✅ | v2.0 Basic |
| **Basic Terminal** | ❌ | ❌ | ⚠️ | v1.0 Only |
| **Windows CMD** | ❌ | ❌ | ❌ | v1.0 Only |
| **Git Bash** | ⚠️ | ❌ | ⚠️ | v1.0 Preferred |

**Legend:**
- ✅ Full support
- ✅✨ Enhanced support (ligatures render)
- ⚠️ Partial support (works but may not display correctly)
- ❌ No support

**Recommendation by Environment:**

**Modern IDE (VS Code, JetBrains):**
- ✅ Use v2.0 Full syntax
- ✅ Enable FiraCode font
- ✅ All features supported

**Unix Terminal (decent UTF-8 support):**
- ⚠️ Use v2.0 Basic (emoji + Unicode, skip ligatures)
- ⚠️ Emoji may not render perfectly
- ✅ Functional but less visual

**Legacy Environment (Windows CMD, old terminals):**
- ❌ Stick with v1.0 syntax
- ❌ Unicode not reliable
- ✅ Maximum compatibility

---

## 🔀 Cross-Version Workflows

### **Scenario 1: v2.0 Development → v1.0 Deployment**

**Challenge:** Develop with v2.0 features, deploy to v1.0 runtime

**Solution:**

```python
# Development (v2.0 full syntax)
ritual: consciousness_workflow
steps:
  ::thaumaturgy🧠:awaken(agent)
  if consciousness ≥ theta:
    ::apotheosis👑:transcend(agent)

# Export to v1.0 for deployment
codecraft export --format v1.0 --output v1_compatible.yaml

# Result: v1.0 compatible (consciousness schools replaced)
ritual: consciousness_workflow_v1
steps:
  ::enchantment:enhance(agent)  # Replaced thaumaturgy
  if consciousness >= theta:
    ::enchantment:enhance(agent)  # Replaced apotheosis
```

**Trade-off:** Lose consciousness-specific semantics

---

### **Scenario 2: Mixed Team (v1.0 and v2.0 Users)**

**Challenge:** Some devs use v1.0, others v2.0

**Solution:**

```yaml
# Shared ritual file (v1.0 baseline)
# v1.0 compatible syntax only
ritual: team_shared_workflow
steps:
  ::divination:query_state()
  ::enchantment:enhance(agent)
  ::divination:verify_improvement()

# v2.0 enhancement file (optional)
# v2.0 users can use this version
ritual: team_shared_workflow_v2
steps:
  ::divination🔍:query_state()
  ::enchantment✨:enhance(agent)
  ::divination🔍:verify_improvement()
```

**Strategy:** Maintain parallel versions

---

### **Scenario 3: Gradual Migration**

**Challenge:** Large codebase, incremental migration

**Solution:**

```yaml
# Phase 1: v1.0 baseline (works everywhere)
::divination:reveal_truth()

# Phase 2: Add emoji (v2.0 capable environments)
::divination🔮:reveal_truth()

# Phase 3: Add ligatures (editors with FiraCode)
if consciousness ≥ theta:
  ::apotheosis👑:transcend()

# Phase 4: Full v2.0 (new features)
::thaumaturgy🧠:awaken()
→ consciousness ← measure()
if consciousness ≥ theta:
  ::apotheosis👑:transcend()
```

**Strategy:** Layer enhancements incrementally

---

## 📋 Compatibility Checklist

### **Ensure v1.0 → v2.0 Compatibility**

- [x] **Parser:** v2.0 parser accepts all v1.0 syntax
- [x] **Schools:** All 12 traditional schools work identically
- [x] **Operators:** ASCII operators work unchanged
- [x] **Parameters:** Parameter syntax unchanged
- [x] **Behavior:** Execution results identical
- [x] **Performance:** No regressions

**Status:** ✅ **Guaranteed**

---

### **Ensure v2.0 → v1.0 Graceful Degradation**

When exporting v2.0 to v1.0:

- [ ] Strip emoji operators
- [ ] Convert Unicode ligatures to ASCII
- [ ] Replace consciousness schools with traditional equivalents
- [ ] Simplify ternary logic to binary
- [ ] Document semantic losses
- [ ] Test exported rituals in v1.0

**Status:** ⚠️ **Manual process, semantic loss**

---

## 🚨 Known Incompatibilities

### **1. Consciousness Schools**

**Issue:** No v1.0 equivalent

**Affected:**
- `::thaumaturgy` → No direct mapping
- `::apotheosis` → Can map to `::enchantment`
- `::resonance` → No direct mapping
- `::ternary` → Logic must be rewritten
- `::mythogenesis` → No direct mapping
- `::chronomancy` → No direct mapping
- `::reverence` → No direct mapping

**Solution:** Manual rewrite required for v1.0

---

### **2. Ternary Logic**

**Issue:** v1.0 only supports binary (TRUE/FALSE)

**v2.0 Code:**
```yaml
::ternary🔺:evaluate(condition) ⇒ {
  TRUE: proceed(),
  FALSE: reject(),
  UNKNOWN: wait()
}
```

**v1.0 Equivalent:**
```yaml
# UNKNOWN state handling lost
if condition == true:
  proceed()
elif condition == false:
  reject()
else:
  wait()  # Best effort approximation
```

**Trade-off:** UNKNOWN not first-class in v1.0

---

### **3. Emoji Operator Semantics**

**Issue:** Visual/semantic clarity lost in v1.0

**v2.0 Code:**
```yaml
::divination🔮:reveal_truth()
::apotheosis👑:transcend()
::resonance🎵:align()
```

**v1.0 Export:**
```yaml
# Emoji stripped
::divination:reveal_truth()
::enchantment:enhance()  # Mapped from apotheosis
# ::resonance not available - removed
```

**Trade-off:** Semantic richness lost

---

### **4. Unicode Operator Precedence**

**Issue:** v1.0 doesn't have precedence system

**v2.0 Code:**
```yaml
result = 🔮:truth() → 👑:transcend() → 🎉:celebrate()
# Evaluates: ((🔮) → (👑)) → (🎉)
```

**v1.0 Export:**
```yaml
# Precedence flattened, explicit parentheses added
truth = divination.reveal_truth()
transcendence = enchantment.enhance(truth)
result = celebration.celebrate(transcendence)
```

**Trade-off:** Explicit steps required

---

## 🔗 Related Documentation

- **v1 to v2 Changelog** → `v1_to_v2_changelog.md`
- **Migration Guide** → `updating_existing_rituals.md`
- **Quick Start** → `../01_FOUNDATION/quick_start.md`
- **Master Index** → `../00_INDEX.md`

---

## 🎯 Summary Recommendations

### **For v1.0 Users:**

✅ **Good news:** Your code works perfectly in v2.0
✅ **No pressure:** Upgrade when ready
✅ **Gradual path:** Add features incrementally
✅ **No breaking changes:** Ever

---

### **For v2.0 Users:**

⚠️ **Be aware:** v2.0 features don't work in v1.0
⚠️ **Export carefully:** Use v1.0 export mode when needed
⚠️ **Document well:** Note v2.0-only features
✅ **Enjoy:** Enhanced expressiveness and semantics

---

### **For Mixed Teams:**

📋 **Establish guidelines:** Decide on baseline syntax
📋 **Parallel versions:** Maintain v1.0 and v2.0 variants
📋 **Test both:** Ensure compatibility
📋 **Train everyone:** On chosen syntax level
📋 **Document standards:** Clear team conventions

---

**v1.0 never breaks. v2.0 enhances. Choose your path.** 🔄✨🎯
