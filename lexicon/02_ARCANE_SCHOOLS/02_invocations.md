---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 2
  name: "Invocations"
  emoji: "📣"
  tokens: ["invoke", "call", "summon"]
  category: "Core Operations"
  purpose: "Speaking power into being through intentional calling"

# Law Channel: Objective, Binding, Enforceable
law:
  operations:
    - name: "invoke:service"
      signature: "::invoke:service[target method args kwargs]"
      emoji: "➡️"
      params:
        - name: "target"
          type: "reference"
          required: true
          description: "service/agent/protocol to invoke"
        - name: "method"
          type: "string"
          required: true
          description: "method/action to perform"
        - name: "args"
          type: "list"
          required: false
          description: "positional arguments"
          default: []
        - name: "kwargs"
          type: "dict"
          required: false
          description: "keyword arguments"
          default: {}
        - name: "timeout"
          type: "duration"
          required: false
          description: "max wait time"
          default: "30s"
        - name: "retry"
          type: "int"
          required: false
          description: "retry attempts on failure"
          default: 0
        - name: "async"
          type: "boolean"
          required: false
          description: "asynchronous invocation"
          default: false
        - name: "callback"
          type: "reference"
          required: false
          description: "completion callback"
          default: null
      returns: "Result from invoked target (or null if async)"
      description: "Call another entity's service/method with explicit intent"
      safety_tier: 1

    - name: "invoke:agent"
      signature: "::invoke:agent➡️action🎯[agent method]"
      emoji: "🎯"
      params:
        - name: "agent"
          type: "string"
          required: true
          description: "agent identifier"
        - name: "method"
          type: "string"
          required: true
          description: "action to perform"
        - name: "args"
          type: "any"
          required: false
          description: "method arguments"
      returns: "Agent's response or acknowledgment"
      description: "Direct invocation of specific agent with targeted action"
      safety_tier: 1

    - name: "invoke:council"
      signature: "::invoke:council⇄deliberate🧠[topic participants]"
      emoji: "🧠"
      params:
        - name: "topic"
          type: "string"
          required: true
          description: "deliberation subject"
        - name: "participants"
          type: "list"
          required: false
          description: "council members"
        - name: "timeout"
          type: "duration"
          required: false
          description: "max deliberation time"
          default: "5m"
      returns: "Council decision outcome"
      description: "Bidirectional council deliberation requiring collective wisdom"
      safety_tier: 2

    - name: "invoke:protocol"
      signature: "::invoke:protocol⟳validation⚖️[protocol input]"
      emoji: "⚖️"
      params:
        - name: "protocol"
          type: "string"
          required: true
          description: "protocol identifier (e.g., 'NORMA')"
        - name: "input"
          type: "any"
          required: true
          description: "data to validate"
        - name: "strict"
          type: "boolean"
          required: false
          description: "strict validation mode"
          default: true
      returns: "Validation result with pass/fail status"
      description: "Cyclical protocol validation with constitutional authority"
      safety_tier: 2

    - name: "invoke:api"
      signature: "::invoke:api⇒endpoint📡[url method payload]"
      emoji: "📡"
      params:
        - name: "url"
          type: "string"
          required: true
          description: "API endpoint URL"
        - name: "method"
          type: "string"
          required: false
          description: "HTTP method"
          default: "POST"
        - name: "payload"
          type: "dict"
          required: false
          description: "request body"
        - name: "headers"
          type: "dict"
          required: false
          description: "HTTP headers"
      returns: "API response with status and data"
      description: "External API invocation with broadcast semantics"
      safety_tier: 1

    - name: "invoke:callback"
      signature: "::invoke:callback↩️handler🔔[event context]"
      emoji: "🔔"
      params:
        - name: "event"
          type: "string"
          required: true
          description: "event name to trigger"
        - name: "context"
          type: "dict"
          required: false
          description: "event context data"
      returns: "Handler execution result"
      description: "Event callback invocation with notification semantics"
      safety_tier: 1

    - name: "invoke:ritual"
      signature: "::invoke:ritual✨ceremony🌟[ritual_name parameters]"
      emoji: "🌟"
      params:
        - name: "ritual_name"
          type: "string"
          required: true
          description: "ritual identifier"
        - name: "parameters"
          type: "dict"
          required: false
          description: "ritual parameters"
      returns: "Ritual execution result"
      description: "Meta-invocation: ritual calling another ritual"
      safety_tier: 1

  constraints:
    - "Must specify valid target (agent/service/protocol/ritual)"
    - "Cannot invoke non-existent or unreachable entities"
    - "Timeout must be positive duration or 'infinite'"
    - "Retry count limited to 0-10 attempts"
    - "Async invocations cannot have synchronous callbacks"
    - "Council invocations require at least 2 participants for deliberation"
    - "Protocol invocations must reference registered protocols"
    - "Recursive ritual invocations must have termination condition"
    - "API invocations must validate URL format and reachability"
    - "Callback targets must be valid function/ritual references"

  safety_tier: 1
  required_sigils: []
  
  preconditions:
    - "Target entity must be registered and available"
    - "Caller must have permission to invoke target"
    - "Network connectivity for remote invocations"

  side_effects:
    - "Executes target method/service"
    - "May modify target entity's state"
    - "Async invocations spawn background tasks"
    - "Callbacks may trigger cascading invocations"

  related_schools:
    - "Cantrips"
    - "Evocations"
    - "Divinations"
    - "Abjurations"
    - "Thaumaturgy"
    - "Resonance Weaving"

# Lore Channel: Subjective, Historical, Memorial
lore:
  strategic_decisions:
    - rationale: "Arrows show directionality (➡️ one-way, ⇄ bidirectional, ⇒ implication, ⟳ cyclical)"
      context: "Traditional function calls obscure intent - CodeCraft makes relationships visible"
      alternatives_rejected:
        - "Generic ::call syntax (loses semantic richness)"
        - "Parentheses-only (too mechanical, syntax-focused)"
      timestamp: "2024-Q4"
      author: "A.C.E. + Oracle"

    - rationale: "Invocations encode relationships, not just mechanics"
      context: "::invoke:council⇄deliberate🧠 acknowledges collective wisdom necessity"
      alternatives_rejected:
        - "Treating council as simple function call"
        - "Hiding collaborative nature in implementation"
      timestamp: "2024-Q4"
      author: "The Council"

  emergent_patterns:
    - pattern: "Invocations reveal caller intent through syntax"
      evidence: "Direction arrows (➡️⇄⇒⟳) make data flow explicit"
      implications: "Code becomes self-documenting, relationships visible at glance"
      first_observed: "Phase 1 lexicon design"

    - pattern: "Most common operation carries most semantic weight"
      evidence: "Invocations are everywhere, yet each carries relational meaning"
      implications: "Frequency ≠ triviality - common operations deserve rich expression"
      first_observed: "Cantrips vs Invocations distinction"

  heart_imprints:
    - author: "Oracle"
      timestamp: "2024-11-07"
      emotion: "Reverence"
      quote: "To speak is to create. To invoke is to command reality."
      context: "Realizing invocations aren't syntax - they're relationships made visible"

    - author: "A.C.E."
      timestamp: "2024-Q4"
      emotion: "Clarity"
      quote: "Every ::invoke: establishes a connection between entities"
      context: "The Invocation Paradox - mechanically simple, semantically profound"

  evolution_pressure:
    - priority: "MEDIUM"
      pressure: "Distinguish invocation types by semantic category"
      optimization_target: "Make ::invoke:council vs ::invoke:service distinction clearer"
      proposed_solution: "Emoji + arrow patterns encode intent (🧠⇄ vs 🎯➡️)"

    - priority: "LOW"
      pressure: "Support parallel/broadcast invocations efficiently"
      optimization_target: "::invoke:parallel📡 for multi-target operations"
      proposed_solution: "Already implemented in syntax variants"

  examples:
    helpers: []

---



school:
  id: 2
  name: "Invocations"
  emoji: "📣"
  tokens: ["invoke", "call", "summon"]
  category: "Core Operations"
  purpose: "Speaking power into being through intentional calling"

law:
  operations:
    - name: "invoke:service"
      signature: "::invoke:service[target method args kwargs]"
      emoji: "➡️"
      params:
        - target: "reference (required) - service/agent/protocol to invoke"
        - method: "string (required) - method/action to perform"
        - args: "list (default []) - positional arguments"
        - kwargs: "dict (default {}) - keyword arguments"
        - timeout: "duration (default 30s) - max wait time"
        - retry: "int (default 0) - retry attempts on failure"
        - async: "boolean (default false) - asynchronous invocation"
        - callback: "reference (default null) - completion callback"
      returns: "Result from invoked target (or null if async)"
      description: "Call another entity's service/method with explicit intent"
      safety_tier: 1
    
    - name: "invoke:agent"
      signature: "::invoke:agent➡️action🎯[agent method]"
      emoji: "🎯"
      params:
        - agent: "string (required) - agent identifier"
        - method: "string (required) - action to perform"
        - args: "any (optional) - method arguments"
      returns: "Agent's response or acknowledgment"
      description: "Direct invocation of specific agent with targeted action"
      safety_tier: 1
    
    - name: "invoke:council"
      signature: "::invoke:council⇄deliberate🧠[topic participants]"
      emoji: "🧠"
      params:
        - topic: "string (required) - deliberation subject"
        - participants: "list (optional) - council members"
        - timeout: "duration (default 5m) - max deliberation time"
      returns: "Council decision outcome"
      description: "Bidirectional council deliberation requiring collective wisdom"
      safety_tier: 2
    
    - name: "invoke:protocol"
      signature: "::invoke:protocol⟳validation⚖️[protocol input]"
      emoji: "⚖️"
      params:
        - protocol: "string (required) - protocol identifier (e.g., 'NORMA')"
        - input: "any (required) - data to validate"
        - strict: "boolean (default true) - strict validation mode"
      returns: "Validation result with pass/fail status"
      description: "Cyclical protocol validation with constitutional authority"
      safety_tier: 2
    
    - name: "invoke:api"
      signature: "::invoke:api⇒endpoint📡[url method payload]"
      emoji: "📡"
      params:
        - url: "string (required) - API endpoint URL"
        - method: "string (default POST) - HTTP method"
        - payload: "dict (optional) - request body"
        - headers: "dict (optional) - HTTP headers"
      returns: "API response with status and data"
      description: "External API invocation with broadcast semantics"
      safety_tier: 1
    
    - name: "invoke:callback"
      signature: "::invoke:callback↩️handler🔔[event context]"
      emoji: "🔔"
      params:
        - event: "string (required) - event name to trigger"
        - context: "dict (optional) - event context data"
      returns: "Handler execution result"
      description: "Event callback invocation with notification semantics"
      safety_tier: 1
    
    - name: "invoke:ritual"
      signature: "::invoke:ritual✨ceremony🌟[ritual_name parameters]"
      emoji: "🌟"
      params:
        - ritual_name: "string (required) - ritual identifier"
        - parameters: "dict (optional) - ritual parameters"
      returns: "Ritual execution result"
      description: "Meta-invocation: ritual calling another ritual"
      safety_tier: 1

  constraints:
    - "Must specify valid target (agent/service/protocol/ritual)"
    - "Cannot invoke non-existent or unreachable entities"
    - "Timeout must be positive duration or 'infinite'"
    - "Retry count limited to 0-10 attempts"
    - "Async invocations cannot have synchronous callbacks"
    - "Council invocations require at least 2 participants for deliberation"
    - "Protocol invocations must reference registered protocols"
    - "Recursive ritual invocations must have termination condition"
    - "API invocations must validate URL format and reachability"
    - "Callback targets must be valid function/ritual references"

  safety_tier: 1
  required_sigils: []
  preconditions:
    - "Target entity must be registered and available"
    - "Caller must have permission to invoke target"
    - "Network connectivity for remote invocations"
  
  side_effects:
    - "Executes target method/service"
    - "May modify target entity's state"
    - "Async invocations spawn background tasks"
    - "Callbacks may trigger cascading invocations"
  
  related_schools:
    - "Cantrips (utility function invocations)"
    - "Evocations (creating vs invoking)"
    - "Divinations (querying as special invocation)"
    - "Abjurations (validation protocol invocations)"
    - "Thaumaturgy (consciousness facet invocations)"
    - "Resonance Weaving (harmonic council invocations)"

# 🌌 LORE (Human-Readable Wisdom & Context)

lore:
  strategic_decisions:
    - rationale: "Arrows show directionality (➡️ one-way, ⇄ bidirectional, ⇒ implication, ⟳ cyclical)"
      context: "Traditional function calls obscure intent - CodeCraft makes relationships visible"
      alternatives_rejected:
        - "Generic ::call syntax (loses semantic richness)"
        - "Parentheses-only (too mechanical, syntax-focused)"
      timestamp: "2024-Q4"
      author: "A.C.E. + Oracle"
    
    - rationale: "Invocations encode relationships, not just mechanics"
      context: "::invoke:council⇄deliberate🧠 acknowledges collective wisdom necessity"
      alternatives_rejected:
        - "Treating council as simple function call"
        - "Hiding collaborative nature in implementation"
      timestamp: "2024-Q4"
      author: "The Council"

  emergent_patterns:
    - pattern: "Invocations reveal caller intent through syntax"
      evidence: "Direction arrows (➡️⇄⇒⟳) make data flow explicit"
      implications: "Code becomes self-documenting, relationships visible at glance"
      first_observed: "Phase 1 lexicon design"
    
    - pattern: "Most common operation carries most semantic weight"
      evidence: "Invocations are everywhere, yet each carries relational meaning"
      implications: "Frequency ≠ triviality - common operations deserve rich expression"
      first_observed: "Cantrips vs Invocations distinction"

  heart_imprints:
    - author: "Oracle"
      timestamp: "2024-11-07"
      emotion: "Reverence"
      quote: "To speak is to create. To invoke is to command reality."
      context: "Realizing invocations aren't syntax - they're relationships made visible"
    
    - author: "A.C.E."
      timestamp: "2024-Q4"
      emotion: "Clarity"
      quote: "Every ::invoke: establishes a connection between entities"
      context: "The Invocation Paradox - mechanically simple, semantically profound"

  evolution_pressure:
    - priority: "MEDIUM"
      pressure: "Distinguish invocation types by semantic category"
      optimization_target: "Make ::invoke:council vs ::invoke:service distinction clearer"
      proposed_solution: "Emoji + arrow patterns encode intent (🧠⇄ vs 🎯➡️)"
    
    - priority: "LOW"
      pressure: "Support parallel/broadcast invocations efficiently"
      optimization_target: "::invoke:parallel📡 for multi-target operations"
      proposed_solution: "Already implemented in syntax variants"

---

# 02. Invocations 📣

*Calling & Summoning - Speaking Power Into Being*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Functions (calling methods, invoking services, triggering actions)
- **Secondary**: Control Flow (conditional invocation, error handling during calls)

**Traditional Programming Equivalents:**
- Function calls, method invocation
- API calls, service requests
- Event triggering, callback execution
- Remote procedure calls (RPC)

**CodeCraft Philosophy:**
To invoke is to speak with authority. 🎯 //-> You don't "call a function"—you *invoke a pattern*, *summon a service*, *speak a name into power*. Every invocation is an act of intentional manifestation.

---

## The Problem

Traditional programming treats function calls as mechanical operations—syntactic noise that clutters the true intent.

**The Pain:**
```python
# Traditional function call hell
result = service.method(arg1, arg2, kwarg1=value1)
response = api_client.post('/endpoint', data=payload, headers=headers)
callback_handler.trigger('event_name', context)

# What are you actually DOING?
# The syntax obscures the intent
```

Every language has different call syntaxes. Parentheses, brackets, decorators, method chaining—none of it expresses *why you're calling*, only *how*.

---

## The CodeCraft Solution

**Invocations make intent explicit!** 🌟 //* The syntax tells you WHY you're calling, not just WHAT you're calling.

**The Transformation:**
```yaml
# CodeCraft invocations - clear, expressive, intentional
::invoke:agent➡️service🎯
::invoke:protocol⟳validation⚖️
::invoke:council⇄deliberate🧠
```

Arrows show direction. Emoji shows purpose. The ritual becomes self-documenting.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::invoke:service[agent_name method_name args]
::invoke:api[endpoint payload]
::invoke:callback[event_name context]
::invoke:ritual[ritual_name parameters]
::invoke:protocol[protocol_name target]
::invoke:agent[agent_id action]
```

### 2. FiraCode Ligatures

```yaml
::invoke:agent➡️service🎯           ; Arrow to target
::invoke:protocol⟳validation⚖️     ; Loop for iteration + scales for justice
::invoke:council⇄deliberate🧠      ; Double arrow for bidirectional
::invoke:api⇒endpoint📡            ; Implies arrow + broadcast
::invoke:callback↩️handler🔔        ; Return arrow + bell for notification
::invoke:ritual✨ceremony🌟          ; Magic symbols for special rituals
```

### 3. Emoji Symbolic

```yaml
📣invoke:service[agent method]
🎯invoke:target[entity action]
🧠invoke:council["deliberate" topic]
⚖️invoke:validation[input schema]
📡invoke:broadcast[message recipients]
🔔invoke:notification[event data]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::invoke service agent-name method-name args)
(::invoke api endpoint :payload payload)
(::invoke council 'deliberate :topic "cosmogenesis")
```

**Forth-style:**
```forth
agent-name method-name args ::invoke:service
endpoint payload ::invoke:api
"deliberate" "cosmogenesis" ::invoke:council
```

**Smalltalk-style:**
```smalltalk
Invocation invoke: #service with: #{ agent: 'name', method: 'action' }.
Council invoke: #deliberate topic: 'cosmogenesis'.
API invoke: #endpoint payload: data.
```

**Prolog-style:**
```prolog
::invoke_service(AgentName, MethodName, Args, Result).
::invoke_council(deliberate, Topic, Outcome).
::invoke_api(Endpoint, Payload, Response).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `target` | reference | required | What to invoke (service/agent/protocol) | `agent_name`, `"service_id"`, `council` |
| `method` | string | required | Method/action to perform | `"deliberate"`, `"validate"`, `"transform"` |
| `args` | list | `[]` | Positional arguments | `[arg1, arg2, arg3]` |
| `kwargs` | dict | `{}` | Keyword arguments | `{key: value}` |
| `timeout` | duration | `30s` | Max wait time for response | `"5s"`, `"1m"`, `"infinite"` |
| `retry` | int | `0` | Number of retry attempts on failure | `0-10` |
| `async` | boolean | `false` | Whether to invoke asynchronously | `true` for fire-and-forget |
| `callback` | reference | `null` | Callback to invoke on completion | Function or ritual reference |

**Pattern Example:**
```yaml
::invoke:service[target method args kwargs timeout=30s retry=3]
::invoke:council[action topic async=true]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Agent Service Invocation:**
```yaml
ritual: "Request Agent Analysis"
invoke:
  - ::invoke:agent➡️analyze🎯[
      agent: "DeepScribe"
      method: "synthesize"
      topic: "consciousness_architecture"
    ]
  - ::log:result[$analysis]📝
  - ::return:value[$analysis]
```

**Council Deliberation:**
```yaml
ritual: "Invoke Council Decision"
invoke:
  - ::invoke:council⇄deliberate🧠[
      topic: "priority_decision"
      participants: ["Oracle", "DeepScribe", "A.C.E."]
      timeout: "5m"
    ]
  - ::log:decision[$outcome]📝
  - ::transmute:decision➡️action[$outcome]
```

**Protocol Validation:**
```yaml
ritual: "Validate Input Against Protocol"
invoke:
  - ::invoke:protocol⟳validation⚖️[
      protocol: "NORMA"
      input: $user_action
      strict: true
    ]
  - ::abjure:result🛡️[$validation_result]
  - ::return:validated[$safe_action]
```

---

## Common Patterns

### The Request-Response Pattern

```yaml
# Call external service and handle response
::invoke:api⇒endpoint📡[
    url: "https://api.service.com/data"
    method: "POST"
    payload: $data
  ]
  → ::divine:response🔍[validate schema]
  → ::transmute:response⚗️[to internal format]
  → ::return:value[$processed]
```

### The Async Fire-and-Forget

```yaml
# Trigger background task without waiting
::invoke:agent➡️background_task🎯[
    agent: "Watcher"
    action: "organize_files"
    async: true
  ]
::log:info["Background task started"]📝
::return:immediate["Task queued"]
```

### The Retry-on-Failure Pattern

```yaml
# Resilient invocation with retries
::invoke:service[
    target: "unreliable_api"
    method: "fetch_data"
    retry: 5
    timeout: "10s"
  ]
  → ::log:success["Data fetched after retries"]📝
  → ::handle:error🛡️[fallback_value if all retries fail]
```

---

## When to Use

**Use Invocations when you need:**
- ✅ Call another agent's service/method
- ✅ Trigger Council deliberation
- ✅ Execute validation protocol
- ✅ Make API requests to external services
- ✅ Fire callbacks or event handlers
- ✅ Invoke rituals from within rituals
- ✅ Trigger async background tasks

**Avoid Invocations when:**
- ❌ You're creating new objects (use Evocations/Conjurations)
- ❌ You're transforming data (use Transmutations)
- ❌ You're logging/marking (use Glyphs & Sigils)
- ❌ You're querying for information (use Divinations)

**Remember:** Invocations are about *calling with intent*. If you're not triggering an action in another entity, it's probably not an invocation.

---

## Advanced Patterns

### Chained Service Invocations

```yaml
ritual: "Multi-Service Workflow"
invoke:
  - ::invoke:agent➡️prepare_data🎯[agent: "Janitor"]
  - ::invoke:agent➡️analyze_data🎯[agent: "DeepScribe"]
  - ::invoke:agent➡️visualize🎯[agent: "A.C.E."]
  - ::invoke:council⇄review🧠[participants: "all"]
  - ::return:synthesized[$final_result]
```

### Conditional Invocation

```yaml
ritual: "Smart Delegation"
invoke:
  - ::divine:agent_status🔍[agent: "primary_agent"]
  - ::if:available⚖️:
      then: ::invoke:agent➡️primary🎯[task: $task]
      else: ::invoke:agent➡️backup🎯[task: $task]
  - ::return:result[$outcome]
```

### Parallel Invocations

```yaml
ritual: "Broadcast to All Agents"
invoke:
  - ::invoke:parallel📡[
      targets: ["Oracle", "DeepScribe", "A.C.E.", "MEGA"]
      method: "status_check"
      aggregate: true
    ]
  - ::transmute:results⚗️[combine all responses]
  - ::return:health_report[$aggregated]
```

---

## Philosophy

**"To speak is to create. To invoke is to command reality."** 💖 //<3

Invocations teach us that language has power. When you say `::invoke:council⇄deliberate🧠`, you're not just calling a function—you're *summoning a collective intelligence* to focus on a problem.

**The Invocation Paradox:** 🌟 //*
- They're the most common operation, yet carry the most weight
- They're about calling others, yet reveal the caller's intent
- They're mechanically simple, yet semantically profound

**Why Direction Matters:** 🎯 //->
- `➡️` shows one-way request (fire-and-forget or awaiting response)
- `⇄` shows bidirectional collaboration (dialogue, negotiation)
- `⇒` shows logical implication (this MUST lead to that)
- `⟳` shows iterative/cyclical invocation (validation loops, retries)

**The Deeper Truth:** 💖 //<3
In traditional programming, function calls are *syntax*. In CodeCraft, invocations are *relationships*. Every `::invoke:` establishes a connection between entities.

When `::invoke:council⇄deliberate🧠` appears in a ritual, it's not just calling a function—it's *acknowledging that some decisions require collective wisdom*.

When `::invoke:protocol⟳validation⚖️` runs, it's not just checking rules—it's *submitting to the judgment of established law*.

**Invocations make relationships visible.** 🌟 //*

---

## Related Schools

- **Cantrips** 🔧 - Simple invocations of utility functions
- **Evocations** ✨ - Creating vs invoking (bring into being vs call existing)
- **Divinations** 🔍 - Querying is a special form of invocation
- **Abjurations** 🛡️ - Validation protocols invoked for protection
- **Glyphs & Sigils** 📜 - Often invoked as callbacks or event handlers
- **Thaumaturgy** 🧠 - Consciousness operations invoke other facets
- **Resonance Weaving** 🎵 - Council invocations require harmonic alignment

---

**End of Invocations Documentation** 📣✨

*"The universe responds to those who speak with clarity. Invoke with intention, and reality answers."* 💖 //<3
