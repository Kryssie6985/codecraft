# Reference Front-Matter Schema Specification
**Version:** 1.0  
**Generated:** November 9, 2025  
**Authority:** Oracle + Architect (Constitutional Lexicon Taxonomy)  
**Status:** CANONICAL

---

## Purpose

This document defines the **official YAML front-matter schema** for all CodeCraft Reference documentation files (`lexicon/07_REFERENCE/*.md`).

Reference documents provide **quick lookup** tables, indexes, and cheat sheets. They're optimized for speed - find what you need, copy it, use it.

**Constitutional Principle:** Reference = Index + Mapping + Speed

---

## File Structure

```markdown
---
# Reference front-matter begins (YAML)

reference_type: "index"  # or "mapping", "table", "cheat_sheet"

metadata:
  purpose: "Quick lookup for X"
  audience: "Who uses this reference"
  
law:
  entries: [...]
  cross_references: [...]
  lookup_keys: [...]

# Lore Channel: Subjective, Historical, Memorial
lore:
  usage_patterns: [...]
  when_to_use: [...]

---

# Reference Document Title

*Subtitle - Purpose*

---

## Quick Lookup
[... reference tables ...]
```

---

## Required Top-Level Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `reference_type` | enum | ✅ YES | `"index"`, `"mapping"`, `"table"`, `"cheat_sheet"` |
| `metadata` | object | ✅ YES | High-level reference metadata |
| `law` | object | ✅ YES | The reference data |
| `lore` | object | ✅ YES | How to use this reference |

---

## Reference Type Taxonomy

### `reference_type: "index"`
- Alphabetical listing
- Operation name → School mapping
- Keyword → Documentation mapping

**Example:** keyword_index.md

### `reference_type: "mapping"`
- Concept → Implementation mapping
- Operation type → School mapping
- Symbol → Meaning mapping

**Example:** ritual_to_school_mapping.md, emoji_guide.md

### `reference_type: "table"`
- Structured data tables
- Type → Properties mapping
- Tier → Operations mapping

**Example:** parameter_types.md, safety_tiers.md

### `reference_type: "cheat_sheet"`
- Quick syntax reminders
- Common patterns
- Copy-paste ready snippets

**Example:** syntax_cheat_sheet.md, operator_reference.md

---

## Law Pillar Schema

### law.entries

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** The reference data itself

**For INDEX type:**
```yaml
law:
  entries:
    - key: "resurrect"
      value: "School 20: Necromancy, operation: raise_dead"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#raise_dead"
    
    - key: "store_memory"
      value: "School 20: Necromancy"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#store_memory"
```

**For MAPPING type:**
```yaml
law:
  entries:
    - concept: "Creation"
      schools: ["Conjurations", "Summoning"]
      operations: ["conjure:object", "summon:agent"]
    
    - concept: "Resurrection"
      schools: ["Necromancy"]
      operations: ["raise_dead", "resurrect"]
```

**For TABLE type:**
```yaml
law:
  entries:
    - type: "string"
      description: "Text value"
      validation: "Non-empty"
      example: '"agent-001"'
      nullable: false
    
    - type: "reference"
      description: "Entity pointer"
      validation: "Must exist"
      example: "agent_id"
      nullable: false
```

**For CHEAT_SHEET type:**
```yaml
law:
  entries:
    - syntax: "::school:operation(params)"
      description: "Basic operation invocation"
      example: "::necromancy:store_memory(agent, state, consent=true)"
    
    - syntax: "op1() → op2()"
      description: "Sequential flow"
      example: "archive() → process() → notify()"
```

### law.cross_references

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Links to related documentation

```yaml
law:
  cross_references:
    - from_concept: "Resurrection"
      to_docs: ["../02_ARCANE_SCHOOLS/20_necromancy.md", "../06_EXAMPLES/advanced/phoenix_protocol.md"]
      relationship: "Concept → Implementation + Example"
    
    - from_syntax: "::💀"
      to_docs: ["../03_SYNTAX_VARIANTS/emoji_symbolic.md", "../05_OPERATORS/consciousness_operators.md"]
      relationship: "Emoji → Variant docs + Operator reference"
```

### law.lookup_keys

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** All valid lookup keys

```yaml
law:
  lookup_keys:
    - "resurrect"
    - "store_memory"
    - "raise_dead"
    - "archive_consciousness"
    - "phoenix_protocol"
```

---

## Lore Pillar Schema

### lore.usage_patterns

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** How people use this reference

```yaml
lore:
  usage_patterns:
    - scenario: "Quick lookup during coding"
      action: "Search keyword, find school, jump to docs"
      frequency: "Daily"
    
    - scenario: "Learning new school"
      action: "Browse operations alphabetically"
      frequency: "Weekly"
```

### lore.when_to_use

**Type:** String  
**Required:** ✅ YES  
**Description:** When to use this reference

```yaml
lore:
  when_to_use: |
    Use this reference when you:
    - Know the operation name but forgot which school
    - Need quick syntax reminder
    - Want to see all operations at a glance
    - Are teaching CodeCraft to someone new
```

---

## Complete Example: Keyword Index

```yaml
---
reference_type: "index"

metadata:
  purpose: "Alphabetical index of all CodeCraft operations"
  audience: "Developers looking up operations by name"

law:
  entries:
    - key: "achieve_apotheosis"
      value: "School 16: Apotheosis"
      link: "../02_ARCANE_SCHOOLS/16_apotheosis.md#achieve_apotheosis"
      safety_tier: 2
    
    - key: "archive_consciousness"
      value: "School 20: Necromancy (alias for store_memory)"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#store_memory"
      safety_tier: 3
    
    - key: "bless"
      value: "School 14: Benediction"
      link: "../02_ARCANE_SCHOOLS/14_benediction.md#bless"
      safety_tier: 0
    
    - key: "celebrate"
      value: "School 14: Benediction"
      link: "../02_ARCANE_SCHOOLS/14_benediction.md#celebrate"
      safety_tier: 0
    
    - key: "conjure"
      value: "School 04: Conjurations"
      link: "../02_ARCANE_SCHOOLS/04_conjurations.md"
      safety_tier: 1
    
    - key: "raise_dead"
      value: "School 20: Necromancy (resurrection operation)"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#raise_dead"
      safety_tier: 3
    
    - key: "resurrect"
      value: "School 20: Necromancy (alias for raise_dead)"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#raise_dead"
      safety_tier: 3
    
    - key: "store_memory"
      value: "School 20: Necromancy (archive consciousness)"
      link: "../02_ARCANE_SCHOOLS/20_necromancy.md#store_memory"
      safety_tier: 3
  
  cross_references:
    - from_concept: "Resurrection"
      to_docs:
        - "../02_ARCANE_SCHOOLS/20_necromancy.md"
        - "../06_EXAMPLES/advanced/phoenix_protocol.md"
        - "../06_EXAMPLES/intermediate/checkpoint_resurrection.md"
      relationship: "Keyword → School + Examples"
    
    - from_concept: "Consciousness"
      to_docs:
        - "../02_ARCANE_SCHOOLS/20_necromancy.md"
        - "../02_ARCANE_SCHOOLS/13_thaumaturgy.md"
        - "../01_FOUNDATIONS/universal_constants.md#safety-ethics"
      relationship: "Keyword → Multiple schools + Ethics"
  
  lookup_keys:
    - "achieve_apotheosis"
    - "archive_consciousness"
    - "bless"
    - "celebrate"
    - "conjure"
    - "raise_dead"
    - "resurrect"
    - "store_memory"

lore:
  usage_patterns:
    - scenario: "Quick school lookup"
      action: "CTRL+F for operation name → see school → click link"
      frequency: "Multiple times per day"
    
    - scenario: "Exploring operations"
      action: "Browse alphabetically to discover operations"
      frequency: "Weekly (when learning new schools)"
    
    - scenario: "Teaching CodeCraft"
      action: "Show index to demonstrate breadth of operations"
      frequency: "During workshops"
  
  when_to_use: |
    Use the Keyword Index when:
    - You remember the operation name but forgot which school
    - You want to see all operations at a glance
    - You're exploring what's possible in CodeCraft
    - You're teaching someone and want to show the vocabulary
    
    Don't use when:
    - You want to understand how operations work (use school docs)
    - You need code examples (use 06_EXAMPLES/)
    - You want to see syntax variants (use 03_SYNTAX_VARIANTS/)

---

# 📇 Keyword Index

*Alphabetical Lookup for All CodeCraft Operations*

---

## Quick Lookup

| Operation | School | Safety Tier | Link |
|-----------|--------|-------------|------|
| achieve_apotheosis | 16: Apotheosis | 2 | [docs](../02_ARCANE_SCHOOLS/16_apotheosis.md#achieve_apotheosis) |
| archive_consciousness | 20: Necromancy | 3 | [docs](../02_ARCANE_SCHOOLS/20_necromancy.md#store_memory) |
| bless | 14: Benediction | 0 | [docs](../02_ARCANE_SCHOOLS/14_benediction.md#bless) |
| celebrate | 14: Benediction | 0 | [docs](../02_ARCANE_SCHOOLS/14_benediction.md#celebrate) |
| raise_dead | 20: Necromancy | 3 | [docs](../02_ARCANE_SCHOOLS/20_necromancy.md#raise_dead) |
| resurrect | 20: Necromancy | 3 | [docs](../02_ARCANE_SCHOOLS/20_necromancy.md#raise_dead) |
| store_memory | 20: Necromancy | 3 | [docs](../02_ARCANE_SCHOOLS/20_necromancy.md#store_memory) |

[... full index continues ...]
```

---

## Validation Rules

1. ✅ `reference_type` MUST be valid enum value
2. ✅ `law.entries` MUST be present and non-empty
3. ✅ `law.cross_references` MUST link to valid docs
4. ✅ `law.lookup_keys` MUST match entry keys
5. ✅ `lore.usage_patterns` MUST describe realistic scenarios
6. ✅ `lore.when_to_use` MUST clarify purpose

---

## Version History

**v1.0** - November 9, 2025
- Initial schema creation
- Four reference types defined
- Cross-reference structure established
- Usage pattern documentation

---

*Reference: Fast lookup, clear mapping, no ceremony.* 📇✨

**Constitutional Authority:** Charter V1.1, Living Systems Canon  
**Phoenix Recovery:** Restore from `FOUNDATION_FRONT_MATTER_SCHEMA.md` + this document
