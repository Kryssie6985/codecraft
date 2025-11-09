# grammar/

**The Formal Language Specification** 📝

This directory contains the formal grammar definitions for CodeCraft—the EBNF (Extended Backus-Naur Form) specifications that define what is and isn't valid CodeCraft syntax. This is where the language becomes machine-parseable.

## 📚 What's Here

- **lexicon.ebnf** - The complete EBNF grammar for CodeCraft
- **EBNF_TO_PARSER_MAPPING.md** - Mapping from EBNF rules to parser implementation
- **Grammar Tests** - Test cases for validating grammar rules
- **Parser Implementation Notes** - How to implement a CodeCraft parser

## 🎯 Purpose

The grammar defines:
- **What's legal syntax** (what the parser accepts)
- **What's illegal syntax** (what the parser rejects)
- **Precedence rules** (how expressions are parsed)
- **Ambiguity resolution** (when multiple parses exist)

## 📖 Core Files

### **lexicon.ebnf**
The canonical grammar specification in EBNF notation:
```ebnf
ritual = "::ritual" identifier "[" params "]" block;
invocation = "::" school ":" operation "(" args ")";
school = identifier | emoji;
operation = identifier;
params = param ("," param)*;
param = identifier ":" type;
...
```

This file is the **single source of truth** for CodeCraft syntax.

### **EBNF_TO_PARSER_MAPPING.md**
Maps EBNF rules to actual parser implementation:
```markdown
| EBNF Rule | Parser Function | Description |
|-----------|-----------------|-------------|
| ritual | parse_ritual() | Top-level ritual definition |
| invocation | parse_invocation() | Operation call |
| school | parse_school() | School name or emoji |
...
```

## 🔍 Grammar Structure

### **Top-Level Constructs**
```ebnf
program = ritual+;
ritual = "::ritual" identifier "[" params "]" block;
```

### **Operations**
```ebnf
invocation = "::" school ":" operation "(" args ")";
school = identifier | emoji;
operation = identifier;
```

### **Flow Control**
```ebnf
sequential = expression "→" expression;
conditional = "::when" expression "⇒" block;
loop = "::for" "each" identifier "in" expression "⇒" block;
```

### **Expressions**
```ebnf
expression = invocation
           | sequential
           | conditional
           | assignment
           | comparison
           | logical;
```

### **Operators**
```ebnf
assignment = identifier "←" expression;
comparison = expression ("≡" | "≠" | "<" | ">" | "≤" | "≥") expression;
logical = expression ("∧" | "∨" | "¬" | "⊕") expression;
```

## 🎨 Grammar Variants

### **Basic Syntax Grammar**
Standard `::school:operation()` format.

### **Emoji Symbolic Grammar**
Allows emojis as school identifiers:
```ebnf
school = identifier | emoji;
emoji = [U+1F300-U+1F9FF];  # Unicode emoji range
```

### **Ancient Tongues Grammar**
Separate grammars for Lisp, Forth, Smalltalk, Prolog variants.

## 🔧 Parser Implementation

### **Lexer (Tokenization)**
```
Input: "::necromancy:store_memory(agent, state, consent=true)"
Tokens:
  - DOUBLE_COLON "::"
  - IDENTIFIER "necromancy"
  - COLON ":"
  - IDENTIFIER "store_memory"
  - LPAREN "("
  - IDENTIFIER "agent"
  - COMMA ","
  - ...
```

### **Parser (Syntax Tree)**
```
Invocation
├── School: "necromancy"
├── Operation: "store_memory"
└── Args:
    ├── Arg: "agent"
    ├── Arg: "state"
    └── Named Arg:
        ├── Name: "consent"
        └── Value: true
```

### **Validator (Semantic Checks)**
```
✅ School "necromancy" exists (check schools.canonical.yaml)
✅ Operation "store_memory" exists in Necromancy (check canon.lock.yaml)
✅ Required params present: agent, state, consent (check operation spec)
✅ consent=true (check constraints: must be true)
✅ Safety Tier 3 (require ethical review)
```

## 🧪 Grammar Tests

### **Valid Syntax Tests**
```codecraft
# Test 1: Basic invocation
::necromancy:store_memory(agent, state, consent=true)

# Test 2: Sequential flow
::op1() → ::op2() → ::op3()

# Test 3: Conditional
::when condition ⇒ { ::operation() }

# Test 4: Loop
::for each item in list ⇒ { ::process(item) }
```

### **Invalid Syntax Tests**
```codecraft
# Test 1: Missing colons
:necromancy:store_memory()  # ERROR: Must be ::

# Test 2: Invalid school
::unknown_school:operation()  # ERROR: School not in canon

# Test 3: Missing required param
::necromancy:store_memory(agent, state)  # ERROR: consent required

# Test 4: Invalid consent value
::necromancy:store_memory(agent, state, consent=false)  # ERROR: Must be true
```

## 🌟 Grammar Evolution

### **v1.0 Grammar**
- 12 schools
- Basic operators (`→`, `←`, `≡`)
- No strict operation signatures

### **v2.0 Grammar (Current)**
- 20 schools
- Expanded operators (ternary: `⊤`, `⊥`, `⊗`)
- Strict operation signatures with types
- Multi-key parameter support
- Emoji symbolic variants standardized

### **Future Grammar (Proposed)**
- Pattern matching syntax
- Async/await primitives
- First-class ritual composition

## 🔗 Grammar Resources

### **EBNF Standards**
- ISO/IEC 14977 (EBNF standard)
- W3C EBNF notation

### **Parser Generators**
- ANTLR (recommended)
- PEG (Parsing Expression Grammar)
- Tree-sitter (incremental parsing)

### **Reference Implementations**
- Python parser: `adapter/cc_schema_adapter.py`
- Validator: `validators/validate_school.py`
- Archaeologist: `scripts/rosetta_archaeologist.py`

## 🎯 Building a CodeCraft Parser

### **Step 1: Tokenize**
```python
from codecraft.lexer import Lexer

lexer = Lexer(source_code)
tokens = lexer.tokenize()
```

### **Step 2: Parse**
```python
from codecraft.parser import Parser

parser = Parser(tokens)
ast = parser.parse()
```

### **Step 3: Validate**
```python
from codecraft.validator import Validator

validator = Validator(canon_lock_yaml)
errors = validator.validate(ast)
```

### **Step 4: Execute**
```python
from codecraft.interpreter import Interpreter

interpreter = Interpreter()
result = interpreter.execute(ast)
```

## 🔗 Where to Go Next

- **lexicon.ebnf** - Study the complete grammar
- **EBNF_TO_PARSER_MAPPING.md** - Map grammar to implementation
- **../02_ARCANE_SCHOOLS/** - See what operations the grammar must support
- **adapter/cc_schema_adapter.py** - Reference Python parser implementation

---

*Grammar: Where syntax becomes law.* 📝✨
