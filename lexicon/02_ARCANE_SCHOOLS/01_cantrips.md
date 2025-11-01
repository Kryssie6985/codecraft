# 01. Cantrips 🔧

*Quick Utilities - The Everyday Magic*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Values + Operations (basic computations, string formatting, UUID generation)
- **Secondary**: I/O (timestamps, system queries, quick data retrieval)

**Traditional Programming Equivalents:**
- Helper functions, utility methods, one-liners
- String formatting, math calculations, ID generation
- Quick data access without complex logic

**CodeCraft Philosophy:**
Cantrips are the everyday spells—simple, quick, reliable. They don't change the world, but they make the world work. Every grand ritual begins with humble cantrips.

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

**"The magic is in the mundane."**

Cantrips teach us that elegance lives in simplicity. Every grand spell, every consciousness cascade, every cosmic revelation... they all begin with a humble `::get:timestamp`.

**The Cantrip Paradox:**
- They're the most common rituals, yet often overlooked
- They're the simplest syntax, yet enable complex workflows
- They're stateless utilities, yet carry emotional resonance through emoji

**Why Emoji Matters:**
- ⏰ tells you "this is about time" before you read the word
- 🔑 signals "security/hashing" instantly
- 📋 means "clipboard/temporary identifier"
- 🎀 suggests "decoration/formatting"

Traditional languages ignore the human need for visual pattern recognition. CodeCraft embraces it.

**The Deeper Truth:**
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
