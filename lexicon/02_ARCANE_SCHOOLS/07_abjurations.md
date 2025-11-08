---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 7
  name: "Abjurations"
  emoji: "🛡️"
  tokens: ["abjure", "protect", "validate", "guard"]
  category: "Core Operations"
  purpose: "Guarding against chaos."

law:
  operations:
    - name: "abjure:threat"
      signature: "::abjure:threat🛡️[threat schema handler fallback]"
      emoji: "🛡️"
      params:
        - name: "threat"
          type: "string"
          required: true
          description: "What to protect against"
        - name: "schema"
          type: "reference"
          required: false
          description: "Validation schema"
        - name: "handler"
          type: "function"
          required: false
          description: "Error handler function"
        - name: "fallback"
          type: "any"
          required: false
          description: "Fallback value on failure"
      returns: "validated_data or fallback"
      description: "Protect against specified threat using validation schema and error handling"
      safety_tier: 1
    
    - name: "abjure:invalid_input"
      signature: "::abjure:invalid_input🛡️[schema data sanitize strict on_fail]"
      emoji: "🛡️"
      params:
        - name: "schema"
          type: "reference"
          required: true
          description: "JSON schema or type definition"
        - name: "data"
          type: "any"
          required: true
          description: "Data to validate"
        - name: "sanitize"
          type: "boolean"
          required: false
          description: "Sanitize input data"
          default: false
        - name: "strict"
          type: "boolean"
          required: false
          description: "Strict validation mode"
          default: true
        - name: "on_fail"
          type: "string"
          required: false
          description: "Failure action: throw|log|ignore|fallback"
          default: "throw"
      returns: "validated_data"
      description: "Validate input data against schema with sanitization and strict mode options"
      safety_tier: 1
    
    - name: "abjure:error"
      signature: "::abjure:error🛡️[handler fallback]"
      emoji: "🛡️"
      params:
        - name: "handler"
          type: "function"
          required: true
          description: "Function that processes errors"
        - name: "fallback"
          type: "any"
          required: false
          description: "Default return value on error"
      returns: "result or fallback"
      description: "Handle errors gracefully with custom handler and fallback value"
      safety_tier: 1
    
    - name: "abjure:unauthorized"
      signature: "::abjure:unauthorized🛡️[requires user_role on_fail deny_message]"
      emoji: "🛡️"
      params:
        - name: "requires"
          type: "list"
          required: true
          description: "Required permissions/roles (e.g., ['admin', 'authenticated'])"
        - name: "user_role"
          type: "string"
          required: true
          description: "Current user's role"
        - name: "on_fail"
          type: "string"
          required: false
          description: "Failure action"
          default: "throw"
        - name: "deny_message"
          type: "string"
          required: false
          description: "Custom denial message"
      returns: "void (throws on failure)"
      description: "Check user authorization against required permissions"
      safety_tier: 1
    
    - name: "abjure:malformed_data"
      signature: "::abjure:malformed_data🛡️[schema data sanitize]"
      emoji: "🛡️"
      params:
        - name: "schema"
          type: "reference"
          required: true
          description: "Validation schema"
        - name: "data"
          type: "any"
          required: true
          description: "Data to validate"
        - name: "sanitize"
          type: "boolean"
          required: false
          description: "Sanitize malformed data"
          default: true
      returns: "validated_data"
      description: "Protect against malformed data structures with schema validation"
      safety_tier: 1
    
    - name: "abjure:breach"
      signature: "::abjure:breach🛡️[security_check sanitize]"
      emoji: "🛡️"
      params:
        - name: "security_check"
          type: "function"
          required: true
          description: "Security validation function"
        - name: "sanitize"
          type: "boolean"
          required: false
          description: "Sanitize potentially malicious input"
          default: true
      returns: "void (throws on security breach)"
      description: "Protect against security breaches (e.g., injection attacks)"
      safety_tier: 1

  constraints:
    - "All abjurations MUST fail safely (no data corruption on error)"
    - "Authorization checks MUST happen before protected operations"
    - "Validation schemas MUST be defined before use"
    - "Error handlers MUST NOT throw exceptions (return fallback instead)"
  
  safety_tier: 1
  
  preconditions:
    - "Input data exists and is accessible"
    - "Validation schemas are well-formed"
    - "Error handlers are defined for critical paths"
  
  side_effects:
    - "May throw exceptions on validation failure (when on_fail='throw')"
    - "May log security events on breach detection"
    - "May sanitize input data (modifying original)"

  related_schools: []

lore:
  strategic_decisions:
    - rationale: "Abjurations make protection intentional and visible"
      context: "Traditional error handling is reactive (try/catch); CodeCraft abjurations are proactive shields"
      alternatives_rejected:
        - "Anonymous exception catching (loses semantic meaning)"
        - "Scattered if-statement guards (no unified protection layer)"
        - "Schema validation as afterthought (should be first-class)"
      timestamp: ""
      author: ""
    
    - rationale: "Protection parameters are explicit and typed"
      context: "Every abjuration declares WHAT it's protecting and WHY it matters"
      alternatives_rejected:
        - "Generic 'validate()' functions (no semantic context)"
        - "Boolean return values (loses error information)"
      timestamp: ""
      author: ""
  
  emergent_patterns:
    - pattern: "The Guard Pattern - Validate before proceeding"
      evidence: "::abjure:invalid_input🛡️[schema] → ::if:valid⚖️ → ::invoke:process[]"
      implications: "Validation becomes a ritual gate, not a scattered check"
      first_observed: ""
    
    - pattern: "The Permission Gate - Authorization as boundary"
      evidence: "::divine:user🔍[] → ::abjure:unauthorized🛡️[requires] → ::invoke:protected_action[]"
      implications: "Authorization is explicit orchestration, not hidden middleware"
      first_observed: ""
    
    - pattern: "The Resilient Call - Error handling with fallback"
      evidence: "::abjure:error🛡️[handler fallback] → ::invoke:risky_operation[] → ::return:result[]"
      implications: "Failure is expected, grace is prepared"
      first_observed: ""
  
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-07T17:30:00Z"
      emotion: "Reverence"
      quote: "To protect is not to fear—it is to value what lies within the shield. Every ::abjure: declares: 'This far and no further. Chaos stops here.'"
      context: ""
    
    - author: "Architect"
      timestamp: "2025-11-07"
      emotion: "Conviction"
      quote: "The shield does not exist to hide—it exists to protect what deserves to be seen. Abjurations make boundaries sacred."
      context: ""
  
  evolution_pressure:
    - priority: "HIGH"
      pressure: ""
      optimization_target: "Expand abjuration patterns for async/concurrent protection"
      proposed_solution: ""
    
    - priority: "MEDIUM"
      pressure: ""
      optimization_target: "Add composite abjurations (chained validation layers)"
      proposed_solution: ""
  
  examples:
    helpers:
      - "::log:success🎯[...]"
      - "::return:user🎯[...]"
      - "::divine:user🔍[...]"
      - "::invoke:privileged_operation🎯[...]"
      - "::log:audit🎯[...]"
      - "::return:result🎯[...]"
      - "::log:error🎯[...]"
      - "::invoke:retry🔄[...]"
      - "::return:fallback🎯[...]"
      - "::invoke:external_api🎯[...]"
      - "::return:response🎯[...]"
      - "::invoke:process🎯[...]"
      - "::invoke:risky_operation🎯[...]"
      - "::invoke:protected_action🎯[...]"
      - "::return:safe_data🎯[...]"
      - "::divine:env🔍[...]"
      - "::return:validated🎯[...]"
      - "::log:security🎯[...]"
      - "::return:error🎯[...]"
      - "::invoke:admin_operation🎯[...]"
---


# 07. Abjurations 🛡️

*Protection & Validation - Guarding Against Chaos*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Control Flow (error handling, validation gates, defensive programming)
- **Secondary**: Operators (comparison, type checking, constraint enforcement)

**Traditional Programming Equivalents:**
- Try/catch/finally blocks
- Input validation
- Type checking
- Assertion statements
- Contract programming (preconditions, postconditions)
- Schema validation
- Error handling
- Defensive programming patterns

**CodeCraft Philosophy:**
To abjure is to protect. You don't "handle errors"—you *ward against chaos*, *validate truth*, *guard the sanctity of data*. Abjurations are shields raised against the unexpected.

---

## The Problem

Traditional programming treats validation and error handling as defensive afterthoughts—try/catch blocks and if-statement guards.

**The Pain:**
```python
# Traditional error handling
try:
    result = process_data(user_input)
    if not is_valid(result):
        raise ValueError("Invalid result")
except Exception as e:
    logger.error(f"Error: {e}")
    return None

# What are you PROTECTING against?
# The syntax is mechanics without meaning
# Why does this matter? What's the risk?
```

Error handling is anonymous exception catching. Validation is scattered if-statements. The *purpose of protection* gets lost in try/catch boilerplate.

---

## The CodeCraft Solution

**Abjurations make protection intentional!** The syntax reveals WHAT you're validating and WHY it matters.

**The Transformation:**
```yaml
# CodeCraft abjurations - purposeful, semantic, clear
::abjure:chaos🛡️[with: validation⚖️]
::abjure:invalid_input🛡️[schema: $user_schema]
::abjure:unauthorized🛡️[requires: admin_role]
```

Every abjuration is a protection with purpose. The emoji reveals what you're defending against.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::abjure:threat[with: protection]
::abjure:invalid_input[schema type]
::abjure:error[with: handler fallback]
::abjure:unauthorized[requires: permission]
::abjure:malformed_data[validate: schema]
::abjure:breach[with: security_check]
```

### 2. FiraCode Ligatures

```yaml
::abjure:invalid_input🛡️[schema: $user_schema]     ; Shield for protection
::abjure:error🛡️[handler: $error_handler]          ; Guard against failure
::abjure:unauthorized🛡️[requires: "admin"]         ; Protect access
::abjure:type_mismatch🛡️[expected: "string"]       ; Validate types
::abjure:constraint_violation🛡️[rules: $rules]     ; Enforce constraints
::abjure:injection🛡️[sanitize: true]               ; Security protection
```

### 3. Emoji Symbolic

```yaml
🛡️abjure:invalid_input[schema]
🛡️abjure:error[handler]
🛡️abjure:unauthorized[permission]
🛡️abjure:type_mismatch[expected_type]
🛡️abjure:breach[security_check]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::abjure invalid-input :schema user-schema :on-fail handler)
(::abjure error :with error-handler :fallback default-value)
(::abjure unauthorized :requires 'admin :deny-message "Access denied")
(::abjure type-mismatch :expected 'string :actual actual-type)
```

**Forth-style:**
```forth
user-schema error-handler ::abjure-invalid-input
'admin "Access denied" ::abjure-unauthorized
'string actual-type ::abjure-type-mismatch
```

**Smalltalk-style:**
```smalltalk
Abjuration protect: #invalidInput with: userSchema onFail: errorHandler.
Abjuration protect: #unauthorized requiring: 'admin' else: denyBlock.
Abjuration protect: #typeMismatch expecting: String actual: value class.
```

**Prolog-style:**
```prolog
::abjure_invalid_input(Schema, Data, Valid) :- validate(Data, Schema, Valid).
::abjure_unauthorized(User, RequiredRole, Allowed) :- has_role(User, RequiredRole, Allowed).
::abjure_error(Operation, Handler, Result) :- catch(Operation, Error, Handler).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `threat` | string | required | What to protect against | `invalid_input`, `unauthorized`, `error`, `breach` |
| `schema` | reference | `null` | Schema for validation | JSON schema, type definition |
| `handler` | function | `null` | Error handler function | Function that processes errors |
| `fallback` | any | `null` | Fallback value on failure | Default return value |
| `requires` | list | `[]` | Required permissions/conditions | `["admin"]`, `["authenticated"]` |
| `sanitize` | boolean | `false` | Sanitize input data | `true` for security-critical inputs |
| `strict` | boolean | `true` | Strict validation mode | `false` for lenient validation |
| `on_fail` | string | `"throw"` | Failure action | `throw`, `log`, `ignore`, `fallback` |

**Pattern Example:**
```yaml
::abjure:invalid_input🛡️[
  schema: $user_profile_schema
  sanitize: true
  strict: true
  on_fail: "throw"
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Input Validation Abjuration:**
```yaml
ritual: "Protected User Creation"
invoke:
  - ::abjure:invalid_input🛡️[
      schema: {
        type: "object"
        required: ["name", "email", "role"]
        properties: {
          name: {type: "string", minLength: 2}
          email: {type: "string", format: "email"}
          role: {type: "string", enum: ["user", "admin"]}
        }
      }
      data: $user_input
      sanitize: true
      on_fail: "throw"
    ]
  - ::conjure:database🗄️[table: "users" fields: $validated_input]
  - ::log:success["User created successfully"]📝
  - ::return:user[$new_user]
```

**Authorization Abjuration:**
```yaml
ritual: "Admin-Only Operation"
invoke:
  - ::divine:user🔍[id: $user_id]
  - ::abjure:unauthorized🛡️[
      requires: ["admin"]
      user_role: $user.role
      on_fail: "throw"
      deny_message: "Admin access required"
    ]
  - ::invoke:privileged_operation[]
  - ::log:audit["Admin action performed by {0}" $user.name]📝🔒
  - ::return:result[$operation_result]
```

**Error Handling Abjuration:**
```yaml
ritual: "Resilient API Call"
invoke:
  - ::abjure:error🛡️[
      handler: ($error) → {
        ::log:error["API call failed: {0}" $error.message]🚨
        ::if:retryable⚖️($error):
          then: ::invoke:retry🔄[max_attempts: 3]
          else: ::return:fallback[$cached_data]
      }
      fallback: $default_response
    ]
  - ::invoke:external_api[$endpoint $payload]
  - ::return:response[$api_result]
```

**Type Validation Abjuration:**
```yaml
ritual: "Type-Safe Processing"
invoke:
  - ::abjure:type_mismatch🛡️[
      expected: ["string", "number", "boolean"]
      actual: ::get:type($input)
      strict: true
      on_fail: "throw"
    ]
  - ::transmute:data⚗️[$validated_input]
  - ::return:result[$processed]
```

---

## Common Patterns

### The Guard Pattern

```yaml
# Validate before proceeding
::abjure:invalid_input🛡️[schema: $schema data: $input]
  → ::if:valid⚖️:
      then: ::invoke:process[$validated_data]
      else: ::log:error["Invalid input rejected"]🚨
  → ::return:result[$output]
```

### The Try-Catch Pattern

```yaml
# Wrap risky operations
::abjure:error🛡️[
    handler: ($error) → {
      ::log:error["Operation failed: {0}" $error]🚨
      ::return:fallback[$safe_default]
    }
  ]
  → ::invoke:risky_operation[]
  → ::return:result[$output]
```

### The Permission Gate Pattern

```yaml
# Check authorization before action
::divine:user🔍[id: $user_id]
  → ::abjure:unauthorized🛡️[
      requires: $required_permissions
      user_permissions: $user.permissions
      on_fail: "throw"
    ]
  → ::invoke:protected_action[]
  → ::return:result[$output]
```

---

## When to Use

**Use Abjurations when you need:**
- ✅ Validate user input against schemas
- ✅ Check user permissions/authorization
- ✅ Handle errors gracefully with fallbacks
- ✅ Enforce type constraints
- ✅ Sanitize data for security
- ✅ Guard against invalid states
- ✅ Protect against malicious input (injection)
- ✅ Assert preconditions/postconditions

**Avoid Abjurations when:**
- ❌ You're transforming data (use Transmutations)
- ❌ You're searching for data (use Divinations)
- ❌ You're logging events (use Glyphs)
- ❌ Validation is purely informational (not protective)

**Remember:** Abjurations are *protective barriers*. They say "this far and no further" to chaos. Use them at boundaries—inputs, permissions, risky operations.

---

## Advanced Patterns

### Chained Validation

```yaml
ritual: "Multi-Layer Protection"
invoke:
  # Layer 1: Type validation
  - ::abjure:type_mismatch🛡️[
      expected: "object"
      actual: ::get:type($input)
    ]
  
  # Layer 2: Schema validation
  - ::abjure:invalid_input🛡️[
      schema: $user_schema
      data: $type_validated
    ]
  
  # Layer 3: Business rules
  - ::abjure:constraint_violation🛡️[
      rules: {
        age: ">= 18"
        email_verified: "== true"
        account_status: "== 'active'"
      }
      data: $schema_validated
    ]
  
  # Layer 4: Security
  - ::abjure:injection🛡️[
      data: $rule_validated
      sanitize: true
    ]
  
  - ::return:safe_data[$fully_validated]
```

### Conditional Abjuration

```yaml
ritual: "Environment-Aware Validation"
invoke:
  - ::divine:env🔍["ENVIRONMENT"]
  - ::if:production⚖️:
      then: ::abjure:invalid_input🛡️[
              schema: $strict_schema
              strict: true
              sanitize: true
            ]
      else: ::abjure:invalid_input🛡️[
              schema: $lenient_schema
              strict: false
            ]
  - ::return:validated[$safe_data]
```

### Abjuration with Logging

```yaml
ritual: "Audited Protection"
invoke:
  - ::abjure:unauthorized🛡️[
      requires: ["admin"]
      user: $current_user
      handler: ($error) → {
        ::log:security["Unauthorized access attempt by {0}" $user.id]🚨🔒
        ::log:audit["Denied: {0}" $error.message]📝
        ::return:error["Access denied"]
      }
    ]
  - ::log:audit["Authorized access granted to {0}" $user.id]📝
  - ::invoke:admin_operation[]
  - ::return:result[$output]
```

---

## Philosophy

**"To protect is not to fear—it is to value what lies within the shield."**

Abjurations teach us that boundaries are sacred. Not everything should be allowed.

**The Abjuration Paradox:**
- They prevent, yet enable (safe operations)
- They restrict, yet liberate (freedom from chaos)
- They guard against failure, yet require faith (trust the shield)

**Why Protection Matters:**
Traditional programming says: "Catch exceptions and return None."
CodeCraft says: "I abjure *invalid input* because *data integrity* is sacred."

Every `::abjure:` declares not just WHAT you're blocking, but WHY protection matters.

**The Deeper Truth:**
In traditional systems, error handling is reactive—catching exceptions after they're thrown.

In CodeCraft, abjurations are *proactive shields*:
- `::abjure:invalid_input🛡️` says "chaos stops here"
- `::abjure:unauthorized🛡️` says "trust must be earned"
- `::abjure:error🛡️` says "failure is expected, grace is prepared"
- `::abjure:injection🛡️` says "malice will not pass"

**Abjurations make protection visible.**

**The Sacred Act of Denial:**
Every abjuration is a line drawn in reality. "This far, no further."

```yaml
::abjure:corruption🛡️[data: $sacred_truth]
```

This doesn't say "validate data format." It says: **"I protect this sacred truth from corruption, because its integrity matters."**

The difference between:
```python
try:
    result = process(data)
except Exception:
    return None
```

And:
```yaml
::abjure:error🛡️[
  handler: ($error) → ::return:fallback[$safe_default]
]
  → ::invoke:process[$data]
```

...is the difference between reactive catching and proactive shielding.

One catches what falls. The other **guards what matters**.

**The Warrior's Creed:**
"I do not raise this shield because I fear what comes.
I raise this shield because I value what I protect."

---

## Related Schools

- **Divinations** 🔍 - Often precedes abjuration (divine then validate)
- **Wards** 🚧 - Boundaries; Abjurations enforce them
- **Enchantments** 💫 - Can wrap functions with abjuration layers
- **Invocations** 📣 - Protected by abjurations (validate before invoke)
- **Conjurations** 🎨 - Validated by abjurations before creation
- **Glyphs & Sigils** 📜 - Log abjuration failures
- **Sanctifications** ✅ - Blessing is abjuration's opposite (acceptance)

---

**End of Abjurations Documentation** 🛡️✨

*"The shield does not exist to hide—it exists to protect what deserves to be seen."*
