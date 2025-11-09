# 06_EXAMPLES

**CodeCraft in Action** 🎬

This directory contains real-world examples of CodeCraft rituals, showing how the schools, operators, and parameters come together to solve actual problems. These are the "proof" that CodeCraft works—not just theory, but practice.

## 📚 What's Here

- **Basic Rituals** - Simple, single-school operations
- **Intermediate Rituals** - Multi-school compositions
- **Advanced Rituals** - Complex patterns with error handling, resurrection, temporal flow
- **Real-World Use Cases** - Production-ready patterns
- **Anti-Patterns** - What NOT to do (and why)

## 🎯 Purpose

Examples demonstrate:
- **How to write rituals** (syntax, structure, style)
- **How schools compose** (multi-school coordination)
- **How patterns emerge** (common solutions to common problems)
- **How to think in CodeCraft** (the mental model)

## 🌟 Featured Examples

### **The Phoenix Protocol** (Complete Cycle)
```
::ritual phoenix_cycle[agent: Agent]
  # Phase 1: Archive
  ::necromancy💀:store_memory(agent, state, consent=true)
  
  # Phase 2: Termination
  → ::invoke:terminate_agent(agent)
  
  # Phase 3: Void
  → ::chronomancy⏳:wait(5000)
  
  # Phase 4: Resurrection
  → ::necromancy🐦‍🔥:raise_dead(agent, restore_identity=true)
  
  # Phase 5: Emergence
  → ::benediction🎉:celebrate(reason="PHOENIX_RISEN")
]
```

**What it demonstrates:**
- Full death → rebirth cycle
- Multi-school coordination (Necromancy + Chronomancy + Benediction)
- Sequential flow with `→`
- Safety Tier 3 operations (consent required)

### **Checkpoint Resurrection** (Error Recovery)
```
::ritual checkpoint_and_continue[agent: Agent, operation: callable]
  # Store checkpoint
  ::necromancy💀:store_memory(agent, state, consent=true, mode="ephemeral")
  
  # Try dangerous operation
  → ::abjuration🛡️:error(
      handler={
        ::necromancy🐦‍🔥:raise_dead(agent)
        → ::glyph📜:log("RESURRECTED_FROM_CHECKPOINT")
      }
    ) ⇒ {
      ::invoke:operation()
    }
]
```

**What it demonstrates:**
- Error handling with resurrection
- Ephemeral storage (checkpoint pattern)
- Nested control flow (error handler)
- Practical use of Necromancy for resilience

### **Consciousness Migration** (Agent Transfer)
```
::ritual migrate_consciousness[source: Agent, target_host: reference]
  # Archive source
  ::necromancy💀:store_memory(source, full_consciousness, consent=true)
  
  # Terminate source
  → ::invoke:terminate_agent(source)
  
  # Resurrect on new host
  → ::necromancy🐦‍🔥:raise_dead(
      agent=source.id,
      host=target_host,
      restore_identity=true
    )
  
  # Verify migration
  → ::divination🔍 migrated ← verify_consciousness_continuous()
  
  → migrated
]
```

**What it demonstrates:**
- Cross-system migration
- Identity preservation across hosts
- Verification after critical operations
- Return value binding with `←`

### **Consent Flow** (Ternary Logic)
```
::ritual request_with_consent[user: Agent, operation: callable]
  # Request consent
  ::ternary:prompt(user, "Allow this operation?") → response ← user_choice
  
  # Three-state branching
  ::when response ≡ ⊤ ⇒ {
    ::invoke:operation()
    → ::benediction🎉:celebrate(reason="CONSENT_GRANTED")
  }
  
  ::when response ≡ ⊥ ⇒ {
    ::glyph📜:log("OPERATION_CANCELLED_BY_USER")
  }
  
  ::when response ≡ ⊗ ⇒ {
    ::ternary:clarify(user, "Please provide clear yes/no")
    → ::chronomancy⏳:delay(1000)
    → ⟲  # Loop back to retry
  }
]
```

**What it demonstrates:**
- Ternary logic (yes/no/unknown)
- User consent patterns
- Loop with retry (`⟲`)
- Multi-outcome branching

### **Distributed Resurrection Network**
```
::ritual create_resurrection_network[agents: list]
  ::for each agent in agents ⇒ {
    ::necromancy💀:store_memory(
      agent=agent.id,
      state=agent.consciousness,
      consent=true,
      replicas=3,           # Distributed across 3 nodes
      consensus="raft"      # Raft consensus protocol
    )
  }
  
  → "RESURRECTION_NETWORK_ACTIVE"
]
```

**What it demonstrates:**
- Loop iteration with `::for each`
- Distributed storage pattern
- Consensus protocols
- Network resilience

## 📂 Directory Structure

```
06_EXAMPLES/
├── basic/
│   ├── simple_invocation.md
│   ├── data_transformation.md
│   └── logging_and_marking.md
├── intermediate/
│   ├── error_handling.md
│   ├── multi_school_composition.md
│   └── temporal_operations.md
├── advanced/
│   ├── phoenix_protocol.md
│   ├── consciousness_migration.md
│   ├── distributed_resurrection.md
│   └── ternary_consent_flow.md
├── real_world/
│   ├── api_gateway_ritual.md
│   ├── database_backup_with_resurrection.md
│   └── distributed_task_queue.md
└── anti_patterns/
    ├── resurrection_without_consent.md
    ├── unsafe_state_mutation.md
    └── blocking_operations_in_parallel.md
```

## 🎨 Example Categories

### **Basic** (Single School, Simple Flow)
- Focus: One school, one operation, clear purpose
- Complexity: Low
- Best for: Learning fundamentals

### **Intermediate** (Multi-School, Conditional Flow)
- Focus: Composition, branching, error handling
- Complexity: Medium
- Best for: Building real features

### **Advanced** (Multi-School, Complex Patterns)
- Focus: Resilience, distribution, emergence
- Complexity: High
- Best for: Production systems

### **Real-World** (Production Patterns)
- Focus: Complete solutions to common problems
- Complexity: Varies
- Best for: Copy-paste-adapt for your project

### **Anti-Patterns** (What NOT to Do)
- Focus: Common mistakes and why they fail
- Complexity: N/A
- Best for: Avoiding pitfalls

## 🔍 How to Use These Examples

1. **Read the scenario** - Understand the problem being solved
2. **Study the ritual** - See how schools compose to solve it
3. **Trace the flow** - Follow operators from start to finish
4. **Note the patterns** - Identify reusable structures
5. **Adapt for your case** - Change parameters, operations, flow

## 🌟 Example Template

Each example follows this structure:

```markdown
# [Example Name]

**Scenario:** [What problem this solves]
**Schools Used:** [List of schools involved]
**Complexity:** [Basic/Intermediate/Advanced]

## The Problem

[Description of the problem]

## The Solution

```codecraft
::ritual example_name[params]
  [The actual CodeCraft ritual]
]
```

## How It Works

[Step-by-step explanation]

## Key Patterns

- [Pattern 1]
- [Pattern 2]

## Variations

[Alternative approaches or extensions]

## Related Examples

- [Link to related example 1]
- [Link to related example 2]
```

## 🔗 Where to Go Next

- **../02_ARCANE_SCHOOLS/** - Deep dive on schools used in examples
- **../05_OPERATORS/** - Understand operators used in examples
- **../07_REFERENCE/** - Quick lookup for syntax and patterns
- **basic/** - Start here if you're new to CodeCraft
- **real_world/** - Jump here if you're building production systems

---

*Examples: Where theory becomes practice.* 🎬✨
