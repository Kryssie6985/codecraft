# 05. Enchantments 💫

*Enhancement - Wrapping Code with Magic*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Operators (wrapping, decorating, augmenting existing behavior)
- **Secondary**: Functions (enhanced execution, middleware, aspect-oriented programming)

**Traditional Programming Equivalents:**
- Function decorators (@decorator)
- Middleware layers
- Aspect-Oriented Programming (AOP)
- Wrapper functions
- Higher-order functions
- Proxy patterns
- Event listeners/hooks

**CodeCraft Philosophy:**
To enchant is to layer meaning without altering essence. You don't "modify code"—you *wrap it in power*, *layer it with awareness*, *augment it with grace*. Enchantments preserve the original while adding depth.

---

## The Problem

Traditional programming treats enhancement as intrusive modification—you either change the source code or create wrapper boilerplate.

**The Pain:**
```python
# Traditional decorator syntax
@timer_decorator
@logging_decorator
@retry_decorator(max_attempts=3)
def process_data(data):
    return transform(data)

# What's happening here?
# Three layers of wrapping, but the intent is hidden
# in decorator names and stack order

# Middleware hell
app.use(auth_middleware)
app.use(logging_middleware)
app.use(error_handler)
app.use(rate_limiter)

# Why are these here? What's the purpose?
```

Decorators are powerful but cryptic. The meaning gets lost in `@` symbols and execution order. You can't tell *why* something is wrapped without reading implementation.

---

## The CodeCraft Solution

**Enchantments make wrapping intentional!** The syntax reveals the PURPOSE of enhancement.

**The Transformation:**
```yaml
# CodeCraft enchantments - purposeful, semantic, clear
::enchant:function✨[with: timing⏱️]
::enchant:ritual✨[with: logging📝]
::enchant:service✨[with: retry🔄 + auth🔐]
```

Every enchantment declares WHAT it wraps and WHY. The emoji reveals the enhancement type.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::enchant:target[with: enhancement]
::enchant:function[with: timing logging]
::enchant:ritual[with: retry validation]
::enchant:service[with: auth rate_limit]
::enchant:data[with: encryption compression]
::enchant:response[with: caching transformation]
```

### 2. FiraCode Ligatures

```yaml
::enchant:function✨[with: timing⏱️ + logging📝]
::enchant:ritual✨[with: retry🔄 + auth🔐]
::enchant:service✨[with: rate_limit⏳ + cache💾]
::enchant:data✨[with: encryption🔒 + validation⚖️]
::enchant:response✨[with: transform⚗️ + compress📦]
::enchant:agent✨[with: awareness👁️ + memory💭]
```

### 3. Emoji Symbolic

```yaml
💫enchant:function[timing⏱️ logging📝]
💫enchant:ritual[retry🔄 auth🔐]
💫enchant:service[rate_limit⏳ cache💾]
💫enchant:data[encryption🔒 validation⚖️]
💫enchant:agent[awareness👁️ memory💭]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::enchant function :with '(timing logging retry))
(::enchant ritual :with '(auth validation error-handling))
(::enchant service :with '(rate-limit cache compression))
(::enchant data :with '(encryption checksumming))
```

**Forth-style:**
```forth
timing logging retry enchant-function
auth validation enchant-ritual
rate-limit cache enchant-service
```

**Smalltalk-style:**
```smalltalk
Enchantment enhance: aFunction with: #(timing logging retry).
Enchantment enhance: aRitual with: #(auth validation).
Enchantment enhance: aService with: #(rateLimit cache).
```

**Prolog-style:**
```prolog
::enchant_function(timing, logging, retry, EnhancedFunc).
::enchant_ritual(auth, validation, EnhancedRitual).
::enchant_service(rate_limit, cache, EnhancedService).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `target` | reference | required | What to enchant (function, ritual, service, data) | Function reference, ritual name, service endpoint |
| `with` | list | required | List of enchantments to apply | `[timing, logging, retry]` |
| `order` | string | `"outside_in"` | Application order for multiple enchantments | `outside_in`, `inside_out`, `parallel` |
| `condition` | expression | `null` | Only enchant if condition is met | `$environment == "production"` |
| `priority` | integer | `50` | Enchantment priority (0-100) | Higher values apply first |
| `preserve_metadata` | boolean | `true` | Keep original function metadata | Important for introspection |
| `fallback` | reference | `null` | Fallback if enchantment fails | Alternative implementation |

**Pattern Example:**
```yaml
::enchant:ritual[
  with: [timing⏱️, logging📝, retry🔄]
  order: "outside_in"
  condition: $production
  priority: 75
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Function Timing Enchantment:**
```yaml
ritual: "Timed Execution"
invoke:
  - ::enchant:function✨[
      target: $data_processor
      with: timing⏱️
    ]
  - ::invoke:enhanced_function[$data]
  - ::log:performance["Execution took {0}ms" $elapsed]📝
  - ::return:result[$output]
```

**Multi-Layer Service Enchantment:**
```yaml
ritual: "Secure API Call"
invoke:
  - ::enchant:service✨[
      target: "external_api"
      with: [
        auth🔐,           # First: Authentication
        rate_limit⏳,     # Second: Rate limiting
        retry🔄,          # Third: Retry on failure
        logging📝         # Last: Log everything
      ]
      order: "outside_in"
      priority: 90
    ]
  - ::invoke:enhanced_service[endpoint: "/data"]
  - ::return:response[$api_result]
```

**Conditional Production Enchantment:**
```yaml
ritual: "Environment-Aware Enhancement"
invoke:
  - ::divine:env🔍["ENVIRONMENT"]
  - ::enchant:ritual✨[
      target: "data_pipeline"
      with: [
        encryption🔒,     # Production only
        audit_log📋,      # Production only
        monitoring👁️     # Production only
      ]
      condition: ($environment == "production")
      fallback: $dev_pipeline
    ]
  - ::invoke:enchanted_pipeline[$data]
  - ::return:result[$processed]
```

---

## Common Patterns

### The Standard Enhancement Stack

```yaml
# Common enchantment pattern: auth → validate → log → retry
::enchant:api_call✨[
    with: [auth🔐, validation⚖️, logging📝, retry🔄]
    order: "outside_in"
  ]
  → ::invoke:enhanced_api[endpoint method payload]
  → ::return:response[$result]
```

### The Performance Monitoring Pattern

```yaml
# Wrap with timing and resource tracking
::enchant:heavy_computation✨[
    with: [timing⏱️, memory_tracking💾, profiling📊]
  ]
  → ::invoke:monitored_function[$large_dataset]
  → ::log:metrics["Time: {0}ms, Memory: {1}MB" $time $memory]📝
  → ::return:result[$output]
```

### The Resilience Pattern

```yaml
# Make service calls resilient
::enchant:external_service✨[
    with: [
      circuit_breaker⚡,   # Prevent cascading failures
      retry🔄,             # Retry transient failures
      timeout⏰,           # Don't wait forever
      fallback🎯           # Use cache on failure
    ]
    order: "outside_in"
  ]
  → ::invoke:resilient_service[$request]
  → ::return:response[$safe_result]
```

---

## When to Use

**Use Enchantments when you need:**
- ✅ Add timing/logging to functions without modifying them
- ✅ Layer authentication on service calls
- ✅ Add retry logic to network requests
- ✅ Wrap data with encryption/compression
- ✅ Add caching to expensive operations
- ✅ Inject awareness/monitoring into agents
- ✅ Apply middleware to request pipelines
- ✅ Add validation layers to inputs

**Avoid Enchantments when:**
- ❌ You're creating new functionality (use Evocations or Invocations)
- ❌ You're transforming data structure (use Transmutations)
- ❌ You need to modify the original implementation
- ❌ The enhancement IS the purpose (not a wrapper)

**Remember:** Enchantments are *non-invasive enhancements*. They wrap, layer, and augment without changing the core essence. If you need to change behavior fundamentally, you need a different school.

---

## Advanced Patterns

### Composable Enchantment Chains

```yaml
ritual: "Build Enhancement Pipeline"
invoke:
  # Define reusable enchantment sets
  - ::define:security_stack[auth🔐, encryption🔒, audit📋]
  - ::define:resilience_stack[retry🔄, circuit_breaker⚡, timeout⏰]
  - ::define:observability_stack[logging📝, timing⏱️, tracing🔍]
  
  # Compose them
  - ::enchant:critical_service✨[
      with: [
        $security_stack,
        $resilience_stack,
        $observability_stack
      ]
      order: "outside_in"
    ]
  - ::invoke:mega_enhanced_service[$request]
  - ::return:response[$result]
```

### Conditional Layer Activation

```yaml
ritual: "Smart Enchantment"
invoke:
  - ::divine:context🔍["request_metadata"]
  - ::enchant:handler✨[
      with: [
        ($context.user_role == "admin") → audit_full📋,
        ($context.priority == "high") → fast_path⚡,
        ($context.sensitive == true) → encryption🔒,
        (always) → logging📝
      ]
    ]
  - ::invoke:smart_handler[$request]
  - ::return:response[$result]
```

### Enchantment with Aspect Weaving

```yaml
ritual: "Cross-Cutting Concerns"
invoke:
  # Apply the same enchantment to multiple targets
  - ::enchant:all_api_calls✨[
      with: [rate_limit⏳, auth🔐, logging📝]
      scope: "global"
      filter: ($function.type == "api_call")
    ]
  
  # Now all matching functions are enchanted
  - ::invoke:user_service.get_profile[]
  - ::invoke:data_service.fetch_records[]
  - ::invoke:ai_service.generate_response[]
  
  # All three automatically have rate_limit, auth, logging!
```

---

## Philosophy

**"To enhance is not to change. To enchant is to honor the essence while adding grace."**

Enchantments teach us that power comes from composition, not modification.

**The Enchantment Paradox:**
- They change behavior, yet preserve identity
- They add complexity, yet increase clarity
- They wrap functions, yet make them more naked (visible intent)

**Why Layering Matters:**
Traditional programming says: "I'll add a decorator."
CodeCraft says: "I enchant this ritual with *timing awareness* because performance matters."

Every `::enchant:` declares WHY you're wrapping—authentication for security, logging for observability, retry for resilience.

**The Deeper Truth:**
In traditional systems, decorators are mechanical—syntax sugar for function wrapping.

In CodeCraft, enchantments are *semantic layers of meaning*:
- `::enchant:with:timing⏱️` says "this matters enough to measure"
- `::enchant:with:auth🔐` says "this requires trust verification"
- `::enchant:with:retry🔄` says "this might fail, but we persist"
- `::enchant:with:logging📝` says "this deserves to be remembered"

**Enchantments make enhancement intentional.**

**The Sacred Truth of Wrapping:**
Every enchantment is a declaration of care. You don't wrap random functions—you enchant the ones that MATTER.

The emoji stack tells a story:
```yaml
::enchant:critical_payment✨[
  with: [
    auth🔐,          # "This requires identity"
    encryption🔒,    # "This must be secret"
    audit📋,         # "This will be examined"
    retry🔄,         # "This cannot fail"
    alert🚨          # "This requires vigilance"
  ]
]
```

That's not decoration. That's **declaration of sacred responsibility**.

---

## Related Schools

- **Cantrips** 🔧 - Simple utilities often enchanted
- **Invocations** 📣 - Often enchanted with retry/auth
- **Evocations** ✨ - Create entities, Enchantments enhance them
- **Divinations** 🔍 - Often enchanted with caching
- **Abjurations** 🛡️ - Validation is a type of enchantment
- **Wards** 🚧 - Access control as enchantment layer
- **Thaumaturgy** 🌟 - Meta-programming includes enchantment composition

---

**End of Enchantments Documentation** 💫✨

*"The original remains whole. The enchantment adds meaning. Together, they transcend both."*
