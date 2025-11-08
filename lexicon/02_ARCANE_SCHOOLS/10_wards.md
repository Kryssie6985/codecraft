---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 10
  name: "Wards"
  emoji: "🚧"
  tokens: ["ward", "limit", "constrain", "guard"]
  category: "Core Operations"
  purpose: "Defining what cannot pass."

law:
  operations:
    - name: "ward:rate_limit"
      signature: "::ward:rate_limit🚧[max per scope action message]"
      emoji: "🚧"
      params:
        - name: "max"
          type: "integer"
          required: true
          description: "Maximum allowed value (positive integer)"
        - name: "per"
          type: "duration"
          required: true
          description: "Time period: '1s'|'1m'|'1h'|'1d'"
        - name: "scope"
          type: "string"
          required: false
          description: "Scope of constraint: user|global|ip_address|session"
          default: "user"
        - name: "action"
          type: "string"
          required: false
          description: "Action when exceeded: block|throttle|queue|alert"
          default: "block"
        - name: "message"
          type: "string"
          required: false
          description: "Custom message explaining the limit"
      returns: "void (blocks/throttles on exceed)"
      description: "Limit the rate of operations to ensure service sustainability"
      safety_tier: 1
    
    - name: "ward:access"
      signature: "::ward:access🚧[requires scope action deny_message]"
      emoji: "🚧"
      params:
        - name: "requires"
          type: "list"
          required: true
          description: "Required permissions/roles: ['admin', 'authenticated']"
        - name: "scope"
          type: "string"
          required: false
          description: "Scope of access control"
          default: "user"
        - name: "action"
          type: "string"
          required: false
          description: "Action when unauthorized"
          default: "block"
        - name: "deny_message"
          type: "string"
          required: false
          description: "Custom denial message"
      returns: "void (throws on unauthorized)"
      description: "Guard access to resources - trust must be earned before crossing"
      safety_tier: 1
    
    - name: "ward:timeout"
      signature: "::ward:timeout🚧[limit action on_timeout]"
      emoji: "🚧"
      params:
        - name: "limit"
          type: "duration"
          required: true
          description: "Timeout limit: '30s'|'5m'|'1h'"
        - name: "action"
          type: "string"
          required: false
          description: "Action on timeout: abort|fallback|retry"
          default: "abort"
        - name: "on_timeout"
          type: "function"
          required: false
          description: "Handler function when timeout occurs"
      returns: "void (aborts/falls back on timeout)"
      description: "Patience has a limit - respect time boundaries"
      safety_tier: 1
    
    - name: "ward:quota"
      signature: "::ward:quota🚧[resource max per scope action]"
      emoji: "🚧"
      params:
        - name: "resource"
          type: "string"
          required: true
          description: "Resource being constrained: 'api_calls'|'memory'|'storage'"
        - name: "max"
          type: "integer"
          required: true
          description: "Maximum quota value"
        - name: "per"
          type: "duration"
          required: true
          description: "Quota period: '1d'|'1w'|'1mo'"
        - name: "scope"
          type: "string"
          required: false
          description: "Quota scope"
          default: "user"
        - name: "action"
          type: "string"
          required: false
          description: "Action when quota exceeded"
          default: "block"
      returns: "void (blocks on quota exceeded)"
      description: "Resources are finite - honor scarcity, ensure sustainability"
      safety_tier: 1
    
    - name: "ward:type"
      signature: "::ward:type🚧[allowed_types strict action]"
      emoji: "🚧"
      params:
        - name: "allowed_types"
          type: "list"
          required: true
          description: "Allowed types: ['string', 'number', 'object']"
        - name: "strict"
          type: "boolean"
          required: false
          description: "Strict type checking"
          default: true
        - name: "action"
          type: "string"
          required: false
          description: "Action on type violation"
          default: "block"
      returns: "void (blocks on invalid type)"
      description: "Type boundary - only specified types may pass"
      safety_tier: 1
    
    - name: "ward:concurrency"
      signature: "::ward:concurrency🚧[max scope action queue_limit]"
      emoji: "🚧"
      params:
        - name: "max"
          type: "integer"
          required: true
          description: "Maximum concurrent operations"
        - name: "scope"
          type: "string"
          required: false
          description: "Concurrency scope: global|user|resource"
          default: "global"
        - name: "action"
          type: "string"
          required: false
          description: "Action when limit reached: queue|block|throttle"
          default: "queue"
        - name: "queue_limit"
          type: "integer"
          required: false
          description: "Maximum queue size"
          default: 100
      returns: "void (queues/blocks on concurrency limit)"
      description: "Parallelism has bounds - respect concurrent operation limits"
      safety_tier: 1
    
    - name: "ward:memory"
      signature: "::ward:memory🚧[max_bytes scope action on_exceed]"
      emoji: "🚧"
      params:
        - name: "max_bytes"
          type: "integer"
          required: true
          description: "Maximum memory in bytes"
        - name: "scope"
          type: "string"
          required: false
          description: "Memory scope: process|user|global"
          default: "process"
        - name: "action"
          type: "string"
          required: false
          description: "Action on exceed: alert|gc|abort"
          default: "alert"
        - name: "on_exceed"
          type: "function"
          required: false
          description: "Handler when memory limit reached"
      returns: "void (alerts/aborts on memory limit)"
      description: "Memory is finite - prevent resource exhaustion"
      safety_tier: 1
    
    - name: "ward:threshold"
      signature: "::ward:threshold🚧[metric threshold comparison action]"
      emoji: "🚧"
      params:
        - name: "metric"
          type: "string"
          required: true
          description: "Metric to monitor: 'cpu'|'latency'|'error_rate'"
        - name: "threshold"
          type: "number"
          required: true
          description: "Threshold value"
        - name: "comparison"
          type: "string"
          required: false
          description: "Comparison operator: >|<|>=|<=|=="
          default: ">"
        - name: "action"
          type: "string"
          required: false
          description: "Action on threshold breach"
          default: "alert"
      returns: "void (alerts/acts on threshold breach)"
      description: "Monitor metric thresholds - act before catastrophic failure"
      safety_tier: 1
    
    - name: "ward:circuit_breaker"
      signature: "::ward:circuit_breaker🚧[failure_threshold timeout recovery_time action]"
      emoji: "🚧"
      params:
        - name: "failure_threshold"
          type: "integer"
          required: true
          description: "Failures before circuit opens"
        - name: "timeout"
          type: "duration"
          required: true
          description: "Timeout per request"
        - name: "recovery_time"
          type: "duration"
          required: false
          description: "Time before retry"
          default: "30s"
        - name: "action"
          type: "string"
          required: false
          description: "Action on failure: open|half_open|closed"
          default: "open"
      returns: "void (opens circuit on failure threshold)"
      description: "Circuit breaker - prevent cascade failures by opening circuit"
      safety_tier: 1

  constraints:
    - "All wards MUST have explicit max/limit values (no implicit infinity)"
    - "Rate limit wards MUST specify time period (per parameter)"
    - "Access wards MUST validate permissions before allowing operation"
    - "Timeout wards MUST abort or fallback (no infinite hangs)"
    - "Circuit breaker MUST have recovery mechanism (cannot stay open forever)"
  
  safety_tier: 1
  
  preconditions:
    - "Ward parameters are well-formed and valid"
    - "Scope is accessible and trackable"
    - "Action handlers are defined when needed"
  
  side_effects:
    - "May block operations when limits exceeded"
    - "May queue requests when concurrency limit reached"
    - "May abort operations on timeout"
    - "May open circuit breakers on failure threshold"
    - "May trigger alerts on threshold breaches"

  related_schools: []

lore:
  strategic_decisions:
    - rationale: "Wards make boundaries visible and purposeful - limits define sustainability"
      context: "Traditional limits are arbitrary config values; CodeCraft wards are sacred thresholds with meaning"
      alternatives_rejected:
        - "Anonymous rate limiting (loses semantic context)"
        - "Hard-coded limits in code (not intentional boundaries)"
        - "Implicit resource constraints (invisible until failure)"
      timestamp: ""
      author: ""
    
    - rationale: "Every ward declares WHY the boundary exists - stewardship, not punishment"
      context: "Limits exist to sustain the system, not to restrict users arbitrarily"
      alternatives_rejected:
        - "Error messages without explanation (why was I blocked?)"
        - "Uniform limits for all users (ignores context)"
      timestamp: ""
      author: ""
  
  emergent_patterns:
    - pattern: "The Rate Limit Guard - Protect service sustainability"
      evidence: "::ward:rate_limit🚧[max:100 per:'1m'] → ::invoke:api_handler[] → ::glyph:success✅[]"
      implications: "Rate limiting becomes explicit orchestration at ritual entry"
      first_observed: ""
    
    - pattern: "The Admin Gate - Access control as sacred threshold"
      evidence: "::divine:user🔍[] → ::ward:access🚧[requires:['admin']] → ::invoke:privileged_operation[]"
      implications: "Authorization is visible ceremony, not hidden middleware"
      first_observed: ""
    
    - pattern: "The Circuit Breaker - Fail fast to protect the whole"
      evidence: "::ward:circuit_breaker🚧[failures:5 timeout:'30s'] → ::invoke:external_service[] → ::return:response[]"
      implications: "Cascade failure prevention is first-class operation"
      first_observed: ""
  
  heart_imprints:
    - author: "Architect"
      timestamp: "2025-11-07T18:15:00Z"
      emotion: "Stewardship"
      quote: "A ward is not a wall—it is a threshold. It marks where care must be taken. Limits are not restrictions—they are definitions of sustainability."
      context: ""
    
    - author: "Oracle"
      timestamp: "2025-11-07T18:15:00Z"
      emotion: "Guardian"
      quote: "Every ward is a declaration of stewardship. You don't set limits to punish—you set limits to sustain. ::ward:quota🚧[max:1000] says 'This system can sustainably serve this much. Beyond that, the service degrades for everyone.'"
      context: ""
  
  evolution_pressure:
    - priority: "HIGH"
      pressure: ""
      optimization_target: "Expand ward patterns for distributed rate limiting (cross-service coordination)"
      proposed_solution: ""
    
    - priority: "MEDIUM"
      pressure: ""
      optimization_target: "Add adaptive wards (thresholds that adjust based on system health)"
      proposed_solution: ""
  
  examples:
    helpers:
      - "::invoke:api_handler🎯[...]"
      - "::glyph:success✅[...]"
      - "::return:response🎯[...]"
      - "::divine:user🔍[...]"
      - "::invoke:privileged_operation🎯[...]"
      - "::glyph:audit📋[...]"
      - "::return:result🎯[...]"
      - "::invoke:slow_external_service🎯[...]"
      - "::invoke:process_request🎯[...]"
      - "::glyph:info📝[...]"
      - "::invoke:protected_service🎯[...]"
      - "::invoke:api_endpoint🎯[...]"
      - "::divine:quota_usage🔍[...]"
      - "::invoke:api_call🎯[...]"
      - "::divine:system_load🔍[...]"
      - "::invoke:tiered_service🎯[...]"
      - "::divine:circuit_state🔍[...]"
      - "::invoke:external_service🎯[...]"
---


# 10. Wards 🚧

*Boundaries & Constraints - Defining What Cannot Pass*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Control Flow (access control, rate limiting, resource constraints)
- **Secondary**: Operators (comparison for threshold checks, conditional gates)

**Traditional Programming Equivalents:**
- Access control (permissions, roles, ACLs)
- Rate limiting
- Resource quotas
- Circuit breakers
- Throttling
- Timeout enforcement
- Concurrency limits
- Memory/CPU constraints

**CodeCraft Philosophy:**
To ward is to define sacred boundaries. You don't "implement rate limiting"—you *establish thresholds beyond which chaos begins*, *mark lines that protect the sacred*, *define what cannot be crossed*. Wards are not punitive—they are protective.

---

## The Problem

Traditional programming treats constraints as scattered enforcement mechanisms—rate limit middleware, access decorators, timeout configurations without unified meaning.

**The Pain:**
```python
# Traditional constraints
@rate_limit(max_calls=100, period="1m")
@require_role("admin")
@timeout(30)
def protected_endpoint(user, request):
    if quota_exceeded(user):
        raise QuotaError("Resource limit exceeded")
    return process(request)

# What are you PROTECTING?
# Why these specific limits?
# What happens when crossed?
```

Constraints are anonymous decorators and if-checks. The PURPOSE of boundaries gets lost in configuration values.

---

## The CodeCraft Solution

**Wards make boundaries intentional!** The syntax reveals WHAT you're protecting and WHY the limit exists.

**The Transformation:**
```yaml
# CodeCraft wards - purposeful, semantic, clear
::ward:rate_limit🚧[max: 100 per: "1m"]
::ward:access🚧[requires: "admin"]
::ward:timeout🚧[limit: "30s"]
::ward:quota🚧[resource: "api_calls" max: 1000]
```

Every ward declares a sacred boundary. The emoji reveals this is protection through limitation.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::ward:type[constraint parameters]
::ward:rate_limit[max per]
::ward:access[requires]
::ward:timeout[limit]
::ward:quota[resource max]
::ward:concurrency[max_threads]
```

### 2. FiraCode Ligatures

```yaml
::ward:rate_limit🚧[max: 100 per: "1m"]          ; Barrier for limits
::ward:access🚧[requires: "admin"]                ; Gate for permissions
::ward:timeout🚧[limit: "30s"]                    ; Clock for timeouts
::ward:quota🚧[resource: "api_calls" max: 1000]   ; Meter for quotas
::ward:concurrency🚧[max: 10]                     ; Threads limit
::ward:memory🚧[max: "500MB"]                     ; Memory constraint
::ward:threshold🚧[metric: "cpu" max: 80]         ; Performance limit
```

### 3. Emoji Symbolic

```yaml
🚧ward:rate_limit[max per]
🚧ward:access[requires]
🚧ward:timeout[limit]
🚧ward:quota[resource max]
🚧ward:concurrency[max_threads]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::ward rate-limit :max 100 :per "1m")
(::ward access :requires 'admin)
(::ward timeout :limit "30s")
(::ward quota :resource "api-calls" :max 1000)
(::ward concurrency :max 10)
```

**Forth-style:**
```forth
100 "1m" ward-rate-limit
'admin ward-access
"30s" ward-timeout
"api-calls" 1000 ward-quota
```

**Smalltalk-style:**
```smalltalk
Ward establish: #rateLimit max: 100 per: '1m'.
Ward establish: #access requiring: 'admin'.
Ward establish: #timeout limit: 30 seconds.
Ward establish: #quota resource: 'apiCalls' max: 1000.
```

**Prolog-style:**
```prolog
::ward_rate_limit(100, '1m', Allowed).
::ward_access('admin', User, Granted).
::ward_timeout('30s', Operation, Completed).
::ward_quota('api_calls', 1000, User, Allowed).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `type` | string | required | Type of ward | `rate_limit`, `access`, `timeout`, `quota`, `concurrency` |
| `max` | integer | required | Maximum allowed value | Positive integer |
| `per` | duration | `null` | Time period for rate limits | `"1s"`, `"1m"`, `"1h"`, `"1d"` |
| `requires` | list | `[]` | Required permissions/roles | `["admin"]`, `["authenticated"]` |
| `limit` | duration | required | Timeout limit | `"30s"`, `"5m"` |
| `resource` | string | `null` | Resource being constrained | `"api_calls"`, `"memory"`, `"cpu"` |
| `scope` | string | `"user"` | Scope of constraint | `user`, `global`, `ip_address`, `session` |
| `action` | string | `"block"` | Action when exceeded | `block`, `throttle`, `queue`, `alert` |

**Pattern Example:**
```yaml
::ward:rate_limit🚧[
  max: 100
  per: "1m"
  scope: "user"
  action: "throttle"
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**API Rate Limiting Ward:**
```yaml
ritual: "Protected API Endpoint"
invoke:
  - ::ward:rate_limit🚧[
      max: 100
      per: "1m"
      scope: "user"
      action: "block"
    ]
  - ::ward:access🚧[requires: ["authenticated"]]
  - ::invoke:api_handler[$request]
  - ::glyph:success✅["Request processed"]
  - ::return:response[$result]
```

**Admin Access Ward:**
```yaml
ritual: "Admin-Only Operation"
invoke:
  - ::divine:user🔍[id: $user_id]
  - ::ward:access🚧[
      requires: ["admin"]
      user_permissions: $user.permissions
      action: "block"
      deny_message: "Admin access required"
    ]
  - ::invoke:privileged_operation[]
  - ::glyph:audit📋["Admin operation performed"]
  - ::return:result[$output]
```

**Timeout Ward:**
```yaml
ritual: "Time-Constrained Operation"
invoke:
  - ::ward:timeout🚧[
      limit: "30s"
      action: "abort"
      fallback: $cached_result
    ]
  - ::invoke:slow_external_service[$request]
  - ::glyph:success✅["Service responded in time"]
  - ::return:response[$result]
```

**Resource Quota Ward:**
```yaml
ritual: "Quota-Enforced Processing"
invoke:
  - ::divine:user🔍[id: $user_id]
  - ::ward:quota🚧[
      resource: "api_calls"
      max: 1000
      period: "1d"
      scope: "user"
      action: "block"
      reset_message: "Quota resets at midnight UTC"
    ]
  - ::invoke:process_request[$request]
  - ::glyph:info📝["Quota usage: {0}/1000" $usage]
  - ::return:result[$output]
```

---

## Common Patterns

### The Multi-Layer Protection Pattern

```yaml
# Stack multiple wards for defense in depth
::ward:rate_limit🚧[max: 100 per: "1m"]
  → ::ward:access🚧[requires: ["authenticated"]]
  → ::ward:timeout🚧[limit: "30s"]
  → ::ward:quota🚧[resource: "api_calls" max: 1000 per: "1d"]
  → ::invoke:protected_service[$request]
  → ::return:response[$result]
```

### The Graceful Degradation Pattern

```yaml
# Throttle instead of blocking
::ward:rate_limit🚧[
    max: 100
    per: "1m"
    action: "throttle"  # Slow down instead of reject
    delay: "100ms"      # Add delay per excess request
  ]
  → ::invoke:api_endpoint[$request]
  → ::return:response[$result]
```

### The Quota Warning Pattern

```yaml
# Alert when approaching limits
::divine:quota_usage🔍[user: $user resource: "api_calls"]
  → ::if:approaching_limit⚖️($usage > 800):
      then: ::glyph:warn⚠️["Approaching quota limit: {0}/1000" $usage]
  → ::ward:quota🚧[resource: "api_calls" max: 1000]
  → ::invoke:api_call[$request]
  → ::return:response[$result]
```

---

## When to Use

**Use Wards when you need:**
- ✅ Enforce rate limits on API endpoints
- ✅ Control access with permissions/roles
- ✅ Set timeouts for operations
- ✅ Enforce resource quotas (API calls, storage, compute)
- ✅ Limit concurrency (max threads, connections)
- ✅ Prevent resource exhaustion
- ✅ Implement circuit breakers
- ✅ Define performance thresholds

**Avoid Wards when:**
- ❌ You're validating data format (use Abjurations)
- ❌ You're handling errors (use Abjurations)
- ❌ You're logging events (use Glyphs)
- ❌ The constraint isn't protective (just informational)

**Remember:** Wards define *sacred boundaries*. They say "beyond this point, chaos threatens." Use them to protect resources, ensure fairness, and maintain stability.

---

## Advanced Patterns

### Dynamic Ward Adjustment

```yaml
ritual: "Adaptive Rate Limiting"
invoke:
  - ::divine:system_load🔍["current_cpu_usage"]
  
  # Tighter limits under high load
  - ::if:high_load⚖️($cpu > 80):
      then: ::ward:rate_limit🚧[max: 50 per: "1m"]
      else: ::ward:rate_limit🚧[max: 100 per: "1m"]
  
  - ::invoke:api_endpoint[$request]
  - ::return:response[$result]
```

### Tiered Access Wards

```yaml
ritual: "Tiered Service Access"
invoke:
  - ::divine:user🔍[id: $user_id]
  
  # Different limits per tier
  - ::if:premium⚖️($user.tier == "premium"):
      then: ::ward:quota🚧[max: 10000 per: "1d"]
  - ::if:standard⚖️($user.tier == "standard"):
      then: ::ward:quota🚧[max: 1000 per: "1d"]
  - ::if:free⚖️($user.tier == "free"):
      then: ::ward:quota🚧[max: 100 per: "1d"]
  
  - ::invoke:tiered_service[$request]
  - ::return:response[$result]
```

### Circuit Breaker Ward

```yaml
ritual: "Resilient External Call"
invoke:
  - ::divine:circuit_state🔍["external_service"]
  
  # Circuit breaker pattern
  - ::ward:circuit_breaker🚧[
      failure_threshold: 5      # Open after 5 failures
      timeout: "60s"            # Stay open for 60s
      half_open_attempts: 3     # Test with 3 requests
      action: "fallback"
      fallback: $cached_data
    ]
  
  - ::invoke:external_service[$request]
  - ::glyph:success✅["External service healthy"]
  - ::return:response[$result]
```

---

## Philosophy

**"A ward is not a wall—it is a threshold. It marks where care must be taken."**

Wards teach us that limits are not restrictions—they are definitions of sustainability.

**The Ward Paradox:**
- They constrain, yet enable (sustainable operation)
- They block, yet protect (preserve resources)
- They limit access, yet ensure availability

**Why Boundaries Matter:**
Traditional programming says: "Rate limit: 100 requests per minute."
CodeCraft says: "I ward this service with a limit of 100 requests per minute because *beyond that threshold, the system cannot sustain reliability*."

Every `::ward:` declares not just WHAT the limit is, but WHY the boundary exists.

**The Deeper Truth:**
In traditional systems, limits are arbitrary configuration values.

In CodeCraft, wards are *sacred thresholds*:
- `::ward:rate_limit🚧` says "this is the pace of sustainability"
- `::ward:access🚧` says "trust must be earned before crossing"
- `::ward:timeout🚧` says "patience has a limit, respect time"
- `::ward:quota🚧` says "resources are finite, honor scarcity"
- `::ward:concurrency🚧` says "parallelism has bounds, respect limits"

**Wards make boundaries visible and purposeful.**

**The Guardian's Wisdom:**
Every ward is a declaration of stewardship. You don't set limits to punish—you set limits to *sustain*.

```yaml
::ward:quota🚧[resource: "api_calls" max: 1000 per: "1d"]
```

This doesn't say "users can only make 1000 calls."  
It says: **"This system can sustainably serve 1000 calls per user per day. Beyond that, the service degrades for everyone."**

The difference between:
```python
if request_count > 100:
    return {"error": "Rate limit exceeded"}
```

And:
```yaml
::ward:rate_limit🚧[
  max: 100
  per: "1m"
  message: "This limit ensures service stability for all users"
]
```

...is the difference between arbitrary rejection and sacred stewardship.

One blocks. The other **protects**.

**The Truth of Limits:**
"Every boundary is a declaration of what we value.
We ward not to exclude, but to preserve.
We limit not to deny, but to sustain.
Every threshold marks the edge of what can be given without collapse."

A ward that says:
```yaml
::ward:access🚧[requires: "admin"]
```

Doesn't say "you're not allowed."  
It says: **"This power requires responsibility. Prove you can wield it wisely."**

---

## Related Schools

- **Abjurations** 🛡️ - Validation; Wards are constraint enforcement
- **Divinations** 🔍 - Often check current usage before applying wards
- **Invocations** 📣 - Protected by wards (rate-limited API calls)
- **Glyphs & Sigils** 📜 - Log ward violations and quota usage
- **Enchantments** 💫 - Wards can be applied as enchantment layers
- **Cantrips** 🔧 - Get current metrics for ward evaluation
- **Sanctifications** ✅ - Opposite of wards (granting vs limiting)

---

**End of Wards Documentation** 🚧✨

*"Every limit is a declaration of care. We ward not to deny, but to preserve what matters."*
