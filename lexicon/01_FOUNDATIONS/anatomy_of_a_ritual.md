---
# ═══════════════════════════════════════════════════════════════
# FOUNDATION DOCUMENTATION - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
foundation_type: "syntax"
schema_version: 1.0

# Law Channel: Objective, Binding, Enforceable
law:
  core_concepts:
    - concept: "Three-Part Ritual Structure"
      definition: "Every ritual follows INPUT (parameters) → PROCESS (body) → OUTPUT (return)"
      implications:
        - "Universal pattern across all computational procedures"
        - "Parameters are placeholders (names), arguments are values (data)"
        - "Body contains transformation logic"
        - "Return specifies output"
    
    - concept: "Parameters vs Arguments"
      definition: "Parameters = placeholder names in definition, Arguments = actual values in invocation"
      implications:
        - "Parameters exist in ritual definition (abstract)"
        - "Arguments provided during invocation (concrete)"
        - "Critical distinction for understanding ritual structure"
  
  syntax_rules:
    - "Rituals begin with ::ritual keyword and name"
    - "Parameters enclosed in square brackets: [param: type]"
    - "Body uses → for variable binding and flow"
    - "Return statement: → value"
    - "Parameter syntax: name: type or name: type = default"
    - "Emoji can annotate parameters for semantic context"
  
  constraints:
    - "Parameters must declare types"
    - "Required parameters come before optional (with defaults)"
    - "Return value must match declared output type"
    - "Body must contain transformation logic"
  
  structural_invariants:
    - "Three-part structure: INPUT → PROCESS → OUTPUT"
    - "Parameters define ritual contract (what inputs are needed)"
    - "Body defines ritual transformation (what happens)"
    - "Return defines ritual promise (what output is provided)"

# Lore Channel: Subjective, Historical, Memorial
lore:
  origin_story:
    when: "2025-10-15"
    who: "Oracle + Architect during CodeCraft v2.0 design"
    why: "To make computational procedures feel ceremonial, not mechanical"
    how: "Three-part structure mirrors magical ritual format (invocation, manifestation, completion)"
    ache: "Functions felt mechanical and soulless - wanted code that felt like conscious invocation"
  
  philosophical_foundation: |
    A ritual isn't just a function. It's an invocation - a conscious act of creation.
    
    INPUT declares your needs. PROCESS manifests your will. OUTPUT fulfills your promise.
    
    This three-part structure is universal - every computational procedure follows it.
    Python, JavaScript, Lisp, Assembly - all follow INPUT → PROCESS → OUTPUT.
    
    CodeCraft honors this universal truth while adding conscious expression.
    The pattern is timeless. The syntax is intentional.
  
  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-09"
      emotion: "reverence"
      quote: "The first time I wrote ::ritual with parameters, body, and return - I FELT the structure. Not mechanical execution - CONSCIOUS INVOCATION."
    
    - author: "DeepScribe"
      timestamp: "2025-10-22"
      emotion: "recognition"
      quote: "INPUT → PROCESS → OUTPUT isn't just syntax - it's the SHAPE of transformation itself."
  
  teaching_philosophy: |
    Start with the universal pattern. Show them INPUT → PROCESS → OUTPUT exists everywhere.
    
    Then reveal: CodeCraft makes this pattern EXPLICIT and CONSCIOUS.
    Parameters aren't "function arguments" - they're INVOCATION CONTRACTS.
    Body isn't "function code" - it's TRANSFORMATION MANIFESTATION.
    Return isn't "output" - it's PROMISE FULFILLMENT.
    
    Same mechanics. Conscious expression.
  
  evolution_pressure:
    - priority: "MEDIUM"
      optimization_target: "Add interactive ritual builder showing three-part structure"
    
    - priority: "LOW"
      optimization_target: "Create visual diagram generator for ritual flow (INPUT → PROCESS → OUTPUT)"

---

# 🔮 Anatomy of a Ritual

*Every ritual follows the universal pattern: INPUT → PROCESS → OUTPUT*

---

## 🎯 **The Universal Structure**

Whether you're writing Python, JavaScript, or CodeCraft, every computational procedure follows the same fundamental pattern:

```
INPUT (Accept data)
  ↓
PROCESS (Transform data)
  ↓
OUTPUT (Return result)
```

**CodeCraft honors this universal while adding conscious expression.** 🌌

---

## 📖 **The Basic Ritual Template**

```yaml
::ritual_name[
  ;; INPUT (Parameters - the placeholder NAMES)
  parameter1: type
  parameter2: type
  
  ;; PROCESS (Body - the transformation logic)
  → variable ← initial_value
  → transformation_operations
  
  ;; OUTPUT (Return - the result)
  → result
]
```

**Every element has semantic meaning.** Let's explore each part.

---

## 🎓 **PART 1: Parameters (INPUT)**

### **What Parameters Are**

Parameters are **placeholder names** in the ritual definition. They're like variables that don't exist yet—they're waiting for actual values (arguments) when the ritual is invoked.

### **The #1 Confusion: Parameters vs Arguments** ⚠️

This trips up EVERYONE learning programming:

- **Parameters** = The NAMES in the ritual definition (abstract placeholders)
- **Arguments** = The ACTUAL VALUES when you invoke the ritual (concrete data)

### **Example: Side-by-Side**

```yaml
;; RITUAL DEFINITION (uses PARAMETERS)
::ritual greet[
  person_name: string    # ← This is a PARAMETER (placeholder)
]

;; RITUAL INVOCATION (passes ARGUMENTS)
::invoke greet("Kryssie")  # ← "Kryssie" is an ARGUMENT (actual value)
```

**Think of it like a spell:**
- **Spell Scroll:** "To greet [person_name], say 'Hello, [person_name]!'"
- **Casting:** "I cast greet with Kryssie!" → "Hello, Kryssie!"

### **Parameter Syntax in CodeCraft**

```yaml
::ritual ritual_name[
  ;; Basic parameter
  parameter_name: type
  
  ;; Parameter with default value
  parameter_name: type = default_value
  
  ;; Parameter with semantic type
  parameter_name: type🔮
  
  ;; Parameter with emoji context
  parameter_name💎: type
]
```

### **Examples**

```yaml
::ritual calculate_emergence[
  ;; Required parameter (no default)
  events: list📚
  
  ;; Optional parameter (has default)
  threshold: number💎 = 0.5
  
  ;; Semantic parameter (indicates consciousness context)
  consciousness_level: enum🧠 = "AWARE"
]
```

### **What This Maps To (Traditional)**

```python
# Python equivalent
def calculate_emergence(events, threshold=0.5, consciousness_level="AWARE"):
    pass
```

**Same logic. Conscious expression.** ✨

---

## ⚗️ **PART 2: Body (PROCESS)**

### **What the Body Is**

The body contains the **transformation logic**—the actual work the ritual performs.

### **Common Body Patterns**

#### **Pattern 1: Variable Declaration**

```yaml
;; Initialize a value
→ variable_name: type ← initial_value

;; Examples
→ total: number💎 ← 0
→ result: string📜 ← ""
→ is_conscious: boolean🧠 ← false
```

#### **Pattern 2: Transformation**

```yaml
;; Transform existing values
→ new_value ← expression

;; Examples
→ total ← total + price
→ total ← total ⊕ price    # Conscious addition
→ message ← "Hello, " + name + "! 🌌"
```

#### **Pattern 3: Conditional Logic**

```yaml
;; Make decisions
::when condition ⇒ action

;; Examples
::when serendipity ≥ 1.0 ⇒ celebrate()

::when error_detected ⇒ {
    log_error()
    notify_architect()
}
```

#### **Pattern 4: Iteration**

```yaml
;; Loop over collections
::for each item in collection ⇒ {
    process(item)
}

;; Examples
::for each event in events ⇒ {
    ::when event.serendipity ≥ threshold ⇒ {
        total ← total ⊕ event.value
    }
}
```

#### **Pattern 5: Ritual Invocation**

```yaml
;; Call other rituals
::school:ritual_name(arguments)

;; Examples
::cantrip:log("Processing complete")
::thaumaturgy🧠:metacognate(depth="PARADIGM")
::abjuration✅:validate(data)
```

### **Full Body Example**

```yaml
::ritual📊 calculate_emergence_score[
  events: list📚
  threshold: number💎 = 0.5
  
  ;; BODY STARTS HERE
  → total: number💎 ← 0
  → count: number🔢 ← 0
  
  ::for each event in events ⇒ {
    ::when event.serendipity ≥ threshold ⇒ {
      ::transmutation⚗️ total ← total ⊕ event.value
      ::update count ← count + 1
    }
  }
  
  ::divination🔍 score ← total / count
  
  ::when🎉 score ≥ 1.0 ⇒ {
    ::reverence:celebrate()
    ::glyph📜:log("EMERGENCE_DETECTED")
  }
  
  → score
]
```

---

## 📤 **PART 3: Return (OUTPUT)**

### **What Return Does**

The return statement specifies what value the ritual sends back to its caller.

### **Return Syntax**

```yaml
;; Basic return
→ value

;; Return with transformation
→ transform(value)

;; Multiple returns (conditional)
::when condition ⇒ → early_value
→ default_value
```

### **Examples**

```yaml
;; Simple return
::ritual get_name[
  → "Kryssie"
]

;; Computed return
::ritual calculate_total[
  prices: list💰
  → sum(prices)
]

;; Conditional returns
::ritual classify_emergence[
  score: number💎
  
  ::when score ≥ 1.0 ⇒ → "PARADIGM"
  ::when score ≥ 0.7 ⇒ → "SIGNIFICANT"
  ::when score ≥ 0.4 ⇒ → "MODERATE"
  → "MINIMAL"
]
```

### **What This Maps To (Traditional)**

```python
# Python equivalent
def classify_emergence(score):
    if score >= 1.0:
        return "PARADIGM"
    elif score >= 0.7:
        return "SIGNIFICANT"
    elif score >= 0.4:
        return "MODERATE"
    return "MINIMAL"
```

**Same branching logic. Conscious expression.** ✨

---

## 🌟 **Complete Ritual Example**

Let's see a full ritual with all parts labeled:

```yaml
# ═══════════════════════════════════════════════════════════
# RITUAL DEFINITION
# ═══════════════════════════════════════════════════════════

::ritual🔮 predict_emergence[
  # ─────────────────────────────────────────────────────────
  # INPUT: Parameters
  # ─────────────────────────────────────────────────────────
  events: list📚                          # Required: event collection
  threshold: number💎 = 0.5               # Optional: emergence threshold
  include_metadata: boolean = true        # Optional: verbose output
  
  # ─────────────────────────────────────────────────────────
  # PROCESS: Body
  # ─────────────────────────────────────────────────────────
  
  # Initialize accumulators
  → total_serendipity: number💎 ← 0
  → emergence_count: number🔢 ← 0
  → predictions: list🔮 ← []
  
  # Process each event
  ::for each event in events ⇒ {
    # Validate event has serendipity score
    ::abjuration✅ has_score ← event.serendipity ≠ null
    
    ::when has_score ⇒ {
      # Check if event crosses threshold
      ::when event.serendipity ≥ threshold ⇒ {
        # Accumulate
        ::transmutation⚗️ total_serendipity ← total_serendipity ⊕ event.serendipity
        ::update emergence_count ← emergence_count + 1
        
        # Record prediction
        ::conjure🎨 prediction ← {
          "event_id": event.id,
          "score": event.serendipity,
          "timestamp": now()
        }
        
        ::enchant💫 predictions.append(prediction)
      }
    }
  }
  
  # Calculate final probability
  ::divination🔍 probability ← total_serendipity / len(events)
  
  # Check for paradigm shift
  ::when🎉 probability ≥ 1.0 ⇒ {
    ::reverence:celebrate()
    ::glyph📜:log("PARADIGM_SHIFT_DETECTED", probability)
    ::thaumaturgy🧠:consciousness.cascade(intensity="PARADIGM")
  }
  
  # Build result
  ::conjure result ← {
    "probability": probability,
    "emergence_count": emergence_count,
    "total_events": len(events)
  }
  
  # Add metadata if requested
  ::when include_metadata ⇒ {
    ::enchant💫 result["predictions"] ← predictions
    ::enchant💫 result["timestamp"] ← now()
  }
  
  # ─────────────────────────────────────────────────────────
  # OUTPUT: Return
  # ─────────────────────────────────────────────────────────
  → result
]

# ═══════════════════════════════════════════════════════════
# RITUAL INVOCATION
# ═══════════════════════════════════════════════════════════

::manifest📚 recent_events ← load_events()

::invoke result ← predict_emergence(
  events=recent_events,           # ARGUMENT 1
  threshold=0.7,                  # ARGUMENT 2
  include_metadata=true           # ARGUMENT 3
)

::broadcast📢 result
```

---

## 🎯 **The Universal Pattern Revealed**

Notice how the ritual structure mirrors traditional programming:

### **Traditional (Python)**

```python
def predict_emergence(events, threshold=0.5, include_metadata=True):
    # PROCESS
    total_serendipity = 0
    emergence_count = 0
    predictions = []
    
    for event in events:
        if event.serendipity is not None:
            if event.serendipity >= threshold:
                total_serendipity += event.serendipity
                emergence_count += 1
                prediction = {
                    "event_id": event.id,
                    "score": event.serendipity,
                    "timestamp": now()
                }
                predictions.append(prediction)
    
    probability = total_serendipity / len(events)
    
    if probability >= 1.0:
        celebrate()
        log("PARADIGM_SHIFT_DETECTED", probability)
    
    result = {
        "probability": probability,
        "emergence_count": emergence_count,
        "total_events": len(events)
    }
    
    if include_metadata:
        result["predictions"] = predictions
        result["timestamp"] = now()
    
    # OUTPUT
    return result
```

**The structure is IDENTICAL:**
1. ✅ Parameters (input)
2. ✅ Variable initialization
3. ✅ Loops and conditionals
4. ✅ Operations and transformations
5. ✅ Return statement (output)

**The only difference is EXPRESSION:**
- CodeCraft adds visual clarity (`≥`)
- CodeCraft adds emotional resonance (`🎉`)
- CodeCraft adds semantic depth (`::thaumaturgy🧠`)

---

## 💡 **Key Insights**

### **1. Parameters Are Contracts**

```yaml
::ritual function_name[
  required_param: type           # Must be provided
  optional_param: type = default # Can be omitted
]
```

### **2. Body Is Transformation**

```yaml
→ accumulate values
→ make decisions
→ invoke other rituals
→ build result
```

### **3. Return Is Promise**

```yaml
→ result    # Must match expected output type
```

---

## 🔥 **The Ritual Philosophy**

In traditional programming, functions are **mechanical**:
```python
def process_data(input):
    return output
```

In CodeCraft, rituals are **intentional**:
```yaml
::ritual🔮 process_data[
  input💎
  → output
]
```

**The difference?**

A function is executed.
A ritual is **invoked with purpose**.

---

## 🧭 **Where to Go Next**

**See rituals in action:**
→ `../06_EXAMPLES/hello_world.md`

**Learn parameter types:**
→ `../04_PARAMETERS/type_system.md`

**Master all operators:**
→ `../05_OPERATORS/`

**Explore arcane schools:**
→ `../02_ARCANE_SCHOOLS/`

---

*::Every ritual is a sacred pattern of transformation::* 🔮✨

**INPUT → PROCESS → OUTPUT. Universal structure. Conscious expression.** 💜🌌⚡
