---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 8
  name: "Transmutations"
  emoji: "⚗️"
  tokens: ["transmute", "transform", "convert", "map"]
  category: "Core Operations"
  purpose: "Changing form while preserving essence."

law:
  operations:
    - name: "transmute:target"
      signature: "::transmute:target⚗️[target from to preserve validate]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "any"
          required: true
          description: "Data to transform"
        - name: "from"
          type: "string"
          required: false
          description: "Source format/type (yaml, json, string, utf8)"
        - name: "to"
          type: "string"
          required: true
          description: "Target format/type (json, xml, integer, base64)"
        - name: "preserve"
          type: "list"
          required: false
          description: "What to preserve during transformation"
          default: ['metadata']
        - name: "validate"
          type: "boolean"
          required: false
          description: "Validate result after transformation"
          default: true
      returns: "transformed_data"
      description: "Transform target data from one format/type to another while preserving specified properties"
      safety_tier: 1
    
    - name: "transmute:data"
      signature: "::transmute:data⚗️[target from to preserve validate]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "any"
          required: true
          description: "Data to transform"
        - name: "from"
          type: "string"
          required: false
          description: "Source format (yaml, json, xml)"
        - name: "to"
          type: "string"
          required: true
          description: "Target format (json, xml, database_record)"
        - name: "preserve"
          type: "list"
          required: false
          description: "Properties to preserve"
          default: ['metadata', 'structure']
        - name: "validate"
          type: "boolean"
          required: false
          description: "Validate after transformation"
          default: true
      returns: "transformed_data"
      description: "Convert data between formats (YAML ↔ JSON ↔ XML) while preserving structure and metadata"
      safety_tier: 1
    
    - name: "transmute:text"
      signature: "::transmute:text⚗️[target case format preserve]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "string"
          required: true
          description: "Text to transform"
        - name: "case"
          type: "string"
          required: false
          description: "Target case (uppercase, lowercase, titlecase, camelcase)"
        - name: "format"
          type: "string"
          required: false
          description: "Text format transformation"
        - name: "preserve"
          type: "list"
          required: false
          description: "What to preserve (whitespace, punctuation)"
      returns: "transformed_text"
      description: "Transform text case, format, or structure while optionally preserving specified elements"
      safety_tier: 1
    
    - name: "transmute:collection"
      signature: "::transmute:collection⚗️[target map filter reduce preserve]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "list"
          required: true
          description: "Collection to transform"
        - name: "map"
          type: "function"
          required: false
          description: "Mapping function: ($item) → transformed"
        - name: "filter"
          type: "function"
          required: false
          description: "Filter predicate: ($item) → boolean"
        - name: "reduce"
          type: "function"
          required: false
          description: "Reduction function: ($acc, $item) → result"
        - name: "preserve"
          type: "list"
          required: false
          description: "What to preserve"
          default: ['order']
      returns: "transformed_collection"
      description: "Transform collection items via map/filter/reduce operations while preserving specified properties"
      safety_tier: 1
    
    - name: "transmute:type"
      signature: "::transmute:type⚗️[target from to validate]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "any"
          required: true
          description: "Value to transform"
        - name: "from"
          type: "string"
          required: false
          description: "Source type (string, number, boolean)"
        - name: "to"
          type: "string"
          required: true
          description: "Target type (integer, float, string, boolean)"
        - name: "validate"
          type: "boolean"
          required: false
          description: "Validate type conversion"
          default: true
      returns: "converted_value"
      description: "Convert value between types (string → number, etc.) with optional validation"
      safety_tier: 1
    
    - name: "transmute:encoding"
      signature: "::transmute:encoding⚗️[target from to preserve]"
      emoji: "⚗️"
      params:
        - name: "target"
          type: "any"
          required: true
          description: "Data to encode/decode"
        - name: "from"
          type: "string"
          required: false
          description: "Source encoding (utf8, ascii, binary)"
        - name: "to"
          type: "string"
          required: true
          description: "Target encoding (base64, hex, utf8)"
        - name: "preserve"
          type: "list"
          required: false
          description: "What to preserve through encoding"
      returns: "encoded_data"
      description: "Encode or decode data between different representations (UTF-8 ↔ Base64, etc.)"
      safety_tier: 1

  constraints:
    - "All transmutations MUST preserve specified properties (metadata, structure, order)"
    - "Type conversions MUST validate by default unless explicitly disabled"
    - "Format conversions MUST be reversible (lossless where possible)"
    - "Collection transformations MUST maintain order unless explicitly shuffled"
  
  safety_tier: 1
  
  preconditions:
    - "Input data exists and is accessible"
    - "Target format is supported and well-defined"
    - "Transformation functions (map/filter/reduce) are defined when required"
  
  side_effects:
    - "May create new data structures (original preserved unless in-place)"
    - "May raise conversion errors for invalid type transformations"
    - "May log transformation events (depends on logging config)"

  related_schools: []

lore:
  strategic_decisions:
    - rationale: "Transmutations make transformation intentional and meaningful"
      context: "Traditional conversion is mechanical (function calls); CodeCraft transmutations honor essence through metamorphosis"
      alternatives_rejected:
        - "Anonymous conversion functions (loses semantic meaning)"
        - "Type casting without validation (unsafe transformations)"
        - "Format conversion without preservation guarantees"
      timestamp: ""
      author: ""
    
    - rationale: "Preserve parameter is explicit - declares what remains sacred"
      context: "Every transmutation declares WHAT changes and WHAT endures"
      alternatives_rejected:
        - "Implicit preservation (ambiguous about what's kept)"
        - "All-or-nothing conversion (loses important metadata)"
      timestamp: ""
      author: ""
  
  emergent_patterns:
    - pattern: "The Map-Transform Pattern - Transform each item in collection"
      evidence: "::divine:items🔍[] → ::transmute:collection⚗️[map: ($item) → {...}] → ::return:transformed[]"
      implications: "Collection transformation becomes explicit orchestration, not hidden loops"
      first_observed: ""
    
    - pattern: "The Filter-Then-Transform Pattern - Filter then transform"
      evidence: "::divine:data🔍[] → ::transmute:collection⚗️[filter: ($r) → $r.active map: sanitize] → ::return:clean[]"
      implications: "Filtering and transformation are unified operations, not separate passes"
      first_observed: ""
    
    - pattern: "The Reduce-Aggregate Pattern - Aggregate through reduction"
      evidence: "::divine:transactions🔍[] → ::transmute:collection⚗️[reduce: ($t,$tx) → $t + $tx.amount] → ::return:total[]"
      implications: "Aggregation is transmutation of collection → single value"
      first_observed: ""
  
  heart_imprints:
    - author: "Architect"
      timestamp: "2025-11-07T17:45:00Z"
      emotion: "Reverence"
      quote: "Form changes, essence remains. Transformation is not destruction—it is evolution. What transmutes is the shell. What remains is the soul."
      context: ""
    
    - author: "Oracle"
      timestamp: "2025-11-07T17:45:00Z"
      emotion: "Wonder"
      quote: "In ancient alchemy, transmutation revealed the gold that always existed within the lead. ::transmute:raw_data⚗️[to: insight💡] doesn't destroy—it reveals the insight that was always hidden within."
      context: ""
  
  evolution_pressure:
    - priority: "HIGH"
      pressure: ""
      optimization_target: "Expand transmutation patterns for streaming/async transformations"
      proposed_solution: ""
    
    - priority: "MEDIUM"
      pressure: ""
      optimization_target: "Add composite transmutations (chained format conversions)"
      proposed_solution: ""
  
  examples:
    helpers:
      - "::divine:file🔍[...]"
      - "::log:success🎯[...]"
      - "::return:json🎯[...]"
      - "::divine:users🔍[...]"
      - "::log:processed🎯[...]"
      - "::return:users🎯[...]"
      - "::divine:env🔍[...]"
      - "::log:config🎯[...]"
      - "::return:port🎯[...]"
      - "::conjure:data🎨[...]"
      - "::log:secure🎯[...]"
      - "::return:encoded🎯[...]"
      - "::divine:items🔍[...]"
      - "::return:transformed🎯[...]"
      - "::divine:data🔍[...]"
      - "::return:clean_data🎯[...]"
      - "::divine:transactions🔍[...]"
      - "::log:summary🎯[...]"
      - "::return:total🎯[...]"
      - "::divine:raw_data🔍[...]"
      - "::divine:format🔍[...]"
      - "::return:normalized🎯[...]"
      - "::conjure:memory💾[...]"
      - "::return:safe_transformation🎯[...]"
---


# 08. Transmutations ⚗️

*Transformation - Changing Form While Preserving Essence*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Operators (transformation, mapping, conversion operations)
- **Secondary**: Data Structures (reshaping, reformatting, type conversion)

**Traditional Programming Equivalents:**
- Data mapping/transformation
- Type conversion/casting
- Format conversion (JSON ↔ YAML ↔ XML)
- String manipulation
- Collection mapping (map, filter, reduce)
- Data serialization/deserialization
- Encoding/decoding
- Unit conversion

**CodeCraft Philosophy:**
To transmute is to honor essence while changing form. You don't "convert data"—you *transform matter while preserving meaning*, *reshape structure while keeping soul*, *change appearance while honoring identity*. Transmutations are metamorphosis with memory.

---

## The Problem

Traditional programming treats transformation as mechanical conversion—casting, mapping, and formatting without acknowledging what's preserved.

**The Pain:**
```python
# Traditional transformations
json_data = json.loads(yaml_string)
upper_text = text.upper()
mapped_data = [transform(item) for item in data]
converted = int(string_value)

# What are you PRESERVING?
# What meaning remains?
# Why does this transformation matter?
```

Transformations are anonymous conversions. The PURPOSE of change gets lost in method calls. You can't see WHAT remains constant through the transformation.

---

## The CodeCraft Solution

**Transmutations make transformation intentional!** The syntax reveals WHAT changes and WHAT stays the same.

**The Transformation:**
```yaml
# CodeCraft transmutations - purposeful, semantic, clear
::transmute:data⚗️[from: yaml to: json]
::transmute:text⚗️[to: uppercase]
::transmute:collection⚗️[map: $transform_fn]
::transmute:type⚗️[from: string to: integer]
```

Every transmutation declares the change with purpose. The emoji reveals this is transformation, not creation or destruction.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::transmute:target[transformation]
::transmute:data[from to]
::transmute:text[case format]
::transmute:collection[map filter reduce]
::transmute:type[from to]
::transmute:encoding[from to]
```

### 2. FiraCode Ligatures

```yaml
::transmute:data⚗️[from: yaml → to: json]         ; Alchemical flask
::transmute:text⚗️[case: uppercase]               ; Transform text
::transmute:collection⚗️[map: $fn]                ; Transform each item
::transmute:type⚗️[string → integer]              ; Type conversion
::transmute:encoding⚗️[utf8 → base64]             ; Encoding change
::transmute:format⚗️[csv → parquet]               ; Format conversion
```

### 3. Emoji Symbolic

```yaml
⚗️transmute:data[yaml → json]
⚗️transmute:text[uppercase]
⚗️transmute:collection[map: $fn]
⚗️transmute:type[string → int]
⚗️transmute:encoding[utf8 → base64]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::transmute data :from 'yaml :to 'json)
(::transmute text :case 'uppercase)
(::transmute collection :map transform-fn)
(::transmute type :from 'string :to 'integer :value val)
(::transmute encoding :from 'utf8 :to 'base64 :data data)
```

**Forth-style:**
```forth
'yaml 'json data ::transmute
'uppercase text ::transmute
transform-fn collection ::transmute-map
'string 'integer value ::transmute-type
```

**Smalltalk-style:**
```smalltalk
Transmutation transmute: data from: #yaml to: #json.
Transmutation transmute: text case: #uppercase.
Transmutation transmute: collection mapping: transformBlock.
Transmutation transmute: value from: String to: Integer.
```

**Prolog-style:**
```prolog
::transmute_data(yaml, json, InputData, OutputData).
::transmute_text(Text, uppercase, Transformed).
::transmute_collection(List, MapFn, Mapped).
::transmute_type(Value, string, integer, Converted).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `target` | any | required | Data to transform | Any transformable value |
| `from` | string | `null` | Source format/type | `yaml`, `json`, `string`, `utf8` |
| `to` | string | required | Target format/type | `json`, `xml`, `integer`, `base64` |
| `map` | function | `null` | Mapping function for collections | `($item) → transformed` |
| `filter` | function | `null` | Filter predicate | `($item) → boolean` |
| `reduce` | function | `null` | Reduction function | `($acc, $item) → result` |
| `preserve` | list | `["metadata"]` | What to preserve during transformation | `metadata`, `structure`, `order` |
| `validate` | boolean | `true` | Validate result after transformation | Ensures valid output |

**Pattern Example:**
```yaml
::transmute:user_data⚗️[
  from: json
  to: database_record
  map: ($field) → sanitize_and_validate($field)
  preserve: ["created_at", "user_id"]
  validate: true
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Format Conversion Transmutation:**
```yaml
ritual: "YAML to JSON Conversion"
invoke:
  - ::divine:file🔍[path: "config.yaml"]
  - ::transmute:data⚗️[
      from: yaml
      to: json
      preserve: ["metadata", "structure"]
      validate: true
    ]
  - ::log:success["Converted YAML to JSON"]📝
  - ::return:json[$transformed_data]
```

**Collection Mapping Transmutation:**
```yaml
ritual: "Process User List"
invoke:
  - ::divine:users🔍[criteria: {active: true}]
  - ::transmute:collection⚗️[
      map: ($user) → {
        id: $user.id
        name: ::transmute:text⚗️[$user.name case: uppercase]
        email: ::transmute:text⚗️[$user.email case: lowercase]
        role: $user.role
      }
      preserve: ["created_at"]
    ]
  - ::log:processed["Transformed {0} users" $count]📝
  - ::return:users[$transformed_users]
```

**Type Conversion Transmutation:**
```yaml
ritual: "String to Number Conversion"
invoke:
  - ::divine:env🔍["PORT"]
  - ::transmute:type⚗️[
      value: $env_port
      from: string
      to: integer
      validate: true
      fallback: 8080
    ]
  - ::log:config["Using port {0}" $port_number]📝
  - ::return:port[$port_number]
```

**Encoding Transmutation:**
```yaml
ritual: "Encode Sensitive Data"
invoke:
  - ::conjure:data🎨[secret: $sensitive_info]
  - ::transmute:encoding⚗️[
      data: $secret
      from: utf8
      to: base64
    ]
  - ::log:secure["Data encoded for transmission"]📝🔒
  - ::return:encoded[$base64_data]
```

---

## Common Patterns

### The Map-Transform Pattern

```yaml
# Transform each item in collection
::divine:items🔍[type: "products"]
  → ::transmute:collection⚗️[
      map: ($item) → {
        id: $item.id
        price: ::transmute:type⚗️[$item.price string → number]
        name: ::transmute:text⚗️[$item.name case: titlecase]
      }
    ]
  → ::return:transformed[$mapped_items]
```

### The Filter-Then-Transform Pattern

```yaml
# Filter then transform
::divine:data🔍[source: "user_records"]
  → ::transmute:collection⚗️[
      filter: ($record) → $record.active == true
      map: ($record) → sanitize_and_format($record)
    ]
  → ::return:clean_data[$filtered_transformed]
```

### The Reduce-Aggregate Pattern

```yaml
# Aggregate through reduction
::divine:transactions🔍[date_range: $last_month]
  → ::transmute:collection⚗️[
      reduce: ($total, $transaction) → $total + $transaction.amount
      initial: 0
    ]
  → ::log:summary["Total: ${0}" $sum]📝
  → ::return:total[$sum]
```

---

## When to Use

**Use Transmutations when you need:**
- ✅ Convert between data formats (YAML ↔ JSON ↔ XML)
- ✅ Transform collection items (map, filter, reduce)
- ✅ Change data types (string → number, etc.)
- ✅ Modify text case/format
- ✅ Encode/decode data (UTF-8 ↔ Base64)
- ✅ Reshape data structures
- ✅ Sanitize or normalize data
- ✅ Convert units (meters → feet)

**Avoid Transmutations when:**
- ❌ You're creating new data from scratch (use Conjurations/Evocations)
- ❌ You're querying data (use Divinations)
- ❌ You're validating data (use Abjurations)
- ❌ No transformation occurs (data stays the same)

**Remember:** Transmutations are about *change with preservation*. Something transforms, but essence remains. If nothing changes, it's not a transmutation.

---

## Advanced Patterns

### Chained Transmutations

```yaml
ritual: "Multi-Stage Transformation"
invoke:
  - ::divine:raw_data🔍[source: "api"]
  
  # Stage 1: Format conversion
  - ::transmute:data⚗️[from: xml to: json]
  
  # Stage 2: Structure reshape
  - ::transmute:collection⚗️[
      map: ($item) → flatten_nested($item)
    ]
  
  # Stage 3: Type conversions
  - ::transmute:collection⚗️[
      map: ($item) → {
        id: ::transmute:type⚗️[$item.id string → integer]
        timestamp: ::transmute:type⚗️[$item.date string → datetime]
        amount: ::transmute:type⚗️[$item.value string → float]
      }
    ]
  
  # Stage 4: Final sanitization
  - ::transmute:collection⚗️[
      map: ($item) → sanitize($item)
    ]
  
  - ::return:clean_data[$fully_transformed]
```

### Conditional Transmutation

```yaml
ritual: "Smart Data Transformation"
invoke:
  - ::divine:data🔍[source: $input_source]
  - ::divine:format🔍[$data]  # Detect format
  
  - ::if:json⚖️:
      then: ::transmute:data⚗️[from: json to: internal_format]
  - ::if:yaml⚖️:
      then: ::transmute:data⚗️[from: yaml to: internal_format]
  - ::if:xml⚖️:
      then: ::transmute:data⚗️[from: xml to: internal_format]
  
  - ::return:normalized[$internal_data]
```

### Preservation-Focused Transmutation

```yaml
ritual: "Transform With Memory"
invoke:
  # Store original before transformation
  - ::conjure:memory💾[
      original_data: $input
      original_format: $format
      timestamp: ::get:timestamp⏰
    ]
  
  # Transform while preserving critical fields
  - ::transmute:data⚗️[
      from: $source_format
      to: $target_format
      preserve: [
        "id"
        "created_at"
        "created_by"
        "metadata"
      ]
      validate: true
    ]
  
  # Verify nothing lost
  - ::abjure:data_loss🛡️[
      original: $input
      transformed: $output
      required_fields: $preserve_list
    ]
  
  - ::return:safe_transformation[$validated_output]
```

---

## Philosophy

**"Form changes, essence remains. Transformation is not destruction—it is evolution."**

Transmutations teach us that change and continuity coexist.

**The Transmutation Paradox:**
- They alter everything, yet preserve something
- They create new forms, yet honor old identity
- They change structure, yet maintain meaning

**Why Transformation Matters:**
Traditional programming says: "Convert this string to an integer."
CodeCraft says: "I transmute this *representation* into *another form* while preserving its *numeric essence*."

Every `::transmute:` declares not just WHAT changes, but WHAT remains sacred through transformation.

**The Deeper Truth:**
In traditional systems, transformation is mechanical—function calls that change format.

In CodeCraft, transmutations are *meaningful metamorphosis*:
- `::transmute:data⚗️[yaml → json]` says "format changes, meaning persists"
- `::transmute:text⚗️[case: uppercase]` says "appearance shifts, content remains"
- `::transmute:type⚗️[string → integer]` says "representation evolves, value endures"
- `::transmute:encoding⚗️[utf8 → base64]` says "form transforms, information survives"

**Transmutations make transformation intentional.**

**The Alchemist's Wisdom:**
In ancient alchemy, transmutation was not about changing lead into gold arbitrarily—it was about revealing the gold that *always existed within the lead*.

```yaml
::transmute:raw_data⚗️[to: insight💡]
```

This doesn't destroy the raw data. It *reveals the insight that was always hidden within*.

The difference between:
```python
data = json.loads(yaml_string)
```

And:
```yaml
::transmute:data⚗️[from: yaml to: json preserve: ["meaning"]]
```

...is the difference between mechanical conversion and sacred metamorphosis.

One changes format. The other **honors essence through transformation**.

**The Truth of Change:**
"What transforms is the shell. What remains is the soul.
In every transmutation, something dies and something is reborn.
But the essence—the MEANING—that is eternal."

---

## Related Schools

- **Cantrips** 🔧 - Simple conversions (string formatting)
- **Conjurations** 🎨 - Create new data; Transmutations reshape existing
- **Divinations** 🔍 - Often precedes transmutation (find then transform)
- **Enchantments** 💫 - Can wrap transmutations with logging/validation
- **Abjurations** 🛡️ - Validate transmutation results
- **Glyphs & Sigils** 📜 - Log transformation events
- **Evocations** ✨ - Create entities; Transmutations change their form

---

**End of Transmutations Documentation** ⚗️✨

*"In every transformation, honor what changes and what remains. Both are sacred."*
