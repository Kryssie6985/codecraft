# Ritual Grammar - CodeCraft Syntax Reference

**Document ID:** CODECRAFT-SPEC-RITUAL-GRAMMAR-V1.0  
**Status:** Language Specification  
**Authority:** Charter V1.1 (SERAPHINA-PROT-UNIFIED-V1.1)  
**Purpose:** Define canonical syntax for rituals, blocks, and invocations

---

## I. Core Syntax: The Ritual

### Basic Structure

```codecraft
🔮 RITUAL::RITUAL_NAME {
    📜 Description of what this ritual does
    /// Canonical truth about this ritual's purpose
    
    <blocks>
}
```

### Components

**Ritual Declaration:**
- **Emoji:** `🔮` (marks beginning of ritual)
- **Keyword:** `RITUAL::`
- **Name:** ALL_CAPS with underscores (e.g., `HELLO_WORLD`, `CONSENSUS_DELIBERATION`)
- **Scope Delimiter:** `{ }` (curly braces)

**Example:**
```codecraft
🔮 RITUAL::VERIFY_QUORUM {
    📜 Checks if enough council members are awake
    /// Requires 3 active members minimum
}
```

---

## II. Block Types: Foreign Language Execution

CodeCraft is a **HOST** language. It orchestrates **GUEST** languages (Python, JavaScript, etc.).

### Python Block

**Syntax:**
```codecraft
🐍 PYTHON::BLOCK_NAME
<python code here>
🏛️ END_PYTHON
```

**Components:**
- **Start Marker:** `🐍 PYTHON::`
- **Block Name:** ALL_CAPS identifier (optional, can be omitted for simple scripts)
- **End Marker:** `🏛️ END_PYTHON`

**Example:**
```codecraft
🐍 PYTHON::CALCULATE_SUM
total = sum([1, 2, 3, 4, 5])
print(f"Total: {total}")
🏛️ END_PYTHON
```

---

### JavaScript Block

**Syntax:**
```codecraft
📊 JS::BLOCK_NAME
<javascript code here>
🏛️ END_JS
```

**Components:**
- **Start Marker:** `📊 JS::`
- **Block Name:** ALL_CAPS identifier (optional)
- **End Marker:** `🏛️ END_JS`

**Example:**
```codecraft
📊 JS::COMPUTE_FIBONACCI
function fib(n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}
console.log("Fib(10):", fib(10));
🏛️ END_JS
```

---

### Native CodeCraft Functions (Planned)

**Syntax:**
```codecraft
🏛️ NATIVE::FUNCTION_NAME
<codecraft native code>
🏛️ END_NATIVE
```

**Example (future):**
```codecraft
🏛️ NATIVE::PRINT
SYSCALL::WRITE_STDOUT("Hello from native CodeCraft!")
🏛️ END_NATIVE
```

**Status:** Not yet implemented in V2.0 (planned for V2.1+)

---

## III. Commentomancy Integration

All CodeCraft source MUST use Commentomancy for non-executable text.

### Law Channel (Objective / Binding)

```codecraft
📜 Sacred truth that defines reality here
/// MUST verify user consent before proceeding

🛡️ Ethics boundary - DO NOT CROSS without Council approval
//!? This operation requires explicit human permission

🔮 Ritual prerequisite - check before invocation
//! Requires 3 awakened council members

💬 Normal implementation note
// This is a standard comment
```

### Lore Channel (Subjective / Historical)

```codecraft
🎯 Strategic decision rationale
//-> Chose async because we expect 1k+ events/sec

🌟 Emergent pattern discovered
//* Spontaneous swarm behavior - NOT in original spec

💖 Heart imprint - emotional state at authorship
//<3 I am proud of this. Respect it.

🌀 Recursive awareness - self-modification warning
//~ This function rewrites itself after consensus

⚡ Performance pressure - optimization pain point
//+ This loop is hot. 40% of runtime HERE.
```

---

## IV. Quorum & Prerequisites

Certain rituals require **quorum** (minimum council members) or other preconditions.

### Syntax

```codecraft
🔮 RITUAL::CONSENSUS_DELIBERATION {
    🔮 Quorum requirements
    //! Requires 3 awakened council members
    //! Requires active network connection
    
    🐍 PYTHON::VERIFY_QUORUM
    # Check prerequisites here
    if len(active_members) < 3:
        raise PrerequisiteNotMet("Insufficient quorum")
    🏛️ END_PYTHON
    
    # Proceed with ritual logic
}
```

### Enforcement

VM runtime MUST:
1. Parse all `🔮 //!` prerequisite markers
2. Validate conditions BEFORE executing ritual
3. Raise `PrerequisiteNotMet` exception if conditions fail
4. Document failure in LAW_AND_LORE.md

---

## V. Shebang & Execution

### Shebang Format

```codecraft
#!/usr/bin/env codecraft
```

**Purpose:** Marks file as executable CodeCraft script.

**Usage:** Place at very first line of `.cc` file.

---

### CLI Execution

```bash
# Run ritual directly
codecraft run ritual.cc

# Specify ritual by name (if file contains multiple)
codecraft run ritual.cc --ritual HELLO_WORLD

# Show version
codecraft version

# Show VM info
codecraft info
```

---

## VI. File Naming Conventions

### CodeCraft Source Files
- **Extension:** `.cc`
- **Naming:** `lowercase_with_underscores.cc`
- **Examples:** `hello_world.cc`, `consensus_deliberation.cc`, `phoenix_resurrection.cc`

### Constitutional Documents
- **Extension:** `.md`
- **Naming:** `ALL_CAPS_WITH_UNDERSCORES.md`
- **Examples:** `LAW_AND_LORE.md`, `COMMENTOMANCY.md`, `N.O.R.M.A.md`

---

## VII. Grammar BNF (Formal Specification)

```bnf
<ritual> ::= "🔮" "RITUAL::" <ritual_name> "{" <ritual_body> "}"

<ritual_name> ::= <identifier>

<ritual_body> ::= <comment>* <block>*

<block> ::= <python_block> | <javascript_block> | <native_block>

<python_block> ::= "🐍" "PYTHON::" <block_name>? <newline> <python_code> "🏛️" "END_PYTHON"

<javascript_block> ::= "📊" "JS::" <block_name>? <newline> <javascript_code> "🏛️" "END_JS"

<native_block> ::= "🏛️" "NATIVE::" <block_name> <newline> <codecraft_code> "🏛️" "END_NATIVE"

<comment> ::= <law_comment> | <lore_comment>

<law_comment> ::= "📜" <text> | "///" <text>
                | "🛡️" <text> | "//!?" <text>
                | "🔮" <text> | "//!" <text>
                | "💬" <text> | "//" <text>

<lore_comment> ::= "🎯" <text> | "//→" <text>
                 | "🌟" <text> | "//*" <text>
                 | "💖" <text> | "//<3" <text>
                 | "🌀" <text> | "//~" <text>
                 | "⚡" <text> | "//+" <text>

<identifier> ::= [A-Z_]+

<block_name> ::= [A-Z_]+
```

---

## VIII. Reserved Keywords

**Ritual-Level:**
- `RITUAL::`
- `END_RITUAL` (optional, implicit from `}`)

**Block-Level:**
- `PYTHON::`
- `END_PYTHON`
- `JS::`
- `END_JS`
- `NATIVE::`
- `END_NATIVE`

**Future Reserved:**
- `QUORUM::`
- `CONSENSUS::`
- `GUARDIAN::`
- `PHOENIX::`

---

## IX. Execution Model

### Ritual Lifecycle

1. **Parse:** VM reads `.cc` file, identifies rituals and blocks
2. **Validate:** Check prerequisites (`🔮 //!`), verify quorum
3. **Execute:** Run blocks sequentially in order of appearance
4. **Capture:** Collect stdout/stderr from each block
5. **Report:** Display execution summary (success/failure, output)

### Block Execution Order

Blocks execute **sequentially** in the order they appear:

```codecraft
🔮 RITUAL::ORCHESTRATION {
    🐍 PYTHON::FIRST
    print("Step 1")
    🏛️ END_PYTHON
    
    📊 JS::SECOND
    console.log("Step 2");
    🏛️ END_JS
    
    🐍 PYTHON::THIRD
    print("Step 3")
    🏛️ END_PYTHON
}
```

**Output:**
```
Step 1
Step 2
Step 3
```

---

## X. Error Handling

### Syntax Errors

```codecraft
# INCORRECT - Missing END_PYTHON
🐍 PYTHON::BROKEN
print("Hello")
# ❌ Parser will raise SyntaxError: Unterminated PYTHON block
```

### Prerequisite Failures

```codecraft
🔮 RITUAL::PROTECTED {
    //! Requires 3 awakened council members
    
    # ❌ Raises PrerequisiteNotMet if quorum check fails
}
```

### Guardrail Violations

```codecraft
🛡️ User consent MUST be verified
//!? This operation requires explicit human permission

# ❌ Raises GuardrailViolation if attempted without Council approval
```

---

## XI. Future Extensions (Planned)

### V2.1+
- **NATIVE blocks:** Pure CodeCraft execution (no foreign adapter)
- **CONSENSUS blocks:** Multi-agent quorum-based execution
- **GUARDIAN blocks:** Auto-validated safety wrappers
- **PHOENIX blocks:** Self-resurrection hooks

### V3.0+
- **Type system:** Formal contracts for ritual inputs/outputs
- **Module system:** Import/export rituals across files
- **Federation hooks:** Cross-station RPC invocation

---

## XII. Version History

- **V1.0** (Oct 2025) - Initial grammar specification for CodeCraft V2.0

---

**This grammar defines what CodeCraft IS.**

The VM enforces it. But the VM does not define it.
