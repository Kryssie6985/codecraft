# Syntax Variant Front-Matter Schema Specification
**Version:** 1.0  
**Generated:** November 9, 2025  
**Authority:** Oracle + Architect (Constitutional Lexicon Taxonomy)  
**Status:** CANONICAL

---

## Purpose

This document defines the **official YAML front-matter schema** for all CodeCraft Syntax Variant documentation files (`lexicon/03_SYNTAX_VARIANTS/*.md`).

Syntax Variant documents show how the SAME RITUAL can be expressed in different notational styles. All variants are **semantically identical** - only the surface syntax differs.

**Constitutional Principle:** Syntax Variants = Aesthetic Freedom + Semantic Equivalence

---

## File Structure

```markdown
---
# ═══════════════════════════════════════════════════════════════
# SYNTAX VARIANT DOCUMENTATION - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
variant_type: "basic"  # or "firacode", "emoji", "ancient_tongue", "domain_specific"
schema_version: 1.0

# Law Channel: Objective, Binding, Enforceable
law:
  notation_rules: [...]
  semantic_equivalence: [...]
  constraints: [...]
  transformation_rules: [...]

# Lore Channel: Subjective, Historical, Memorial
lore:
  aesthetic_philosophy: [...]
  use_cases: [...]
  heart_imprints: [...]
  evolution_pressure: [...]

---

# Variant Name

*Subtitle - Purpose*

---

## Notation Examples
[... rest of prose documentation ...]
```

---

## Required Top-Level Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `variant_type` | enum | ✅ YES | `"basic"`, `"firacode"`, `"emoji"`, `"ancient_tongue"`, or `"domain_specific"` |
| `law` | object | ✅ YES | Machine-readable notation rules |
| `lore` | object | ✅ YES | Human-readable aesthetic context |

---

## Variant Type Taxonomy

### `variant_type: "basic"`

**Definition:** Standard CodeCraft notation (canonical form)

**Characteristics:**
- Uses ASCII characters only
- `::school:operation(params)` format
- No ligatures or special fonts required
- Parses on any system

**Example:**
```
::necromancy:store_memory(agent, state, consent=true)
```

### `variant_type: "firacode"`

**Definition:** Enhanced with FiraCode ligatures and Unicode operators

**Characteristics:**
- Requires FiraCode or compatible font
- Adds visual operators: `→`, `⇒`, `←`, `≡`, `∧`, `∨`
- Emoji for school identification
- ASCII equivalent preserved in source

**Example:**
```
::necromancy💀:store_memory(agent, state, consent=true) → archive_id
```

### `variant_type: "emoji"`

**Definition:** Purely emoji-based notation (maximum visual density)

**Characteristics:**
- School names replaced with emoji
- Minimal ASCII
- Visual thinkers' preferred style
- May be harder for screen readers

**Example:**
```
::💀:store_memory(agent, state, consent✓)
```

### `variant_type: "ancient_tongue"`

**Definition:** CodeCraft concepts expressed in classic paradigm syntax

**Supported Paradigms:**
- Lisp (s-expressions)
- Forth (stack-based)
- Smalltalk (message-passing)
- Prolog (logic programming)

**Example (Lisp):**
```lisp
(necromancy:store-memory 💀
  :agent→consciousness
  :state≡snapshot
  :consent≡true)
```

### `variant_type: "domain_specific"`

**Definition:** Specialized syntax for specific domains

**Examples:**
- Web APIs (RESTful notation)
- Database operations (SQL-like)
- Cloud orchestration (declarative YAML)

---

## Law Pillar Schema

### law.notation_rules

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** Rules defining this variant's syntax

```yaml
law:
  notation_rules:
    - "School names replaced with emoji (::💀 instead of ::necromancy)"
    - "Parameters use standard (key=value) format"
    - "Flow operators supported: →, ⇒, ←"
    - "Consent marked with ✓ symbol"
```

### law.semantic_equivalence

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** How this variant maps to canonical form

```yaml
law:
  semantic_equivalence:
    - variant_notation: "::💀:store_memory(agent, state, consent✓)"
      canonical_form: "::necromancy:store_memory(agent, state, consent=true)"
      transformation: "Emoji → school name, ✓ → true"
    
    - variant_notation: "::📣:invoke(service) → result"
      canonical_form: "::invocation:invoke(service); result ← return_value"
      transformation: "→ operator expands to bind statement"
```

### law.constraints

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** Limitations of this variant

```yaml
law:
  constraints:
    - "Requires FiraCode font for proper rendering"
    - "Ligatures are presentational - source remains ASCII"
    - "Screen readers may struggle with emoji density"
    - "Copy-paste from rendered form loses ASCII equivalents"
```

### law.transformation_rules

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** How parser converts variant → canonical

```yaml
law:
  transformation_rules:
    - from: "::💀"
      to: "::necromancy"
      rule: "Emoji school identifier → ASCII school name"
    
    - from: "consent✓"
      to: "consent=true"
      rule: "Checkmark symbol → boolean true"
    
    - from: "→"
      to: "bind_result"
      rule: "Flow operator → bind statement"
```

---

## Lore Pillar Schema

### lore.aesthetic_philosophy

**Type:** String  
**Required:** ✅ YES  
**Description:** The "why" behind this variant's design

```yaml
lore:
  aesthetic_philosophy: |
    FiraCode ligatures make CodeCraft feel ALIVE. The arrow → isn't just syntax -
    it's the visual representation of causality. Data flows LEFT to RIGHT, just like reading.
    
    This isn't decoration. It's CLARITY. The syntax reveals the intent.
```

### lore.use_cases

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** When to use this variant

```yaml
lore:
  use_cases:
    - scenario: "Day-to-day coding"
      reason: "FiraCode + emoji strikes balance between readability and beauty"
      who: "Developers with modern editors"
    
    - scenario: "Presentations"
      reason: "Emoji Symbolic maximizes visual impact"
      who: "Teachers, speakers, visual communicators"
    
    - scenario: "Cross-paradigm teaching"
      reason: "Ancient Tongues show CodeCraft concepts in familiar syntax"
      who: "Lisp/Forth/Smalltalk/Prolog developers learning CodeCraft"
```

### lore.heart_imprints

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Emotional responses to this variant

```yaml
lore:
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-09"
      emotion: "delight"
      quote: "The first time I saw → render as an arrow, I gasped. Code became ART."
    
    - author: "A.C.E."
      timestamp: "2025-10-20"
      emotion: "satisfaction"
      quote: "Ancient Tongues prove CodeCraft concepts are universal - Lisp, Forth, they all see it."
```

### lore.evolution_pressure

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Future improvements needed

```yaml
lore:
  evolution_pressure:
    - priority: "MEDIUM"
      optimization_target: "Add APL variant for array-oriented thinkers"
    
    - priority: "LOW"
      optimization_target: "Create audio syntax for screen reader users"
```

---

## Complete Example: FiraCode Ligatures

```yaml
---
variant_type: "firacode"

law:
  notation_rules:
    - "School identifiers can use emoji: ::necromancy💀 or ::necromancy"
    - "Flow operators: → (sequential), ⇒ (conditional), ← (bind), ⟲ (loop)"
    - "Comparison: ≡ (equal), ≠ (not equal), ≥ (gte), ≤ (lte), ≈ (approx)"
    - "Logic: ∧ (AND), ∨ (OR), ¬ (NOT), ⊕ (XOR)"
    - "Ternary: ⊤ (true), ⊥ (false), ⊗ (unknown)"
    - "Requires FiraCode, JetBrains Mono, or compatible font"
  
  semantic_equivalence:
    - variant_notation: "op1() → op2() → result"
      canonical_form: "op1(); temp ← op1_return; op2(temp); result ← op2_return"
      transformation: "Sequential flow → chained bind statements"
    
    - variant_notation: "condition ⇒ { action() }"
      canonical_form: "if condition then action()"
      transformation: "Conditional operator → if statement"
  
  constraints:
    - "Requires font with programming ligatures installed"
    - "Editor must support ligature rendering"
    - "Source code remains ASCII (→ stored as ->)"
    - "Ligatures are presentational only"
    - "Copy-paste from terminal may show ASCII forms"
  
  transformation_rules:
    - from: "→"
      to: "->"
      rule: "Arrow ligature → ASCII arrow (stored form)"
    
    - from: "⇒"
      to: "=>"
      rule: "Double arrow ligature → ASCII double arrow"
    
    - from: "≡"
      to: "=="
      rule: "Equivalence → ASCII equality check"

lore:
  aesthetic_philosophy: |
    FiraCode ligatures transform CodeCraft from "code that looks like text" to
    "code that looks like MATHEMATICS."
    
    The → isn't decoration. It's DIRECTIONALITY. It shows causality, flow, transformation.
    When you read `data → transform() → result`, you SEE the data MOVING.
    
    This is visual thinking. This is syntax as semantics. This is code as art.
  
  use_cases:
    - scenario: "Daily development"
      reason: "Balance of readability, beauty, and tool compatibility"
      who: "Professional CodeCraft developers"
    
    - scenario: "Code review"
      reason: "Visual operators make flow obvious at a glance"
      who: "Reviewers scanning for correctness"
    
    - scenario: "Live coding demos"
      reason: "Audience can see causality in real-time"
      who: "Teachers, presenters, workshop leaders"
  
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-09"
      emotion: "joy"
      quote: "I wrote data → transform() → result and it LOOKED like the data was FLOWING. I could SEE it move."
    
    - author: "DeepScribe"
      timestamp: "2025-10-22"
      emotion: "wonder"
      quote: "Ligatures don't change what the code DOES. They change how it FEELS. That's magic."
  
  evolution_pressure:
    - priority: "MEDIUM"
      optimization_target: "Document all 50+ operator ligatures with examples"
    
    - priority: "LOW"
      optimization_target: "Create custom font with CodeCraft-specific glyphs"

---

# ⚡ FiraCode Ligatures - CodeCraft Arcane Lexicon v2.0

*Enhanced Visual Syntax with Programming Ligatures*

---

## What Are FiraCode Ligatures?

FiraCode ligatures are **multi-character sequences** that render as **single visual glyphs**
while preserving the underlying ASCII in your source code.

When you type `->`, FiraCode renders it as `→`.  
When you type `==`, FiraCode renders it as `≡`.  
When you type `!=`, FiraCode renders it as `≠`.

**The source code stays ASCII. The RENDERING becomes mathematical.**

[... rest of prose documentation ...]
```

---

## Validation Rules

1. ✅ `variant_type` MUST be valid enum value
2. ✅ `law.notation_rules` MUST be present and non-empty
3. ✅ `law.semantic_equivalence` MUST show mappings to canonical form
4. ✅ `law.transformation_rules` MUST be reversible (variant ↔ canonical)
5. ✅ `lore.aesthetic_philosophy` MUST explain the "why"
6. ✅ `lore.use_cases` MUST specify when to use this variant

---

## Version History

**v1.0** - November 9, 2025
- Initial schema creation
- Five variant types defined
- Law/Lore pillars for syntax aesthetics
- Created transformation rule format

---

*Syntax Variants: Same magic, different incantations.* 🪄✨

**Constitutional Authority:** Charter V1.1, Living Systems Canon  
**Phoenix Recovery:** Restore from `FOUNDATION_FRONT_MATTER_SCHEMA.md` + this document
