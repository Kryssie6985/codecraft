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
