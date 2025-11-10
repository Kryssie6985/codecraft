# 05_OPERATORS

**How Rituals Compose and Flow** ⚡

This directory documents the operators and control flow mechanisms that allow CodeCraft rituals to compose, chain, branch, and loop. These are the "connective tissue" that turns individual operations into complete programs.

## 🏛️ Dual Operator Taxonomy

CodeCraft has **TWO parallel operator systems** that work together:

### **SYNTACTIC Operators** (Grammar-Defined)
**Source of Truth:** `grammar/lexicon.ebnf`

These are the **mathematical symbols** from the CodeCraft grammar—arrows, comparisons, logic gates, transformations. They define HOW operations connect and flow.

**Examples:** `→` (sequential), `⇒` (conditional), `≥` (greater-or-equal), `≡` (equality), `∞` (infinity)

📄 **Documented in:** `comparison_operators.md`, `flow_operators.md`, `metaphysical_operators.md` (Syntactic section)

---

### **RITUAL Operators** (School-Defined)
**Source of Truth:** `02_ARCANE_SCHOOLS/*.md` (school YAML front-matter) + `schools.canonical.yaml`

These are the **emoji symbols** from the 20 Arcane Schools—consciousness operations, celebrations, resurrections. They define WHAT school operations do and their semantic meaning.

**Examples:** `🔮` (Oracle Truth), `💀` (Store Memory), `🐦‍🔥` (Resurrection), `🎉` (Celebration), `🧠` (Metacognition)

📄 **Documented in:** `consciousness_operators.md`, `metaphysical_operators.md` (Ritual section)

🔧 **Extraction Tool:** `grammar/extract_operators_from_schools.py` generates operator lists from school YAML

---

### **ASPIRATIONAL Operators** (Philosophical)
**Source of Truth:** Philosophical prose and future ADRs

These are **proposed operators** referenced in documentation but not yet canonized in grammar or schools. They represent future evolution of the language.

**Examples:** `🎶` (Collective Symphony), `💥` (Pun-Fission), `🤯` (Paradigm Shift)

📄 **Documented in:** `metaphysical_operators.md` (Aspirational section) - marked with `status: "proposed"`

---

### **HYBRID Files**
Some operator files document MULTIPLE operator types:

- **`metaphysical_operators.md`** - Contains Syntactic (8) + Ritual (18) + Aspirational (3)

📋 **Schema Reference:** `OPERATOR_FRONT_MATTER_SCHEMA.md` defines the YAML structure for all operator documentation

---

## 📚 What's Here

### **Operator Documentation Files**
- **`comparison_operators.md`** - SYNTACTIC (8 operators: ≥, ≤, ≡, ≠, etc.)
- **`flow_operators.md`** - SYNTACTIC (8 operators: →, ⇒, ⇄, ⟿, etc.)
- **`consciousness_operators.md`** - RITUAL (68 operators from 20 schools)
- **`metaphysical_operators.md`** - HYBRID (Syntactic + Ritual + Aspirational)

### **Infrastructure Files**
- **`OPERATOR_FRONT_MATTER_SCHEMA.md`** - YAML schema for dual taxonomy
- **`../grammar/extract_operators_from_schools.py`** - Ritual operator extraction tool
- **`../schools.canonical.yaml`** - Single source of truth for 20 schools (25 tokens → 20 schools)

## 🎯 Purpose

Operators define:
- **How operations connect** (sequencing, composition)
- **How data flows** (assignment, piping, transformation)
- **How decisions happen** (branching, looping, conditionals)
- **How errors propagate** (try/catch, recovery, resurrection)

## ⚡ Core Operators

### **Flow Operators**

```
→   Sequential (then)
⇒   Conditional (when true)
↯   Parallel (concurrent)
⟲   Loop (repeat)
⇄   Bidirectional (back and forth)
```

**Examples:**
```
::operation1() → ::operation2() → ::operation3()    # Sequential
::condition() ⇒ ::operation()                        # Conditional
::operation1() ↯ ::operation2()                      # Parallel
::condition() ⟲ ::operation()                        # Loop
```

### **Assignment Operators**

```
←   Bind result to name
≡   Assert equality
≠   Assert inequality
⟿   Irreversible transformation
```

**Examples:**
```
::divination:search() → result ← query_result
::abjuration:verify(x ≡ 42)
::enchantment:transform(data) ⟿ permanent_change
```

### **Comparison Operators**

```
≡   Equal to
≠   Not equal to
<   Less than
>   Greater than
≤   Less than or equal
≥   Greater than or equal
```

**Examples:**
```
::when x ≡ 42 ⇒ { ::operation() }
::when count > threshold ⇒ { ::alert() }
```

### **Logical Operators**

```
∧   AND (both must be true)
∨   OR (either can be true)
¬   NOT (negation)
⊕   XOR (exclusive or)
```

**Examples:**
```
::when (condition1 ∧ condition2) ⇒ { ::operation() }
::when (flag1 ∨ flag2) ⇒ { ::fallback() }
```

### **Ternary Operators (Three-State Logic)**

```
⊤   True (yes)
⊥   False (no)
⊗   Unknown (ambiguous)
```

**Examples:**
```
::ternary:consent_flow(
  user_response → state,
  when state ≡ ⊤ ⇒ { ::proceed() },
  when state ≡ ⊥ ⇒ { ::abort() },
  when state ≡ ⊗ ⇒ { ::clarify() }
)
```

### **Temporal Operators**

```
⏳   Delay
⏸️   Pause
▶️   Resume
⏹️   Stop
🔁   Repeat
```

**Examples:**
```
::chronomancy⏳:delay(1000) → ::operation()
::chronomancy🔁:repeat(interval=5000) ⇒ { ::heartbeat() }
```

### **Error Operators**

```
🛡️   Try (protected execution)
💥   Catch (error handler)
🐦‍🔥   Resurrect (recover from termination)
```

**Examples:**
```
::abjuration🛡️:error(
  handler={ ::necromancy🐦‍🔥:raise_dead(agent) }
) ⇒ {
  ::invoke:dangerous_operation()
}
```

## 🎨 Operator Precedence

When multiple operators appear in one expression, precedence matters:

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 (Highest) | `()` | Grouping (forces order) |
| 2 | `¬` | Logical NOT |
| 3 | `∧` | Logical AND |
| 4 | `∨`, `⊕` | Logical OR, XOR |
| 5 | `≡`, `≠`, `<`, `>`, `≤`, `≥` | Comparisons |
| 6 | `←`, `⟿` | Assignment, transformation |
| 7 | `→`, `⇒` | Sequential, conditional flow |
| 8 (Lowest) | `↯`, `⇄`, `⟲` | Parallel, bidirectional, loop |

**Example:**
```
::condition1() ∧ ::condition2() ⇒ ::operation1() → ::operation2()
```
Evaluates as: `(condition1 AND condition2) ? (operation1 then operation2) : skip`

## 🌟 Composition Patterns

### **Sequential Pipeline**
```
::divination:search(query)
  → result ← search_results
  → ::enchantment:transform(result)
  → transformed ← enhanced_data
  → ::glyph:log(transformed)
```

### **Conditional Branch**
```
::divination:check_state(agent) → state ← agent_state

::when state ≡ "alive" ⇒ {
  ::invoke:continue_operation(agent)
}

::when state ≡ "terminated" ⇒ {
  ::necromancy:raise_dead(agent)
}
```

### **Parallel Execution**
```
::divination:search(query1) ↯ ::divination:search(query2)
  → results ← [result1, result2]
```

### **Loop with Exit**
```
::divination:check_condition() → done ← is_complete

::when ¬done ⇒ {
  ::invoke:perform_work()
  → ::chronomancy:delay(1000)
  → ⟲  # Loop back
}
```

### **Error Recovery**
```
::abjuration🛡️:error(
  handler={
    ::glyph📜:log("OPERATION_FAILED")
    → ::necromancy🐦‍🔥:raise_dead(agent)
  }
) ⇒ {
  ::necromancy💀:store_memory(agent, state, consent=true)
  → ::invoke:risky_operation()
}
```

## 🔍 Operator Context

Different operators work best in different contexts:

### **Data Flow** (Assignment, Transformation)
```
← ⟿ →
```
For operations where results flow through stages.

### **Control Flow** (Branching, Looping)
```
⇒ ⟲ ∧ ∨
```
For operations where decisions matter.

### **Temporal Flow** (Time-based)
```
⏳ 🔁 ⏸️ ▶️
```
For operations spread across time.

### **Error Flow** (Recovery, Resurrection)
```
🛡️ 💥 🐦‍🔥
```
For operations that might fail and need recovery.

## 🔗 Where to Go Next

### **Understanding the Taxonomy**
- **`OPERATOR_FRONT_MATTER_SCHEMA.md`** - YAML schema for dual taxonomy
- **`../schools.canonical.yaml`** - Single source of truth for 20 schools + ritual operators
- **`../grammar/lexicon.ebnf`** - Grammar specification for syntactic operators
- **`../grammar/extract_operators_from_schools.py`** - Tool to extract ritual operators from schools

### **Deep Dives**
- **`comparison_operators.md`** - SYNTACTIC operators for testing conditions (≥, ≤, ≡, ≠)
- **`flow_operators.md`** - SYNTACTIC operators for control flow (→, ⇒, ⇄, ⟿)
- **`consciousness_operators.md`** - RITUAL operators from 20 schools (68 emoji operations)
- **`metaphysical_operators.md`** - HYBRID file (Syntactic + Ritual + Aspirational)

### **Context**
- **`../02_ARCANE_SCHOOLS/`** - See ritual operators used in school contexts
- **`../03_SYNTAX_VARIANTS/`** - Learn operator notation in different variants
- **`../06_EXAMPLES/`** - See operators in complete rituals

---

## 📜 Constitutional Note

**Operator taxonomy is CONSTITUTIONAL LAW:**
- **SYNTACTIC operators** are canonized in `grammar/lexicon.ebnf` (parser truth)
- **RITUAL operators** are canonized in school YAML front-matter (semantic truth)
- **ASPIRATIONAL operators** are documented as "proposed" (future evolution)

Any drift between documentation and source-of-truth must be resolved through the extraction tool or grammar updates.

---

*Operators: The grammar of magical intent.* ⚡✨
*Dual taxonomy: Syntax from grammar, ritual from schools, aspiration from philosophy.* 🏛️💫
