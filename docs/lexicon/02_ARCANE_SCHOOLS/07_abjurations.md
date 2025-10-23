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
