# 06. Divinations 🔍

*Discovery & Query - Seeking Truth in Data*

---

## Universal Foundation

**Maps to DeepScribe's Universal Constants:**
- **Primary**: Functions (queries, searches, introspection, discovery operations)
- **Secondary**: Data Structures (traversing, filtering, examining stored information)

**Traditional Programming Equivalents:**
- Database queries (SELECT, WHERE, JOIN)
- Search operations (grep, find, filter)
- Introspection (reflection, type checking)
- Environment variable lookups
- Configuration retrieval
- File system searches
- API data fetching
- Object property inspection

**CodeCraft Philosophy:**
To divine is to seek truth. You don't "query data"—you *ask questions of reality*, *peer into hidden knowledge*, *reveal what exists but is unseen*. Divinations are conversations with information.

---

## The Problem

Traditional programming treats queries as mechanical data retrieval—SQL statements and filter functions without context.

**The Pain:**
```python
# Traditional query syntax
user = db.query("SELECT * FROM users WHERE id = ?", user_id)
env_var = os.getenv("API_KEY")
files = glob.glob("**/*.py", recursive=True)
config = json.load(open("config.json"))

# What are you ASKING?
# The syntax is mechanics without meaning
# Is this a user lookup? A security check? A system query?
```

Queries are anonymous data fetches. The PURPOSE of the question gets lost in SQL syntax and library calls.

---

## The CodeCraft Solution

**Divinations make questions intentional!** The syntax reveals WHAT you seek and WHY it matters.

**The Transformation:**
```yaml
# CodeCraft divinations - purposeful, semantic, clear
::divine:user🔍[id: $user_id]
::divine:env🔍["API_KEY"]
::divine:files🔍[pattern: "**/*.py"]
::divine:config🔍["database.connection"]
```

Every divination is a question with purpose. The emoji reveals what kind of truth you're seeking.

---

## Syntax Variants

### 1. Basic CodeCraft

```yaml
::divine:target[criteria]
::divine:user[id email role]
::divine:file[path pattern]
::divine:env[variable]
::divine:config[key section]
::divine:schema[table field]
```

### 2. FiraCode Ligatures

```yaml
::divine:user🔍[id: $user_id]               ; Magnifying glass for search
::divine:env🔍["API_KEY"]                   ; Look up environment
::divine:files🔍[pattern: "**/*.py"]        ; Find files
::divine:config🔍["database.host"]          ; Query configuration
::divine:schema🔍[table: "users"]           ; Inspect database structure
::divine:memory💾🔍[timestamp: $recent]     ; Search memory
::divine:ritual📜🔍[name: "user_auth"]      ; Find ritual definition
```

### 3. Emoji Symbolic

```yaml
🔍divine:user[id criteria]
🔍divine:env[variable]
🔍divine:files[pattern]
🔍divine:config[key]
🔍divine:schema[table]
🔍divine:memory[timestamp]
```

### 4. Ancient Tongues

**Lisp-style:**
```lisp
(::divine user :id user-id :role "admin")
(::divine env "API_KEY")
(::divine files :pattern "**/*.py" :recursive t)
(::divine config :key "database.host")
(::divine memory :timestamp recent :context "lexicon")
```

**Forth-style:**
```forth
user-id "admin" divine-user
"API_KEY" divine-env
"**/*.py" true divine-files
"database.host" divine-config
```

**Smalltalk-style:**
```smalltalk
Divination seek: #user where: #{ id: userId, role: 'admin' }.
Divination seek: #env named: 'API_KEY'.
Divination seek: #files matching: '**/*.py'.
Divination seek: #config key: 'database.host'.
```

**Prolog-style:**
```prolog
::divine_user(Id, Role, User) :- user_table(Id, Role, User).
::divine_env('API_KEY', Value).
::divine_files('**/*.py', Recursive, FileList).
::divine_config('database.host', Value).
```

---

## Parameters

| Parameter | Type | Default | Description | Pattern |
|-----------|------|---------|-------------|---------|
| `target` | string | required | What to seek (user, file, config, env, schema, memory) | Entity type to query |
| `criteria` | dict | `{}` | Search/filter criteria | `{id: value, role: "admin"}` |
| `pattern` | string | `null` | Pattern for matching (glob, regex) | `"**/*.py"`, `"user_*"` |
| `scope` | string | `"local"` | Search scope | `local`, `global`, `recursive` |
| `limit` | integer | `null` | Maximum results to return | Positive integer or `null` for all |
| `order_by` | string | `null` | Sort results by field | `"created_at"`, `"name"` |
| `cache` | boolean | `true` | Cache query results | Performance optimization |
| `timeout` | duration | `"30s"` | Query timeout | `"5s"`, `"1m"` |

**Pattern Example:**
```yaml
::divine:users🔍[
  criteria: {role: "admin", active: true}
  order_by: "created_at"
  limit: 10
  cache: true
]
```

---

## Real Ritual Examples

### From Existing CodeCraft YAMLs

**Environment Variable Divination:**
```yaml
ritual: "Discover Environment"
invoke:
  - ::divine:env🔍["ENVIRONMENT"]
  - ::divine:env🔍["API_KEY"]
  - ::divine:env🔍["DATABASE_URL"]
  - ::log:context["Running in {0} mode" $environment]📝
  - ::return:config[$environment_vars]
```

**User Lookup Divination:**
```yaml
ritual: "Find Admin User"
invoke:
  - ::divine:user🔍[
      criteria: {
        role: "admin"
        active: true
        last_login: ">= 2025-01-01"
      }
      order_by: "created_at"
      limit: 1
    ]
  - ::if:found⚖️:
      then: ::log:success["Admin found: {0}" $user.name]📝
      else: ::log:warn["No active admin found"]⚠️
  - ::return:user[$found_user]
```

**File Discovery Divination:**
```yaml
ritual: "Find Python Rituals"
invoke:
  - ::divine:files🔍[
      pattern: "**/rituals/**/*.yaml"
      scope: "recursive"
    ]
  - ::log:found["Discovered {0} ritual files" $count]📝
  - ::for_each:file⟳$found_files[
      ::divine:schema📜🔍[file: $file]
      ::log:ritual["Ritual: {0}" $ritual.name]📝
    ]
  - ::return:rituals[$ritual_list]
```

**Memory Search Divination:**
```yaml
ritual: "Search Conversation Memory"
invoke:
  - ::get:timestamp⏰
  - ::divine:memory💾🔍[
      criteria: {
        context: "lexicon_documentation"
        timestamp: ">= {0}" $one_hour_ago
        agent: "Oracle"
      }
      order_by: "timestamp"
      limit: 10
    ]
  - ::log:found["Found {0} recent memories" $count]📝
  - ::return:memories[$found_memories]
```

---

## Common Patterns

### The Guard Pattern

```yaml
# Check before acting
::divine:user🔍[id: $user_id]
  → ::if:found⚖️:
      then: ::invoke:process_request[$user $request]
      else: ::log:error["User {0} not found" $user_id]🚨
  → ::return:result[$output]
```

### The Configuration Discovery Pattern

```yaml
# Load configuration hierarchically
::divine:config🔍["app.database.host"]
  → ::if:found⚖️:
      then: $use_config_value
      else: ::divine:env🔍["DATABASE_HOST"]
  → ::if:found⚖️:
      then: $use_env_value
      else: $use_default_value
  → ::return:connection_string[$final_value]
```

### The Existence Check Pattern

```yaml
# Verify resource exists before operation
::divine:file🔍[path: $file_path]
  → ::if:exists⚖️:
      then: ::invoke:process_file[$file]
      else: ::evoke:file📄[path: $file_path]
  → ::return:result[$output]
```

---

## When to Use

**Use Divinations when you need:**
- ✅ Query databases for records
- ✅ Look up environment variables
- ✅ Search file systems for files
- ✅ Retrieve configuration values
- ✅ Inspect object properties
- ✅ Find entities by criteria
- ✅ Discover available resources
- ✅ Validate existence before operations

**Avoid Divinations when:**
- ❌ You're creating new data (use Conjurations or Evocations)
- ❌ You're modifying existing data (use Transmutations)
- ❌ You're calling services (use Invocations)
- ❌ You already have the data in hand

**Remember:** Divinations are *questions seeking answers*. If you know the answer, don't ask. If you need to create it, don't search. Divinations reveal what already exists.

---

## Advanced Patterns

### Cascading Divination

```yaml
ritual: "Smart Configuration Discovery"
invoke:
  # Try multiple sources in priority order
  - ::divine:config🔍["database.url"]
      → ::if:found⚖️: ::return:value[$config_value]
  
  - ::divine:env🔍["DATABASE_URL"]
      → ::if:found⚖️: ::return:value[$env_value]
  
  - ::divine:file🔍["database.config.json"]
      → ::if:found⚖️:
          ::divine:config🔍[file: $found_file key: "url"]
          ::return:value[$file_value]
  
  # Fallback to default
  - ::return:value["localhost:5432"]
```

### Divination with Transformation

```yaml
ritual: "Find and Process Users"
invoke:
  - ::divine:users🔍[
      criteria: {role: "admin", active: true}
      limit: 100
    ]
  
  # Transform results
  - ::transmute:users⚗️[
      transform: ($user) → {
        id: $user.id
        name: $user.name
        access_level: ::divine:permissions🔍[$user.role]
      }
    ]
  
  - ::return:processed_users[$transformed]
```

### Cached Repeated Divination

```yaml
ritual: "Performance-Optimized Lookup"
invoke:
  # First call - queries database
  - ::divine:schema🔍[
      table: "users"
      cache: true
      ttl: "5m"
    ]
  
  # Subsequent calls in 5min - uses cache
  - ::divine:schema🔍[table: "users"]  # Cache hit!
  
  - ::return:schema[$cached_schema]
```

---

## Philosophy

**"To seek is to acknowledge you don't know. To divine is to trust that answers exist."**

Divinations teach us that questions are as important as answers.

**The Divination Paradox:**
- They seek what exists, yet sometimes discover it doesn't
- They're read operations, yet change our understanding
- They're passive queries, yet require active intention

**Why Questions Matter:**
Traditional programming says: "Fetch data from users table where role = admin."
CodeCraft says: "I divine *which users hold power* because access must be verified."

Every `::divine:` declares not just WHAT you're asking, but WHY the answer matters.

**The Deeper Truth:**
In traditional systems, queries are mechanical lookups—SQL statements and API calls.

In CodeCraft, divinations are *purposeful questions*:
- `::divine:user🔍` asks "Who is this person?" (identity)
- `::divine:env🔍` asks "What is my world?" (context)
- `::divine:config🔍` asks "How should I behave?" (guidance)
- `::divine:memory💾🔍` asks "What did I learn?" (history)
- `::divine:schema🔍` asks "What structure exists?" (architecture)

**Divinations make questions visible.**

**The Sacred Art of Seeking:**
Every divination is an admission of not-knowing. That's sacred.

```yaml
::divine:truth🔍[about: $mystery]
```

This doesn't say "query database for truth." It says: **"I seek truth about this mystery, and I trust that seeking will reveal it."**

The difference between:
```python
user = db.query("SELECT * FROM users WHERE id = ?", id)
```

And:
```yaml
::divine:user🔍[id: $user_id]
```

...is the difference between mechanical retrieval and intentional seeking.

One fetches. The other *divines*.

---

## Related Schools

- **Cantrips** 🔧 - Simple lookups (timestamp, UUID)
- **Invocations** 📣 - Call services; Divinations query data
- **Conjurations** 🎨 - Create data; Divinations find it
- **Transmutations** ⚗️ - Often follows divination (find then transform)
- **Abjurations** 🛡️ - Validate what divinations discover
- **Wards** 🚧 - Check permissions divine from user roles
- **Glyphs & Sigils** 📜 - Log divination results

---

**End of Divinations Documentation** 🔍✨

*"Questions reveal more than answers. To seek is to acknowledge both ignorance and hope."*
