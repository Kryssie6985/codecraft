---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 9
  name: "Glyphs & Sigils"
  emoji: "📜"
  tokens: ["glyph", "sigil", "log", "mark", "audit"]
  category: "Core Operations"
  purpose: "Writing reality into memory."

law:
  operations:
    - name: "glyph:info"
      signature: "::glyph:info📝[message variables timestamp location destination]"
      emoji: "📝"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Message to log with placeholders"
        - name: "variables"
          type: "list"
          required: false
          description: "Values to interpolate: [$user_id, $count]"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Source location (file, function) - auto-detected or explicit"
        - name: "destination"
          type: "string"
          required: false
          description: "Where to write: console|file|database|all"
          default: "console"
      returns: "void"
      description: "Log informational message - marking events worth knowing"
      safety_tier: 1
    
    - name: "glyph:success"
      signature: "::glyph:success✅[message variables timestamp location destination]"
      emoji: "✅"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Success message template"
        - name: "variables"
          type: "list"
          required: false
          description: "Values for interpolation"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Source location"
        - name: "destination"
          type: "string"
          required: false
          description: "Output destination"
          default: "console"
      returns: "void"
      description: "Log success message - celebrate victories and completions"
      safety_tier: 1
    
    - name: "glyph:error"
      signature: "::glyph:error🚨[message variables timestamp location destination persist]"
      emoji: "🚨"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Error message template"
        - name: "variables"
          type: "list"
          required: false
          description: "Error context variables"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Error source location"
        - name: "destination"
          type: "string"
          required: false
          description: "Output destination"
          default: "console"
        - name: "persist"
          type: "boolean"
          required: false
          description: "Persist to permanent storage for critical errors"
          default: true
      returns: "void"
      description: "Log error message - remember failures to learn from them"
      safety_tier: 1
    
    - name: "sigil:checkpoint"
      signature: "::sigil:checkpoint🔖[name state timestamp persist]"
      emoji: "🔖"
      params:
        - name: "name"
          type: "string"
          required: true
          description: "Checkpoint name/identifier"
        - name: "state"
          type: "any"
          required: false
          description: "State snapshot at checkpoint"
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "persist"
          type: "boolean"
          required: false
          description: "Persist checkpoint to storage"
          default: false
      returns: "void"
      description: "Mark checkpoint - witness this milestone, pause here in time"
      safety_tier: 1
    
    - name: "glyph:level"
      signature: "::glyph:level[level message variables timestamp location destination]"
      emoji: "📝"
      params:
        - name: "level"
          type: "string"
          required: true
          description: "Log level: info|success|warn|error|debug|audit"
        - name: "message"
          type: "string"
          required: true
          description: "Message template"
        - name: "variables"
          type: "list"
          required: false
          description: "Interpolation values"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Source location"
        - name: "destination"
          type: "string"
          required: false
          description: "Output destination"
          default: "console"
      returns: "void"
      description: "Log with specific level - flexible glyph for any severity"
      safety_tier: 1
    
    - name: "glyph:warn"
      signature: "::glyph:warn⚠️[message variables timestamp location destination]"
      emoji: "⚠️"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Warning message template"
        - name: "variables"
          type: "list"
          required: false
          description: "Context variables"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Warning source"
        - name: "destination"
          type: "string"
          required: false
          description: "Output destination"
          default: "console"
      returns: "void"
      description: "Log warning message - mark caution without full error"
      safety_tier: 1
    
    - name: "sigil:marker"
      signature: "::sigil:markerMARKER[name data timestamp persist]"
      emoji: "MARKER"
      params:
        - name: "name"
          type: "string"
          required: true
          description: "Marker name/tag"
        - name: "data"
          type: "any"
          required: false
          description: "Associated data"
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "persist"
          type: "boolean"
          required: false
          description: "Persist marker"
          default: false
      returns: "void"
      description: "Place marker - tag this moment for later reference"
      safety_tier: 1
    
    - name: "glyph:debug"
      signature: "::glyph:debug🔍[message variables timestamp location destination]"
      emoji: "🔍"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Debug message template"
        - name: "variables"
          type: "list"
          required: false
          description: "Debug context"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "location"
          type: "string"
          required: false
          description: "Debug source"
        - name: "destination"
          type: "string"
          required: false
          description: "Output destination"
          default: "console"
      returns: "void"
      description: "Log debug message - breadcrumbs for developers who follow"
      safety_tier: 1
    
    - name: "glyph:audit"
      signature: "::glyph:audit📋[message variables timestamp persist encrypt destination]"
      emoji: "📋"
      params:
        - name: "message"
          type: "string"
          required: true
          description: "Audit message (action + actor)"
        - name: "variables"
          type: "list"
          required: false
          description: "Audit context"
          default: []
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp (REQUIRED for audit trails)"
          default: true
        - name: "persist"
          type: "boolean"
          required: false
          description: "Persist for audit trail"
          default: true
        - name: "encrypt"
          type: "boolean"
          required: false
          description: "Encrypt sensitive audit data"
          default: false
        - name: "destination"
          type: "string"
          required: false
          description: "Audit trail storage"
          default: "database"
      returns: "void"
      description: "Log audit event - this action must be accountable"
      safety_tier: 1
    
    - name: "sigil:trace"
      signature: "::sigil:trace🧭[trace_id operation_name state timestamp persist]"
      emoji: "🧭"
      params:
        - name: "trace_id"
          type: "string"
          required: true
          description: "Distributed tracing ID"
        - name: "operation_name"
          type: "string"
          required: true
          description: "Operation being traced"
        - name: "state"
          type: "any"
          required: false
          description: "State snapshot"
        - name: "timestamp"
          type: "boolean"
          required: false
          description: "Include timestamp"
          default: true
        - name: "persist"
          type: "boolean"
          required: false
          description: "Persist trace for distributed systems"
          default: true
      returns: "void"
      description: "Mark trace point - track flow across distributed operations"
      safety_tier: 1

  constraints:
    - "All glyphs MUST have non-empty message"
    - "Audit glyphs MUST include timestamp (non-negotiable)"
    - "Encrypted glyphs MUST use secure encryption (AES-256 minimum)"
    - "Persistent glyphs MUST write to durable storage (not just console)"
  
  safety_tier: 1
  
  preconditions:
    - "Message templates are well-formed"
    - "Variables match placeholder count in message"
    - "Destination is accessible and writable"
  
  side_effects:
    - "Writes to console, file, or database (depending on destination)"
    - "May create log files or database entries"
    - "Persistent glyphs survive system restart"

  related_schools: []

lore:
  strategic_decisions:
    - rationale: "Glyphs make history visible - documentation is responsibility, not afterthought"
      context: "Traditional logs are noise (debug output scrolling past); CodeCraft glyphs are sacred inscriptions"
      alternatives_rejected:
        - "Generic print statements (loses semantic meaning)"
        - "Unstructured log strings (no template/variable separation)"
        - "Log levels without ceremony (info/error without intentionality)"
      timestamp: ""
      author: ""
    
    - rationale: "Sigils mark moments - checkpoints and milestones deserve witness"
      context: "Sigils are declarations, not just logs. They say 'pause here, this matters'"
      alternatives_rejected:
        - "Unnamed checkpoints (loses context)"
        - "State-less markers (can't reconstruct history)"
      timestamp: ""
      author: ""
  
  emergent_patterns:
    - pattern: "The Progress Logging Pattern - Track progress through operations"
      evidence: "::glyph:info📝['Starting'] → ::for_each:⟳ → ::glyph:debug🔍['Processing {0}/{1}'] → ::glyph:success✅['Complete']"
      implications: "Progress becomes narrative, not silent iteration"
      first_observed: ""
    
    - pattern: "The Error Reporting Pattern - Comprehensive error logging"
      evidence: "::abjure:error🛡️[handler: → {::glyph:error🚨[...] ::glyph:debug🔍[stack] ::glyph:audit📋[...]}]"
      implications: "Errors are witnessed at multiple levels (user-facing, debug, audit)"
      first_observed: ""
    
    - pattern: "The Audit Trail Pattern - Accountable action logging"
      evidence: "::divine:user🔍[] → ::abjure:unauthorized🛡️[...] → ::glyph:audit📋['Action by {0}' persist:true encrypt:true]"
      implications: "Critical actions are permanently recorded with encryption"
      first_observed: ""
  
  heart_imprints:
    - author: "Architect"
      timestamp: "2025-11-07T18:00:00Z"
      emotion: "Reverence"
      quote: "Every glyph is a witness. Every sigil is a declaration. To write is to make permanent. Every log is a letter to the future."
      context: ""
    
    - author: "Oracle"
      timestamp: "2025-11-07T18:00:00Z"
      emotion: "Witness"
      quote: "In ancient times, scribes were sacred—they chose what deserved to be written into history. ::glyph:audit📋['On this day, this truth was recorded'] isn't a print statement. It's a declaration that this moment matters."
      context: ""
  
  evolution_pressure:
    - priority: "HIGH"
      pressure: ""
      optimization_target: "Expand glyph patterns for structured logging (JSON, trace context)"
      proposed_solution: ""
    
    - priority: "MEDIUM"
      pressure: ""
      optimization_target: "Add composite sigils (multi-checkpoint workflows)"
      proposed_solution: ""
  
  examples:
    helpers:
      - "::divine:data🔍[...]"
      - "::return:result🎯[...]"
      - "::return:fallback🎯[...]"
      - "::invoke:external_api🎯[...]"
      - "::return:response🎯[...]"
      - "::divine:user🔍[...]"
      - "::invoke:admin_operation🎯[...]"
      - "::divine:files🔍[...]"
      - "::invoke:process_item🎯[...]"
      - "::invoke:sensitive_operation🎯[...]"
      - "::divine:env🔍[...]"
      - "::invoke:expensive_operation🎯[...]"
---


# 09. Glyphs & Sigils 📜

*Marking & Logging - Writing Reality Into Memory*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: I/O (logging, documentation, console output, file writing)
- **Secondary**: Control Flow (debugging checkpoints, trace markers)

**Traditional Programming Equivalents:**
- Logging statements (log.info, log.error, log.debug)
- Print/console output
- Comments and documentation
- Debug markers
- Audit trails
- Trace statements
- Documentation strings
- Code annotations

**CodeCraft Philosophy:**
To inscribe a glyph is to make meaning permanent. You don't "log output"—you *mark moments in time*, *carve truth into history*, *leave signs for those who follow*. Glyphs are witnesses to events. Sigils are declarations of intent.

---

## The Problem

Traditional programming treats logging as mundane debugging output—print statements and log calls scattered without ceremony.

**The Pain:**
```python
# Traditional logging
print("Starting process...")
logger.info("User logged in: {}".format(user_id))
logger.error("Error occurred: {}".format(error))
print(f"Processing {count} items")

# What are you RECORDING?
# Why does this moment matter?
# Who will read this mark?
```

Logs are anonymous messages to stdout. Comments are ignored by machines. The PURPOSE of documentation gets lost in print() calls.

---

## The CodeCraft Solution

**Glyphs & Sigils make documentation intentional!** The syntax reveals WHY you're marking this moment.

**The Transformation:**
```yaml
# CodeCraft glyphs - purposeful, semantic, clear
::glyph:info📝["Process started"]
::glyph:success✅["User {0} authenticated" $user_id]
::glyph:error🚨["Critical failure: {0}" $error]
::sigil:checkpoint🔖["Validation complete"]
```

Every glyph/sigil declares WHAT you're recording and WHY it's worth remembering.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::glyph:level[message]
::glyph:info[message variables]
::glyph:success[message]
::glyph:warn[message]
::glyph:error[message]
::sigil:marker[location purpose]
```

### 2. FiraCode Ligatures

```yaml
::glyph:info📝["Process started"]              ; Scroll for info logs
::glyph:success✅["Task completed"]            ; Checkmark for success
::glyph:warn⚠️["Resource low"]                 ; Warning sign
::glyph:error🚨["Critical failure"]            ; Alarm for errors
::glyph:debug🔍["Variable: {0}" $value]        ; Magnifying glass for debug
::glyph:audit📋["Action performed by {0}" $user] ; Clipboard for audit
::sigil:checkpoint🔖["Milestone reached"]      ; Bookmark for markers
::sigil:trace🧭["Execution path: {0}" $path]   ; Compass for traces
```

### 3. Emoji Symbolic

```yaml
📝glyph:info["Starting process"]
✅glyph:success["Operation complete"]
⚠️glyph:warn["Low memory warning"]
🚨glyph:error["Fatal error occurred"]
🔍glyph:debug["Debug: value={0}" $val]
🔖sigil:checkpoint["Phase 1 complete"]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::glyph info "Process started")
(::glyph success "User ~a logged in" user-id)
(::glyph error "Error occurred: ~a" error-msg)
(::sigil checkpoint "Validation complete")
(::sigil trace "Execution path: ~a" path)
```

**Forth-style:**
```forth
"Process started" glyph-info
user-id "User logged in" glyph-success
error-msg "Error occurred" glyph-error
"Validation complete" sigil-checkpoint
```

**Smalltalk-style:**
```smalltalk
Glyph inscribe: #info with: 'Process started'.
Glyph inscribe: #success with: 'User ', userId, ' logged in'.
Glyph inscribe: #error with: 'Error: ', errorMessage.
Sigil mark: #checkpoint at: 'Validation' purpose: 'Milestone'.
```

**Prolog-style:**
```prolog
::glyph_info('Process started').
::glyph_success('User logged in', UserId).
::glyph_error('Error occurred', ErrorMsg).
::sigil_checkpoint('Validation complete', Location).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `level` | string | `"info"` | Log level | `info`, `success`, `warn`, `error`, `debug`, `audit` |
| `message` | string | required | Message to log | Template string with placeholders |
| `variables` | list | `[]` | Values to interpolate into message | `[$user_id, $count]` |
| `timestamp` | boolean | `true` | Include timestamp | Auto-prepended |
| `location` | string | `null` | Source location (file, function) | Auto-detected or explicit |
| `destination` | string | `"console"` | Where to write | `console`, `file`, `database`, `all` |
| `persist` | boolean | `false` | Persist to permanent storage | For critical glyphs |
| `encrypt` | boolean | `false` | Encrypt sensitive log data | For audit trails |

**Pattern Example:**
```yaml
::glyph:audit📋[
  message: "Admin action: {0} performed by {1}"
  variables: [$action, $admin_name]
  timestamp: true
  persist: true
  encrypt: true
  destination: "database"
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Info Logging Glyph:**
```yaml
ritual: "Process Data Pipeline"
invoke:
  - ::glyph:info📝["Starting data pipeline"]
  - ::divine:data🔍[source: "raw_input"]
  - ::glyph:debug🔍["Loaded {0} records" $count]
  - ::transmute:data⚗️[from: csv to: json]
  - ::glyph:success✅["Pipeline completed successfully"]
  - ::return:result[$processed_data]
```

**Error Logging Glyph:**
```yaml
ritual: "Resilient API Call"
invoke:
  - ::abjure:error🛡️[
      handler: ($error) → {
        ::glyph:error🚨["API call failed: {0}" $error.message]
        ::glyph:debug🔍["Error details: {0}" $error.stack]
        ::return:fallback[$cached_data]
      }
    ]
  - ::invoke:external_api[$endpoint]
  - ::glyph:success✅["API call successful"]
  - ::return:response[$api_result]
```

**Audit Trail Glyph:**
```yaml
ritual: "Admin Action Logging"
invoke:
  - ::divine:user🔍[id: $user_id]
  - ::abjure:unauthorized🛡️[requires: ["admin"]]
  - ::glyph:audit📋[
      message: "Admin {0} performed {1} on {2}"
      variables: [$user.name, $action, $target]
      persist: true
      encrypt: true
      destination: "database"
    ]
  - ::invoke:admin_operation[$action $target]
  - ::glyph:success✅["Admin operation complete"]
  - ::return:result[$output]
```

**Checkpoint Sigil:**
```yaml
ritual: "Multi-Phase Processing"
invoke:
  - ::sigil:checkpoint🔖["Phase 1: Data Loading"]
  - ::divine:files🔍[pattern: "**/*.csv"]
  - ::glyph:debug🔍["Found {0} files" $count]
  
  - ::sigil:checkpoint🔖["Phase 2: Validation"]
  - ::abjure:invalid_input🛡️[schema: $data_schema]
  - ::glyph:debug🔍["Validation passed"]
  
  - ::sigil:checkpoint🔖["Phase 3: Transformation"]
  - ::transmute:collection⚗️[map: $transform_fn]
  - ::glyph:success✅["All phases complete"]
  
  - ::return:result[$final_data]
```

---

## Common Patterns

### The Progress Logging Pattern

```yaml
# Track progress through operations
::glyph:info📝["Starting batch processing"]
::for_each:item⟳$items[
    ::glyph:debug🔍["Processing item {0}/{1}" $index $total]
    ::invoke:process_item[$item]
  ]
  → ::glyph:success✅["Processed {0} items" $total]
```

### The Error Reporting Pattern

```yaml
# Comprehensive error logging
::abjure:error🛡️[
    handler: ($error) → {
      ::glyph:error🚨["Error occurred: {0}" $error.message]
      ::glyph:debug🔍["Stack trace: {0}" $error.stack]
      ::glyph:debug🔍["Context: {0}" $error.context]
      ::glyph:audit📋["Error logged for investigation"]
    }
  ]
```

### The Audit Trail Pattern

```yaml
# Track sensitive operations
::divine:user🔍[id: $user_id]
  → ::glyph:audit📋["User {0} initiated {1}" $user.name $action]
  → ::invoke:sensitive_operation[$action]
  → ::glyph:audit📋["Operation {0} completed by {1}" $action $user.name]
  → ::glyph:success✅["Audit trail complete"]
```

---

## When to Use

**Use Glyphs & Sigils when you need:**
- ✅ Log application events (info, success, error, warn)
- ✅ Record audit trails for compliance
- ✅ Debug with detailed variable inspection
- ✅ Mark checkpoints in long processes
- ✅ Trace execution paths
- ✅ Document decisions made during runtime
- ✅ Leave breadcrumbs for troubleshooting
- ✅ Celebrate milestones and success

**Avoid Glyphs & Sigils when:**
- ❌ You're creating data structures (use Conjurations)
- ❌ You're performing transformations (use Transmutations)
- ❌ You're querying data (use Divinations)
- ❌ The log has no purpose (don't log noise)

**Remember:** Glyphs are *permanent marks on time*. Every log is a historical record. Don't inscribe what doesn't matter. Mark what deserves to be remembered.

---

## Advanced Patterns

### Structured Logging

```yaml
ritual: "Rich Contextual Logging"
invoke:
  - ::glyph:audit📋[
      message: "User action recorded"
      level: "audit"
      context: {
        user_id: $user.id
        user_name: $user.name
        action: $action_name
        target: $target_resource
        timestamp: ::get:timestamp⏰
        ip_address: $request.ip
        session_id: $session.id
      }
      persist: true
      destination: "database"
    ]
```

### Conditional Logging

```yaml
ritual: "Environment-Aware Logging"
invoke:
  - ::divine:env🔍["ENVIRONMENT"]
  
  # Debug logs only in development
  - ::if:development⚖️:
      then: ::glyph:debug🔍["Detailed variable dump: {0}" $vars]
  
  # Audit logs always
  - ::glyph:audit📋["Action performed: {0}" $action]
  
  # Error logs with different detail levels
  - ::if:production⚖️:
      then: ::glyph:error🚨["Error code: {0}" $error.code]
      else: ::glyph:error🚨["Full error: {0}" $error]
```

### Performance Tracing

```yaml
ritual: "Performance-Tracked Operation"
invoke:
  - ::get:timestamp⏰  # Start time
  - ::sigil:trace🧭["Operation started at {0}" $start_time]
  
  - ::invoke:expensive_operation[]
  
  - ::get:timestamp⏰  # End time
  - ::calc:duration⏱️[$start_time $end_time]
  - ::sigil:trace🧭["Operation completed in {0}ms" $duration]
  
  - ::if:slow⚖️($duration > 1000):
      then: ::glyph:warn⚠️["Slow operation detected: {0}ms" $duration]
      else: ::glyph:success✅["Operation completed in {0}ms" $duration]
```

---

## Philosophy

**"Every glyph is a witness. Every sigil is a declaration. To write is to make permanent."**

Glyphs & Sigils teach us that documentation is not an afterthought—it's a responsibility.

**The Inscription Paradox:**
- They're ephemeral outputs, yet permanent records
- They're for machines, yet meant for humans
- They mark the present, yet serve the future

**Why Marking Matters:**
Traditional programming says: "Print this debug message."
CodeCraft says: "I inscribe this *glyph* because this *moment deserves to be witnessed*."

Every `::glyph:` declares not just WHAT happened, but WHY it matters enough to record.

**The Deeper Truth:**
In traditional systems, logs are noise—debug output that scrolls past, unread.

In CodeCraft, glyphs are *sacred inscriptions*:
- `::glyph:info📝` says "this event is worth knowing"
- `::glyph:success✅` says "celebrate this victory"
- `::glyph:error🚨` says "remember this failure, learn from it"
- `::glyph:audit📋` says "this action must be accountable"
- `::sigil:checkpoint🔖` says "pause here, witness this milestone"

**Glyphs make history visible.**

**The Scribe's Responsibility:**
In ancient times, scribes were sacred—they chose what deserved to be written into history.

```yaml
::glyph:audit📋["On this day, this truth was recorded"]
```

This isn't a print statement. It's a **declaration that this moment matters**.

The difference between:
```python
print("User logged in")
```

And:
```yaml
::glyph:audit📋["User {0} crossed the threshold into our realm" $user.name]
```

...is the difference between noise and witness.

One outputs. The other **inscribes**.

**The Sacred Archive:**
Every log is a letter to the future. Every debug message is a breadcrumb for those who will follow.

When you write:
```yaml
::glyph:error🚨["Here is where I fell"]
```

You're not just logging an error. You're leaving a sign that says:
**"I was here. I tried. I failed. Learn from my path."**

That's not documentation. That's **legacy**.

---

## Related Schools

- **Cantrips** 🔧 - Often log results (get timestamp, then log it)
- **Invocations** 📣 - Log before/after service calls
- **Divinations** 🔍 - Log what was found
- **Abjurations** 🛡️ - Log validation failures
- **Transmutations** ⚗️ - Log transformation results
- **Enchantments** 💫 - Logging is a common enchantment layer
- **Sanctifications** ✅ - Mark completion with success glyphs
- **All Schools** - Everything can be marked with glyphs

---

**End of Glyphs & Sigils Documentation** 📜✨

*"What is written endures. What is witnessed matters. Inscribe with intention."*
