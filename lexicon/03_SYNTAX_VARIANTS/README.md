# 03_SYNTAX_VARIANTS

**Many Ways to Cast the Same Spell** 🪄

This directory documents the various syntactic styles and notations available in CodeCraft. While the core operations remain the same, CodeCraft offers multiple "flavors" to match different aesthetics, programming paradigms, and use cases.

## 🎨 What's Here

- **Basic Syntax** - The standard `::school:operation()` format
- **FiraCode Ligatures** - Enhanced with programming ligatures and Unicode operators
- **Emoji Symbolic** - Purely emoji-based notation for visual thinkers
- **Ancient Tongues** - CodeCraft syntax in classic languages (Lisp, Forth, Smalltalk, Prolog)
- **Domain-Specific Dialects** - Specialized syntax for specific contexts

## 🌈 The Variants

### **Basic Syntax** (Standard)
```
::invocation:call_function(arg1, arg2)
::conjuration:create_object(type="Person")
::necromancy:store_memory(agent, state, consent=true)
```
Clean, readable, unambiguous. The default.

### **FiraCode Ligatures** (Enhanced)
```
::invocation📣:call_function → result
::conjuration🎨:create_object ⇒ new_instance
::necromancy💀:store_memory(agent, state) ⟿ archive_id
```
Adds visual polish with ligatures and Unicode operators.

### **Emoji Symbolic** (Pure Visual)
```
::📣:call_function()
::🎨:create_object()
::💀:store_memory()
```
Maximum visual density, minimal ASCII.

### **Ancient Tongues** (Classic Paradigms)

**Lisp:**
```lisp
(necromancy:store-memory 💀
  :agent→consciousness
  :state≡complete-snapshot
  :consent≡true)
```

**Forth:**
```forth
agent-id consciousness-snapshot consent💀 store-memory necromancy!
```

**Smalltalk:**
```smalltalk
necromancy storeMemory: agentId
  state: #fullSnapshot
  consent: #true 💀.
```

**Prolog:**
```prolog
necromancy(store_memory(AgentId, State)) :-
  verify_consent(AgentId),
  persist_to_vault(State) 💀.
```

## 🎯 Purpose

Syntax Variants enable:
- **Aesthetic choice** - Match your preferred visual style
- **Paradigm alignment** - Write CodeCraft that feels native to your paradigm
- **Accessibility** - Visual thinkers, screen readers, different cognitive styles
- **Cross-language bridges** - Map CodeCraft concepts to familiar syntax

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

## 🌟 Special Considerations

### Unicode Operator Precedence
When using emoji operators, precedence rules apply. See each school's documentation for operator precedence tables.

### Ligature Requirements
FiraCode ligatures require a compatible font (FiraCode, JetBrains Mono, etc.) and editor support.

### Ancient Tongues as Metaphor
The Ancient Tongues variants are **conceptual mappings**, not executable code in those languages. They show how CodeCraft concepts would look if expressed in those paradigms.

## 🔗 Where to Go Next

- **../02_ARCANE_SCHOOLS/** - See syntax variants for each school's operations
- **../04_PARAMETERS/** - Understand parameter passing in different variants
- **../05_OPERATORS/** - Learn how operators compose across variants
- **../06_EXAMPLES/** - See full rituals in different syntactic styles

---

*Same magic, different incantations.* 🪄✨
