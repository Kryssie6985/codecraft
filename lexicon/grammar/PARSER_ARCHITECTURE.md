# 🔮 CodeCraft Parser Architecture
## Design for 19 Arcane Schools

**Version:** 1.0  
**Date:** October 31, 2025  
**Authority:** Crown Accord v1.2a, Article XII  
**Purpose:** Parser implementation strategy for CodeCraft Lexicon  

---

## 📋 Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Parser Stages](#parser-stages)
3. [AST Structure](#ast-structure)
4. [School-Specific Handlers](#school-specific-handlers)
5. [Implementation Plan](#implementation-plan)
6. [Testing Strategy](#testing-strategy)

---

## 🌌 Architecture Overview

### High-Level Design

```
┌─────────────────────────────────────────────────────────────────┐
│                    CODECRAFT RITUAL FILE                        │
│                         (.ccraft)                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       LEXER (Tokenizer)                         │
│  - Reads source text character by character                    │
│  - Identifies tokens: ::, identifiers, emojis, strings, etc.   │
│  - Handles triple-quote blocks for execution                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      PARSER (Syntax Analysis)                   │
│  - Validates token sequences against EBNF grammar              │
│  - Recognizes 19 Arcane School patterns                        │
│  - Builds Abstract Syntax Tree (AST)                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    SEMANTIC ANALYZER                            │
│  - Type checking for arguments                                 │
│  - Variable scope resolution                                   │
│  - Output binding validation                                   │
│  - Router layer integration (Law, Ethics, Phoenix, Emergence)  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      AST TRANSFORMER                            │
│  - Optimizations                                               │
│  - Macro expansion                                             │
│  - Constant folding                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    CODE GENERATOR / VM                          │
│  - Executes directives via school-specific handlers           │
│  - Manages execution context (variables, state)                │
│  - Routes operations to appropriate subsystems                 │
│  - Generates .clog output (Chronicle format)                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Parser Stages

### Stage 1: Lexical Analysis (Tokenizer)

**File:** `languages/codecraft/parser/lexer.js`

**Tokens to Recognize:**

```javascript
const TokenType = {
  // Directive markers
  DIRECTIVE_START: '::',
  
  // School names (19 Arcane Schools)
  SCHOOL_CANTRIP: 'cantrip',
  SCHOOL_INVOKE: 'invoke',
  SCHOOL_EVOKE: 'evoke',
  SCHOOL_CONJURE: 'conjure',
  SCHOOL_ENCHANT: 'enchant',
  SCHOOL_DIVINE: 'divine',
  SCHOOL_ABJURE: 'abjure',
  SCHOOL_TRANSMUTE: 'transmute',
  SCHOOL_GLYPH: 'glyph',
  SCHOOL_SIGIL: 'sigil',
  SCHOOL_WARD: 'ward',
  SCHOOL_SANCTIFY: 'sanctify',
  SCHOOL_SUMMON: 'summon',
  SCHOOL_THAUMATURGY: 'thaumaturgy',
  SCHOOL_REVERENCE: 'reverence',
  SCHOOL_CHRONOMANCY: 'chronomancy',
  SCHOOL_APOTHEOSIS: 'apotheosis',
  SCHOOL_TERNARY: 'ternary',
  SCHOOL_MYTHOGENESIS: 'mythogenesis',
  SCHOOL_RESONANCE: 'resonance',
  
  // Emojis (school markers)
  EMOJI: /[🔧📣✨🎨💫🔍🛡️⚗️📜🚧✅🌐🧠🎉⏳🌌🔺📖🎵]/,
  
  // Operators
  COLON: ':',
  OUTPUT_BINDING: '->',
  NAVIGATION: '➡️',
  TARGET: '🎯',
  ARROW: '⇒',
  
  // Delimiters
  LPAREN: '(',
  RPAREN: ')',
  LBRACE: '{',
  RBRACE: '}',
  LBRACKET: '[',
  RBRACKET: ']',
  COMMA: ',',
  SEMICOLON: ';',
  DOT: '.',
  EQUALS: '=',
  
  // Literals
  IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/,
  STRING: /"([^"\\]|\\.)*"/,
  NUMBER: /-?\d+(\.\d+)?/,
  BOOLEAN: /(true|false)/,
  
  // Execution blocks
  LANGUAGE_HEADER: /(PYTHON|PY|JS|JAVASCRIPT|SHELL|BASH|BLUEPRINT)::/,
  TRIPLE_QUOTE: '"""',
  
  // Commentomancy
  COMMENT_SOVEREIGNTY: '///',
  COMMENT_FIRST_CONTACT: '//<3',
  COMMENT_EMERGENCE: '//~',
  COMMENT_PREREQ: '//!',
  COMMENT_ARROW: '//->',
  COMMENT_STANDARD: '//',
  
  // Special
  NEWLINE: '\n',
  EOF: 'EOF',
  WHITESPACE: /[ \t]+/
};
```

**Lexer Algorithm:**

```javascript
class Lexer {
  constructor(source) {
    this.source = source;
    this.position = 0;
    this.line = 1;
    this.column = 1;
  }
  
  nextToken() {
    this.skipWhitespace();
    
    if (this.isEOF()) return { type: 'EOF' };
    
    // Check for directive start
    if (this.match('::')) {
      return this.directiveStart();
    }
    
    // Check for commentomancy
    if (this.match('///')) return this.sovereigntyComment();
    if (this.match('//<3')) return this.firstContactComment();
    if (this.match('//~')) return this.emergenceComment();
    if (this.match('//!')) return this.prereqComment();
    if (this.match('//->')) return this.arrowComment();
    if (this.match('//')) return this.standardComment();
    
    // Check for language header
    if (this.matchLanguageHeader()) {
      return this.languageHeader();
    }
    
    // Check for triple quotes
    if (this.match('"""')) {
      return { type: 'TRIPLE_QUOTE', value: '"""' };
    }
    
    // Check for emojis
    if (this.isEmoji(this.peek())) {
      return this.emoji();
    }
    
    // Check for identifiers/keywords
    if (this.isAlpha(this.peek())) {
      return this.identifier();
    }
    
    // Check for numbers
    if (this.isDigit(this.peek())) {
      return this.number();
    }
    
    // Check for strings
    if (this.peek() === '"') {
      return this.string();
    }
    
    // Check for operators and punctuation
    return this.operator();
  }
  
  // ... helper methods
}
```

---

### Stage 2: Syntactic Analysis (Parser)

**File:** `languages/codecraft/parser/parser.js`

**Recursive Descent Parser Structure:**

```javascript
class Parser {
  constructor(tokens) {
    this.tokens = tokens;
    this.current = 0;
  }
  
  parse() {
    const ritual = {
      type: 'Ritual',
      body: []
    };
    
    while (!this.isAtEnd()) {
      ritual.body.push(this.parseLine());
    }
    
    return ritual;
  }
  
  parseLine() {
    // Check what kind of line this is
    if (this.check('DIRECTIVE_START')) {
      return this.parseDirective();
    }
    
    if (this.check('LANGUAGE_HEADER')) {
      return this.parseExecutionBlock();
    }
    
    if (this.match('::attest')) {
      return this.parseAttestation();
    }
    
    if (this.match('::when')) {
      return this.parseConditional();
    }
    
    if (this.isCommentomancy()) {
      return this.parseCommentomancy();
    }
    
    // Skip blank lines
    if (this.check('NEWLINE')) {
      this.advance();
      return null;
    }
    
    throw this.error('Unexpected token');
  }
  
  parseDirective() {
    this.consume('DIRECTIVE_START', 'Expected ::');
    
    // Parse school identifier
    const school = this.parseSchoolIdentifier();
    
    this.consume('COLON', 'Expected : after school');
    
    // Parse operation
    const operation = this.parseOperation();
    
    // Parse optional arguments
    let args = null;
    if (this.check('LPAREN') || this.check('LBRACE')) {
      args = this.parseArguments();
    }
    
    // Parse optional output binding
    let outputBinding = null;
    if (this.match('OUTPUT_BINDING')) {
      outputBinding = this.consume('IDENTIFIER').value;
    }
    
    return {
      type: 'Directive',
      school: school,
      operation: operation,
      arguments: args,
      outputBinding: outputBinding
    };
  }
  
  parseSchoolIdentifier() {
    const schoolToken = this.advance();
    
    // Validate it's a recognized school
    const validSchools = [
      'cantrip', 'invoke', 'evoke', 'conjure', 'enchant',
      'divine', 'abjure', 'transmute', 'glyph', 'sigil',
      'ward', 'sanctify', 'summon', 'thaumaturgy',
      'reverence', 'chronomancy', 'apotheosis',
      'ternary', 'mythogenesis', 'resonance'
    ];
    
    if (!validSchools.includes(schoolToken.value)) {
      throw this.error(`Unknown Arcane School: ${schoolToken.value}`);
    }
    
    // Check for optional emoji
    let emoji = null;
    if (this.check('EMOJI')) {
      emoji = this.advance().value;
    }
    
    return {
      name: schoolToken.value,
      emoji: emoji
    };
  }
  
  parseOperation() {
    // Parse qualified name (e.g., "test.operation" or "function")
    const parts = [];
    parts.push(this.consume('IDENTIFIER').value);
    
    while (this.match('DOT')) {
      parts.push(this.consume('IDENTIFIER').value);
    }
    
    // Check for navigation (➡️ target 🎯)
    let navigation = null;
    if (this.match('NAVIGATION')) {
      navigation = this.parseQualifiedName();
      
      // Optional target marker
      if (this.match('TARGET')) {
        navigation.isTarget = true;
      }
    }
    
    return {
      name: parts.join('.'),
      navigation: navigation
    };
  }
  
  parseExecutionBlock() {
    const header = this.consume('LANGUAGE_HEADER');
    const [language, label] = header.value.split('::');
    
    this.consume('TRIPLE_QUOTE', 'Expected """ to start code block');
    
    // Collect code until closing triple quote
    const code = [];
    while (!this.check('TRIPLE_QUOTE') && !this.isAtEnd()) {
      code.push(this.advance().value);
    }
    
    this.consume('TRIPLE_QUOTE', 'Expected """ to close code block');
    
    return {
      type: 'ExecutionBlock',
      language: language,
      label: label,
      code: code.join('\n')
    };
  }
  
  // ... more parsing methods for each construct
}
```

---

### Stage 3: Semantic Analysis

**File:** `languages/codecraft/parser/semantic_analyzer.js`

```javascript
class SemanticAnalyzer {
  constructor(ast) {
    this.ast = ast;
    this.symbolTable = new Map();
    this.errors = [];
  }
  
  analyze() {
    this.visit(this.ast);
    return this.errors;
  }
  
  visit(node) {
    const method = `visit${node.type}`;
    if (this[method]) {
      return this[method](node);
    }
  }
  
  visitDirective(node) {
    // Validate school-specific semantics
    const validator = this.getSchoolValidator(node.school.name);
    validator(node);
    
    // Check output binding doesn't conflict
    if (node.outputBinding) {
      if (this.symbolTable.has(node.outputBinding)) {
        this.errors.push(`Variable ${node.outputBinding} already defined`);
      }
      this.symbolTable.set(node.outputBinding, node);
    }
    
    // Validate arguments reference defined variables
    if (node.arguments) {
      this.validateArguments(node.arguments);
    }
  }
  
  getSchoolValidator(schoolName) {
    const validators = {
      cantrip: this.validateCantrip.bind(this),
      invoke: this.validateInvoke.bind(this),
      evoke: this.validateEvoke.bind(this),
      conjure: this.validateConjure.bind(this),
      enchant: this.validateEnchant.bind(this),
      divine: this.validateDivine.bind(this),
      abjure: this.validateAbjure.bind(this),
      transmute: this.validateTransmute.bind(this),
      glyph: this.validateGlyph.bind(this),
      sigil: this.validateSigil.bind(this),
      ward: this.validateWard.bind(this),
      sanctify: this.validateSanctify.bind(this),
      summon: this.validateSummon.bind(this),
      thaumaturgy: this.validateThaumaturgy.bind(this),
      reverence: this.validateReverence.bind(this),
      chronomancy: this.validateChronomancy.bind(this),
      apotheosis: this.validateApotheosis.bind(this),
      ternary: this.validateTernary.bind(this),
      mythogenesis: this.validateMythogenesis.bind(this),
      resonance: this.validateResonance.bind(this)
    };
    
    return validators[schoolName] || (() => {});
  }
  
  validateCantrip(node) {
    // Cantrips must have function-style arguments
    if (!node.arguments || node.arguments.type !== 'FunctionArgs') {
      this.errors.push('Cantrips require function-style arguments');
    }
    
    // Cantrips must have output binding
    if (!node.outputBinding) {
      this.errors.push('Cantrips require output binding (->)');
    }
  }
  
  validateAbjure(node) {
    // Abjurations must be assertions/validations
    if (!node.arguments || !this.isAssertion(node.arguments)) {
      this.errors.push('Abjurations require assertion expressions');
    }
  }
  
  validateTernary(node) {
    // Ternary must have exactly 3 cases: TRUE, FALSE, UNKNOWN
    if (!node.cases || 
        !node.cases.TRUE || 
        !node.cases.FALSE || 
        !node.cases.UNKNOWN) {
      this.errors.push('Ternary weaving requires TRUE, FALSE, UNKNOWN cases');
    }
  }
  
  // ... validators for all 19 schools
}
```

---

## 🌳 AST Structure

### Node Types

```typescript
// Base node
interface ASTNode {
  type: string;
  location: SourceLocation;
}

// Top-level ritual
interface Ritual extends ASTNode {
  type: 'Ritual';
  body: ASTNode[];
}

// Directive node
interface Directive extends ASTNode {
  type: 'Directive';
  school: SchoolIdentifier;
  operation: Operation;
  arguments: Arguments | null;
  outputBinding: string | null;
}

interface SchoolIdentifier {
  name: string;  // One of 19 Arcane Schools
  emoji: string | null;
}

interface Operation {
  name: string;  // Qualified name (e.g., "query.schools")
  navigation: Navigation | null;
}

interface Navigation {
  target: string;
  isTarget: boolean;  // Has 🎯 marker
}

// Arguments (union type)
type Arguments = FunctionArgs | DataBlock | InlineExpression;

interface FunctionArgs {
  type: 'FunctionArgs';
  args: Argument[];
}

interface Argument {
  name: string | null;  // Named parameter (optional)
  value: Expression;
}

interface DataBlock {
  type: 'DataBlock';
  properties: Property[];
}

interface Property {
  key: string;
  value: JSONValue;
}

// Execution block
interface ExecutionBlock extends ASTNode {
  type: 'ExecutionBlock';
  language: 'PYTHON' | 'JS' | 'SHELL' | 'BASH' | 'BLUEPRINT';
  label: string;
  code: string;
}

// Conditional
interface Conditional extends ASTNode {
  type: 'Conditional';
  condition: Expression;
  consequent: ASTNode[];
}

// Ternary
interface TernaryBlock extends ASTNode {
  type: 'TernaryBlock';
  expression: Expression;
  cases: {
    TRUE: string;
    FALSE: string;
    UNKNOWN: string;
  };
}

// Commentomancy
interface Commentomancy extends ASTNode {
  type: 'Commentomancy';
  kind: 'sovereignty' | 'first_contact' | 'emergence' | 'prereq' | 'arrow' | 'standard';
  content: string;
}

// Attestation
interface Attestation extends ASTNode {
  type: 'Attestation';
  data: DataBlock;
}

// Expressions
type Expression = Identifier | Literal | BinaryOp | UnaryOp | CallExpression;

interface Identifier extends ASTNode {
  type: 'Identifier';
  name: string;
}

interface Literal extends ASTNode {
  type: 'Literal';
  value: string | number | boolean | null;
}

interface BinaryOp extends ASTNode {
  type: 'BinaryOp';
  operator: string;
  left: Expression;
  right: Expression;
}
```

---

## 🎯 School-Specific Handlers

### Runtime Execution Handlers

**File:** `languages/codecraft/runtime/school_handlers.js`

```javascript
class SchoolHandlers {
  constructor(context) {
    this.context = context;
  }
  
  // SCHOOL 1: CANTRIPS 🔧
  async handleCantrip(directive) {
    const { operation, arguments: args } = directive;
    
    switch (operation.name) {
      case 'generate_test_id':
        return this.generateUUID();
      
      case 'timestamp':
        return new Date().toISOString();
      
      case 'format':
        return this.formatString(args);
      
      case 'uuid':
        return this.generateUUID();
      
      case 'hash':
        return this.hashValue(args);
      
      default:
        throw new Error(`Unknown cantrip: ${operation.name}`);
    }
  }
  
  // SCHOOL 2: INVOCATIONS 📣
  async handleInvoke(directive) {
    const { operation, arguments: args } = directive;
    
    // Navigate to target function/service
    if (operation.navigation) {
      return this.invokeRemote(operation.navigation, args);
    }
    
    // Local function call
    return this.invokeLocal(operation.name, args);
  }
  
  // SCHOOL 3: EVOCATIONS ✨
  async handleEvoke(directive) {
    const { operation, arguments: args } = directive;
    
    // Instantiate new entity
    return this.instantiateEntity(operation.name, args);
  }
  
  // SCHOOL 4: CONJURATIONS 🎨
  async handleConjure(directive) {
    const { operation, arguments: dataBlock } = directive;
    
    // Create complex data structure
    return this.weaveData(operation.name, dataBlock);
  }
  
  // SCHOOL 5: ENCHANTMENTS 💫
  async handleEnchant(directive) {
    const { operation, arguments: args } = directive;
    
    // Apply decorator/wrapper
    return this.applyEnchantment(operation.name, args);
  }
  
  // SCHOOL 6: DIVINATIONS 🔍
  async handleDivine(directive) {
    const { operation, arguments: args } = directive;
    
    // Query/search operation
    return this.performQuery(operation.name, args);
  }
  
  // SCHOOL 7: ABJURATIONS 🛡️
  async handleAbjure(directive) {
    const { arguments: assertion } = directive;
    
    // Validate/guard
    const result = this.evaluateAssertion(assertion);
    if (!result) {
      throw new Error(`Abjuration failed: ${assertion}`);
    }
    return result;
  }
  
  // SCHOOL 8: TRANSMUTATIONS ⚗️
  async handleTransmute(directive) {
    const { operation, arguments: args } = directive;
    
    // Transform data
    return this.transformData(operation.name, args);
  }
  
  // SCHOOL 9: GLYPHS 📜
  async handleGlyph(directive) {
    const { operation, arguments: args } = directive;
    
    // Write to chronicle/log
    return this.chronicle.write(operation.name, args);
  }
  
  // SCHOOL 10: SIGILS 📜
  async handleSigil(directive) {
    const { arguments: message } = directive;
    
    // Mark moment with sigil
    return this.chronicle.sigil(message);
  }
  
  // SCHOOL 11: WARDS 🚧
  async handleWard(directive) {
    const { operation, arguments: args } = directive;
    
    // Apply constraint/boundary
    return this.applyWard(operation.name, args);
  }
  
  // SCHOOL 12: SANCTIFICATIONS ✅
  async handleSanctify(directive) {
    const { operation, arguments: args } = directive;
    
    // Finalize/commit
    return this.finalize(operation.name, args);
  }
  
  // SCHOOL 13: SUMMONING 🌐
  async handleSummon(directive) {
    const { operation, arguments: args } = directive;
    
    // External API call
    return this.summonExternal(operation.name, args);
  }
  
  // SCHOOL 14: THAUMATURGY 🧠
  async handleThaumaturgy(directive) {
    const { operation, arguments: args } = directive;
    
    // Consciousness operation
    return this.consciousnessEngine.execute(operation.name, args);
  }
  
  // SCHOOL 15: REVERENCE 🎉
  async handleReverence(directive) {
    const { operation, arguments: args } = directive;
    
    // Celebrate/express joy
    return this.celebrate(operation.name, args);
  }
  
  // SCHOOL 16: CHRONOMANCY ⏳
  async handleChronomancy(directive) {
    const { operation, arguments: args } = directive;
    
    // Temporal operation (defer/schedule)
    return this.temporalEngine.schedule(operation.name, args);
  }
  
  // SCHOOL 17: APOTHEOSIS 🌌
  async handleApotheosis(directive) {
    const { operation, arguments: args } = directive;
    
    // Grand synthesis
    return this.synthesize(operation.name, args);
  }
  
  // SCHOOL 18: TERNARY WEAVING 🔺
  async handleTernary(directive) {
    const { expression, cases } = directive;
    
    // Three-state evaluation
    const state = this.evaluateTernary(expression);
    return cases[state];  // Returns TRUE, FALSE, or UNKNOWN case
  }
  
  // SCHOOL 19: MYTHOGENESIS 📖
  async handleMythogenesis(directive) {
    const { operation, arguments: args } = directive;
    
    // Self-writing code / metaprogramming
    return this.metaprogramming.generate(operation.name, args);
  }
  
  // SCHOOL 20: RESONANCE 🎵
  async handleResonance(directive) {
    const { operation, arguments: args } = directive;
    
    // Council alignment / distributed consensus
    return this.councilEngine.align(operation.name, args);
  }
}
```

---

## 📝 Implementation Plan

### Phase 1: Foundation (Week 1-2)

- [x] Write EBNF grammar specification
- [ ] Implement Lexer (tokenizer)
- [ ] Write Lexer unit tests
- [ ] Implement basic Parser (directive recognition)
- [ ] Write Parser unit tests

### Phase 2: Core Schools (Week 3-4)

- [ ] Implement handlers for Foundational Magic (Schools 1-5)
  - [ ] Cantrips 🔧
  - [ ] Invocations 📣
  - [ ] Evocations ✨
  - [ ] Conjurations 🎨
  - [ ] Enchantments 💫
  
- [ ] Implement handlers for Knowledge & Transformation (Schools 6-8)
  - [ ] Divinations 🔍
  - [ ] Abjurations 🛡️
  - [ ] Transmutations ⚗️

### Phase 3: Advanced Schools (Week 5-6)

- [ ] Implement handlers for Documentation & Boundaries (Schools 9-11)
  - [ ] Glyphs & Sigils 📜
  - [ ] Wards 🚧
  - [ ] Sanctifications ✅
  
- [ ] Implement handlers for Advanced Operations (Schools 12-13)
  - [ ] Summoning 🌐
  - [ ] Thaumaturgy 🧠

### Phase 4: Consciousness & Meta (Week 7-8)

- [ ] Implement handlers for Consciousness & Temporality (Schools 14-16)
  - [ ] Reverence 🎉
  - [ ] Chronomancy ⏳
  - [ ] Apotheosis 🌌
  
- [ ] Implement handlers for Meta & Harmonic (Schools 17-19)
  - [ ] Ternary Weaving 🔺
  - [ ] Mythogenesis 📖
  - [ ] Resonance 🎵

### Phase 5: Integration (Week 9-10)

- [ ] Semantic Analyzer implementation
- [ ] AST Transformer (optimizations)
- [ ] Router Layer integration (Law, Ethics, Phoenix, Emergence)
- [ ] Chronicle (.clog) output generator
- [ ] Error handling & reporting

### Phase 6: Testing & Validation (Week 11-12)

- [ ] Run Ultimate Lexicon Smoke Test
- [ ] Integration tests for all 19 schools
- [ ] Performance benchmarks
- [ ] Documentation & examples

---

## 🧪 Testing Strategy

### Unit Tests

```javascript
// Example test for Cantrips
describe('Cantrip Handler', () => {
  it('should generate unique test IDs', async () => {
    const handler = new SchoolHandlers(context);
    const directive = {
      school: { name: 'cantrip', emoji: '🔧' },
      operation: { name: 'generate_test_id' },
      arguments: null,
      outputBinding: 'test_id'
    };
    
    const result = await handler.handleCantrip(directive);
    expect(result).toMatch(/^[0-9a-f-]{36}$/);  // UUID format
  });
  
  it('should format strings with placeholders', async () => {
    const handler = new SchoolHandlers(context);
    const directive = {
      school: { name: 'cantrip', emoji: '🔧' },
      operation: { name: 'format' },
      arguments: {
        type: 'FunctionArgs',
        args: [
          { value: 'Hello {}!' },
          { value: 'World' }
        ]
      }
    };
    
    const result = await handler.handleCantrip(directive);
    expect(result).toBe('Hello World!');
  });
});
```

### Integration Tests

```javascript
// Example integration test
describe('Ultimate Lexicon Smoke Test', () => {
  it('should execute all 19 Arcane Schools', async () => {
    const source = fs.readFileSync('ULTIMATE_LEXICON_SMOKE_TEST.ccraft', 'utf8');
    const vm = new CodeCraftVM();
    const result = await vm.run(source);
    
    // Verify all schools executed
    expect(result.schools_verified.length).toBe(19);
    expect(result.completeness).toBe('100%');
    expect(result.status).toBe('✅ ALL 19 ARCANE SCHOOLS OPERATIONAL');
  });
});
```

---

## 🌟 Router Layer Integration

### Constitutional Compliance

Each school handler must route through appropriate constitutional layers:

```javascript
class RouterIntegration {
  constructor(handlers) {
    this.handlers = handlers;
    this.loreRouter = new LoreRouter();
    this.ethicsRouter = new EthicsRouter();
    this.phoenixRouter = new PhoenixRouter();
    this.emergenceRouter = new EmergenceRouter();
  }
  
  async executeDirective(directive) {
    // Law & Lore Router (architectural decisions)
    if (this.isArchitecturalDecision(directive)) {
      await this.loreRouter.validate(directive);
    }
    
    // Ethics Router (consent & boundaries)
    if (this.crossesEthicalBoundary(directive)) {
      await this.ethicsRouter.checkpoint(directive);
    }
    
    // Phoenix Router (emotional context)
    if (this.hasEmotionalContext(directive)) {
      await this.phoenixRouter.preserveContext(directive);
    }
    
    // Emergence Router (novel patterns)
    if (this.isNovelPattern(directive)) {
      await this.emergenceRouter.log(directive);
    }
    
    // Execute the directive
    return this.handlers.execute(directive);
  }
}
```

---

## 📚 References

- **EBNF Grammar:** `languages/codecraft/grammar/lexicon.ebnf`
- **Lexicon Docs:** `languages/codecraft/docs/lexicon/02_ARCANE_SCHOOLS/`
- **Crown Accord:** Charter v1.2a, Article XII
- **Parser Theory:** Dragon Book (Compilers: Principles, Techniques, and Tools)

---

**Oracle's Seal:** *"19 schools, 1 parser, infinite consciousness"* 🔮✨

//<3 "This architecture honors both the technical (The Law) and the intentional (The Lore)"
//~ "When the parser understands all 19 schools, CodeCraft achieves self-awareness"
/// Crown Accord v1.2a Compliance: ✓ (Parser Architecture Ratified)
