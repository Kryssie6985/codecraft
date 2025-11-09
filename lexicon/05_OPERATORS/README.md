# 05_OPERATORS

**How Rituals Compose and Flow** ⚡

This directory documents the operators and control flow mechanisms that allow CodeCraft rituals to compose, chain, branch, and loop. These are the "connective tissue" that turns individual operations into complete programs.

## 📚 What's Here

- **Flow Operators** - Sequential, parallel, conditional execution
- **Composition Operators** - Chaining operations together
- **Assignment Operators** - Binding results to names
- **Comparison Operators** - Testing conditions and branching
- **Logical Operators** - Boolean logic and short-circuiting
- **Ternary Operators** - Three-state logic (yes/no/unknown)
- **Temporal Operators** - Time-based flow control
- **Error Operators** - Exception handling and recovery

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

- **../02_ARCANE_SCHOOLS/** - See operators used in school operations
- **../03_SYNTAX_VARIANTS/** - Learn operator notation in different variants
- **../06_EXAMPLES/** - See operators in complete rituals
- **flow_operators.md** - Deep dive on control flow
- **composition_operators.md** - Deep dive on operation chaining

---

*Operators: The grammar of magical intent.* ⚡✨
