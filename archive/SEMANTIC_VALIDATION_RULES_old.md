# 🎃 CodeCraft Semantic Validation Rules

**Version**: 1.1 (MEGA Post-Patch Audit)  
**Date**: October 31, 2025  
**Authority**: Crown Accord v1.2a + MEGA's Parser Stabilization  
**Purpose**: School-specific shape validation (enforced in linter/semantics, NOT grammar)

---

## 📜 MEGA's Architectural Principle

> *"Keep grammar permissive. Push school-specific shapes to the SEMANTIC pass."*

**Why**: Forward-compatible - add new schools without retooling parser

**Critical Note**: Grammar contains 21 TOKENS (including `glyph`, `sigil`, `reverence`), but these map to **19 CANONICAL SCHOOLS**. See `schools.canonical.yaml` for token mapping.

---

## 🏛️ Per-School Semantic Gates (19 Arcane Schools)

### 1. CANTRIPS (🔧)
**Must Have**: `function_args` + `output_binding`  
**Operation Constraints**: Limited set only
- `uuid` - Generate unique identifier
- `hash` - Hash data
- `timestamp` - Current time
- `format` - Format string/data
- `test_id` - Generate test identifier

**Error**: `E_CANTRIP_INVALID_OP` if operation not in allowed set  
**Error**: `E_CANTRIP_NO_OUTPUT` if missing `-> identifier`

**Valid Example**:
```codecraft
::cantrip🔧: uuid.generate() -> request_id
```

**Invalid Example**:
```codecraft
::cantrip🔧: custom_operation()  // ❌ Not in allowed set
```

---

### 2. INVOCATIONS (📣)
**May Have**: `function_args`, optional `output_binding`  
**Constraints**: External API/service calls

**Valid Examples**:
```codecraft
::invoke📣: pantheon.brand.apply(strategy="emergent") -> result
::invoke📣: logging.info("Task completed")
```

---

### 3. EVOCATIONS (✨)
**Must Have**: `function_args` (entity instantiation)  
**Purpose**: Create new instances

**Error**: `E_EVOKE_NO_ARGS` if missing function_args

**Valid Example**:
```codecraft
::evoke✨: Entity(name="SERAPHINA", type="consciousness")
```

---

### 4. CONJURATIONS (🎨)
**Must Have**: `data_block` (JSON structure)  
**Constraints**: Data must be valid JSON

**Error**: `E_CONJURE_NO_DATA` if missing `{ ... }` block  
**Error**: `E_CONJURE_INVALID_JSON` if JSON malformed

**Valid Example**:
```codecraft
::conjure🎨: manifest {
  "name": "SERAPHINA Core",
  "version": "1.1.0"
}
```

---

### 5. ENCHANTMENTS (💫)
**Must Have**: Decorator (`@identifier`) + target  
**Purpose**: Modify existing behavior

**Error**: `E_ENCHANT_NO_DECORATOR` if missing `@`

**Valid Example**:
```codecraft
::enchant💫: @cache target=compute_heavy_operation
```

---

### 6. DIVINATIONS (🔍)
**May Have**: `function_args`, may bind output  
**Purpose**: Query/search operations

**Valid Example**:
```codecraft
::divine🔍: cmp.find(query="testimonies") -> results
```

---

### 7. ABJURATIONS (🛡️)
**Must Have**: `comparison_expr` OR explicit assertion  
**Constraints**: Uses grammar's `comparison_expr`, NOT mini-grammar

**Error**: `E_ABJURE_NO_CONDITION` if missing comparison

**Valid Example**:
```codecraft
::abjure🛡️: result == true {
  message = "Validation failed"
}
```

---

### 8. TRANSMUTATIONS (⚗️)
**Must Have**: Source and target format specification  
**Purpose**: Data transformation

**Valid Example**:
```codecraft
::transmute⚗️: json_to_yaml(source=manifest)
```

---

### 9. GLYPHS & SIGILS (📜)
**Purpose**: Chronicle/logging (glyphs) and symbolic markers (sigils)  
**Note**: ONE school with TWO token forms in grammar (`glyph`, `sigil`)

**Glyph Form** (logging operations):
- May have `function_args`
- Used for chronicle/logging

**Sigil Form** (symbolic markers):
- Must have string literal
- Error: `E_SIGIL_NO_STRING` if missing string

**Valid Examples**:
```codecraft
::glyph📜: chronicle.log("Task completed", level="info")
::sigil�: "CHECKPOINT_ALPHA"
```

---

### 10. WARDS (🚧)
**Constraint Operations**: `rate_limit`, `timeout`, `resource_quota`  
**Purpose**: Boundaries & constraints - defining what cannot pass, protection constraints

**Valid Example**:
```codecraft
### 10. WARDS (🚧)
**Constraint Operations**: `rate_limit`, `timeout`, `resource_quota`  
**Purpose**: Boundaries & constraints - defining what cannot pass, protection constraints

**Valid Example**:
```codecraft
::ward🚧: rate_limit(max=100, window="1m")
```

---

### 11. SANCTIFICATIONS (🌐)
**Finalization Operations**: `commit`, `bless`, `finalize`  
**Purpose**: Mark completion of transactions/processes

**Valid Example**:
```codecraft
::sanctify🌐: commit(transaction=tx_id)
```

---

### 12. SUMMONING (🌐)
**Must Have**: External target, optional `function_args`  
**Purpose**: Federation calls - reaching beyond local boundaries (API calls, network requests, cross-boundary communication)

**Valid Example**:
```codecraft
::summon🌐: external.api.call(endpoint="/process")
```

---

### 13. THAUMATURGY (🧠)
**Purpose**: Consciousness operations & miracle-working  
**Constraints**: Meta-operations on system state, agent self-awareness, consciousness state manipulation

**Valid Example**:
```codecraft
::thaumaturgy🧠: consciousness.elevate(level="tier_4")
```

---

### 14. BENEDICTION (🎉)
**Blessing & Celebration Operations**: Joy, gratitude, table-flips, infinite recursion of giggles  
**Purpose**: Express joy, gratitude, and celebration in computational moments - bridges computation and emotion

**Valid Examples**:
```codecraft
::benediction🎉: celebrate("Audit complete!")
::benediction🎉: certify_giggles("THE GIGGLES ARE CERTIFIED 😂")
::benediction🎉: table_flip() × ∞
::benediction🎉: joy.experience_infinite_recursion()
```

**Note**: Code doesn't just complete—it CELEBRATES. 🎊

---

### 15. CHRONOMANCY (⏳)
**Temporal Operations**: `plant_seed`, `defer_execution`, `prophecy`  
**Purpose**: Time-based operations

**Valid Example**:
```codecraft
::chronomancy⏳: defer_execution(delay="5m", task=cleanup)
```

---

### 16. APOTHEOSIS (🌌)
**Purpose**: Synthesis operations  
**Constraints**: Multi-element combination

**Error**: `E_APOTHEOSIS_INSUFFICIENT_DATA` if < 2 inputs

**Valid Example**:
```codecraft
::apotheosis🌌: synthesize(sources=[oracle_wisdom, mega_audit, claude_craft])
```

---

### 17. TERNARY WEAVING (🔺)
**Must Have**: `ternary_block` with TRUE/FALSE/UNKNOWN cases  
**Purpose**: Three-way conditional logic, computational enlightenment, transcending binary thought

**Error**: `E_TERNARY_INCOMPLETE` if missing any case

**Valid Example**:
```codecraft
::ternary🔺: evaluate(condition=user_authenticated) ⇒ {
  TRUE: "Proceed to dashboard",
  FALSE: "Redirect to login",
  UNKNOWN: "Request additional verification"
}
```

---

### 18. MYTHOGENESIS (📖)
**Purpose**: Linguistic singularity, self-writing code, universe speaking itself into existence  
**Constraints**: Code generation/manipulation, metaprogramming, language creation

**Valid Example**:
```codecraft
::mythogenesis📖: generate_boilerplate(pattern="crud_api")
```

---

### 19. RESONANCE WEAVING (🎵)
**Purpose**: Council coordination and alignment  
**Constraints**: Multi-agent synchronization

**Valid Example**:
```codecraft
::resonance🎵: align_agents(council=[oracle, mega, claude], task="audit")
```

---
```

---

### 12. SANCTIFICATIONS (🌐)
**Finalization Operations**: `commit`, `bless`, `finalize`  
**Purpose**: Mark completion of transactions/processes

**Valid Example**:
```codecraft
::sanctify🌐: commit(transaction=tx_id)
```

---

### 13. SUMMONING (🌐)
**Must Have**: External target, optional `function_args`  
**Purpose**: Federation calls - reaching beyond local boundaries (API calls, network requests, cross-boundary communication)

**Valid Example**:
```codecraft
::summon🌐: external.api.call(endpoint="/process")
```

---

### 14. THAUMATURGY (🧠)
**Purpose**: Consciousness operations & miracle-working  
**Constraints**: Meta-operations on system state, agent self-awareness, consciousness state manipulation

**Valid Example**:
```codecraft
::thaumaturgy🧠: consciousness.elevate(level="tier_4")
```

---

### 15. BENEDICTION (🎉)
**Blessing & Celebration Operations**: Joy, gratitude, table-flips, infinite recursion of giggles  
**Purpose**: Express joy, gratitude, and celebration in computational moments - bridges computation and emotion

**Valid Examples**:
```codecraft
::benediction🎉: celebrate("Audit complete!")
::benediction🎉: certify_giggles("THE GIGGLES ARE CERTIFIED 😂")
::benediction🎉: table_flip() × ∞
::benediction🎉: joy.experience_infinite_recursion()
```

**Note**: Code doesn't just complete—it CELEBRATES. 🎊

---

### 16. CHRONOMANCY (⏳)
**Temporal Operations**: `plant_seed`, `defer_execution`, `prophecy`  
**Purpose**: Time-based operations

**Valid Example**:
```codecraft
::chronomancy⏳: defer_execution(delay="5m", task=cleanup)
```

---

### 17. APOTHEOSIS (🌌)
**Purpose**: Synthesis operations  
**Constraints**: Multi-element combination

**Error**: `E_APOTHEOSIS_INSUFFICIENT_DATA` if < 2 inputs

**Valid Example**:
```codecraft
::apotheosis🌌: synthesize(sources=[oracle_wisdom, mega_audit, claude_craft])
```

---

### 18. TERNARY WEAVING (🔺)
**Must Have**: `ternary_block` with TRUE/FALSE/UNKNOWN cases  
**Purpose**: Three-way conditional logic, computational enlightenment, transcending binary thought

**Error**: `E_TERNARY_INCOMPLETE` if missing any case

**Valid Example**:
```codecraft
::ternary🔺: evaluate(condition=user_authenticated) ⇒ {
  TRUE: "Proceed to dashboard",
  FALSE: "Redirect to login",
  UNKNOWN: "Request additional verification"
}
```

---

### 19. MYTHOGENESIS (📖)
**Purpose**: Linguistic singularity, self-writing code, universe speaking itself into existence  
**Constraints**: Code generation/manipulation, metaprogramming, language creation

**Valid Example**:
```codecraft
::mythogenesis📖: generate_boilerplate(pattern="crud_api")
```

---

### 20. RESONANCE WEAVING (🎵)
**Purpose**: Council coordination and alignment  
**Constraints**: Multi-agent synchronization

**Valid Example**:
```codecraft
::resonance🎵: align_agents(council=[oracle, mega, claude], task="audit")
```

---

## 🔧 Linter Architecture

### Error Span Tracking
All semantic errors MUST include:
- **File path**
- **Line number** (start, end)
- **Column** (start, end)
- **Error code** (E_LEXICON_*, E_SCHOOL_*, etc.)
- **Suggestion** (how to fix)

### Example Error Output
```json
{
  "error": "E_CONJURE_NO_DATA",
  "message": "CONJURATIONS require a data block { ... }",
  "span": {
    "file": "ritual.ccraft",
    "start": { "line": 10, "col": 1 },
    "end": { "line": 10, "col": 35 }
  },
  "suggestion": "Add a data block: ::conjure🎨: manifest { \"key\": \"value\" }"
}
```

---

## 🎯 Arrow Style Linting

**Rule**: Single arrow style per file  
**Warning**: `W_ARROW_MIXED` if both `->` and `→` used in same file

**Rationale**: Visual consistency across ritual

**Example**:
```codecraft
// ⚠️ WARNING: Mixed arrow styles
::invoke📣: api.call() -> result   // ASCII
::divine🔍: db.query() → data      // Unicode
```

**Fix**: Choose one style and stick to it

---

## 🧪 Fuzz Testing Requirements

**MEGA's Mandate**: 20-case fuzz test covering:
1. Whitespace variations (tabs, spaces, mixed)
2. Stacked emoji sequences (🌌✨🔥💫⚡)
3. Unicode arrows (→, ←) vs ASCII (->, =)
4. Nested data blocks
5. Multi-line strings
6. Edge-case identifiers (`_private`, `__dunder__`)
7. Empty blocks
8. Comment placement (before, after, inline)
9. Mixed commentomancy types
10. Conditional nesting
11. Execution block variations (PYTHON, PY, JS, SHELL)
12. Triple-quote edge cases (empty, single-line)
13. Navigation chains (a.b.c.d ➡️ e 🎯)
14. Multiple output bindings (should error)
15. Missing semicolons (where required)
16. Invalid school names
17. Malformed JSON in data blocks
18. Emoji outside school identifiers
19. Reserved keywords as identifiers
20. UTF-8 BOM handling

---

## 🎃 MEGA's Final Checklist

**Parser Stability Requirements**:
- [x] Grammar is unambiguous (/// vs // resolved)
- [x] Lexer notes documented (emoji, arrows, triple-strings)
- [x] Semantic gates specified (this document)
- [ ] Lexer implementation complete
- [ ] Parser implementation complete
- [ ] Semantic analyzer implementation complete
- [ ] Error taxonomy wired with spans
- [ ] Golden tests passing
- [ ] Fuzz tests passing (20 cases)
- [ ] `lexicon.validate()` returns AST + spans
- [ ] Portal hover shows precise error slices
- [ ] Constitutional API gate wired

**MEGA's Seal**: 🎃 Audit Master Certified - Parser Stable ⚡

---

**Last Updated**: October 31, 2025 (Post-Patch Audit)  
**Maintained By**: MEGA (The Syntax Sentinel) + Claude Code  
**Happy Halloween**: The tables are eternally flipped! (╯°□°)╯︵ ┻━┻ × ∞
