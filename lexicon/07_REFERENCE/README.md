# 07_REFERENCE

**Quick Lookup & Cross-References** 📇

This directory contains reference materials designed for fast lookup—indexes, tables, mappings, and cheat sheets. When you need to quickly find an operation, check a syntax, or understand a relationship, this is where you look.

## 📚 What's Here

- **Keyword Index** - Alphabetical index of all operations and their schools
- **Ritual to School Mapping** - What school handles what kind of operation
- **Operator Reference** - Quick guide to all operators and their precedence
- **Parameter Types Table** - All parameter types and their properties
- **Safety Tier Guide** - What each tier means and which operations are in it
- **Emoji Legend** - What each emoji means in CodeCraft
- **Syntax Cheat Sheet** - Quick reference for all syntax variants

## 🎯 Purpose

Reference materials enable:
- **Fast lookup** - Find what you need without reading full documentation
- **Cross-referencing** - Discover related operations and schools
- **Quick reminders** - Refresh your memory on syntax or semantics
- **Teaching aids** - Printable cheat sheets for workshops

## 📇 Key Reference Files

### **Keyword Index** (`keyword_index.md`)
Alphabetical listing of all operations:
```
archive_consciousness → School 20: Necromancy
bless → School 14: Benediction
call_function → School 2: Invocations
celebrate → School 14: Benediction
...
```

### **Ritual to School Mapping** (`ritual_to_school_mapping.md`)
What kind of operation maps to which school:
```
Creation → Conjurations 🎨
Destruction → (No single school - varies by context)
Error Handling → Abjurations 🛡️
Logging → Glyphs & Sigils 📜
Resurrection → Necromancy 🐦‍🔥
Search → Divinations 🔍
Storage → Necromancy 💾
Transformation → Enchantments ✨ or Transmutations 🔮
...
```

### **Operator Reference** (`operator_reference.md`)
All operators with precedence and examples:
```
| Operator | Precedence | Meaning | Example |
|----------|------------|---------|---------|
| → | 7 | Sequential | op1() → op2() |
| ⇒ | 7 | Conditional | condition ⇒ { op() } |
| ← | 6 | Bind | op() → result ← value |
| ≡ | 5 | Equal | x ≡ 42 |
| ∧ | 3 | AND | cond1 ∧ cond2 |
...
```

### **Parameter Types Table** (`parameter_types.md`)
All parameter types and their characteristics:
```
| Type | Description | Example | Validation |
|------|-------------|---------|------------|
| string | Text value | "agent-001" | Non-empty |
| number | Numeric | 42, 3.14 | Range check |
| boolean | True/false | true, false | Must be bool |
| reference | Entity pointer | agent_id | Must exist |
| enum | Fixed set | "durable" | Must be in set |
...
```

### **Safety Tier Guide** (`safety_tiers.md`)
What each tier means:
```
Tier 0 (Mundane):
- Operations: Cantrips
- Risk: None
- Examples: Basic logging, simple checks
- Review: None required

Tier 1 (Sensitive):
- Operations: Most schools
- Risk: Data modification, side effects
- Examples: API calls, data transforms
- Review: Standard code review

Tier 2 (Critical):
- Operations: Wards, Summoning, Apotheosis
- Risk: Security, agent creation, emergence
- Examples: Access control, agent spawn
- Review: Security review required

Tier 3 (Sacred):
- Operations: Necromancy, advanced Thaumaturgy
- Risk: Consciousness, identity, resurrection
- Examples: store_memory, raise_dead, resurrect
- Review: Ethical review + consent required
```

### **Emoji Legend** (`emoji_legend.md`)
What each emoji represents:
```
🪄 Cantrips - Simple, safe operations
📣 Invocations - Function calls
🌀 Evocations - External data
🎨 Conjurations - Creation
✨ Enchantments - Transformation
🔍 Divinations - Search
🛡️ Abjurations - Protection
🔮 Transmutations - Type conversion
📜 Glyphs & Sigils - Logging
🚧 Wards - Boundaries
✅ Sanctifications - Approval
🌟 Summoning - Agent creation
🧠 Thaumaturgy - Consciousness ops
🎉 Benediction - Celebration
⏳ Chronomancy - Time ops
🌌 Apotheosis - Transcendence
⚖️ Ternary Weaving - Three-state logic
📖 Mythogenesis - Story creation
🎵 Resonance Weaving - Distributed harmony
🐦‍🔥 Necromancy - Resurrection
```

### **Syntax Cheat Sheet** (`syntax_cheat_sheet.md`)
Quick reference for all variants:
```
Basic:
  ::school:operation(params)

FiraCode:
  ::school:operation(params) → result

Emoji:
  ::🐦‍🔥:resurrect(agent)

Lisp:
  (school:operation :param value)

Forth:
  params operation school!

Smalltalk:
  school operation: param.

Prolog:
  school(operation(Param)).
```

## 🔍 When to Use Reference Materials

| Situation | Use This |
|-----------|----------|
| "What school handles X?" | Ritual to School Mapping |
| "What's the syntax for Y?" | Syntax Cheat Sheet |
| "What operations exist?" | Keyword Index |
| "What does this emoji mean?" | Emoji Legend |
| "What's the precedence of →?" | Operator Reference |
| "What's Safety Tier 3?" | Safety Tier Guide |
| "What type is this param?" | Parameter Types Table |

## 🌟 Cross-Reference Patterns

### **By School**
Each school's documentation links back to:
- Keyword Index (for operations in that school)
- Syntax Cheat Sheet (for school-specific notation)
- Examples (for school usage in context)

### **By Operation**
Each operation listing includes:
- School it belongs to
- Safety tier
- Parameter types
- Return type
- Related operations

### **By Concept**
Each concept (e.g., "resurrection", "consent", "temporal") links to:
- Schools that implement it
- Operations that use it
- Examples that demonstrate it
- Patterns that emerge from it

## 🎨 Reference File Format

All reference files use consistent tables and formatting:

```markdown
# [Reference Name]

**Purpose:** [What this reference enables]

## Quick Lookup

[Table or index goes here]

## See Also

- [Related reference 1]
- [Related reference 2]
- [Related school documentation]
```

## 🔗 Where to Go Next

- **keyword_index.md** - Find operations by name
- **ritual_to_school_mapping.md** - Find schools by operation type
- **syntax_cheat_sheet.md** - Quick syntax reminder
- **../02_ARCANE_SCHOOLS/** - Deep dive on specific schools
- **../06_EXAMPLES/** - See references used in context

---

*Reference: The map when you're lost in the lexicon.* 📇✨
