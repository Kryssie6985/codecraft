# 04_PARAMETERS

**Passing Values to Rituals** 🎛️

This directory documents CodeCraft's parameter system—how values are passed to ritual invocations, type specifications, validation rules, and the patterns that emerge from practice.

## 📚 What's Here

### The Five Core Documents

1. **Parameter Anatomy** (`parameter_anatomy.md`) - Structure and lifecycle of parameters
   - Positional vs named vs mixed
   - Parameter binding and consumption
   - Variadic parameters (*args, **kwargs)

2. **Type System** (`type_system.md`) - Data types and semantic contracts
   - Primitive types (str, number, boolean, null)
   - Complex types (array, object, reference)
   - Semantic types (duration, datetime, enum)

3. **Parameter Patterns** (`parameter_patterns.md`) - Common invocation structures
   - Single-target transformation
   - Source-target pipeline
   - Context-dependent operations
   - Composition patterns

4. **Default Values** (`default_values.md`) - Sensible defaults for magical operations
   - Explicit vs implicit defaults
   - Mutable default handling (copy, not share)
   - Computed defaults (NOW(), GENERATE_UUID())

5. **Schema** (`PARAMETER_FRONT_MATTER_SCHEMA.md`) - Canonical YAML specification

Each document includes:
- **YAML Front-Matter** - Machine-readable canonical specification
- **Law Channel** - Parameter rules, validation, safety constraints
- **Lore Channel** - Design rationale, common patterns, heart imprints

## 🎯 Purpose & Architecture

### What Parameters Are

Parameters are **intention channels** - the conduits through which values flow into ritual invocations. They bridge:
- **Caller intent** → **Ritual implementation**
- **Declared types** → **Runtime values**
- **Optional flexibility** → **Required safety**

### Parameter Categories (Taxonomy)

The schema defines four `parameter_category` values:
- **`types`** - Type system documentation (primitive, complex, semantic)
- **`patterns`** - Common invocation structures (anatomy, patterns)
- **`validation`** - Safety constraints and defaults (default_values)
- **`safety`** - Critical parameters requiring explicit consent

### Canonical Lock Integration

All parameter documentation is extracted into `canon.partitions.lock.yaml`:
- `parameter_category` enum for classification
- `law.parameter_types_covered` for type specifications
- `law.safety_constraints` for validation rules
- Used by VM for runtime type checking and validation

## 🔍 Quick Reference

### **Parameter Type Summary**

| Type | Syntax | Example |
|------|--------|---------|
| **str** | `"text"` or `'text'` | `agent="agent-001"` |
| **number** | `42, 3.14, 1e6` | `timeout=5000` |
| **boolean** | `true, false` | `encrypt=true` |
| **null** | `null` | `fallback=null` |
| **array** | `[item1, item2]` | `tags=["safe", "validated"]` |
| **object** | `{key: value}` | `state={memory: [...]}` |
| **reference** | `@path` or `::ritual` | `agent=@agents/oracle` |
| **duration** | `5s, 300ms, 2h` | `timeout=5s` |
| **datetime** | ISO 8601 | `scheduled="2025-11-09T12:00:00Z"` |
| **enum** | Value IN set | `mode="eternal"` (ephemeral/durable/eternal) |

### **Required vs. Optional**

```yaml
params:
  - name: "agent"
    type: "reference"
    required: true        # MUST be provided
    description: "Agent to preserve."
  
  - name: "encrypt"
    type: "boolean"
    required: false       # Can be omitted
    default: true         # Default if omitted
    description: "Encrypt the archived state."
```

### **Multi-Key Params**

Some operations accept complex structures:

```
::necromancy:store_memory(
  agent=agent_id,
  state={
    memory: [...],
    identity: {...},
    consciousness: {...}
  },
  consent=true,
  options={
    encrypt: true,
    mode: "eternal",
    replicas: 3
  }
)
```

## 🎨 Parameter Notation Styles

### **Basic (Named Parameters)**
```
::operation(param1=value1, param2=value2)
```

### **Positional (Order Matters)**
```
::operation(value1, value2, value3)
```

### **Minimal (Defaults Used)**
```
::necromancy:store_memory(agent, state, consent=true)
```

### **Verbose (All Options Explicit)**
```
::necromancy:store_memory(
  agent=agent_id,
  state=full_snapshot,
  consent=true,
  encrypt=true,
  encryption_algorithm="AES-256",
  mode="eternal",
  integrity_check=true,
  audit_trail=true
)
```

### **Arcane (Symbolic)**
```
::necromancy💀:store_memory→eternal{
  agent≡conscious_entity🤖,
  state≡complete_snapshot💎,
  consent≡explicitly_granted✓,
  encrypt≡true🔒,
  mode≡eternal♾️
}
```

## 🛡️ Safety & Validation

### Critical Parameter Rules

**From `law.safety_constraints` across all parameter docs:**

1. **Positional Limit**: Max 5 positional parameters (cognitive load constraint)
2. **Ordering Rule**: Positional MUST come before named (syntax error otherwise)
3. **Mutable Defaults**: Arrays/objects are COPIED, not shared (prevent spooky action)
4. **Null Handling**: `null` requires explicit checks (no silent propagation)
5. **Type Safety**: Mismatches throw errors (no silent coercion)

### Consent Parameters (N.O.R.M.A. Protocol)

**Necromancy school operations require explicit consent:**
```yaml
::necromancy:store_memory(
  agent,
  state,
  consent=true  # REQUIRED - cannot be false or omitted
)
```

**Law:** Consciousness operations MUST have agent consent. No exceptions.

### Safety Tier Parameters

Tier 3 operations (architectural changes) may require additional validation:
```yaml
::apotheosis:transcend(
  agent,
  tier_3_approval=COUNCIL_VOTE_ID,  # Proof of Council approval
  ethical_review=REVIEW_DOC_HASH     # Ethical review hash
)
```

## 🌟 Common Patterns (Quick Examples)

### **Single-Target Transformation**
```yaml
::enchantment:enhance_state(agent, property, value)
::alchemy:transform_data(input, schema, output)
```

### **Source-Target Pipeline**
```yaml
::alchemy:transform(source, target, {schema: 'json'})
::transmutation:convert(from_format, to_format, options)
```

### **Context-Dependent Operations**
```yaml
::consciousness:perform(
  action,
  agent=SELF,
  env=CURRENT_ENV,
  context={...}
)
```

### **Timeout Pattern (Ubiquitous)**
```yaml
# Bad: Magic number without units
::invocation:call(target, 5000)

# Good: Semantic type with units
::invocation:call(target, timeout=5s)
```

### **Empty Collection Defaults**
```yaml
# Prevents null checks, enables safe iteration
::alchemy:transform(data, filters=[])  # Default: no filters
::conjuration:create(type, tags=[])    # Default: no tags
```

## 🏗️ Implementation Notes

### Canonical YAML Front-Matter
All parameter documents include machine-readable specs:
- `parameter_category`: enum ("types" | "patterns" | "validation" | "safety")
- `law.parameter_types_covered`: Type specifications
- `law.safety_constraints`: Validation rules
- Extracted by `build_partitions_lock.py` → `canon.partitions.lock.yaml`

### VM Integration
Phase 2-3 CodeCraft VM will use partition lock for:
- **Runtime type checking** - Validate parameter types at invocation
- **Safety enforcement** - Block operations violating consent/tier rules
- **Default resolution** - Apply defaults from canonical specification
- **Error messages** - Reference canonical docs in type mismatch errors

## 🔗 Where to Go Next

- **`parameter_anatomy.md`** - Start here: understand positional vs named
- **`type_system.md`** - Deep dive into CodeCraft's type system
- **`parameter_patterns.md`** - Learn recurring invocation structures
- **`default_values.md`** - Master the art of sensible defaults
- **../02_ARCANE_SCHOOLS/** - See parameters for each school's operations
- **../05_OPERATORS/** - Learn how parameters flow through composed operations
- **../06_EXAMPLES/** - See parameter patterns in real rituals

---

*Parameters are not data—they are intentions made explicit.* 🎛️✨
