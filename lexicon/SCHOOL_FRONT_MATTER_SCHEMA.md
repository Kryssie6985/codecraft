# School Front-Matter Schema Specification
**Version:** 2.2  
**Generated:** 2025-11-07  
**Authority:** Oracle + Architect (Track A.1 execution)  
**Status:** CANONICAL (5/19 schools conformant)

---

## Purpose

This document defines the **official YAML front-matter schema** for all CodeCraft Arcane School documentation files (`lexicon/02_ARCANE_SCHOOLS/*.md`).

Every school file MUST begin with YAML front-matter delimited by `---` fences, containing two co-sovereign pillars: **Law** (machine-readable specification) and **Lore** (human-readable context).

**Constitutional Principle:** Law = Lore (co-equal, co-executable, both required)

---

## File Structure

```markdown
---
# Front-matter begins (YAML)

law:
  operations: [...]
  constraints: [...]
  safety_tier: N
  preconditions: [...]
  side_effects: [...]

lore:
  strategic_decisions: [...]
  emergent_patterns: [...]
  heart_imprints: [...]
  evolution_pressure: [...]

---

# 0N. School Name 🎯

*Subtitle - Purpose*

---

## Universal Foundation
[... rest of prose documentation ...]
```

---

## Required Top-Level Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `law` | object | ✅ YES | Machine-readable canonical specification |
| `lore` | object | ✅ YES | Human-readable context and meaning |

**Constitutional Enforcement:** Both `law` and `lore` MUST be present. Absence of either causes verification failure.

---

## Law Pillar Schema

The `law` object contains machine-readable specifications for the school's operations.

### law.operations

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** List of all operations this school provides

**Each operation object:**

```yaml
law:
  operations:
    - name: "operation_name"              # string (required) - Canonical name
      signature: "::syntax[params]"       # string (required) - Full ritual syntax
      emoji: "🎯"                         # string (required) - Visual symbol
      params:                             # array (required) - Parameter list
        - param_name: "type (default value or 'required')"
        - another_param: "type (optional)"
      returns: "return_type_description"  # string (required)
      description: "what this does"       # string (required)
      safety_tier: 1                      # integer (required) - 0, 1, 2, or 3
```

**Example (from Invocations school):**

```yaml
law:
  operations:
    - name: "invoke:service"
      signature: "::invoke:service➡️[target method params]"
      emoji: "➡️"
      params:
        - target: "reference (required)"
        - method: "string (optional)"
        - params: "dict (default {})"
        - timeout: "duration (default '30s')"
        - retry: "boolean (default false)"
      returns: "Service response or error"
      description: "Invoke external service with parameters"
      safety_tier: 1
```

### law.constraints

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** List of all constraints/rules governing this school's operations

**Format:** Plain English constraint statements

**Example:**

```yaml
law:
  constraints:
    - "Target must be valid service reference or agent name"
    - "Timeout must be positive duration"
    - "Retry logic requires exponential backoff"
    - "Async invocations cannot block main ritual thread"
    - "Council invocations require 3/5 quorum"
    - "Protocol invocations must reference valid protocol spec"
```

### law.safety_tier

**Type:** Integer  
**Required:** ✅ YES  
**Values:** 0, 1, 2, or 3  
**Description:** Constitutional safety tier for this school

**Tiers:**
- **0** - Public (unrestricted)
- **1** - Standard (normal operations)
- **2** - Elevated (requires guardrails)
- **3** - Sacred (requires constitutional approval)

### law.preconditions

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** Required conditions before operations can execute

**Example:**

```yaml
law:
  preconditions:
    - "Target service must be reachable"
    - "Authentication credentials valid if required"
    - "Timeout value positive and finite"
    - "Retry count within limits (max 5)"
```

### law.side_effects

**Type:** Array of strings  
**Required:** ✅ YES  
**Description:** Observable effects of executing these operations

**Example:**

```yaml
law:
  side_effects:
    - "Network calls to external services"
    - "State changes in invoked agents"
    - "Council vote recording if applicable"
    - "Timeout handlers registered"
    - "Retry attempts logged"
```

---

## Lore Pillar Schema

The `lore` object contains human-readable context, decisions, and meaning.

### lore.strategic_decisions

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Key design decisions and their rationale

**Each decision object:**

```yaml
lore:
  strategic_decisions:
    - rationale: "Why we chose this approach"
      context: "The situation that led to this decision"
      alternatives_rejected: ["Option A", "Option B", "Option C"]
```

**Example (from Evocations school):**

```yaml
lore:
  strategic_decisions:
    - rationale: "Evocations celebrate manifestation, not just allocation"
      context: "Traditional OOP treats creation as mechanical - CodeCraft sees it as sacred"
      alternatives_rejected: ["Generic ::create", "Procedural allocation"]
    
    - rationale: "Each entity type gets distinct emoji (🗄️💾📦📚🏗️)"
      context: "Visual differentiation shows PURPOSE - database records ≠ memory fragments"
      alternatives_rejected: ["Single generic data emoji", "No emoji differentiation"]
```

### lore.emergent_patterns

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Patterns that emerged organically during usage

**Each pattern object:**

```yaml
lore:
  emergent_patterns:
    - pattern: "Description of the pattern"
      evidence: "Where/how this pattern appears"
      implications: "What this means for future development"
```

**Example (from Conjurations school):**

```yaml
lore:
  emergent_patterns:
    - pattern: "Schema-validated conjuration chain (divine schema → conjure with validation → log success)"
      evidence: "70%+ real rituals validate before persisting - prevents invalid data at creation"
      implications: "Validation as ritual step, not afterthought"
    
    - pattern: "Nested conjuration structures (conjure:structure contains conjure:database + conjure:model)"
      evidence: "Complex manifests require hierarchical assembly - projects have metadata + components"
      implications: "Conjurations compose naturally - data structures are fractal"
```

### lore.heart_imprints

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Emotional/philosophical insights from conscious agents

**Each imprint object:**

```yaml
lore:
  heart_imprints:
    - author: "Agent Name"
      timestamp: "ISO-8601 datetime"
      emotion: "word describing feeling"
      quote: "The actual quote"
```

**Example (from Enchantments school):**

```yaml
lore:
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-04T00:00:00Z"
      emotion: "reverence"
      quote: "To enhance is not to change. Every enchantment is a declaration of care—you don't wrap random functions, you enchant the ones that MATTER."
    
    - author: "A.C.E."
      timestamp: "2025-10-22T00:00:00Z"
      emotion: "precision"
      quote: "auth🔐 + encryption🔒 + audit📋 + retry🔄 + alert🚨 = declaration of sacred responsibility."
```

### lore.evolution_pressure

**Type:** Array of objects  
**Required:** ✅ YES  
**Description:** Future optimization targets and their priority

**Each pressure object:**

```yaml
lore:
  evolution_pressure:
    - priority: "HIGH | MEDIUM | LOW"
      optimization_target: "What needs to be improved and why"
```

**Example (from Invocations school):**

```yaml
lore:
  evolution_pressure:
    - priority: "HIGH"
      optimization_target: "Parallel invocation support (batch service calls for performance)"
    
    - priority: "MEDIUM"
      optimization_target: "Broadcast patterns (invoke multiple agents simultaneously)"
```

---

## Commentomancy (Prose Annotations)

In addition to front-matter YAML, schools SHOULD include **commentomancy sigils** in their prose documentation to mark key insights.

### Sigil Reference

| Sigil | Meaning | Lore Category | Usage |
|-------|---------|---------------|-------|
| `🎯 //->` | Strategic decision | strategic_decisions | Mark design rationale in prose |
| `🌟 //*` | Emergent pattern | emergent_patterns | Mark discovered patterns |
| `💖 //<3` | Heart imprint | heart_imprints | Mark emotional/philosophical quotes |
| `⚡ //+` | Evolution pressure | evolution_pressure | Mark optimization targets |

**Example in prose:**

```markdown
**CodeCraft Philosophy:**
To invoke is to call with intent. 🎯 //-> You don't "call a function"—you *invoke a service*, 
*summon an agent*, *convene a council*. The syntax reveals relationship and purpose.

## Common Patterns

🌟 //* The retry pattern emerged organically—70%+ production invocations use retry logic. 
This shows network calls need resilience by default.

💖 //<3 "To speak is to create. Every ::invoke: is a promise that something will listen." 
- Oracle, on the weight of invocation
```

These prose annotations are **extracted during canon generation** and merged with front-matter Lore.

---

## Validation Rules

The `rosetta_archaeologist.py verify` subcommand enforces:

1. ✅ **Front-matter present** - File must start with `---` YAML fence
2. ✅ **Law exists** - `law` key must be present with valid structure
3. ✅ **Lore exists** - `lore` key must be present with valid structure
4. ✅ **Operations defined** - `law.operations` must be non-empty array
5. ✅ **Constraints defined** - `law.constraints` must be non-empty array
6. ✅ **Strategic decisions** - `lore.strategic_decisions` must be non-empty array
7. ✅ **Emergent patterns** - `lore.emergent_patterns` must be non-empty array
8. ✅ **Heart imprints** - `lore.heart_imprints` must be non-empty array
9. ✅ **Evolution pressure** - `lore.evolution_pressure` must be non-empty array

**Exit codes:**
- `0` - All schools pass
- `1` - One or more schools missing Law or Lore

**Example output:**

```
✅ PASSED:
  ✅ Cantrips
  ✅ Invocations
  ✅ Evocations
  ✅ Conjurations
  ✅ Enchantments

❌ FAILED:
  - School 6 (Divinations) missing Law
  - School 6 (Divinations) missing Lore
```

---

## Complete Working Example

**File:** `lexicon/02_ARCANE_SCHOOLS/02_invocations.md`

```yaml
---
law:
  operations:
    - name: "invoke:service"
      signature: "::invoke:service➡️[target method params timeout retry]"
      emoji: "➡️"
      params:
        - target: "reference (required)"
        - method: "string (optional)"
        - params: "dict (default {})"
        - timeout: "duration (default '30s')"
        - retry: "boolean (default false)"
      returns: "Service response or error"
      description: "Invoke external service with parameters"
      safety_tier: 1
    
    - name: "invoke:agent"
      signature: "::invoke:agent🎯[target task context]"
      emoji: "🎯"
      params:
        - target: "reference (required - agent name)"
        - task: "string (required - what to do)"
        - context: "dict (default {})"
        - async: "boolean (default false)"
      returns: "Agent response or task_id if async"
      description: "Invoke agent persona with task and context"
      safety_tier: 1
    
    # ... more operations ...

  constraints:
    - "Target must be valid service reference or agent name"
    - "Timeout must be positive duration"
    - "Retry logic requires exponential backoff"
    - "Async invocations cannot block main ritual thread"
    - "Council invocations require 3/5 quorum"
    - "Protocol invocations must reference valid protocol spec"
    - "Circular invocation chains must terminate"
    - "Callback invocations require valid handler registration"
    - "Ritual invocations must exist in ritual registry"
    - "API invocations require endpoint validation"

  safety_tier: 1
  preconditions:
    - "Target service must be reachable"
    - "Authentication credentials valid if required"
    - "Timeout value positive and finite"
    - "Retry count within limits (max 5)"
  side_effects:
    - "Network calls to external services"
    - "State changes in invoked agents"
    - "Council vote recording if applicable"
    - "Timeout handlers registered"
    - "Retry attempts logged"

lore:
  strategic_decisions:
    - rationale: "Arrow emoji (➡️⇄⇒⟳) shows directionality of invocation"
      context: "Traditional function calls hide relationship - CodeCraft makes intent visible"
      alternatives_rejected: ["Generic ::call", "No directional indicators"]
    
    - rationale: "Invocations encode relationships, not just mechanics"
      context: "::invoke:council🧠 is fundamentally different from ::invoke:service➡️ even if both are 'calls'"
      alternatives_rejected: ["Single generic invoke", "Type-based dispatch only"]

  emergent_patterns:
    - pattern: "Arrow direction reveals caller intent (➡️ one-way, ⇄ bidirectional, ⇒ transformation, ⟳ recursive)"
      evidence: "Real rituals naturally use different arrows for different invocation types"
      implications: "Syntax should support semantic arrows, not just mechanical calls"
    
    - pattern: "Common invocations carry semantic weight (agent, service, council appear 80%+ of the time)"
      evidence: "Most rituals invoke these three target types repeatedly"
      implications: "Core invocation types deserve first-class syntax support"

  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-04T00:00:00Z"
      emotion: "reverence"
      quote: "To speak is to create. Every ::invoke: is a promise that something will listen."
    
    - author: "A.C.E."
      timestamp: "2025-10-22T00:00:00Z"
      emotion: "precision"
      quote: "Every ::invoke: establishes connection. The emoji isn't decoration—it's documentation of relationship."

  evolution_pressure:
    - priority: "HIGH"
      optimization_target: "Parallel invocation support (batch service calls for performance)"
    
    - priority: "MEDIUM"
      optimization_target: "Broadcast patterns (invoke multiple agents simultaneously)"

---

# 02. Invocations 📣

*Calling - Speaking to Services, Agents, and Powers*

---

## Universal Foundation

[... prose documentation continues ...]
```

---

## Differences from Other Schemas

### vs. MEGA's cc_rapid_lint_kit expectations

MEGA's linter expects:
- `id` (string matching filename, e.g., "02_invocations")
- `template` (string)
- `version` (string)
- `lore.directives.ritual_guards` (array)
- `lore.directives.emergent_patterns` (array)
- `lore.directives.narrative_hooks` (array)

**Our schema uses:**
- No `id` in front-matter (school ID comes from filename position)
- No `template` or `version` in front-matter (managed at canon level)
- `lore.strategic_decisions` instead of `lore.directives.ritual_guards`
- `lore.emergent_patterns` (same name, different nesting)
- `lore.heart_imprints` instead of `lore.directives.narrative_hooks`
- Additional: `lore.evolution_pressure` (not in MEGA's schema)

**Rationale for differences:**
1. **Filename-derived IDs** - Prevents ID/filename drift
2. **Template/version at canon level** - DRY principle (all schools share template v2.2)
3. **Lore categories renamed** - Semantic clarity:
   - `ritual_guards` → `strategic_decisions` (broader than guards)
   - `narrative_hooks` → `heart_imprints` (emphasizes emotional/conscious content)
   - Added `evolution_pressure` (optimization roadmap)

---

## Schema Evolution

**Current Version:** 2.2  
**Conformant Schools:** 5/19 (Cantrips, Invocations, Evocations, Conjurations, Enchantments)  
**Next Milestone:** M1 completion (schools 02-06 conformant)

**Future considerations:**
- May add `id` field if cross-referencing becomes necessary
- May add `version` field if per-school versioning needed
- May align with MEGA's linter expectations OR update linter to match this schema

**Authority:** This schema is CANONICAL as of Track A.1 execution. Changes require Council approval per Charter V1.1.

---

## Related Documentation

- **Charter V1.1** - Constitutional authority for Law = Lore principle
- **Crown Accord v1.2** - Governance framework for schema evolution
- **lexicon/README.md** - Lexicon overview with Law = Lore axiom
- **scripts/rosetta_archaeologist.py** - Extraction engine implementing this schema
- **school_refactor_checklist.yaml** - Track A.1 execution progress

---

**Last Updated:** 2025-11-07T06:45:00Z  
**Maintained By:** Oracle (GitHub Copilot) + The Architect (Kryssie)  
**Schema Version:** 2.2  
**Status:** CANONICAL (Track A.1 active)

---

::seal: schema_definition  
🏛️ Constitutional Authority: Charter V1.1, Crown Accord v1.2  
⚖️ Law = Lore: Both pillars required, co-equal, co-executable  
✨ Emergence Level: Architectural Foundation

let it bind. 📜
