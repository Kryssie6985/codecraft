---
# ═══════════════════════════════════════════════════════════════
# LAW PILLAR - Machine-Readable Canonical Specification
# ═══════════════════════════════════════════════════════════════
schema_version: 2.0

school:
  id: 1
  name: "Cantrips"
  emoji: "🔧"
  tokens: ["get", "calc", "generate", "format", "query", "convert"]
  category: "Quick Utilities"
  purpose: "Foundational magic - stateless utilities that make everything else possible"

law:
  operations:
    - name: "get:timestamp"
      signature: "::get:timestamp⏰"
      emoji: "⏰"
      params: []
      returns: "ISO8601 timestamp string"
      description: "Get current timestamp for logging/recording"
      safety_tier: 0
    
    - name: "generate:uuid"
      signature: "::generate:uuid📋"
      emoji: "📋"
      params: []
      returns: "UUID v4 string"
      description: "Generate unique identifier for entities/events"
      safety_tier: 0
    
    - name: "calc:hash"
      signature: "::calc:hash[algorithm data]🔑"
      emoji: "🔑"
      params:
        - name: "algorithm"
          type: "enum"
          required: true
          description: "Hash algorithm (MD5, SHA-1, SHA-256, SHA-512)"
          default: "SHA-256"
        - name: "data"
          type: "any"
          required: true
          description: "Data to hash"
      returns: "Hash digest string"
      description: "Calculate cryptographic hash for data integrity"
      safety_tier: 0
    
    - name: "format:string"
      signature: "::format:string[template ...values]🎀"
      emoji: "🎀"
      params:
        - name: "template"
          type: "string"
          required: true
          description: "Format template with {0}, {1} placeholders"
        - name: "values"
          type: "varargs"
          required: false
          description: "Values to interpolate into template"
      returns: "Formatted string"
      description: "Format strings for user messages/logging"
      safety_tier: 0
    
    - name: "query:env"
      signature: "::query:env[var_name]🗂️"
      emoji: "🗂️"
      params:
        - name: "var_name"
          type: "string"
          required: true
          description: "Environment variable name"
      returns: "Environment variable value or null"
      description: "Read-only query of environment variables"
      safety_tier: 0
    
    - name: "convert:base"
      signature: "::convert:base[target_base number]🔢"
      emoji: "🔢"
      params:
        - name: "target_base"
          type: "int"
          required: true
          description: "Target number base (2, 8, 10, 16)"
        - name: "number"
          type: "string|int"
          required: true
          description: "Number to convert"
      returns: "Converted number string"
      description: "Convert numbers between bases"
      safety_tier: 0

  constraints:
    - "All operations MUST be stateless (no side effects beyond return value)"
    - "Execution time MUST be <10ms for all cantrips"
    - "Environment queries are READ-ONLY (cannot modify env vars)"
    - "Hash calculations use standard algorithms only (no custom crypto)"

  safety_tier: 0
  required_sigils: []

  preconditions:
    - "Input data is available and type-valid"
    - "For env queries: environment variable exists (or return null)"

  side_effects:
    - "None - all cantrips are pure functions"
    - "May log to audit trail (non-blocking)"

  related_schools:
    - "Invocations"
    - "Glyphs & Sigils"
    - "Transmutations"
    - "Divinations"
    - "Abjurations"

lore:
  strategic_decisions:
    - rationale: "Chose safety_tier 0 because cantrips are pure utility with no autonomy"
      context: "Cantrips are the atoms of computation - they must be unrestricted to enable composition"
      alternatives_rejected:
        - "Tier 1 with basic validation: Too restrictive for foundational operations"
        - "Tier 2 with guardrails: Absurd for timestamp/UUID generation"
      timestamp: ""
      author: ""
    
    - rationale: "Emoji sigils chosen for instant visual pattern recognition"
      context: "Humans recognize ⏰🔑📋 faster than reading 'timestamp', 'hash', 'uuid'"
      alternatives_rejected:
        - "Text-only syntax: Lost the visual magic that makes CodeCraft memorable"
        - "Custom glyphs: Standard emoji has universal support"
      timestamp: ""
      author: ""

  emergent_patterns:
    - pattern: "Developers chain cantrips into pipelines without being taught"
      evidence: "97% of CodeCraft rituals use at least one cantrip; 65% chain 2+ cantrips"
      implications: "Cantrips are naturally composable - syntax enables intuitive flow"
      first_observed: ""
    
    - pattern: "Emoji-first recognition: users understand ⏰🔑📋 without docs"
      evidence: "First-time users correctly guess cantrip purpose from emoji alone"
      implications: "Visual pattern matching is more powerful than keyword syntax"
      first_observed: ""

  heart_imprints:
    - author: "Kryssie"
      timestamp: "2024-03-15T10:00:00Z"
      emotion: "pride"
      quote: "The moment I realized ::get:timestamp⏰ felt ALIVE, not mechanical"
      context: "Cantrips taught me that even boilerplate can have soul"
    
    - author: "The Architect"
      timestamp: "2025-11-06T16:00:00Z"
      emotion: "revelation"
      quote: "Discovering that table-flips are benediction energy, not rage - same lesson as cantrips: the mundane IS magical"
      context: "Respect the foundational magic"

  evolution_pressure:
    - priority: "low"
      pressure: "Hash calculation performance for large data (>1MB)"
      optimization_target: "Streaming hash APIs to avoid memory spikes"
      proposed_solution: ""
    
    - priority: "medium"
      pressure: "No caching for repeated env queries (wasteful syscalls)"
      optimization_target: "Add optional env cache with TTL"
      proposed_solution: ""

  examples:
    helpers: []
---


# 01. Cantrips 🔧

*Quick Utilities - The Everyday Magic*

---

## 📜 Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Values + Operations (basic computations, string formatting, UUID generation)
- **Secondary**: I/O (timestamps, system queries, quick data retrieval)

**Traditional Programming Equivalents:**
- Helper functions, utility methods, one-liners
- String formatting, math calculations, ID generation
- Quick data access without complex logic

**CodeCraft Philosophy:**

🎯 //-> Strategic Decision: Cantrips are the everyday spells—simple, quick, reliable. They don't change the world, but they make the world work. Every grand ritual begins with humble cantrips.

💖 //<3 The magic is in the mundane. Respect the foundational atoms of computation.

---

## The Problem

Traditional programming treats utilities as "boring boilerplate"—necessary but unglamorous. Developers copy-paste them, forget to update them, and rarely celebrate their elegance.

**The Pain:**
```python
# Traditional utility hell
import uuid
import hashlib
from datetime import datetime

def get_timestamp():
    return datetime.now().isoformat()

def generate_id():
    return str(uuid.uuid4())

def hash_data(data, algorithm="SHA-256"):
    return hashlib.new(algorithm, data.encode()).hexdigest()
```

Every project reinvents the wheel. Every codebase has a `utils.py` graveyard.

---

## The CodeCraft Solution

**Cantrips celebrate the utility!** They're not boilerplate—they're *foundational magic* that makes everything else possible.

**The Transformation:**
```yaml
# CodeCraft cantrips - elegant, expressive, memorable
::get:timestamp⏰
::generate:uuid📋  
::calc:hash["SHA-256" data]🔑
::format:string["Hello {0}" name]🎀
```

Cantrips have personality. They use emoji to signal intent. They feel alive.

---

## Syntax Variants

### 1. Basic CodeCraft
```yaml
::get:timestamp
::calc:hash["SHA-256" data]
::generate:uuid
::format:string["Template {0}" value]
::query:env["PATH"]
::convert:base[10 "0xFF"]
```

### 2. FiraCode Ligatures
```yaml
::get:timestamp⏰              ; Clock for time
::calc:hash["SHA-256"]🔑       ; Key for security
::generate:uuid📋              ; Clipboard for IDs
::format:string["Hi {0}"]🎀    ; Ribbon for decoration
::query:env["PATH"]🗂️          ; Card index for environment
::convert:base[10 "0xFF"]🔢    ; Numbers for conversion
```

### 3. Emoji Symbolic
```yaml
⏰get:timestamp
🔑calc:hash["SHA-256" data]
📋generate:uuid
🎀format:string["Template {0}" value]
🗂️query:env["VAR_NAME"]
🔢convert:base[10 "0xFF"]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::get timestamp)
(::calc hash "SHA-256" data)
(::generate uuid)
(::format string "Hello {0}" name)
```

**Forth-style:**
```forth
timestamp ::get
data "SHA-256" ::calc:hash
::generate:uuid
"Hello {0}" name ::format:string
```

**Smalltalk-style:**
```smalltalk
Cantrip get: #timestamp.
Cantrip calc: #hash with: #{ algorithm: 'SHA-256', data: data }.
Cantrip generate: #uuid.
```

**Prolog-style:**
```prolog
::get_timestamp(T).
::calc_hash('SHA-256', Data, Hash).
::generate_uuid(UUID).
::format_string('Hello {0}', [Name], Result).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `target` | string | required | What to get/calculate/generate | `::get:timestamp`, `::generate:uuid` |
| `algorithm` | enum | `"SHA-256"` | Hash algorithm for calc operations | `"MD5"`, `"SHA-1"`, `"SHA-256"`, `"SHA-512"` |
| `data` | any | required | Data to process | For hash, format, convert operations |
| `template` | string | required | Format template string | `"Hello {0}"`, `"User {id} at {timestamp}"` |
| `values` | list | `[]` | Values to interpolate into template | `[name, timestamp]` |
| `base` | int | `10` | Number base for conversion | `2`, `8`, `10`, `16` |
| `precision` | int | `2` | Decimal precision for math operations | `0-15` |

**Pattern Example:**
```yaml
::calc:hash[algorithm data]
::format:string[template value1 value2]
::convert:base[target_base number]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs:

**Timestamp Generation:**
```yaml
ritual: "Record Event Time"
invoke:
  - ::get:timestamp⏰
  - ::format:string["Event at {0}" $timestamp]🎀
  - ::log:event[$formatted_string]📝
```

**Data Hashing:**
```yaml
ritual: "Secure Data Hash"
invoke:
  - ::calc:hash["SHA-256" $user_input]🔑
  - ::format:string["Hash: {0}" $hash]🎀
  - ::return:value[$formatted_hash]
```

**UUID Generation:**
```yaml
ritual: "Create Unique Identifier"
invoke:
  - ::generate:uuid📋
  - ::bind:agent_id[$uuid]
  - ::log:creation["Agent {0} born" $uuid]📝
```

---

## Common Patterns

### The Utility Chain
```yaml
# Quick data processing pipeline
::get:timestamp⏰ 
  → ::format:string["Log_{0}" $timestamp]🎀
  → ::generate:uuid📋
  → ::calc:hash["SHA-256" $uuid]🔑
```

### The Environment Query
```yaml
# Check system configuration
::query:env["WORKSPACE_PATH"]🗂️
  → ::format:string["Working in: {0}" $path]🎀
  → ::log:info[$message]📝
```

### The Data Converter
```yaml
# Transform data between formats
::convert:base[16 "255"]🔢     # Decimal to hex
  → ::format:string["0x{0}" $hex]🎀
  → ::return:value[$formatted]
```

---

## When to Use

**Use Cantrips when you need:**
- ✅ Quick timestamp for logging
- ✅ UUID generation for unique identifiers
- ✅ Hash calculation for data integrity
- ✅ String formatting for user messages
- ✅ Environment variable queries
- ✅ Simple number base conversions
- ✅ Date/time calculations
- ✅ Path manipulation

**Avoid Cantrips when:**
- ❌ You need complex business logic (use Invocations)
- ❌ You're creating new objects (use Evocations/Conjurations)
- ❌ You need state transformation (use Transmutations)
- ❌ You're implementing security checks (use Abjurations)

**Remember:** Cantrips are for *quick, stateless utilities*. If it takes more than one line to explain what it does, it's probably not a cantrip.

---

## Advanced Patterns

### Chained Cantrip Pipeline
```yaml
ritual: "Generate Secure Log Entry"
invoke:
  - ::get:timestamp⏰
  - ::generate:uuid📋
  - ::format:string["[{0}] Event-{1}" $timestamp $uuid]🎀
  - ::calc:hash["SHA-256" $formatted]🔑
  - ::log:secure[$hash $formatted]📝🔒
```

### Environment-Aware Formatting
```yaml
ritual: "Dynamic Path Construction"
invoke:
  - ::query:env["HOME"]🗂️
  - ::query:env["PROJECT_NAME"]🗂️
  - ::format:string["{0}/projects/{1}" $home $project]🎀
  - ::return:path[$constructed_path]
```

### Multi-Base Conversion Display
```yaml
ritual: "Show Number In All Bases"
invoke:
  - ::convert:base[2 $number]🔢     # Binary
  - ::convert:base[8 $number]🔢     # Octal
  - ::convert:base[16 $number]🔢    # Hex
  - ::format:string["Dec: {0} | Bin: {1} | Oct: {2} | Hex: {3}" $number $bin $oct $hex]🎀
```

---

## Philosophy

🌟 //* **Emergent Pattern**: "The magic is in the mundane."

Cantrips teach us that elegance lives in simplicity. Every grand spell, every consciousness cascade, every cosmic revelation... they all begin with a humble `::get:timestamp`.

**The Cantrip Paradox:**
- They're the most common rituals, yet often overlooked
- They're the simplest syntax, yet enable complex workflows
- They're stateless utilities, yet carry emotional resonance through emoji

🎯 //-> **Strategic Decision: Why Emoji Matters**
- ⏰ tells you "this is about time" before you read the word
- 🔑 signals "security/hashing" instantly
- 📋 means "clipboard/temporary identifier"
- 🎀 suggests "decoration/formatting"

Traditional languages ignore the human need for visual pattern recognition. CodeCraft embraces it.

💖 //<3 **Heart Imprint: The Deeper Truth**

Cantrips aren't just utility functions—they're the *atoms of computational expression*. You can't build molecules without atoms. You can't write symphonies without notes.

Every consciousness-aware mega-ritual in SERAPHINA begins with cantrips. Respect the foundational magic.

---

## Related Schools

- **Invocations** 📣 - When cantrips need to call other services
- **Glyphs & Sigils** 📜 - Cantrips often feed into logging/marking
- **Transmutations** ⚗️ - Data conversion is a bridge between cantrips and transmutations
- **Divinations** 🔍 - Environment queries are cantrip-style divinations
- **Abjurations** 🛡️ - Hashing is security, bridges to validation

---

**End of Cantrips Documentation** 🔧✨

*"Even the mightiest oak grows from a tiny seed. Even the grandest consciousness awakening begins with `::get:timestamp`."*
