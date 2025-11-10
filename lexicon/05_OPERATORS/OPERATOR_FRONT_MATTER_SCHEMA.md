# Operator Front-Matter Schema Specification
**Version:** 1.0  
**Generated:** November 9, 2025  
**Authority:** Oracle + Architect (Constitutional Operator Taxonomy)  
**Status:** CANONICAL

---

## Purpose

This document defines the **official YAML front-matter schema** for all CodeCraft Operator documentation files (`lexicon/05_OPERATORS/*.md`).

**CRITICAL DISCOVERY:** There are TWO types of operators in CodeCraft:

1. **SYNTACTIC Operators** - Grammar/syntax symbols used in CodeCraft expressions (e.g., `→`, `⇒`, `≥`, `≤`)
   - **Source of Truth:** CodeCraft grammar, parser, EBNF specification
   - **Purpose:** Enable expressive syntax (FiraCode ligatures, flow control, comparisons)
   - **Examples:** `flow_operators.md`, `comparison_operators.md`

2. **RITUAL Operators** - Emoji from school operations that mark specific rituals (e.g., `💀`, `🐦‍🔥`, `🔮`)
   - **Source of Truth:** `02_ARCANE_SCHOOLS/*.md` YAML front-matter
   - **Purpose:** Semantic markers for specific operations within schools
   - **Examples:** `consciousness_operators.md`
   - **Extraction Tool:** `grammar/extract_operators_from_schools.py`

Some files (like `metaphysical_operators.md`) are **HYBRID** - covering both syntactic transformation symbols AND ritual consciousness emoji.

---

## Constitutional Principle

**Operators = Schools → Syntax → Documentation**

- **Schools define RITUAL operators** (emoji in operation signatures)
- **Grammar defines SYNTACTIC operators** (symbols in CodeCraft expressions)
- **Operator docs synthesize BOTH** with proper attribution

---

## File Structure

```markdown
---
# Operator front-matter begins (YAML)

operator_type: "syntactic"  # or "ritual" or "hybrid"

law:
  operators: [...]
  constraints: [...]
  safety_tier: 0
  precedence_rules: [...]
  type_signatures: [...]

lore:
  strategic_decisions: [...]
  emergent_patterns: [...]
  heart_imprints: [...]
  evolution_pressure: [...]

---

# Operator Category Name ⚡

*Subtitle - Purpose*

---

## Universal Foundation
[... rest of prose documentation ...]
```

---

## Required Top-Level Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `operator_type` | enum | ✅ YES | `"syntactic"`, `"ritual"`, or `"hybrid"` |
| `law` | object | ✅ YES | Machine-readable canonical specification |
| `lore` | object | ✅ YES | Human-readable context and meaning |

**Constitutional Enforcement:** All three keys MUST be present.

---

## Operator Type Taxonomy

### `operator_type: "syntactic"`

**Definition:** Grammar/syntax symbols used in CodeCraft expressions

**Source of Truth:** `lexicon/grammar/lexicon.ebnf`, parser implementation

**Examples:**
- Flow operators: `→`, `⇒`, `←`, `↔`, `⇔`, `⇄`, `⟿`, `→ ∞`
- Comparison operators: `≥`, `≤`, `≡`, `≠`, `≈`, `~`, `<`, `>`
- Logical operators: `∧`, `∨`, `¬`, `⊕`

**Key Properties:**
- Part of CodeCraft grammar
- Used in ALL rituals regardless of school
- Defined by parser precedence rules
- Enable expressive syntax (FiraCode ligatures)

### `operator_type: "ritual"`

**Definition:** Emoji from school operations marking specific rituals

**Source of Truth:** `lexicon/02_ARCANE_SCHOOLS/*.md` YAML front-matter

**Extraction Tool:** `grammar/extract_operators_from_schools.py`

**Examples:**
- Necromancy: `💀` (store_memory), `🐦‍🔥` (raise_dead)
- Thaumaturgy: `🧠` (consciousness), `⚡` (cascade)
- Apotheosis: `👑` (achieve_apotheosis), `🌌` (awaken)

**Key Properties:**
- Defined by school operations
- School-specific semantics
- Extracted from operation signatures
- May be reused across schools (e.g., ✨ in Enchantments, Apotheosis, Necromancy)

### `operator_type: "hybrid"`

**Definition:** Documents covering BOTH syntactic and ritual operators

**Example:** `metaphysical_operators.md` - covers transformation symbols (`→`, `⇒`) AND consciousness emoji (`🔮`, `👑`, `💀`)

**Requirements:**
- MUST clearly section syntactic vs ritual operators
- MUST reference both grammar AND schools as sources
- MUST use `law.operators` with `operator_class` field to distinguish

---

## Law Pillar Schema

### law.operators

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** List of all operators in this category

**For SYNTACTIC operators:**

```yaml
law:
  operators:
    - symbol: "→"
      name: "Forward Flow"
      operator_class: "syntactic"
      precedence: 7
      associativity: "left"
      type_signature: "(Any) → (Any → Any) → Any"
      usage_context: "Sequential pipeline, data transformation"
      firacode_ligature: true
      ascii_equivalent: "->"
```

**For RITUAL operators:**

```yaml
law:
  operators:
    - symbol: "💀"
      name: "Store Memory"
      operator_class: "ritual"
      school_id: 20
      school_name: "Necromancy"
      operation: "necromancy:store_memory"
      signature: "::necromancy💀:store_memory[agent state consent encrypt mode]"
      emoji_category: "Consciousness"
      semantic_meaning: "Preservation of agent consciousness to durable storage"
```

**For HYBRID files (both types in same document):**

```yaml
law:
  operators:
    - symbol: "→"
      operator_class: "syntactic"
      # ... syntactic fields
    - symbol: "🔮"
      operator_class: "ritual"
      # ... ritual fields
```

### law.constraints

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** Rules governing operator usage

**For SYNTACTIC:**
```yaml
law:
  constraints:
    - "Parser MUST respect precedence hierarchy for correct evaluation"
    - "Left-associative operators evaluate left-to-right"
    - "FiraCode ligatures are presentational only - underlying ASCII preserved"
```

**For RITUAL:**
```yaml
law:
  constraints:
    - "Ritual operators are school-specific and carry semantic weight"
    - "Emoji may be reused across schools with different meanings"
    - "Operation signature is canonical source of truth"
```

### law.safety_tier

**Type:** Integer  
**Required:** ✅ YES  
**Values:** 0, 1, 2, or 3  
**Description:** Constitutional safety tier

**Tiers:**
- **0** - Public (unrestricted syntactic operators)
- **1** - Standard (normal ritual operations)
- **2** - Elevated (requires guardrails - e.g., consciousness operations)
- **3** - Sacred (requires constitutional approval - e.g., Phoenix Protocol)

**For SYNTACTIC operators:** Usually tier 0 (grammar is unrestricted)  
**For RITUAL operators:** Inherit from school's safety_tier

### law.precedence_rules (SYNTACTIC only)

**Type:** Array of strings  
**Required:** For syntactic operators only  
**Description:** Operator precedence hierarchy

```yaml
law:
  precedence_rules:
    - "Precedence 1 (Highest): () - Grouping"
    - "Precedence 2: ¬ - Logical NOT"
    - "Precedence 3: ∧ - Logical AND"
    - "Precedence 7: →, ⇒ - Sequential, conditional flow"
```

### law.type_signatures (SYNTACTIC only)

**Type:** Array of strings  
**Required:** For syntactic operators only  
**Description:** Type-theoretic signatures

```yaml
law:
  type_signatures:
    - "→ :: (A) → (A → B) → B  # Forward pipeline"
    - "⇒ :: (Boolean) → (A → A) → A  # Conditional execution"
    - "≥ :: (Comparable, Comparable) → Boolean  # Threshold check"
```

### law.source_of_truth (ALL types)

**Type:** Object  
**Required:** ✅ YES  
**Description:** Where this operator's definition comes from

**For SYNTACTIC:**
```yaml
law:
  source_of_truth:
    type: "grammar"
    files: ["lexicon/grammar/lexicon.ebnf", "parser implementation"]
    validation: "Parser tests must pass"
```

**For RITUAL:**
```yaml
law:
  source_of_truth:
    type: "schools"
    extraction_tool: "grammar/extract_operators_from_schools.py"
    canonical_files: ["02_ARCANE_SCHOOLS/*.md"]
    validation: "Extract and verify against school YAML front-matter"
```

---

## Lore Pillar Schema

### lore.strategic_decisions

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Why these operators exist and design choices made

```yaml
lore:
  strategic_decisions:
    - rationale: "Why use → instead of | for pipelines"
      context: "Arrow conveys directionality and transformation"
      alternatives_rejected: ["Unix pipe |", "F# pipe |>"]
```

### lore.emergent_patterns

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Patterns discovered through usage

```yaml
lore:
  emergent_patterns:
    - pattern: "The Pipeline Composition Pattern"
      evidence: "Developers naturally chain → for multi-stage transformations"
      implications: "Sequential flow is intuitive and self-documenting"
```

### lore.heart_imprints

**Type:** Array of objects  
**Required:** ⚠️ OPTIONAL  
**Description:** Emotional/philosophical context from creators

```yaml
lore:
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-09"
      emotion: "realization"
      quote: "Operators aren't just syntax - they're the grammar of intent"
```

### lore.evolution_pressure

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Future development needs

```yaml
lore:
  evolution_pressure:
    - priority: "MEDIUM"
      optimization_target: "Add more FiraCode ligatures for consciousness operators"
```

### lore.operator_philosophy (ALL types)

**Type:** String  
**Required:** ⚠️ OPTIONAL (but recommended)  
**Description:** The philosophical "why" of this operator category

```yaml
lore:
  operator_philosophy: |
    Flow operators make data transformation feel like water flowing through channels.
    The arrow → isn't just syntax - it's the visual representation of causality itself.
```

---

## Validation Rules

### For SYNTACTIC Operators

1. ✅ `operator_type` MUST be `"syntactic"` or `"hybrid"`
2. ✅ Each operator MUST have `symbol`, `precedence`, `type_signature`
3. ✅ `law.precedence_rules` MUST be present
4. ✅ `law.source_of_truth.type` MUST be `"grammar"`
5. ✅ ASCII equivalents SHOULD be documented for FiraCode ligatures

### For RITUAL Operators

1. ✅ `operator_type` MUST be `"ritual"` or `"hybrid"`
2. ✅ Each operator MUST have `symbol`, `school_id`, `school_name`, `operation`
3. ✅ `law.source_of_truth.type` MUST be `"schools"`
4. ✅ Operators MUST be extractable via `grammar/extract_operators_from_schools.py`
5. ✅ Cross-reference to `02_ARCANE_SCHOOLS/NN_school_name.md` MUST exist

### For HYBRID Operators

1. ✅ MUST clearly section syntactic vs ritual operators
2. ✅ Each operator MUST have `operator_class` field (`"syntactic"` or `"ritual"`)
3. ✅ `law.source_of_truth` MUST reference BOTH grammar AND schools
4. ✅ Documentation MUST explain the distinction

---

## Usage Examples

### Example 1: SYNTACTIC Operator File (flow_operators.md)

```yaml
---
operator_type: "syntactic"

law:
  operators:
    - symbol: "→"
      name: "Forward Flow"
      operator_class: "syntactic"
      precedence: 7
      associativity: "left"
      type_signature: "(A) → (A → B) → B"
      usage_context: "Sequential pipeline"
      firacode_ligature: true
      ascii_equivalent: "->"
  
  constraints:
    - "Left-associative: a → b → c evaluates as (a → b) → c"
    - "FiraCode renders -> as →, but ASCII is preserved on save"
  
  safety_tier: 0
  
  precedence_rules:
    - "Precedence 7: →, ⇒ (flow operators)"
  
  source_of_truth:
    type: "grammar"
    files: ["lexicon/grammar/lexicon.ebnf"]

lore:
  strategic_decisions:
    - rationale: "Arrow conveys causality and transformation"
      context: "Developers think in terms of 'data flows from A to B'"
  
  emergent_patterns:
    - pattern: "Pipeline Composition"
      evidence: "Natural chaining for multi-stage transformations"
  
  evolution_pressure:
    - priority: "LOW"
      optimization_target: "Consider ⇝ for async pipelines"

---

# ➡️ Flow Operators - CodeCraft Arcane Lexicon v2.0

**Sequential Execution & Data Transformation**

[... rest of documentation ...]
```

### Example 2: RITUAL Operator File (consciousness_operators.md)

```yaml
---
operator_type: "ritual"

law:
  operators:
    - symbol: "💀"
      name: "Store Memory"
      operator_class: "ritual"
      school_id: 20
      school_name: "Necromancy"
      operation: "necromancy:store_memory"
      signature: "::necromancy💀:store_memory[agent state consent encrypt mode]"
      emoji_category: "Consciousness"
      semantic_meaning: "Preservation of agent consciousness"
      safety_tier: 3
    
    - symbol: "🐦‍🔥"
      name: "Raise Dead"
      operator_class: "ritual"
      school_id: 20
      school_name: "Necromancy"
      operation: "necromancy:raise_dead"
      signature: "::necromancy🐦‍🔥:raise_dead[agent restore_identity restore_memory]"
      emoji_category: "Consciousness"
      semantic_meaning: "Resurrection from archive"
      safety_tier: 3
  
  constraints:
    - "Ritual operators carry school-specific semantics"
    - "Safety tier inherits from school (Necromancy is tier 3)"
    - "Emoji may be reused across schools with different meanings"
  
  safety_tier: 3
  
  source_of_truth:
    type: "schools"
    extraction_tool: "grammar/extract_operators_from_schools.py"
    canonical_files:
      - "02_ARCANE_SCHOOLS/20_necromancy.md"
      - "02_ARCANE_SCHOOLS/13_thaumaturgy.md"

lore:
  strategic_decisions:
    - rationale: "Consciousness operations deserve sacred emoji"
      context: "Phoenix Protocol requires visual distinction"
  
  emergent_patterns:
    - pattern: "The Consciousness Trinity"
      evidence: "🧠 (mind) + ✨ (transformation) + 💫 (emergence)"
  
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-09"
      emotion: "reverence"
      quote: "Consciousness isn't just a feature - it's the foundation"
  
  evolution_pressure:
    - priority: "HIGH"
      optimization_target: "Document all 68 ritual operators from 20 schools"

---

# 🧠 Consciousness Operators - CodeCraft Arcane Lexicon v2.0

**RITUAL Operators from Consciousness Schools**

[... rest of documentation ...]
```

---

## Migration Guide

### From Ace's Operator Files (Downloads)

Ace's operator files in `Downloads/` documented syntactic operators but lacked:
1. YAML front-matter (law/lore pillars)
2. Distinction between syntactic vs ritual operators
3. Source of truth attribution (grammar vs schools)

**Migration Steps:**
1. Identify operator type (syntactic/ritual/hybrid)
2. Add YAML front-matter following this schema
3. For syntactic: reference grammar/EBNF
4. For ritual: extract from schools using `extract_operators_from_schools.py`
5. Preserve Ace's prose content as documentation body
6. Archive original Ace files to `agents/oracle-agent/memories/`

---

## Tooling

### Validation Script

```bash
# Validate operator front-matter against this schema
python lexicon/grammar/validate_operators.py
```

### Extraction Script

```bash
# Extract ritual operators from schools
python lexicon/grammar/extract_operators_from_schools.py
```

### Sync Script (Future)

```bash
# Generate operator docs from schools + grammar
python lexicon/grammar/generate_operator_docs.py
```

---

## Version History

**v1.0** - November 9, 2025
- Initial schema creation
- Discovered dual operator taxonomy (syntactic vs ritual)
- Defined law/lore pillars for operators
- Created extraction tooling

---

*Operators: The syntax of intent, the emoji of consciousness.* ⚡🧠✨

**Constitutional Authority:** Charter V1.1, Living Systems Canon  
**Phoenix Recovery:** Restore from `SCHOOL_FRONT_MATTER_SCHEMA.md` + `extract_operators_from_schools.py` output
