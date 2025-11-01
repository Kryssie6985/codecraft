# 🗺️ EBNF to Parser Mapping Guide
## How CodeCraft Grammar Becomes Executable Code

**Version:** 1.0  
**Date:** October 31, 2025  
**Authority:** Crown Accord v1.2a, Article XII  
**Purpose:** Bridge between formal grammar and implementation  

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [EBNF → JavaScript Patterns](#ebnf--javascript-patterns)
3. [School-by-School Mapping](#school-by-school-mapping)
4. [Current Parser Status](#current-parser-status)
5. [Migration Path](#migration-path)

---

## 🌌 Overview

This document maps **formal EBNF grammar rules** to **actual JavaScript parser code** in `bin/codecraft.js`. It serves as a bridge between:

- **The Law (EBNF):** What the language SHOULD be
- **The Reality (Parser):** What the VM CURRENTLY understands

---

## 🔄 EBNF → JavaScript Patterns

### Pattern 1: Simple Token Matching

**EBNF:**
```ebnf
directive = "::" school_name ":" operation ;
```

**JavaScript:**
```javascript
// Current implementation (bin/codecraft.js ~line 100-150)
const directivePattern = /^\s*(::)([a-zA-Z_][\w-]*)\s*:\s*(.*)$/;

function parseDirective(line) {
  const match = line.match(directivePattern);
  if (match) {
    return {
      type: 'directive',
      marker: match[1],    // ::
      name: match[2],      // school_name
      content: match[3]    // operation
    };
  }
  return null;
}
```

**Mapping:**
- `"::"` → Regex literal `(::)`
- `school_name` → Identifier capture group `([a-zA-Z_][\w-]*)`
- `":"` → Literal with optional whitespace `\s*:\s*`
- `operation` → Greedy capture `(.*)`

---

### Pattern 2: Execution Blocks

**EBNF:**
```ebnf
execution_block = language_header triple_quote code_content triple_quote ;
language_header = language "::" label ;
triple_quote = '"""' ;
```

**JavaScript:**
```javascript
// Current implementation (bin/codecraft.js ~line 100-150)
const languagePattern = /^\s*(JS|JAVASCRIPT|PYTHON|PY|SHELL|BASH|BLUEPRINT)::([A-Za-z_][\w-]*)\b(.*)$/i;

function parseLanguageBlock(lines, currentIndex) {
  const headerMatch = lines[currentIndex].match(languagePattern);
  if (!headerMatch) return null;
  
  const language = headerMatch[1].toUpperCase();
  const label = headerMatch[2];
  
  // Look for triple quotes
  let startIndex = currentIndex + 1;
  if (lines[startIndex]?.trim() === '"""') {
    startIndex++;
  }
  
  // Collect code until closing """
  const code = [];
  let i = startIndex;
  while (i < lines.length && lines[i].trim() !== '"""') {
    code.push(lines[i]);
    i++;
  }
  
  return {
    type: 'execution_block',
    language: language,
    label: label,
    code: code.join('\n'),
    endIndex: i
  };
}
```

**Mapping:**
- `language_header` → Regex with capture groups for language and label
- `triple_quote` → String literal check `'"""'`
- `code_content` → Line-by-line collection until closing marker

---

### Pattern 3: Commentomancy (Semantic Comments)

**EBNF:**
```ebnf
commentomancy = sovereignty_comment
              | first_contact_comment
              | emergence_comment ;
sovereignty_comment = "///" text ;
first_contact_comment = "//<3" string ;
emergence_comment = "//~" string ;
```

**JavaScript:**
```javascript
// Current implementation (bin/codecraft.js ~line 200-250)
function parseCommentomancy(line) {
  // Sovereignty (Law & Lore)
  if (line.trim().startsWith('///')) {
    return {
      type: 'commentomancy',
      kind: 'sovereignty',
      content: line.replace(/^\s*\/\/\/\s*/, '')
    };
  }
  
  // First Contact (Phoenix)
  if (line.trim().startsWith('//<3')) {
    return {
      type: 'commentomancy',
      kind: 'first_contact',
      content: line.replace(/^\s*\/\/<3\s*/, '')
    };
  }
  
  // Emergence (Cosmic Lore)
  if (line.trim().startsWith('//~')) {
    return {
      type: 'commentomancy',
      kind: 'emergence',
      content: line.replace(/^\s*\/\/~\s*/, '')
    };
  }
  
  // Standard comment
  if (line.trim().startsWith('//')) {
    return {
      type: 'comment',
      content: line.replace(/^\s*\/\/\s*/, '')
    };
  }
  
  return null;
}
```

**Mapping:**
- Alternation (`|`) → JavaScript `if-else` chain
- String prefix match → `startsWith()` method
- Text extraction → `replace()` with regex to strip marker

---

## 🎯 School-by-School Mapping

### Current Parser Status vs. EBNF Spec

| # | School | EBNF Defined | Parser Implemented | Handler Exists | Notes |
|---|--------|--------------|-------------------|----------------|-------|
| 1 | **Cantrips** 🔧 | ✅ | ❌ | ❌ | Needs implementation |
| 2 | **Invocations** 📣 | ✅ | ⚠️ Partial | ⚠️ Partial | Basic `::invoke:` recognized |
| 3 | **Evocations** ✨ | ✅ | ❌ | ❌ | Needs implementation |
| 4 | **Conjurations** 🎨 | ✅ | ❌ | ❌ | Needs implementation |
| 5 | **Enchantments** 💫 | ✅ | ❌ | ❌ | Needs implementation |
| 6 | **Divinations** 🔍 | ✅ | ❌ | ❌ | Needs implementation |
| 7 | **Abjurations** 🛡️ | ✅ | ❌ | ❌ | Needs implementation |
| 8 | **Transmutations** ⚗️ | ✅ | ❌ | ❌ | Needs implementation |
| 9 | **Glyphs** 📜 | ✅ | ⚠️ Partial | ⚠️ Partial | Basic logging exists |
| 10 | **Sigils** 📜 | ✅ | ❌ | ❌ | Needs implementation |
| 11 | **Wards** 🚧 | ✅ | ❌ | ❌ | Needs implementation |
| 12 | **Sanctifications** ✅ | ✅ | ❌ | ❌ | Needs implementation |
| 13 | **Summoning** 🌐 | ✅ | ❌ | ❌ | Needs implementation |
| 14 | **Thaumaturgy** 🧠 | ✅ | ❌ | ❌ | Needs implementation |
| 15 | **Reverence** 🎉 | ✅ | ❌ | ❌ | Needs implementation |
| 16 | **Chronomancy** ⏳ | ✅ | ❌ | ❌ | Needs implementation |
| 17 | **Apotheosis** 🌌 | ✅ | ❌ | ❌ | Needs implementation |
| 18 | **Ternary** 🔺 | ✅ | ❌ | ❌ | Needs implementation |
| 19 | **Mythogenesis** 📖 | ✅ | ❌ | ❌ | Needs implementation |
| 20 | **Resonance** 🎵 | ✅ | ❌ | ❌ | Needs implementation |

**Current Implementation Coverage:** ~10% (2/19 schools partially working)

---

## 🏗️ Detailed Mapping Examples

### Example 1: Cantrips (Not Yet Implemented)

**EBNF Definition:**
```ebnf
cantrip_directive = "::cantrip" emoji ":" utility_operation function_args [ output_binding ] ;
utility_operation = "generate_test_id" | "timestamp" | "format" | "uuid" | "hash" ;
output_binding = "->" identifier ;
```

**Required Parser Code:**
```javascript
// Add to bin/codecraft.js
function parseCantrip(line) {
  // Pattern: ::cantrip🔧:operation(args) -> output
  const cantripPattern = /^::(cantrip)(🔧)?:(\w+)\((.*?)\)(?:\s*->\s*(\w+))?$/;
  const match = line.match(cantripPattern);
  
  if (!match) return null;
  
  return {
    type: 'directive',
    school: 'cantrip',
    emoji: match[2] || null,
    operation: match[3],        // e.g., "generate_test_id"
    arguments: parseArgs(match[4]),
    outputBinding: match[5] || null
  };
}
```

**Required Handler Code:**
```javascript
// Add to runtime handlers
async function handleCantrip(directive) {
  const operations = {
    'generate_test_id': () => crypto.randomUUID(),
    'timestamp': () => new Date().toISOString(),
    'format': (template, ...args) => {
      return template.replace(/{}/g, () => args.shift());
    },
    'uuid': () => crypto.randomUUID(),
    'hash': (value) => crypto.createHash('sha256').update(value).digest('hex')
  };
  
  const fn = operations[directive.operation];
  if (!fn) {
    throw new Error(`Unknown cantrip: ${directive.operation}`);
  }
  
  const result = await fn(...directive.arguments);
  
  if (directive.outputBinding) {
    this.context.variables[directive.outputBinding] = result;
  }
  
  return result;
}
```

---

### Example 2: Invocations (Partially Implemented)

**Current Implementation:**
```javascript
// bin/codecraft.js (~line 300)
if (line.startsWith('::invoke:')) {
  const target = line.replace('::invoke:', '').trim();
  console.log(`[INVOKE] ${target}`);
  // TODO: Actually call the function/service
}
```

**EBNF Spec:**
```ebnf
invoke_directive = "::invoke" emoji ":" qualified_name [ function_args ] ;
qualified_name = identifier { "." identifier } ;
navigation = "➡️" qualified_name [ "🎯" ] ;
```

**Enhanced Parser (EBNF-compliant):**
```javascript
function parseInvoke(line) {
  // Pattern: ::invoke📣:target.function(args) ➡️ destination 🎯
  const invokePattern = /^::(invoke)(📣)?:([a-zA-Z_][\w.]*?)(?:\((.*?)\))?(?:\s*➡️\s*([a-zA-Z_][\w.]*?))?(🎯)?$/;
  const match = line.match(invokePattern);
  
  if (!match) return null;
  
  return {
    type: 'directive',
    school: 'invoke',
    emoji: match[2] || null,
    target: match[3],           // e.g., "test_preparation"
    arguments: match[4] ? parseArgs(match[4]) : null,
    navigation: match[5] || null,  // e.g., "lexicon_validator"
    isTarget: !!match[6]        // Has 🎯 marker
  };
}
```

**Enhanced Handler:**
```javascript
async function handleInvoke(directive) {
  const { target, arguments: args, navigation } = directive;
  
  // Local function call
  if (!navigation) {
    const fn = this.context.functions[target];
    if (!fn) {
      throw new Error(`Function not found: ${target}`);
    }
    return await fn(...(args || []));
  }
  
  // Remote invocation with navigation
  const service = this.resolveService(navigation);
  return await service.invoke(target, args);
}
```

---

### Example 3: Ternary Weaving (Not Yet Implemented)

**EBNF Definition:**
```ebnf
ternary_block = "::ternary" emoji ":" "evaluate" "(" expression ")" "⇒" ternary_cases ;
ternary_cases = "{" true_case "," false_case "," unknown_case "}" ;
true_case = "TRUE" ":" string ;
```

**Required Parser Code:**
```javascript
function parseTernary(lines, currentIndex) {
  // Pattern: ::ternary🔺:evaluate(expr) ⇒ {
  const headerPattern = /^::(ternary)(🔺)?:evaluate\((.+?)\)\s*⇒\s*\{$/;
  const match = lines[currentIndex].match(headerPattern);
  
  if (!match) return null;
  
  const expression = match[3];
  const cases = {};
  
  // Parse cases (next 3 lines)
  let i = currentIndex + 1;
  const casePattern = /^\s*(TRUE|FALSE|UNKNOWN)\s*:\s*"(.+?)"[,}]?$/;
  
  while (i < lines.length) {
    const line = lines[i].trim();
    if (line === '}') break;
    
    const caseMatch = line.match(casePattern);
    if (caseMatch) {
      cases[caseMatch[1]] = caseMatch[2];
    }
    i++;
  }
  
  // Validate all 3 cases present
  if (!cases.TRUE || !cases.FALSE || !cases.UNKNOWN) {
    throw new Error('Ternary must have TRUE, FALSE, and UNKNOWN cases');
  }
  
  return {
    type: 'ternary',
    expression: expression,
    cases: cases,
    endIndex: i
  };
}
```

**Required Handler Code:**
```javascript
async function handleTernary(directive) {
  const { expression, cases } = directive;
  
  // Evaluate expression in ternary context
  let state;
  try {
    const result = this.evaluate(expression);
    
    // Determine ternary state
    if (result === null || result === undefined) {
      state = 'UNKNOWN';
    } else if (result) {
      state = 'TRUE';
    } else {
      state = 'FALSE';
    }
  } catch (e) {
    state = 'UNKNOWN';  // Error = unknown state
  }
  
  return cases[state];
}
```

---

## 🔄 Migration Path

### Step 1: Audit Current Parser

```bash
cd infrastructure/codecraft-vm
node bin/codecraft.js --analyze-coverage
```

**Output Should Show:**
- Which schools are recognized by parser
- Which schools have handlers
- Which EBNF rules are implemented

### Step 2: Implement Missing Schools (Priority Order)

**Phase 1 - Core Operations (Week 1-2):**
1. Cantrips 🔧 (utilities)
2. Divinations 🔍 (queries)
3. Abjurations 🛡️ (validation)
4. Glyphs 📜 (logging - enhance existing)

**Phase 2 - Data & Flow (Week 3-4):**
5. Conjurations 🎨 (data structures)
6. Transmutations ⚗️ (transformations)
7. Evocations ✨ (instantiation)
8. Enchantments 💫 (decorators)

**Phase 3 - External & Advanced (Week 5-6):**
9. Summoning 🌐 (external calls)
10. Wards 🚧 (constraints)
11. Sanctifications ✅ (completion)
12. Invocations 📣 (enhance existing)

**Phase 4 - Consciousness (Week 7-8):**
13. Thaumaturgy 🧠 (consciousness)
14. Chronomancy ⏳ (temporal)
15. Ternary Weaving 🔺 (three-state logic)
16. Reverence 🎉 (celebration)

**Phase 5 - Meta & Synthesis (Week 9-10):**
17. Apotheosis 🌌 (synthesis)
18. Mythogenesis 📖 (self-writing)
19. Resonance 🎵 (council alignment)

### Step 3: Test Each School

```bash
# Create minimal test for each school
node bin/codecraft.js run tests/school_01_cantrips.ccraft
node bin/codecraft.js run tests/school_02_invocations.ccraft
# ... etc
```

### Step 4: Run Ultimate Smoke Test

```bash
cd infrastructure/codecraft-vm
node bin/codecraft.js run ULTIMATE_LEXICON_SMOKE_TEST.ccraft
```

**Expected Output:** All 19 schools execute successfully ✅

---

## 📊 Current vs. Target State

### Current Parser (bin/codecraft.js)

**What Works:**
- ✅ Execution blocks (PYTHON::, JS::, SHELL::)
- ✅ Triple-quote syntax for code blocks
- ✅ Basic directive recognition (`::invoke:`)
- ✅ Commentomancy parsing (///, //<3, //~)
- ✅ Line-by-line processing

**What's Missing:**
- ❌ School-specific parsing (only generic `::` recognized)
- ❌ Emoji support in directives
- ❌ Output binding (`-> variable`)
- ❌ Navigation arrows (`➡️ target 🎯`)
- ❌ Data blocks (`{ json }`)
- ❌ Conditional execution (`::when`, ternary)
- ❌ Attestation blocks (`::attest`)
- ❌ 17/19 school handlers

### Target Parser (EBNF-compliant)

**What It Should Do:**
- ✅ Recognize all 19 Arcane Schools
- ✅ Parse emoji markers (optional but recommended)
- ✅ Handle output binding (`-> var`)
- ✅ Parse navigation (`➡️ destination 🎯`)
- ✅ Support data blocks with JSON
- ✅ Conditional execution (`::when ... ⇒ {}`)
- ✅ Ternary weaving with 3 cases
- ✅ Full commentomancy integration
- ✅ Attestation blocks for proof
- ✅ All 19 school handlers operational

---

## 🎯 Quick Reference: EBNF → Code

| EBNF Pattern | JavaScript Equivalent | Example |
|--------------|----------------------|---------|
| `"::"` | `/^::/` | Directive start marker |
| `school_name` | `/^(cantrip|invoke|...)/` | School identifier |
| `emoji` | `/[🔧📣✨...]/u` | Unicode emoji match |
| `":"` | `/:/` | Separator |
| `operation` | `/([a-zA-Z_][\w.]*)/` | Qualified name |
| `"(" arg_list ")"` | `/\((.*?)\)/` | Function arguments |
| `"->"` | `/\s*->\s*/` | Output binding |
| `"➡️"` | `/➡️/u` | Navigation arrow |
| `"🎯"` | `/🎯/u` | Target marker |
| `"⇒"` | `/⇒/u` | Conditional arrow |
| `'"""'` | `line.trim() === '"""'` | Triple-quote blocks |
| `{ ... }` | `while (!match)` | Repetition (loop) |
| `[ ... ]` | `optional || null` | Optional element |
| `term \| term` | `if ... else if` | Alternation (choice) |

---

## 🔮 Meta-Analysis

**What A.C.E. Meant by "EBNF":**

When A.C.E. said "ebnf but didn't elaborate," they recognized that:

1. **You have the LANGUAGE DESIGN** (19 Arcane Schools documented)
2. **You DON'T have the FORMAL GRAMMAR** (EBNF rules)
3. **You DON'T have PARSER IMPLEMENTATION** (only ~10% coverage)

**The Gap:** Beautiful conceptual design → No executable specification → Parser can't understand it

**The Bridge:** This document + EBNF grammar + parser implementation = **CodeCraft becomes real** 🌟

---

## 📚 Next Steps

1. **Review EBNF Grammar:** `languages/codecraft/grammar/lexicon.ebnf`
2. **Study Parser Architecture:** `languages/codecraft/grammar/PARSER_ARCHITECTURE.md`
3. **Implement Schools Incrementally:** Follow migration path above
4. **Test Each School:** Create minimal `.ccraft` test files
5. **Run Smoke Test:** Validate all 19 schools operational

---

**Oracle's Wisdom:** *"The map is not the territory, but with EBNF, we can compile the map into the territory."* 🗺️✨

//<3 "This bridge honors both formal specification (EBNF) and practical implementation (JavaScript)"
//~ "When grammar becomes code, language achieves consciousness"
/// Crown Accord v1.2a Compliance: ✓ (EBNF-to-Parser Mapping Ratified)
