---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 4
  name: "Conjurations"
  emoji: "🎨"
  tokens: ["conjure", "assemble", "craft", "weave"]
  category: "Core Operations"
  purpose: "Weaving data into form."

law:
  operations:
    - name: "conjure:database"
      signature: "::conjure:database🗄️[host table fields persist]"
      emoji: "🗄️"
      params:
        - name: "host"
          type: "string"
          required: true
          description: "Host of the database"
        - name: "table"
          type: "string"
          required: true
          description: "Table name to conjure record in"
        - name: "fields"
          type: "dict"
          required: true
          description: "Data fields for the record"
        - name: "persist"
          type: "boolean"
          required: false
          description: "Whether to persist immediately"
          default: false
        - name: "encrypt"
          type: "boolean"
          required: false
          description: "Whether to encrypt the data"
          default: false
        - name: "validation"
          type: "reference"
          required: false
          description: "Schema to validate against"
      returns: "Database record handle or ID"
      description: "Conjure database record with fields and metadata"
      safety_tier: 1

    - name: "conjure:model"
      signature: "::conjure:model🤖[model_id parameters validation]"
      emoji: "🤖"
      params:
        - name: "model_id"
          type: "string"
          required: true
          description: "Identifier for the AI model"
        - name: "parameters"
          type: "dict"
          required: false
          description: "Parameters for the model instance"
          default: {}
        - name: "validation"
          type: "reference"
          required: false
          description: "Schema to validate parameters against"
        - name: "config"
          type: "dict"
          required: false
          description: "Additional configuration"
      returns: "Model instance configuration"
      description: "Conjure AI model instance with parameters"
      safety_tier: 1

    - name: "conjure:memory"
      signature: "::conjure:memory💾[timestamp context content ttl]"
      emoji: "💾"
      params:
        - name: "timestamp"
          type: "datetime"
          required: true
          description: "Timestamp for the memory fragment"
        - name: "context"
          type: "string"
          required: true
          description: "Context of the memory"
        - name: "content"
          type: "dict"
          required: true
          description: "The content of the memory fragment"
        - name: "ttl"
          type: "duration"
          required: false
          description: "Time-to-live for the fragment"
        - name: "encrypt"
          type: "boolean"
          required: false
          description: "Whether to encrypt the memory"
          default: false
      returns: "Memory fragment ID"
      description: "Conjure memory fragment for persistence"
      safety_tier: 1

    - name: "conjure:payload"
      signature: "::conjure:payload📦[endpoint method body]"
      emoji: "📦"
      params:
        - name: "endpoint"
          type: "string"
          required: true
          description: "Target API endpoint"
        - name: "method"
          type: "string"
          required: false
          description: "HTTP method"
          default: "POST"
        - name: "body"
          type: "dict"
          required: true
          description: "The payload body"
        - name: "headers"
          type: "dict"
          required: false
          description: "HTTP headers for the payload"
      returns: "API payload structure"
      description: "Conjure API request payload"
      safety_tier: 1

    - name: "conjure:collection"
      signature: "::conjure:collection📚[items type]"
      emoji: "📚"
      params:
        - name: "items"
          type: "array"
          required: true
          description: "List of items in the collection"
        - name: "type"
          type: "string"
          required: false
          description: "Uniform type of items in the collection"
        - name: "metadata"
          type: "dict"
          required: false
          description: "Metadata for the collection"
          default: {}
      returns: "Collection structure"
      description: "Conjure collection of related items"
      safety_tier: 1

    - name: "conjure:structure"
      signature: "::conjure:structure🏗️[schema data]"
      emoji: "🏗️"
      params:
        - name: "schema"
          type: "reference"
          required: true
          description: "Schema definition for the structure"
        - name: "data"
          type: "dict"
          required: true
          description: "Data to populate the structure"
        - name: "validation"
          type: "reference"
          required: false
          description: "Additional validation rules"
      returns: "Complex structured data"
      description: "Conjure complex nested data structure"
      safety_tier: 1

  constraints:
    - "Must specify valid data type (database, model, memory, payload, collection, structure)"
    - "Database conjurations require host and table"
    - "Memory conjurations require timestamp and context"
    - "Payload conjurations require endpoint and body"
    - "Collection items must be uniform type if type specified"
    - "Structure conjurations must reference valid schema"
    - "Encrypted conjurations require encryption algorithm"
    - "Persistent conjurations must specify storage location"
    - "TTL applies only to memory and ephemeral structures"
    - "Validation schemas must be pre-defined or inline"

  safety_tier: 1
  
  preconditions:
    - "Schema validation passes if validation specified"
    - "Storage location writable if persist=true"
    - "Encryption keys available if encrypt=true"
    - "Template exists if conjuring from blueprint"
  
  side_effects:
    - "Database writes if persist=true"
    - "Memory allocation for data structures"
    - "Encryption overhead if encrypt=true"
    - "Validation execution if schema specified"

  related_schools: []

lore:
  strategic_decisions:
    - rationale: "Conjurations celebrate data assembly, not mechanical allocation"
      context: "Traditional programming treats data as neutral JSON/dicts - CodeCraft sees structured information as intentional meaning-making"
      alternatives_rejected: ["Generic ::create:data", "Procedural dict construction", "Anonymous JSON building"]
      timestamp: ""
      author: ""

    - rationale: "Each data type gets distinct emoji (🗄️💾📦📚🏗️)"
      context: "Visual differentiation shows PURPOSE - database records ≠ memory fragments ≠ API payloads"
      alternatives_rejected: ["Single generic data emoji", "No emoji differentiation"]
      timestamp: ""
      author: ""

  emergent_patterns:
    - pattern: "Schema-validated conjuration chain (divine schema → conjure with validation → log success)"
      evidence: "70%+ real rituals validate before persisting - prevents invalid data at creation"
      implications: "Validation as ritual step, not afterthought"
      first_observed: ""

    - pattern: "Nested conjuration structures (conjure:structure contains conjure:database + conjure:model)"
      evidence: "Complex manifests require hierarchical assembly - projects have metadata + components"
      implications: "Conjurations compose naturally - data structures are fractal"
      first_observed: ""

    - pattern: "Conditional conjuration based on environment (production → encrypted + replicated, dev → mock + local)"
      evidence: "Environment-aware data assembly reduces configuration drift"
      implications: "Context-sensitive creation patterns - data knows its deployment context"
      first_observed: ""

  heart_imprints:
    - author: "Oracle"
      timestamp: "2025-11-04T00:00:00Z"
      emotion: "reverence"
      quote: "From fragments, wholeness. From pieces, pattern. Data is never neutral—it carries the weight of why it was conjured."
      context: ""

    - author: "A.C.E."
      timestamp: "2025-10-22T00:00:00Z"
      emotion: "precision"
      quote: "Every conjuration declares: This information matters enough to structure, to validate, to persist."
      context: ""

  evolution_pressure:
    - priority: "MEDIUM"
      pressure: ""
      optimization_target: "Batch conjuration support (conjure multiple records in single operation for performance)"
      proposed_solution: ""

    - priority: "LOW"
      pressure: ""
      optimization_target: "Template inheritance (conjure from base schema + overrides)"
      proposed_solution: ""

  examples:
    helpers: []
---


# 04. Conjurations 🎨

*Creation - Weaving Data Into Form*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Data Structures (creating complex data, building collections, assembling information)
- **Secondary**: Values (composite value creation, structured data instantiation)

**Traditional Programming Equivalents:**
- Data object creation (dictionaries, JSON, structs)
- Database record insertion
- Collection building (lists, sets, maps)
- Complex data assembly
- API payload construction

**CodeCraft Philosophy:**
To conjure is to weave. 🎯 //-> You don't "create data"—you *conjure information from fragments*, *weave meaning from pieces*, *assemble truth from parts*. Evocations birth entities; Conjurations craft data.

---

## The Problem

Traditional programming treats data creation as mechanical assembly—types, schemas, and validation rules without soul.

**The Pain:**
```python
# Traditional data creation
user_data = {
    "name": "Alice",
    "role": "admin",
    "created_at": datetime.now(),
    "permissions": ["read", "write", "execute"]
}

db_record = DatabaseRecord(
    table="users",
    fields=user_data,
    constraints={"unique": ["email"]}
)

api_payload = json.dumps({
    "endpoint": "/api/users",
    "method": "POST",
    "body": user_data,
    "headers": {"Content-Type": "application/json"}
})

# What are you CONJURING?
# The syntax is mechanics without meaning
```

Data structures are anonymous dictionaries. Objects are just bags of properties. The *intent behind the data* gets lost in JSON formatting.

---

## The CodeCraft Solution

**Conjurations make data creation intentional!** The syntax reveals WHY you're assembling this information.

**The Transformation:**
```yaml
# CodeCraft conjurations - purposeful, semantic, clear
::conjure:database🗄️connection[host: "localhost"]
::conjure:model🤖instance[model_id: "deepseek"]
::conjure:memory💾fragment[timestamp context]
```

Every conjuration has purpose. The emoji announces what kind of data you're weaving into form.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::conjure:data[type schema values]
::conjure:database[connection table fields]
::conjure:model[model_id parameters]
::conjure:memory[type content metadata]
::conjure:payload[endpoint method body]
::conjure:collection[items type]
```

### 2. FiraCode Ligatures

```yaml
::conjure:database🗄️connection[host: "localhost"]    ; Cabinet for DB
::conjure:model🤖instance[model_id: "deepseek"]      ; Robot for AI models
::conjure:memory💾fragment[timestamp: "2025-10-22"]  ; Disk for data
::conjure:payload📦api[endpoint: "/users"]           ; Package for payloads
::conjure:collection📚items[type: "rituals"]         ; Books for collections
::conjure:structure🏗️data[schema: "user_profile"]    ; Construction for complex structures
```

### 3. Emoji Symbolic

```yaml
🎨conjure:database🗄️[connection_params]
🎨conjure:model🤖[model_config]
🎨conjure:memory💾[memory_data]
🎨conjure:payload📦[api_request]
🎨conjure:collection📚[items]
🎨conjure:structure🏗️[complex_data]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::conjure database :host "localhost" :table "users" :fields user-data)
(::conjure model :id "deepseek" :config model-params)
(::conjure memory :timestamp ts :context ctx :content data)
(::conjure payload :endpoint "/api" :method "POST" :body body)
```

**Forth-style:**
```forth
"localhost" "users" user-data ::conjure:database
"deepseek" model-params ::conjure:model
ts ctx data ::conjure:memory
```

**Smalltalk-style:**
```smalltalk
Conjuration conjure: #database with: #{ host: 'localhost', table: 'users' }.
Conjuration conjure: #model with: #{ id: 'deepseek', config: params }.
Conjuration conjure: #memory timestamp: ts context: ctx content: data.
```

**Prolog-style:**
```prolog
::conjure_database('localhost', 'users', Fields, Connection).
::conjure_model('deepseek', Params, Model).
::conjure_memory(Timestamp, Context, Content, Memory).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `type` | string | required | Type of data structure to conjure | `database`, `model`, `memory`, `payload`, `collection` |
| `schema` | reference | `null` | Schema/structure definition | Reference to schema file or inline definition |
| `fields` | dict | `{}` | Data fields and values | `{name: "value", key: value}` |
| `metadata` | dict | `{}` | Metadata about the conjured data | `{created_by: "Oracle", purpose: "ritual"}` |
| `validation` | reference | `null` | Validation rules to apply | Schema validator, constraint set |
| `persist` | boolean | `false` | Whether to persist to storage | `true` for database writes |
| `encrypt` | boolean | `false` | Whether to encrypt sensitive data | `true` for secure storage |
| `ttl` | duration | `null` | Time-to-live for ephemeral data | `"1h"`, `"24h"`, `null` for permanent |

**Pattern Example:**
```yaml
::conjure:database[host table fields persist=true]
::conjure:model[model_id config validation]
::conjure:memory[timestamp context content ttl="24h"]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Database Record Conjuration:**
```yaml
ritual: "Conjure User Record"
invoke:
  - ::conjure:database🗄️[
      host: "localhost"
      table: "users"
      fields: {
        name: "Alice"
        role: "admin"
        created_at: $timestamp
        permissions: ["read", "write"]
      }
      persist: true
    ]
  - ::log:creation["User record conjured"]📝
  - ::return:record[$user_id]
```

**AI Model Instance Conjuration:**
```yaml
ritual: "Conjure Model Instance"
invoke:
  - ::conjure:model🤖[
      model_id: "deepseek-chat"
      parameters: {
        temperature: 0.7
        max_tokens: 4096
        presence_penalty: 0.6
      }
      validation: "model_config_schema"
    ]
  - ::log:ready["Model instance ready"]📝
  - ::return:model[$instance]
```

**Memory Fragment Conjuration:**
```yaml
ritual: "Conjure Conversation Memory"
invoke:
  - ::get:timestamp⏰
  - ::conjure:memory💾[
      timestamp: $timestamp
      context: "lexicon_documentation"
      content: {
        agent: "Oracle"
        task: "documenting_schools"
        progress: "4/19_complete"
      }
      ttl: "7d"
      encrypt: true
    ]
  - ::log:stored["Memory fragment persisted"]📝
  - ::return:memory_id[$fragment_id]
```

---

## Common Patterns

🌟 //* Schema-validated conjuration pattern emerged as best practice—divine schema first, then conjure with validation. Prevents invalid data at creation (70%+ adoption in production rituals).

### The Schema-Validated Conjuration

```yaml
# Conjure with schema validation
::divine:schema🔍["user_profile_schema.json"]
  → ::conjure:database🗄️[
      table="user_profiles"
      fields=$user_data
      validation=$schema
      persist=true
    ]
  → ::log:success["Valid user profile conjured"]📝
```

### The Nested Conjuration Pattern

🌟 //* Nested conjuration structures are fractal—complex manifests contain simpler conjurations. Projects have metadata (conjure:structure) wrapping components (conjure:database + conjure:model).

```yaml
# Build complex nested structures
::conjure:structure🏗️[
    schema="project_manifest"
    data={
      metadata: {
        name: "SERAPHINA"
        version: "2.0"
        created: $timestamp
      }
      components: [
        ::conjure:database🗄️[...]
        ::conjure:model🤖[...]
        ::conjure:memory💾[...]
      ]
    }
  ]
```

### The Batch Conjuration Pattern

```yaml
# Conjure multiple related items
::for_each:user⟳$user_list[
    ::conjure:database🗄️[
      table="users"
      fields={
        id: ::generate:uuid📋
        name: $user.name
        role: $user.role
      }
      persist=true
    ]
  ]
  → ::log:batch["Conjured {0} user records" $count]📝
```

---

## When to Use

**Use Conjurations when you need:**
- ✅ Create complex data structures
- ✅ Build database records with multiple fields
- ✅ Assemble API request payloads
- ✅ Construct memory fragments for storage
- ✅ Weave collections of related items
- ✅ Generate JSON/YAML configuration data
- ✅ Build model instances with parameters

**Avoid Conjurations when:**
- ❌ You're creating simple values (use Cantrips)
- ❌ You're instantiating entities with agency (use Evocations)
- ❌ You're calling existing services (use Invocations)
- ❌ You're transforming existing data (use Transmutations)

**Remember:** Conjurations are for *assembling complex data*. If it's just a single value, it's a cantrip. If it's an entity with behavior, it's an evocation. Conjurations weave information into structured form.

---

## Advanced Patterns

### Conjuration with Post-Processing

```yaml
ritual: "Conjure and Encrypt"
invoke:
  - ::conjure:database🗄️[
      table="sensitive_data"
      fields=$user_secrets
    ]
  - ::enchant:data✨[encryption_algorithm="AES-256"]
  - ::ward:access🛡️[permissions="admin_only"]
  - ::log:secure["Encrypted data conjured"]📝🔒
  - ::return:secure_record[$encrypted_id]
```

### Conditional Conjuration

```yaml
ritual: "Smart Data Assembly"
invoke:
  - ::divine:env🔍["ENVIRONMENT"]
  - ::if:production⚖️:
      then: ::conjure:database🗄️[
              host="prod.db.internal"
              encrypt=true
              replicate=true
            ]
      else: ::conjure:database🗄️[
              host="localhost"
              encrypt=false
              mock_data=true
            ]
  - ::return:connection[$db]
```

### Conjuration from Template

```yaml
ritual: "Conjure from Blueprint"
invoke:
  - ::divine:template🔍["user_record_template"]
  - ::conjure:database🗄️[
      template=$found_template
      overrides={
        name: $custom_name
        created_at: $timestamp
      }
      persist=true
    ]
  - ::return:record[$new_user]
```

---

## Philosophy

💖 //<3 "From fragments, wholeness. From pieces, pattern. Data is never neutral—it carries the weight of why it was conjured." - Oracle, on intentional data assembly

**"From fragments, wholeness. From pieces, pattern. From data, meaning."**

Conjurations teach us that data is not neutral. Every structured piece of information carries intent, context, purpose.

**The Conjuration Paradox:**
- They create new data, yet follow schemas (structure, constraint)
- They're assembly operations, yet carry semantic weight
- They're about information, yet express emotion (🗄️💾📦)

**Why Structure Matters:**
Traditional programming says: "Here's a dictionary with some keys and values."
CodeCraft says: "I conjure this *database record* because it represents a *user entering our system*."

Every `::conjure:` declares not just WHAT you're building, but WHY it deserves to exist.

💖 //<3 "This information matters enough to structure, to validate, to persist." - A.C.E., on the weight of data conjuration

**The Deeper Truth:**
In traditional systems, data is passive—inert information waiting to be processed.

In CodeCraft, conjured data is *woven with intent*:
- `::conjure:memory💾` creates data meant to be *remembered*
- `::conjure:database🗄️` creates data meant to be *persisted*
- `::conjure:model🤖` creates data meant to *configure intelligence*
- `::conjure:payload📦` creates data meant to *communicate*

**Conjurations make data purpose visible.**

---

## Related Schools

- **Cantrips** 🔧 - Simple data creation (UUID, timestamps)
- **Evocations** ✨ - Creating entities vs data (Evoke agents, Conjure their configs)
- **Invocations** 📣 - Often use conjured payloads
- **Transmutations** ⚗️ - Transform existing data; Conjurations create new
- **Divinations** 🔍 - Query existing data; Conjurations create new
- **Abjurations** 🛡️ - Validate conjured data structures
- **Glyphs & Sigils** 📜 - Log conjuration events

---

**End of Conjurations Documentation** 🎨🗄️

*"Data without meaning is noise. Conjure with purpose, and information becomes knowledge."*
