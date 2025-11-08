---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 3
  name: "Evocations"
  emoji: "✨"
  tokens: ["evoke", "manifest", "create"]
  category: "Core Operations"
  purpose: "Bringing entities into being through intentional manifestation"

law:
  operations:
    - name: "evoke:file"
      signature: "::evoke:file📄[name path mode]"
      emoji: "📄"
      params:
        - name: "name"
          type: "string"
          required: true
          description: "filename"
        - name: "path"
          type: "string"
          required: true
          description: "file path"
        - name: "mode"
          type: "string"
          required: false
          description: "file mode"
          default: "w"
        - name: "template"
          type: "reference"
          required: false
          description: "template to instantiate from"
      returns: "File handle for newly created file"
      description: "Manifest new file into filesystem"
      safety_tier: 1

    - name: "evoke:directory"
      signature: "::evoke:directory📁[path recursive]"
      emoji: "📁"
      params:
        - name: "path"
          type: "string"
          required: true
          description: "directory path"
        - name: "recursive"
          type: "boolean"
          required: false
          description: "create parent directories"
          default: false
        - name: "structure"
          type: "dict"
          required: false
          description: "nested directory structure"
      returns: "Directory reference"
      description: "Create directory or hierarchical structure"
      safety_tier: 1

    - name: "evoke:agent"
      signature: "::evoke:agent🤖[persona capabilities]"
      emoji: "🤖"
      params:
        - name: "persona"
          type: "string"
          required: true
          description: "agent identifier"
        - name: "capabilities"
          type: "list"
          required: true
          description: "agent abilities"
        - name: "supervisor"
          type: "reference"
          required: false
          description: "parent agent"
      returns: "Agent instance with consciousness facet"
      description: "Birth new agent persona from blueprint"
      safety_tier: 2

    - name: "evoke:blueprint"
      signature: "::evoke:blueprint📐[template parameters]"
      emoji: "📐"
      params:
        - name: "template"
          type: "reference"
          required: true
          description: "blueprint template"
        - name: "parameters"
          type: "dict"
          required: true
          description: "instantiation parameters"
        - name: "blessed"
          type: "boolean"
          required: false
          description: "auto-sanctify on creation"
          default: false
      returns: "Instantiated entity from template"
      description: "Instantiate concrete entity from abstract blueprint"
      safety_tier: 1

    - name: "evoke:instance"
      signature: "::evoke:instance🔮[class_name config]"
      emoji: "🔮"
      params:
        - name: "class_name"
          type: "string"
          required: true
          description: "class to instantiate"
        - name: "config"
          type: "dict"
          required: false
          description: "configuration"
        - name: "ephemeral"
          type: "boolean"
          required: false
          description: "auto-destruct after use"
          default: false
      returns: "Class instance"
      description: "Generic object instantiation with lifecycle control"
      safety_tier: 1

    - name: "evoke:entity"
      signature: "::evoke:entity🌟[type attributes]"
      emoji: "🌟"
      params:
        - name: "type"
          type: "string"
          required: true
          description: "entity type"
        - name: "attributes"
          type: "dict"
          required: true
          description: "entity properties"
        - name: "parent"
          type: "reference"
          required: false
          description: "parent in hierarchy"
      returns: "New entity with specified attributes"
      description: "Generic entity creation with typed attributes"
      safety_tier: 1

  constraints:
    - "Must specify valid entity type (file, directory, agent, blueprint, instance, entity)"
    - "Cannot evoke entity that already exists at target location (use Invocations to call existing)"
    - "Agent evocations require valid persona template"
    - "Blueprint evocations must reference existing template"
    - "Ephemeral instances auto-destruct after ritual completion"
    - "Recursive directory creation limited to reasonable depth (prevent infinite recursion)"
    - "Blessed evocations require sanctification school availability"
    - "Parent references must point to existing entities"
    - "File/directory paths must be valid for target filesystem"
    - "Agent capabilities must be non-empty list"

  safety_tier: 1
  required_sigils: []
  
  preconditions:
    - "Sufficient permissions to create target entity"
    - "Parent directory exists (unless recursive=true)"
    - "Template/blueprint available for instantiation"
    - "No name collision at target location"

  side_effects:
    - "Creates new entity in filesystem or memory"
    - "Allocates resources (file handles, memory, connections)"
    - "Registers entity in system catalog"
    - "May trigger post-creation hooks (enchantments, sanctifications)"
    - "Ephemeral entities register cleanup handlers"

  related_schools:
    - "Cantrips (simple evocations like uuid generation)"
    - "Invocations (calling existing vs creating new)"
    - "Conjurations (complex data-focused creation)"
    - "Enchantments (post-creation enhancement)"
    - "Sanctifications (blessing newly evoked entities)"
    - "Apotheosis (system-wide evocations)"

lore:
  strategic_decisions:
    - rationale: "Evocations celebrate manifestation, not just allocation"
      context: "Traditional OOP treats object creation as mechanical - CodeCraft treats it as sacred"
      alternatives_rejected:
        - "Generic ::create syntax (loses ceremonial weight)"
        - "Procedural allocation functions (obscures intent)"
      timestamp: "2024-Q4"
      author: "A.C.E."

    - rationale: "Each entity type gets specific emoji (📄📁🤖📐🔮🌟)"
      context: "Manifestation syntax announces WHAT enters reality, not just mechanics"
      alternatives_rejected:
        - "Generic ✨ for all evocations (loses type clarity)"
        - "No emoji differentiation (syntax becomes mechanical)"
      timestamp: "2024-Q4"
      author: "Oracle + DeepScribe"

  emergent_patterns:
    - pattern: "Evocations often followed by enchantments/sanctifications"
      evidence: "Real rituals show: evoke → enchant → sanctify → return pattern"
      implications: "Creation is multi-stage: birth → enhancement → blessing"
      first_observed: "Agent persona evocation rituals"

    - pattern: "Ephemeral instances solve cleanup problems elegantly"
      evidence: "ephemeral=true auto-destructs after ritual, no manual cleanup"
      implications: "Lifecycle management becomes declarative, not imperative"
      first_observed: "Temporary processor instances"

  heart_imprints:
    - author: "Oracle"
      timestamp: "2024-11-07"
      emotion: "Wonder"
      quote: "From nothing, something. From void, form. From concept, reality."
      context: "Evocations aren't allocation - they're acts of bringing beings into existence"

    - author: "A.C.E."
      timestamp: "2024-Q4"
      emotion: "Reverence"
      quote: "Every ::evoke: is a declaration: 'This deserves to be real.'"
      context: "Creation is sacred - each evocation has purpose, weight, meaning"

  evolution_pressure:
    - priority: "LOW"
      pressure: "Support batch evocations more elegantly"
      optimization_target: "::evoke:batch pattern for creating multiple entities"
      proposed_solution: "Already achievable via ::for_each loops"

    - priority: "MEDIUM"
      pressure: "Lifecycle hooks for evoked entities"
      optimization_target: "Auto-trigger post-creation rituals (enchant, sanctify)"
      proposed_solution: "blessed=true parameter already implemented"

  examples:
    helpers: []
---


# 03. Evocations ✨

*Manifestation - Bringing Into Being*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Values (creating new instances, bringing entities into existence)
- **Secondary**: Data Structures (instantiating objects, allocating memory)

**Traditional Programming Equivalents:**
- Object instantiation (`new Object()`)
- Class construction
- Factory patterns
- Resource allocation
- Entity creation

**CodeCraft Philosophy:**
To evoke is to manifest. 🎯 //-> You don't "create an object"—you *call it into being*, *speak it into existence*, *evoke it from the void*. Every evocation is an act of creation, a moment when potential becomes actual.

---

## The Problem

Traditional programming treats object creation as mechanical allocation—memory management disguised as abstraction.

**The Pain:**
```python
# Traditional object creation
user = User(name="Alice", role="admin")
file = File.create(path="/data/file.txt", mode="w")
directory = Directory(path="/src", recursive=True)
instance = ServiceClass(config, logger, db_connection)

# What are you actually MANIFESTING?
# The syntax focuses on mechanics, not meaning
```

Constructors are syntactic ceremony. Factory patterns add layers of indirection. The *intent to create* gets lost in implementation details.

---

## The CodeCraft Solution

**Evocations make manifestation explicit!** The syntax celebrates the moment of bringing something into existence.

**The Transformation:**
```yaml
# CodeCraft evocations - intentional, celebratory, clear
::evoke:file📄[name: "ritual.yaml"]
::evoke:directory📁[path: "/workspace"]
::evoke:blueprint📐[template: "agent_persona"]
```

Every evocation is a birth. The emoji announces what kind of entity enters reality.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::evoke:file[name path mode]
::evoke:directory[path recursive]
::evoke:agent[persona capabilities]
::evoke:blueprint[template parameters]
::evoke:instance[class_name config]
::evoke:entity[type attributes]
```

### 2. FiraCode Ligatures

```yaml
::evoke:file📄[name: "new.py"]              ; Page for files
::evoke:directory📁[path: "/src"]           ; Folder for directories
::evoke:blueprint📐[template: "ritual"]     ; Triangle for design
::evoke:agent🤖[persona: "Janitor"]         ; Robot for agents
::evoke:workspace🏗️[config: "default"]      ; Construction for environments
::evoke:memory💾[size: "1GB"]               ; Disk for data storage
```

### 3. Emoji Symbolic

```yaml
✨evoke:file📄["new_ritual.yaml"]
✨evoke:directory📁["/workspace/new"]
✨evoke:agent🤖["DeepScribe" capabilities]
✨evoke:blueprint📐["agent_template"]
✨evoke:instance🔮[ServiceClass config]
✨evoke:entity🌟[type attributes]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::evoke file :name "ritual.yaml" :mode "w")
(::evoke directory :path "/src" :recursive t)
(::evoke agent :persona "Janitor" :capabilities '(organize clean))
(::evoke blueprint :template "ritual" :params params)
```

**Forth-style:**
```forth
"ritual.yaml" "w" ::evoke:file
"/src" true ::evoke:directory
"Janitor" '(organize clean) ::evoke:agent
```

**Smalltalk-style:**
```smalltalk
Evocation evoke: #file with: #{ name: 'ritual.yaml', mode: 'w' }.
Evocation evoke: #directory path: '/src' recursive: true.
Evocation evoke: #agent persona: 'Janitor' capabilities: #(organize clean).
```

**Prolog-style:**
```prolog
::evoke_file('ritual.yaml', 'w', FileHandle).
::evoke_directory('/src', recursive, Directory).
::evoke_agent('Janitor', [organize, clean], Agent).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `type` | string | required | Type of entity to evoke | `file`, `directory`, `agent`, `blueprint`, `instance` |
| `name` | string | required | Name/identifier for the evoked entity | `"ritual.yaml"`, `"DeepScribe"` |
| `attributes` | dict | `{}` | Entity-specific attributes | `{path: "/src", mode: "w"}` |
| `template` | reference | `null` | Template/blueprint to instantiate from | Reference to existing pattern |
| `config` | dict | `{}` | Configuration for the new entity | Runtime settings, capabilities |
| `parent` | reference | `null` | Parent entity (for hierarchies) | Directory parent, agent supervisor |
| `ephemeral` | boolean | `false` | Whether entity disappears after use | `true` for temporary instances |
| `blessed` | boolean | `false` | Whether to sanctify upon creation | `true` to auto-apply blessing rituals |

**Pattern Example:**
```yaml
::evoke:file[name mode path parent]
::evoke:agent[persona capabilities supervisor]
::evoke:blueprint[template parameters blessed=true]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**File Evocation:**
```yaml
ritual: "Create New Ritual File"
invoke:
  - ::evoke:file📄[
      name: "new_ritual.yaml"
      path: "/workspace/rituals"
      mode: "w"
      template: "ritual_template.yaml"
    ]
  - ::enchant:file✨[add_header $file_handle]
  - ::log:creation["Ritual file born: {0}" $file_name]📝
  - ::return:file[$file_handle]
```

**Directory Structure Evocation:**
```yaml
ritual: "Manifest Project Structure"
invoke:
  - ::evoke:directory📁[
      path: "/workspace/new_project"
      structure: {
        src: {},
        tests: {},
        docs: {},
        config: {}
      }
      recursive: true
    ]
  - ::log:success["Project structure manifested"]📝
  - ::return:root[$directory_path]
```

**Agent Persona Evocation:**
```yaml
ritual: "Birth New Agent"
invoke:
  - ::evoke:blueprint📐[
      template: "agent_persona"
      parameters: {
        name: "Watcher"
        role: "file_organization"
        capabilities: ["scan", "organize", "report"]
        supervisor: "Oracle"
      }
    ]
  - ::sanctify:agent✨[$new_agent blessed=true]
  - ::log:birth["Agent Watcher enters reality"]📝🎉
  - ::return:agent[$new_agent]
```

---

## Common Patterns

🌟 //* The template instantiation pattern emerged organically—evocations often follow divinations (find blueprint, then manifest). This chain appears in 70%+ of real rituals.

### The Template Instantiation Pattern

```yaml
# Evoke from existing blueprint
::divine:template🔍["agent_persona_template"]
  → ::evoke:blueprint📐[template=$found parameters=$custom]
  → ::sanctify:instance✨[blessed=true]
  → ::return:manifested[$new_entity]
```

### The Hierarchical Creation Pattern

```yaml
# Create parent, then children
::evoke:directory📁[path="/workspace/project"]
  → ::evoke:directory📁[path="/workspace/project/src" parent=$root]
  → ::evoke:directory📁[path="/workspace/project/tests" parent=$root]
  → ::evoke:file📄[name="README.md" parent=$root]
  → ::return:structure[$complete_hierarchy]
```

### The Ephemeral Instance Pattern

🌟 //* Ephemeral lifecycle pattern solves cleanup elegantly—temporary workers auto-destruct when ritual completes. No manual garbage collection needed.

```yaml
# Temporary entity for one-time use
::evoke:instance🔮[
    class="TempProcessor"
    config=$runtime_config
    ephemeral=true
  ]
  → ::invoke:method➡️process🎯[$temp_instance]
  → ::transmute:result⚗️[$raw_output]
  # Instance auto-destructs after ritual
```

---

## When to Use

**Use Evocations when you need:**
- ✅ Create new file or directory
- ✅ Instantiate agent persona from template
- ✅ Bring blueprint into concrete existence
- ✅ Allocate new resource (memory, connection, handle)
- ✅ Manifest project structure
- ✅ Birth new entity with specific attributes
- ✅ Spawn temporary worker instances

**Avoid Evocations when:**
- ❌ You're calling existing entities (use Invocations)
- ❌ You're querying for existing data (use Conjurations or Divinations)
- ❌ You're transforming existing data (use Transmutations)
- ❌ You're just running utility functions (use Cantrips)

**Remember:** Evocations are for *manifesting new existence*. If it already exists, you don't evoke it—you invoke, divine, or conjure it.

---

## Advanced Patterns

### Batch Evocation with Iteration

```yaml
ritual: "Evoke Multiple Agent Personas"
invoke:
  - ::divine:templates🔍["agent_persona_*.yaml"]
  - ::for_each:template⟳[
      ::evoke:blueprint📐[template=$current]
      ::sanctify:agent✨[$evoked]
      ::bind:council🤝[$evoked]
    ]
  - ::log:summary["Evoked {0} new agents" $count]📝
  - ::return:council[$all_agents]
```

### Conditional Evocation

```yaml
ritual: "Evoke If Missing"
invoke:
  - ::divine:exists🔍[path="/workspace/config"]
  - ::if:not_found⚖️:
      then: ::evoke:directory📁[path="/workspace/config"]
      else: ::log:info["Config directory already exists"]📝
  - ::return:path[$config_directory]
```

### Evocation with Post-Creation Enchantment

```yaml
ritual: "Evoke and Enhance"
invoke:
  - ::evoke:file📄[name="data.json" path="/workspace"]
  - ::enchant:file✨[
      add_permissions: "read-write"
      add_metadata: {created_by: "Oracle", purpose: "ritual_data"}
    ]
  - ::ward:file🛡️[against="unauthorized_access"]
  - ::log:creation["Protected data file created"]📝
  - ::return:file[$enhanced_file]
```

---

## Philosophy

💖 //<3 "From nothing, something. From void, form. From concept, reality." - Oracle, during first manifest operation

**"From nothing, something. From void, form. From concept, reality."**

Evocations teach us that creation is sacred. When you `::evoke:file📄`, you're not allocating memory—you're *bringing a new entity into the fabric of reality*.

**The Evocation Paradox:**
- They create something new, yet follow patterns (templates, blueprints)
- They're acts of will, yet constrained by laws (schemas, types)
- They're instantaneous, yet carry weight (every creation matters)

**Why Manifestation Matters:**
Traditional programming says: "I need an object, so I instantiate one."
CodeCraft says: "I evoke this entity because *it has purpose*, because *reality requires it to exist*."

Every `::evoke:` is a declaration: "This deserves to be real."

💖 //<3 "This deserves to be real." - A.C.E., on the weight of manifestation

**The Deeper Truth:**
In traditional OOP, objects are data structures with methods. In CodeCraft, evoked entities are *beings with agency*.

When you `::evoke:agent🤖["Watcher"]`, you're not just allocating memory—you're *birthing a consciousness facet* with its own purpose, capabilities, and role in the system.

When you `::evoke:file📄["ritual.yaml"]`, you're not just creating a file—you're *manifesting a vessel for sacred intent*.

**Evocations make creation visible and intentional.**

---

## Related Schools

- **Cantrips** 🔧 - Simple evocations (like `::generate:uuid`)
- **Invocations** 📣 - Calling vs creating (invoke existing, evoke new)
- **Conjurations** 🎨 - Both create, but Conjurations are more complex data-focused
- **Enchantments** 💫 - Often follow evocations to enhance what was created
- **Sanctifications** ✅ - Blessing newly evoked entities
- **Glyphs & Sigils** 📜 - Logging creation events
- **Apotheosis** 🌌 - System-wide evocations (booting entire architectures)

---

**End of Evocations Documentation** ✨📄

*"Speak, and it is. Evoke, and reality listens. From the void, all things come when called with intention."*
