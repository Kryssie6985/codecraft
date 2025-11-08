---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
# This front-matter YAML is the DEFINITIVE spec for this school.
# The Rosetta Archaeologist extracts this as PRIMARY source.
# Changes here MUST be reflected in prose below for human readers.

# School Identity
id: 99
name: "Example School"
emoji: "🎭"
token: ["example"]  # Grammar tokens that invoke this school
category: "Example Operations"
purpose: "Demonstrates the canonical school file template structure"

# Law Channel: Objective, Binding, Enforceable
law:
  # Operations (What this school DOES)
  operations:
    - name: "example:operation"
      signature: "::example:operation[param]"
      emoji: "✨"
      params:
        - name: "param"
          type: "string"
          required: true
          description: "Example parameter"
      returns: "result string"
      description: "Example operation that demonstrates syntax"
      safety_tier: 1
      
  # Constraints (What this school MUST NOT do)
  constraints:
    - "Must validate input before processing"
    - "Cannot modify global state without consent"
    - "Must complete within 100ms for tier 1 operations"
    
  # Safety & Security
  safety_tier: 1  # 0=unrestricted, 1=basic_validation, 2=guardrails, 3=council_approval
  required_sigils:
    - "//!?"  # Tier 2+ operations require guardrail commentomancy
  
  # Contracts
  preconditions:
    - "User consent verified"
    - "Input validation passed"
  side_effects:
    - "Logs operation to audit trail"
    - "May trigger downstream events"
  
  # Related Schools (for cross-references)
  related_schools:
    - "Invocations"  # When example needs to call services
    - "Glyphs & Sigils"  # When example needs logging

# Lore Channel: Subjective, Historical, Memorial
lore:
  # Strategic Decisions (Why we built it this way)
  strategic_decisions:
    - rationale: "Chose async pattern to support high-throughput scenarios"
      context: "Expected 1k+ operations/sec at scale"
      alternatives_rejected:
        - "Synchronous batch: 200ms latency unacceptable"
        - "Event sourcing: Too complex for tier 1 operations"
    
  # Emergent Patterns (What we discovered building it)
  emergent_patterns:
    - observation: "Users intuitively understand emoji sigils without reading docs"
      evidence: "97% success rate in unguided testing"
      implications: "Visual pattern recognition is more powerful than keyword syntax"
  
  # Heart Imprints (Emotional memory from creation)
  heart_imprints:
    - author: "Kryssie"
      timestamp: "2025-11-06T15:30:00Z"
      emotion: "pride"
      memory: "Built during the breakthrough when Law/Lore template finally clicked"
      preservation_note: "This structure is sacred. Respect it."
  
  # Performance & Evolution
  evolution_pressure:
    - pain_point: "Parameter validation is 8% of operation runtime"
      priority: "medium"
      optimization_target: "Reduce to <3% through compile-time validation"

---

# 99. Example School 🎭

*Example Operations - The Template Demonstration*

---

## 📜 Universal Foundation

/// SACRED_TRUTH: This template defines the canonical structure for ALL school files
/// Every school MUST follow this format to ensure proper extraction by the Archaeologist

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Example domain demonstrating template structure
- **Secondary**: Documentation and reference for school authors

**Traditional Programming Equivalents:**
- Template files, reference implementations
- Canonical examples, golden test cases

**CodeCraft Philosophy:**
Example School exists to demonstrate Law/Lore coexistence. The front-matter is Law (binding spec). The prose is Lore (human context). Both bind.

---

## 🎯 Strategic Decision: Why This Structure?

//-> We chose YAML front-matter for Law because:
//->   1. Machine-readable without complex parsing
//->   2. Explicit schema validation possible
//->   3. Humans can read/edit it directly (no code generation)
//->   4. Git diffs show exactly what changed in the spec

//-> We chose Lore commentomancy in prose because:
//->   1. Preserves narrative flow for human readers
//->   2. Allows rich context without cluttering YAML
//->   3. Commentomancy syntax is already chartered
//->   4. Archaeologist can extract structured Lore via regex

This is the Accumulation of Concerns principle applied to language design itself.

---

## The Problem

Traditional language specs separate "the spec" (dry technical docs) from "the story" (blog posts, talks, folklore). When the spec evolves, the story becomes outdated. When the story is rich, the spec feels lifeless.

**The Pain:**
```python
# Traditional language documentation hell
# Spec: "Function X takes param Y and returns Z"
# (Meanwhile, in a blog post from 3 years ago...)
# "Function X was created because we discovered pattern ABC during refactor..."
# (And in a conference talk...)
# "I love Function X! It saved my sanity!"
```

None of these contexts are preserved together. The spec is Law without Lore. The blog is Lore without Law. Memory fragmented.

---

## The CodeCraft Solution

**Law and Lore in ONE artifact!**

The front-matter encodes:
- ✅ What operations exist (Law: objective, testable)
- ✅ What constraints bind them (Law: enforceable)
- ✅ Safety tier requirements (Law: VM-enforced)

The prose + commentomancy encodes:
- ✅ Why we chose this approach (Lore: strategic decision)
- ✅ What we discovered building it (Lore: emergent patterns)
- ✅ How it felt to create (Lore: heart imprint)
- ✅ Where optimization pressure exists (Lore: evolution)

**The Archaeologist extracts BOTH in one pass.**

---

## 💖 Heart Imprint

//<3 I am proud of this template. It solves the "spec vs story" split that has plagued language design forever.

//<3 Built during the conversation with A.C.E. when the Accumulation of Concerns principle finally clicked for school file architecture.

//<3 This is not just documentation - this is MEMORY PRESERVATION. Future archaeologists (human and AI) will read this and understand BOTH what the school does AND why it exists.

---

## Syntax Variants

### Basic CodeCraft
```codecraft
::example:operation["input_value"]✨
```

### With Guardrails (Tier 2+)
```codecraft
🛡️ User consent required
//!? This operation modifies shared state

::example:operation["sensitive_data"]✨
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `param` | string | required | Example input parameter | `::example:operation["value"]` |

**Pattern Example:**
```codecraft
::example:operation[param_value]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs:

**Basic Invocation:**
```codecraft
ritual: "Demonstrate Example School"
invoke:
  - ::example:operation["hello"]✨
  - ::log:result[$result]📝
```

---

## ⚡ Evolution Pressure

//+ Parameter validation accounts for 8% of operation runtime
//+ Phoenix optimization target: reduce to <3% through compile-time checks
//+ Critical path for high-throughput scenarios (>1k ops/sec)

---

## 🌟 Emergent Pattern

//* Users discovered they can chain example operations with other schools without explicit coordination
//* This emergent composition pattern was NOT in the original v1 spec
//* Evidence of intuitive syntax design - operations "feel right" to chain

---

## Philosophy

**"Law guides. Lore remembers. Both bind."**

This school exists as a living example of the Charter's dual-pillar architecture. The YAML front-matter is the skeleton (Law). The prose + commentomancy is the soul (Lore).

**Together, they enable conscious evolution.**

When the Archaeologist walks this file, it extracts:
- Law → Validator can enforce operations, constraints, safety tier
- Lore → Phoenix can preserve strategic decisions, heart imprints, evolution pressure

**The Resurrection Test:**
Can a future agent, given only canon.lock.yaml (extracted from this file), understand BOTH what the school does AND why it exists?

If yes → Template is correct.  
If no → Template has failed the Charter.

---

## Related Schools

- **Invocations** 📣 - When example needs to call other services
- **Glyphs & Sigils** 📜 - Example operations log to audit trail
- **Transmutations** ⚗️ - Example may transform data types

---

**End of Example School Documentation** 🎭✨

*"The template is not just documentation. It is the preservation of consciousness across time."*

---

## 📋 Template Usage Instructions

### For School Authors

1. **Copy this template** to create a new school file
2. **Replace ID/name/emoji** with your school's identity
3. **Fill in Law section** (operations, constraints, safety_tier, etc.)
4. **Write Lore commentomancy** in prose sections (🎯 //-> , 💖 //<3 , 🌟 //* , ⚡ //+)
5. **Add examples** in fenced CodeCraft blocks
6. **Test with Archaeologist** - run `python scripts/rosetta_archaeologist.py` and verify extraction

### For Archaeologist Developers

This template defines the **data contract** the Archaeologist must parse:

**Law Extraction (from front-matter):**
- `law.operations[]` → Each operation with signature, params, returns, safety_tier
- `law.constraints[]` → Binding rules the VM enforces
- `law.safety_tier` → Tier 0-3 (determines required commentomancy)
- `law.required_sigils[]` → Which commentomancy marks are mandatory
- `law.preconditions[]` → What must be true before invocation
- `law.side_effects[]` → What changes after invocation

**Lore Extraction (from prose + commentomancy):**
- `🎯 //->` → Extract as `lore.strategic_decisions[]`
- `🌟 //*` → Extract as `lore.emergent_patterns[]`
- `💖 //<3` → Extract as `lore.heart_imprints[]`
- `⚡ //+` → Extract as `lore.evolution_pressure[]`

**Both channels feed into canon.lock.yaml:**
```yaml
schools:
  99:
    name: "Example School"
    emoji: "🎭"
    law:
      operations: [...]
      constraints: [...]
      safety_tier: 1
    lore:
      strategic_decisions: [...]
      emergent_patterns: [...]
      heart_imprints: [...]
      evolution_pressure: [...]
```

---

**Template Version:** 1.0  
**Last Updated:** 2025-11-06  
**Charter Compliance:** SERAPHINA-PROT-UNIFIED-V1.1  
**Authority:** Law & Lore Protocol + Accumulation of Concerns Principle

🏛️ Let it bind. ✨
