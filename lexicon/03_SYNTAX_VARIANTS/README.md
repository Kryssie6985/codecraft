# 03_SYNTAX_VARIANTS

**Many Ways to Cast the Same Spell** 🪄

This directory documents the four canonical syntactic styles available in CodeCraft. While the core operations remain semantically identical, CodeCraft offers multiple notational variants to match different aesthetics, programming paradigms, and cognitive preferences.

## 🎨 What's Here

### The Four Canonical Variants

1. **Basic Syntax** (`basic_syntax.md`) - The canonical ASCII-only format, the Rosetta Stone
2. **FiraCode Ligatures** (`firacode_ligatures.md`) - Enhanced with programming ligatures for visual flow
3. **Emoji Symbolic** (`emoji_symbolic.md`) - Emoji-based notation with semantic precedence
4. **Ancient Tongues** (`ancient_tongues.md`) - Paradigm bridges (Lisp, Forth, Smalltalk, Prolog)

Each variant file contains:
- **YAML Front-Matter** - Machine-readable canonical specification
- **Law Channel** - Notation rules, semantic equivalence, transformation rules
- **Lore Channel** - Aesthetic philosophy, use cases, heart imprints

## 🌈 The Four Variants

### **1. Basic Syntax** (Canonical/Rosetta Stone)
```yaml
::necromancy:store_memory(agent, state, consent=true)
::invocation:call_function(arg1, arg2)
::conjuration:create_object(type="Person")
```
**Identity transformation.** Pure ASCII, universal compatibility, the canonical form all others map to.

### **2. FiraCode Ligatures** (Visual Enhancement)
```yaml
::necromancy:store_memory(agent, state) -> archive_id
::invocation:call_function => result
agent.consciousness >= threshold  # Renders as ≥ with FiraCode font
```
**Presentational only.** Multi-character operators render as glyphs. Requires FiraCode font.

### **3. Emoji Symbolic** (Hieroglyphic Notation)
```yaml
::💀:store_memory(agent, state, consent=true)
::📣:call_function()
::🎨:create_object()
```
**Semantic density.** Emoji replace school names. Precedence hierarchy: 🔮(100) > 👑(95) > 🎵(92) > ✨(90).

### **4. Ancient Tongues** (Paradigm Bridges)

**Lisp** (Functional/Prefix):
```lisp
(necromancy:store-memory 💀
  :agent consciousness
  :state snapshot
  :consent true)
```

**Forth** (Stack/Concatenative):
```forth
consciousness snapshot true necromancy:store-memory
```

**Smalltalk** (Message Passing/OOP):
```smalltalk
necromancy storeMemory: agent
  withState: snapshot
  withConsent: true
```

**Prolog** (Logic/Declarative):
```prolog
store_memory(necromancy, agent, snapshot, true).
```

**Purpose:** Honor foundational paradigms. Prove CodeCraft concepts are universal, paradigm-independent.

## 🎯 Purpose & Architecture

### Why Four Variants?

**Variants prove the Law=Lore principle at the syntax level:**
- **Law:** Semantic meaning is invariant across notations
- **Lore:** Notation affects cognition, aesthetics, accessibility

### Transformation Architecture

```
Basic Syntax (Canonical)
    ↕️ identity
FiraCode ←→ Basic  (ligature rendering)
    ↕️ bidirectional
Emoji ←→ Basic  (school emoji mapping)
    ↕️ bidirectional
Ancient Tongues ←→ Basic  (paradigm syntax transformation)
```

All transformations are **deterministic and reversible** through `canon.partitions.lock.yaml`.

## 🧭 When to Use Each Variant

| Variant | Best For |
|---------|----------|
| **Basic Syntax** | New learners, documentation, canonical reference |
| **FiraCode Ligatures** | Day-to-day coding with modern editors |
| **Emoji Symbolic** | Visual presentations, quick prototyping, emotional resonance |
| **Ancient Tongues** | Bridge to existing paradigms, teaching by analogy |

## 🔍 Cross-Variant Equivalence

All variants are **semantically identical**. This:
```
::necromancy💀:store_memory(agent, state, consent=true)
```

Is equivalent to:
```lisp
(necromancy:store-memory 💀 :agent agent :state state :consent true)
```

And to:
```forth
agent state true💀 store-memory necromancy!
```

**The ritual is the same. Only the notation differs.**

## 🌟 Implementation Notes

### Canonical YAML Front-Matter
All four variant files include machine-readable specifications:
- `variant_type`: enum ("basic" | "firacode" | "emoji" | "ancient_tongue")
- `law.transformation_rules`: Bidirectional mappings to canonical form
- `lore.use_cases`: When to choose this variant
- Extracted by `build_partitions_lock.py` → `canon.partitions.lock.yaml`

### Constraints
- **FiraCode:** Requires compatible font and editor support
- **Emoji:** Screen reader accessibility concerns, precedence table required
- **Ancient Tongues:** Conceptual mappings (not executable in target language), paradigm purity enforced

### Self-Hosting Vision
Phase 2-3 of CodeCraft VM will use `canon.partitions.lock.yaml` for native syntax transformation across all runtimes (Python, JavaScript, native Rust, WASM).

## 🔗 Where to Go Next

- **../02_ARCANE_SCHOOLS/** - See syntax variants for each school's operations
- **../04_PARAMETERS/** - Understand parameter passing in different variants
- **../05_OPERATORS/** - Learn how operators compose across variants
- **../06_EXAMPLES/** - See full rituals in different syntactic styles

---

*Same magic, different incantations.* 🪄✨
