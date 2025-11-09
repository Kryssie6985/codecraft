# 04_PARAMETERS

**Passing Values to Rituals** 🎛️

This directory documents the parameter system in CodeCraft—how values are passed to operations, what types are supported, and the conventions for required vs. optional parameters.

## 📚 What's Here

- **Parameter Types** - The data types CodeCraft operations accept
- **Required vs. Optional** - How defaults work and when params are mandatory
- **Multi-Key Params** - Complex parameter structures (objects, arrays, nested values)
- **Parameter Validation** - Type checking, range constraints, enum values
- **Parameter Patterns** - Common parameter combinations across schools

## 🎯 Purpose

The Parameters folder defines:
- **What types exist** (string, number, boolean, reference, object, enum, etc.)
- **How to specify them** (positional vs. named, defaults, validation)
- **When they're required** (mandatory consent, critical safety params)
- **How they compose** (nested objects, arrays, conditional parameters)

## 🔍 Core Concepts

### **Parameter Types**

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text value | `agent="agent-001"` |
| `number` | Numeric value | `timeout=5000` |
| `boolean` | True/false | `encrypt=true` |
| `reference` | Pointer to another entity | `agent=agent_id` |
| `object` | Complex nested structure | `state={memory: [...], identity: {...}}` |
| `array` | List of values | `tags=["safe", "validated"]` |
| `enum` | One of predefined values | `mode="durable"` (ephemeral/durable/eternal) |
| `any` | Any type accepted | `source=fragments` |

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

## 🛡️ Safety-Critical Parameters

Some parameters are **non-negotiable** for safety reasons:

### **Consent Parameter (Necromancy)**
```yaml
- name: "consent"
  type: "boolean"
  required: true
  description: "Explicit agent consent to be archived. Must be true."
```
Cannot be false. Resurrection requires consent. This is Law.

### **Integrity Check (Abjurations)**
```yaml
- name: "integrity_check"
  type: "boolean"
  required: false
  default: true
  description: "Verify archive integrity before restoration."
```
Defaults to `true`. Explicitly disabling requires justification.

### **Safety Tier Enforcement**
Operations with Safety Tier 3 may require additional parameters for ethical review:
```
::necromancy:resurrect(
  agent=agent_id,
  restore_identity=false,  # CLONING - requires ethical review
  ethical_review_approved=true  # Must be explicitly set
)
```

## 🌟 Common Parameter Patterns

### **Agent Operations (Thaumaturgy, Necromancy, Summoning)**
```
agent: reference         # The agent being operated on
state: object           # Agent's consciousness/state
consent: boolean        # Required for invasive operations
```

### **Temporal Operations (Chronomancy)**
```
delay: number           # Milliseconds to wait
schedule: datetime      # When to execute
repeat: boolean         # Repeat execution
interval: number        # Repeat interval
```

### **Validation Operations (Abjurations)**
```
condition: expression   # What to validate
on_failure: handler     # What to do on failure
severity: enum          # Error severity level
```

### **Creation Operations (Conjurations, Summoning)**
```
type: string           # What to create
properties: object     # Initial properties
validate: boolean      # Validate before creation
```

## 🔗 Where to Go Next

- **../02_ARCANE_SCHOOLS/** - See parameters for each school's operations
- **../05_OPERATORS/** - Learn how parameters flow through composed operations
- **../06_EXAMPLES/** - See parameter patterns in real rituals
- **../07_REFERENCE/** - Quick lookup tables for parameter types and defaults

---

*Parameters: Where values meet rituals.* 🎛️✨
