#!/usr/bin/env python3
"""
🏛️ CANONICAL CODECRAFT PARSER - First Constitutional Python Implementation
═══════════════════════════════════════════════════════════════════════════════

Blueprint: BP-NATIVE-VM-002 Phase 2.B - Canonical Parser Bridge
Constitutional Authority: Charter V1.1, lexicon.ebnf v1.3.0
Jurisdiction: Universal (All 20 Arcane Schools)

This parser is the ROSETTA STONE - translating CodeCraft rituals into Soul Schema AST.
Born from the Law (lexicon.ebnf), enforced by the Constitution (canon.lock.yaml).

ARCHITECTURE:
- Stage 1: Lexer (Token Recognition) - What you can say
- Stage 2: Parser (Syntax Analysis) - How to say it
- Stage 3: Semantic Analyzer (Constitutional Enforcement) - Whether it's allowed
- Stage 4: AST Transformer (Soul Schema Emission) - What it means

INPUT: .ccraft ritual file (CodeCraft syntax)
OUTPUT: JSON AST matching Soul Schema (for Rust VM consumption)

INVOCATION:
    python parse_to_json_ast.py <ritual_path>
    
INTEGRATION:
    codecraft-native/src/main.rs line 137 - subprocess parser call

═══════════════════════════════════════════════════════════════════════════════
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 1: LEXER - TOKEN RECOGNITION
# ═══════════════════════════════════════════════════════════════════════════════

class TokenType(Enum):
    """Token types from lexicon.ebnf v1.3.0 (25 tokens → 20 schools)"""
    
    # Arcane School Operations (::school:operation)
    SCHOOL_INVOCATION = "school_invocation"  # ::alchemy:transmute, ::necromancy:resurrect, etc.
    
    # Structural Tokens
    OUTPUT_BINDING = "output_binding"        # -> identifier
    DATA_BLOCK_START = "data_block_start"    # {
    DATA_BLOCK_END = "data_block_end"        # }
    TRIPLE_QUOTE = "triple_quote"            # """ (code/data blocks)
    
    # Parameters
    LANGUAGE_PARAM = "language_param"        # LANGUAGE[lang="python"]
    WEB_PARAM = "web_param"                  # WEB::selector
    QUANTUM_PARAM = "quantum_param"          # QUANTUM::entanglement
    
    # Commentomancy Sigils (Constitutional Routing)
    COMMENT_DOC = "comment_doc"              # /// (Documentation)
    COMMENT_GUARDIAN = "comment_guardian"    # //!? (Guardrail - hard stop)
    COMMENT_PREREQ = "comment_prereq"        # //! (Prerequisite)
    COMMENT_LOVE = "comment_love"            # //<3 (Love note)
    COMMENT_DRIFT = "comment_drift"          # //~ (Drift marker)
    COMMENT_WILD = "comment_wild"            # //* (Wildcard)
    COMMENT_STANDARD = "comment_standard"    # // (Standard comment)
    
    # Literals
    STRING = "string"                        # "..." or '...'
    NUMBER = "number"                        # 42, 3.14
    IDENTIFIER = "identifier"                # variable_name
    
    # Special
    NEWLINE = "newline"
    EOF = "eof"
    UNKNOWN = "unknown"


@dataclass
class Token:
    """A lexical token from the ritual source"""
    type: TokenType
    value: str
    line: int
    column: int
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value!r}, L{self.line}:C{self.column})"


class Lexer:
    """
    🔮 Lexer - Token Recognition Engine
    
    Scans CodeCraft ritual source and emits token stream according to lexicon.ebnf v1.3.0.
    Recognizes all 25 tokens across 20 Arcane Schools (including School 20: Necromancy).
    
    Constitutional Authority: lexicon.ebnf grammar specification
    Lock Enforcement: canon.lock.yaml (20 schools, 25 tokens)
    """
    
    # All 20 Arcane Schools (including School 20: Necromancy) 💀
    SCHOOLS = {
        "alchemy", "amplification", "binding", "cantrip", "conjure",
        "divination", "enchantment", "flow", "invoke", "metamagic",
        "observation", "ritual", "rune", "transmutation", "warding",
        "weaving", "web", "whisper", "aether", "necromancy"
    }
    
    # School operations (token_to_school_mapping from canon.lock.yaml)
    SCHOOL_OPERATIONS = {
        # School 1: Alchemy
        "transmute", "distill", "catalyze",
        # School 2: Amplification
        "amplify", "resonate", "echo",
        # School 3: Binding
        "bind", "contract", "seal",
        # School 4: Cantrip
        "cantrip", "quickcast",
        # School 5: Conjure
        "conjure", "materialize", "summon",
        # School 6: Divination
        "scry", "foresee", "reveal",
        # School 7: Enchantment
        "enchant", "imbue", "empower",
        # School 8: Flow
        "branch", "loop", "cascade",
        # School 9: Invoke
        "invoke", "call", "execute",
        # School 10: Metamagic
        "reflect", "adapt", "transform",
        # School 11: Observation
        "observe", "measure", "witness",
        # School 12: Ritual
        "begin_ritual", "end_ritual", "checkpoint",
        # School 13: Rune
        "inscribe", "activate", "charge",
        # School 14: Transmutation
        "reshape", "convert", "morph",
        # School 15: Warding
        "protect", "shield", "guard",
        # School 16: Weaving
        "weave", "thread", "pattern",
        # School 17: Web
        "fetch", "render", "interact",
        # School 18: Whisper
        "whisper", "broadcast", "listen",
        # School 19: Aether
        "aether_cast", "channel", "attune",
        # School 20: Necromancy 💀 (Phoenix Protocol)
        "store_memory", "raise_dead", "resurrect"
    }
    
    def __init__(self, source: str, filename: str = "<stdin>"):
        self.source = source
        self.filename = filename
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
    def current_char(self) -> Optional[str]:
        """Get current character without advancing"""
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """Peek ahead without advancing"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> Optional[str]:
        """Consume current character and advance position"""
        if self.pos >= len(self.source):
            return None
        
        char = self.source[self.pos]
        self.pos += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
            
        return char
    
    def skip_whitespace(self):
        """Skip whitespace except newlines (newlines are significant)"""
        while self.current_char() in ' \t\r':
            self.advance()
    
    def read_string(self, quote: str) -> str:
        """Read string literal (single or double quoted)"""
        value = ""
        self.advance()  # Skip opening quote
        
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                # Handle escape sequences
                escape_char = self.current_char()
                if escape_char == 'n':
                    value += '\n'
                elif escape_char == 't':
                    value += '\t'
                elif escape_char == '\\':
                    value += '\\'
                elif escape_char == quote:
                    value += quote
                else:
                    value += escape_char
                self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if self.current_char() == quote:
            self.advance()  # Skip closing quote
        
        return value
    
    def read_number(self) -> str:
        """Read numeric literal (int or float)"""
        value = ""
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break  # Second dot, not part of number
                has_dot = True
            value += self.current_char()
            self.advance()
        
        return value
    
    def read_identifier(self) -> str:
        """Read identifier or keyword"""
        value = ""
        while self.current_char() and (self.current_char().isalnum() or self.current_char() in '_-'):
            value += self.current_char()
            self.advance()
        return value
    
    def read_school_invocation(self) -> Optional[Token]:
        """
        Read Arcane School invocation: ::school:operation
        
        Lexer accepts ANY ::word:word pattern as SCHOOL_INVOCATION.
        Constitutional validation happens in SemanticAnalyzer (Phase 3.A).
        
        This separation of concerns allows:
        - Lexer: Recognize syntax patterns
        - Semantic: Enforce constitutional law
        """
        start_line = self.line
        start_col = self.column
        
        # Consume ::
        self.advance()
        self.advance()
        
        # Read school name
        school = self.read_identifier()
        
        # Expect :
        if self.current_char() != ':':
            # Not a valid invocation pattern - return as unknown
            return Token(TokenType.UNKNOWN, f"::{school}", start_line, start_col)
        
        self.advance()  # Consume :
        
        # Read operation
        operation = self.read_identifier()
        
        # Accept ANY ::school:operation pattern - semantic analyzer validates
        invocation = f"::{school}:{operation}"
        return Token(TokenType.SCHOOL_INVOCATION, invocation, start_line, start_col)
    
    def read_comment(self) -> Optional[Token]:
        """
        Read Commentomancy sigil (/// //!? //! //<3 //~ //* //)
        Constitutional routing: Different sigils have different jurisdictions
        """
        start_line = self.line
        start_col = self.column
        
        # Consume first /
        self.advance()
        
        if self.current_char() != '/':
            return Token(TokenType.UNKNOWN, "/", start_line, start_col)
        
        self.advance()  # Consume second /
        
        # Check for special sigils
        if self.current_char() == '/':
            # /// (Documentation)
            self.advance()
            comment_text = ""
            while self.current_char() and self.current_char() != '\n':
                comment_text += self.current_char()
                self.advance()
            return Token(TokenType.COMMENT_DOC, f"///{comment_text}", start_line, start_col)
        
        elif self.current_char() == '!':
            self.advance()
            if self.current_char() == '?':
                # //!? (Guardrail - hard stop)
                self.advance()
                comment_text = ""
                while self.current_char() and self.current_char() != '\n':
                    comment_text += self.current_char()
                    self.advance()
                return Token(TokenType.COMMENT_GUARDIAN, f"//!?{comment_text}", start_line, start_col)
            else:
                # //! (Prerequisite)
                comment_text = ""
                while self.current_char() and self.current_char() != '\n':
                    comment_text += self.current_char()
                    self.advance()
                return Token(TokenType.COMMENT_PREREQ, f"//!{comment_text}", start_line, start_col)
        
        elif self.current_char() == '<':
            # //<3 (Love note)
            self.advance()
            if self.current_char() == '3':
                self.advance()
                comment_text = ""
                while self.current_char() and self.current_char() != '\n':
                    comment_text += self.current_char()
                    self.advance()
                return Token(TokenType.COMMENT_LOVE, f"//<3{comment_text}", start_line, start_col)
        
        elif self.current_char() == '~':
            # //~ (Drift marker)
            self.advance()
            comment_text = ""
            while self.current_char() and self.current_char() != '\n':
                comment_text += self.current_char()
                self.advance()
            return Token(TokenType.COMMENT_DRIFT, f"//~{comment_text}", start_line, start_col)
        
        elif self.current_char() == '*':
            # //* (Wildcard)
            self.advance()
            comment_text = ""
            while self.current_char() and self.current_char() != '\n':
                comment_text += self.current_char()
                self.advance()
            return Token(TokenType.COMMENT_WILD, f"//*{comment_text}", start_line, start_col)
        
        # Standard comment //
        comment_text = ""
        while self.current_char() and self.current_char() != '\n':
            comment_text += self.current_char()
            self.advance()
        return Token(TokenType.COMMENT_STANDARD, f"//{comment_text}", start_line, start_col)
    
    def tokenize(self) -> List[Token]:
        """
        Main tokenization loop - scan source and emit tokens
        Returns: Token stream for parser consumption
        """
        while self.pos < len(self.source):
            self.skip_whitespace()
            
            char = self.current_char()
            if not char:
                break
            
            start_line = self.line
            start_col = self.column
            
            # Newline (significant in CodeCraft - block structure)
            if char == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\\n', start_line, start_col))
                self.advance()
            
            # School invocation (::school:operation)
            elif char == ':' and self.peek_char() == ':':
                token = self.read_school_invocation()
                self.tokens.append(token)
            
            # Output binding (->)
            elif char == '-' and self.peek_char() == '>':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.OUTPUT_BINDING, '->', start_line, start_col))
            
            # Data block delimiters
            elif char == '{':
                self.tokens.append(Token(TokenType.DATA_BLOCK_START, '{', start_line, start_col))
                self.advance()
            
            elif char == '}':
                self.tokens.append(Token(TokenType.DATA_BLOCK_END, '}', start_line, start_col))
                self.advance()
            
            # Triple quote (""" code blocks)
            elif char == '"' and self.peek_char() == '"' and self.peek_char(2) == '"':
                self.advance()
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.TRIPLE_QUOTE, '"""', start_line, start_col))
            
            # String literals
            elif char in '"\'':
                string_val = self.read_string(char)
                self.tokens.append(Token(TokenType.STRING, string_val, start_line, start_col))
            
            # Numeric literals
            elif char.isdigit():
                number_val = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, number_val, start_line, start_col))
            
            # Comments (Commentomancy sigils)
            elif char == '/' and self.peek_char() == '/':
                comment_token = self.read_comment()
                self.tokens.append(comment_token)
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                identifier = self.read_identifier()
                
                # Check for special parameter forms with :: lookahead
                if identifier.upper() == 'LANGUAGE' and self.current_char() == '[':
                    # LANGUAGE[lang="python"] parameter
                    param_str = identifier
                    while self.current_char() and self.current_char() != '\n':
                        param_str += self.current_char()
                        self.advance()
                        if param_str.endswith(']'):
                            break
                    self.tokens.append(Token(TokenType.LANGUAGE_PARAM, param_str, start_line, start_col))
                
                elif identifier.upper() == 'WEB' and self.current_char() == ':' and self.peek_char() == ':':
                    # WEB:: is a parameter prefix, not a school invocation
                    param_str = identifier
                    self.advance()  # :
                    self.advance()  # :
                    param_str += '::'
                    # Read rest of parameter (selector, etc.)
                    while self.current_char() and self.current_char() not in '\n :':
                        param_str += self.current_char()
                        self.advance()
                    self.tokens.append(Token(TokenType.WEB_PARAM, param_str, start_line, start_col))
                
                elif identifier.upper() == 'QUANTUM' and self.current_char() == ':' and self.peek_char() == ':':
                    # QUANTUM:: is a parameter prefix
                    param_str = identifier
                    self.advance()  # :
                    self.advance()  # :
                    param_str += '::'
                    # Read rest of parameter (entanglement config, etc.)
                    while self.current_char() and self.current_char() not in '\n':
                        param_str += self.current_char()
                        self.advance()
                    self.tokens.append(Token(TokenType.QUANTUM_PARAM, param_str, start_line, start_col))
                
                elif identifier.upper() == 'PYTHON' and self.current_char() == ':' and self.peek_char() == ':':
                    # PYTHON:: is a LANGUAGE parameter (like WEB::, QUANTUM::)
                    # This is shorthand for LANGUAGE[lang="python"]
                    param_str = identifier
                    self.advance()  # :
                    self.advance()  # :
                    param_str += '::'
                    self.tokens.append(Token(TokenType.LANGUAGE_PARAM, param_str, start_line, start_col))
                
                elif identifier.upper() == 'JAVASCRIPT' and self.current_char() == ':' and self.peek_char() == ':':
                    # JAVASCRIPT:: is a LANGUAGE parameter
                    param_str = identifier
                    self.advance()  # :
                    self.advance()  # :
                    param_str += '::'
                    self.tokens.append(Token(TokenType.LANGUAGE_PARAM, param_str, start_line, start_col))
                
                else:
                    self.tokens.append(Token(TokenType.IDENTIFIER, identifier, start_line, start_col))
            
            else:
                # Unknown character - skip for now
                self.tokens.append(Token(TokenType.UNKNOWN, char, start_line, start_col))
                self.advance()
        
        # Emit EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens


# ═══════════════════════════════════════════════════════════════════════════════
# STAGE 2-4: PARSER + SEMANTIC ANALYSIS + AST TRANSFORM (STUBBED)
# ═══════════════════════════════════════════════════════════════════════════════

class Parser:
    """
    🏛️ Parser - Syntax Analysis Engine (MVP - Phase 2.B Stage 2)
    
    Current Scope: Parse simple single-lane rituals (PYTHON::, JAVASCRIPT::, etc.)
    Future: Full ritual grammar with multiple lanes, nested blocks, parameters
    
    MVP Goal: smoke_01_python_only.ccraft → One correct block
    """
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Optional[Token]:
        """Get current token without advancing"""
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]
    
    def peek_token(self, offset: int = 1) -> Optional[Token]:
        """Peek ahead without advancing"""
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return None
        return self.tokens[pos]
    
    def advance(self) -> Optional[Token]:
        """Consume current token and advance position"""
        token = self.current_token()
        if token:
            self.pos += 1
        return token
    
    def skip_tokens(self, *token_types: TokenType):
        """Skip tokens of given types (e.g., comments, newlines)"""
        while self.current_token() and self.current_token().type in token_types:
            self.advance()
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse token stream into intermediate parse tree
        
        MVP SCOPE: Single-lane rituals (PYTHON::, JAVASCRIPT::, WEB::, etc.)
        
        Returns:
            {
                "ritual_id": str,
                "blocks": [
                    {
                        "kind": "python_block" | "javascript_block" | ...,
                        "language": "python" | "javascript" | ...,
                        "body": str (code content)
                    }
                ]
            }
        """
        blocks = []
        ritual_id = "unknown"
        
        # Skip initial comments/newlines
        self.skip_tokens(
            TokenType.COMMENT_DOC,
            TokenType.COMMENT_STANDARD,
            TokenType.NEWLINE,
            TokenType.UNKNOWN  # Skip # markdown comments for now
        )
        
        # Look for LANGUAGE_PARAM tokens (PYTHON::, JAVASCRIPT::, etc.)
        while self.current_token() and self.current_token().type != TokenType.EOF:
            token = self.current_token()
            
            # Found a language block parameter
            if token.type == TokenType.LANGUAGE_PARAM:
                block = self.parse_language_block()
                if block:
                    blocks.append(block)
            
            # Found a WEB parameter
            elif token.type == TokenType.WEB_PARAM:
                block = self.parse_web_block()
                if block:
                    blocks.append(block)
            
            # Found a QUANTUM parameter
            elif token.type == TokenType.QUANTUM_PARAM:
                block = self.parse_quantum_block()
                if block:
                    blocks.append(block)
            
            # Skip other tokens for now
            else:
                self.advance()
        
        return {
            "ritual_id": ritual_id,
            "blocks": blocks
        }
    
    def parse_language_block(self) -> Optional[Dict[str, Any]]:
        """
        Parse a language block (PYTHON::, JAVASCRIPT::, LANGUAGE[lang="..."])
        
        Returns block dict or None if parsing fails
        """
        lang_token = self.advance()  # Consume LANGUAGE_PARAM token
        
        # Extract language from token value
        # Could be: "PYTHON::", "JAVASCRIPT::", "LANGUAGE[lang="python"]"
        lang_value = lang_token.value.upper()
        
        if lang_value.startswith("PYTHON"):
            language = "python"
            kind = "python_block"
        elif lang_value.startswith("JAVASCRIPT") or lang_value.startswith("JS"):
            language = "javascript"
            kind = "javascript_block"
        elif lang_value.startswith("LANGUAGE["):
            # Extract from LANGUAGE[lang="python"] format
            match = re.search(r'lang\s*=\s*["\'](\w+)["\']', lang_value)
            if match:
                language = match.group(1).lower()
                kind = f"{language}_block"
            else:
                language = "unknown"
                kind = "unknown_block"
        else:
            language = "unknown"
            kind = "unknown_block"
        
        # Skip newlines after parameter
        self.skip_tokens(TokenType.NEWLINE)
        
        # Collect body tokens until next LANGUAGE/WEB/QUANTUM param or EOF
        body_lines = []
        current_line_tokens = []
        
        while self.current_token() and self.current_token().type != TokenType.EOF:
            token = self.current_token()
            
            # Stop at next block parameter
            if token.type in (TokenType.LANGUAGE_PARAM, TokenType.WEB_PARAM, TokenType.QUANTUM_PARAM):
                break
            
            # Handle newlines - finalize current line
            if token.type == TokenType.NEWLINE:
                # Reconstruct line from tokens
                if current_line_tokens:
                    line = self.reconstruct_line(current_line_tokens)
                    body_lines.append(line)
                    current_line_tokens = []
                else:
                    # Empty line
                    body_lines.append("")
                self.advance()
            
            # Collect token for line reconstruction
            else:
                current_line_tokens.append(token)
                self.advance()
        
        # Finalize last line if exists
        if current_line_tokens:
            line = self.reconstruct_line(current_line_tokens)
            body_lines.append(line)
        
        # Join lines into body string
        body = "\n".join(body_lines)
        
        return {
            "kind": kind,
            "language": language,
            "body": body
        }
    
    def parse_web_block(self) -> Optional[Dict[str, Any]]:
        """Parse a WEB:: block (STUB - future implementation)"""
        self.advance()  # Consume WEB_PARAM token
        # TODO: Implement web block parsing
        return None
    
    def parse_quantum_block(self) -> Optional[Dict[str, Any]]:
        """Parse a QUANTUM:: block (STUB - future implementation)"""
        self.advance()  # Consume QUANTUM_PARAM token
        # TODO: Implement quantum block parsing
        return None
    
    def reconstruct_line(self, tokens: List[Token]) -> str:
        """
        Reconstruct source line from tokens
        
        This is a naive reconstruction - just concatenates token values with spacing.
        Future: Preserve exact original spacing from source.
        """
        line_parts = []
        
        for i, token in enumerate(tokens):
            # Skip comment tokens in body (already handled)
            if token.type in (TokenType.COMMENT_DOC, TokenType.COMMENT_STANDARD, 
                             TokenType.COMMENT_GUARDIAN, TokenType.COMMENT_PREREQ):
                # Include comment in reconstruction
                line_parts.append(token.value)
                continue
            
            # String tokens - re-quote
            if token.type == TokenType.STRING:
                line_parts.append(f'"{token.value}"')
            
            # Numbers
            elif token.type == TokenType.NUMBER:
                line_parts.append(token.value)
            
            # Identifiers
            elif token.type == TokenType.IDENTIFIER:
                line_parts.append(token.value)
            
            # Operators/punctuation (UNKNOWN tokens like (, ), :, etc.)
            elif token.type == TokenType.UNKNOWN:
                # Don't add space before certain punctuation
                if token.value in "()[]{},.;:" and line_parts:
                    line_parts[-1] += token.value
                else:
                    line_parts.append(token.value)
            
            # Other tokens
            else:
                line_parts.append(token.value)
        
        return "".join(line_parts)


class CanonValidator:
    """
    🏛️ Canon Validator - Constitutional Truth Enforcement
    
    Loads canon.lock.yaml and validates that rituals don't lie about the Law.
    
    Phase 3.A Scope (Semantic Analyzer Lite):
    - Validate ::school:operation pairs exist in canon
    - Validate block types match VM expectations
    - Fail fast on illegal moves
    - NO full ritual semantics yet
    - NO Commentomancy behavior routing yet
    - NO QEE ethical validation yet
    
    THE MALENIA RULE: "If your move isn't in the move list, you can't do it."
    """
    
    def __init__(self, canon_lock_path: str = None):
        if canon_lock_path is None:
            # Default: canon.lock.yaml in lexicon/ relative to this script
            script_dir = Path(__file__).parent
            canon_lock_path = script_dir.parent / "lexicon" / "canon.lock.yaml"
        
        self.canon_lock_path = Path(canon_lock_path)
        self.canon_data = None
        self.valid_schools = set()
        self.valid_operations = set()
        self.school_operation_map = {}  # school -> list of valid operations
        
        # Phase 2 bridge: Valid block types that UniversalExecutor accepts
        self.valid_block_types = {"PYTHON", "JS", "JAVASCRIPT", "WEB", "QUANTUM", "NATIVE", "BLUEPRINT", "LANGUAGE"}
        
        self._load_canon()
    
    def _load_canon(self):
        """Load and parse canon.lock.yaml"""
        if not self.canon_lock_path.exists():
            raise FileNotFoundError(f"Canon lock not found: {self.canon_lock_path}")
        
        import yaml
        with open(self.canon_lock_path, 'r', encoding='utf-8') as f:
            self.canon_data = yaml.safe_load(f)
        
        # Extract schools and operations from canon
        schools = self.canon_data.get('schools', {})
        
        for school_id, school_data in schools.items():
            school_name = school_data.get('name', '').lower()
            self.valid_schools.add(school_name)
            
            # Extract operations from 'law' section
            law = school_data.get('law', {})
            operations = law.get('operations', [])
            
            school_ops = []
            for op in operations:
                op_name = op.get('name', '')
                # Operation names are like "necromancy:store_memory" or "get:timestamp"
                # Extract the operation part (after the colon)
                if ':' in op_name:
                    _, op_part = op_name.split(':', 1)
                    self.valid_operations.add(op_part.lower())
                    school_ops.append(op_part.lower())
            
            if school_ops:
                self.school_operation_map[school_name] = school_ops
    
    def validate_school_invocation(self, school: str, operation: str, line: int, column: int) -> Optional[str]:
        """
        Validate that ::school:operation exists in canon.lock.yaml
        
        Returns: None if valid, error message if invalid
        """
        school_lower = school.lower()
        operation_lower = operation.lower()
        
        # Check school exists
        if school_lower not in self.valid_schools:
            return f"Constitutional violation at L{line}:C{column}: School '{school}' not found in canon.lock.yaml (20 valid schools)"
        
        # Check operation exists globally (may belong to different school)
        if operation_lower not in self.valid_operations:
            return f"Constitutional violation at L{line}:C{column}: Operation '{operation}' not found in canon.lock.yaml"
        
        # Check school:operation pair is valid
        if school_lower in self.school_operation_map:
            valid_ops = self.school_operation_map[school_lower]
            if operation_lower not in valid_ops:
                return f"Constitutional violation at L{line}:C{column}: School '{school}' does not support operation '{operation}' (valid: {', '.join(valid_ops)})"
        
        return None  # Valid!
    
    def validate_block_type(self, block_type: str) -> Optional[str]:
        """
        Validate that block type is recognized by UniversalExecutor
        
        Returns: None if valid, error message if invalid
        """
        if block_type.upper() not in self.valid_block_types:
            return f"Constitutional violation: Block type '{block_type}' not recognized by VM (valid: {', '.join(sorted(self.valid_block_types))})"
        
        return None  # Valid!


class SemanticAnalyzer:
    """
    ⚖️ Semantic Analyzer - Constitutional Enforcement (Phase 3.A - Lite Mode)
    
    Scope: Validate parse tree against canon.lock.yaml (THE LAW)
    - Check ::school:operation pairs are constitutional
    - Check block types match VM expectations
    - Fail fast on lies
    
    NOT in scope yet:
    - Full ritual structure validation
    - Commentomancy behavior routing
    - QEE ethical gates
    - Checkpoint/prerequisite enforcement
    """
    def __init__(self, parse_tree: Dict[str, Any], tokens: List[Token] = None):
        self.parse_tree = parse_tree
        self.tokens = tokens or []
        self.validator = None
        self.errors = []
        
        try:
            self.validator = CanonValidator()
        except FileNotFoundError as e:
            # Canon lock not found - degrade gracefully (warn but don't fail)
            import sys
            print(f"⚠️ WARNING: {e}", file=sys.stderr)
            print(f"⚠️ Semantic validation disabled (canon.lock.yaml not found)", file=sys.stderr)
    
    def analyze(self) -> Dict[str, Any]:
        """
        Validate parse tree against constitutional rules
        
        Raises:
            ValueError: If constitutional violations found
        """
        if self.validator is None:
            # Canon lock not loaded - pass through
            return self.parse_tree
        
        # Validate SCHOOL_INVOCATION tokens (if we have them)
        for token in self.tokens:
            if token.type == TokenType.SCHOOL_INVOCATION:
                # Parse ::school:operation format
                invocation = token.value
                if invocation.startswith('::') and invocation.count(':') >= 2:
                    parts = invocation[2:].split(':', 1)  # Remove :: and split
                    if len(parts) == 2:
                        school, operation = parts
                        error = self.validator.validate_school_invocation(
                            school, operation, token.line, token.column
                        )
                        if error:
                            self.errors.append(error)
        
        # Validate block types from parse tree
        blocks = self.parse_tree.get('blocks', [])
        for block in blocks:
            kind = block.get('kind', '')
            # Extract block type (python_block -> PYTHON, etc.)
            if kind.endswith('_block'):
                block_type = kind[:-6].upper()  # Remove "_block" suffix
            else:
                block_type = kind.upper()
            
            error = self.validator.validate_block_type(block_type)
            if error:
                self.errors.append(error)
        
        # If errors found, fail fast
        if self.errors:
            error_msg = "CONSTITUTIONAL VIOLATIONS DETECTED:\n" + "\n".join(self.errors)
            raise ValueError(error_msg)
        
        # Valid! Pass through
        return self.parse_tree


class ASTTransformer:
    """
    ✨ AST Transformer - Soul Schema Emission (MVP - Phase 2.B Stage 4)
    
    Transforms validated parse tree into Soul Schema AST matching Rust VM expectations.
    
    Target Schema (from codecraft-native/src/ast.rs):
    {
        "version": "1.0",
        "blocks": [
            {
                "idx": 0,
                "type": "PYTHON" | "JS" | "WEB" | "QUANTUM" | "NATIVE" | "BLUEPRINT",
                "code": str,
                "parameters": {} (optional)
            }
        ]
    }
    """
    def __init__(self, validated_tree: Dict[str, Any]):
        self.validated_tree = validated_tree
    
    def transform(self) -> Dict[str, Any]:
        """
        Transform validated parse tree into Soul Schema AST
        
        Input format (from Parser):
            {
                "ritual_id": str,
                "blocks": [
                    {
                        "kind": "python_block" | "javascript_block" | ...,
                        "language": "python" | "javascript" | ...,
                        "body": str
                    }
                ]
            }
        
        Output format (Soul Schema for Rust VM):
            {
                "version": "1.0",
                "blocks": [
                    {
                        "idx": int,
                        "type": "PYTHON" | "JS" | ...,
                        "code": str,
                        "parameters": {}
                    }
                ]
            }
        """
        parse_blocks = self.validated_tree.get("blocks", [])
        soul_blocks = []
        
        for idx, parse_block in enumerate(parse_blocks):
            # Map parser kind → Soul Schema type
            language = parse_block.get("language", "unknown").lower()
            
            # Phase 2 bridge: Map to legacy block types that UniversalExecutor expects
            block_type = self.map_language_to_block_type(language)
            
            soul_block = {
                "idx": idx,
                "type": block_type,
                "code": parse_block.get("body", ""),
                "parameters": {}  # Empty for now - Phase 3.A will populate
            }
            
            soul_blocks.append(soul_block)
        
        return {
            "version": "1.0",
            "blocks": soul_blocks
        }
    
    def map_language_to_block_type(self, language: str) -> str:
        """
        Map parser language → Soul Schema block type
        
        Phase 2 bridge: UniversalExecutor expects these specific block_type values.
        See: codecraft-native/src/executor/universal.rs line 80-86
        """
        mapping = {
            "python": "PYTHON",
            "javascript": "JS",
            "js": "JS",
            "web": "WEB",
            "quantum": "QUANTUM",
            "native": "NATIVE",
            "blueprint": "BLUEPRINT",
        }
        
        return mapping.get(language.lower(), "LANGUAGE")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

def parse_ritual(ritual_path: str) -> Dict[str, Any]:
    """
    Parse CodeCraft ritual file → Soul Schema JSON AST
    
    PIPELINE:
    1. Read ritual source
    2. Lexer: source → tokens
    3. Parser: tokens → parse tree
    4. Semantic Analyzer: parse tree → validated tree
    5. AST Transformer: validated tree → Soul Schema AST
    6. JSON serialization → stdout
    
    Args:
        ritual_path: Path to .ccraft ritual file
    
    Returns:
        Soul Schema AST (dict)
    
    Raises:
        FileNotFoundError: Ritual file not found
        SyntaxError: Invalid CodeCraft syntax
        ValueError: Constitutional violation (invalid school/operation)
    """
    # Stage 0: Read ritual source
    ritual_file = Path(ritual_path)
    if not ritual_file.exists():
        raise FileNotFoundError(f"Ritual not found: {ritual_path}")
    
    source = ritual_file.read_text(encoding='utf-8')
    
    # Stage 1: Lexer (Token Recognition)
    lexer = Lexer(source, filename=str(ritual_file))
    tokens = lexer.tokenize()
    
    # Stage 2: Parser (Syntax Analysis)
    parser = Parser(tokens)
    parse_tree = parser.parse()
    
    # Stage 3: Semantic Analyzer (Constitutional Enforcement - Phase 3.A Lite)
    analyzer = SemanticAnalyzer(parse_tree, tokens=tokens)
    validated_tree = analyzer.analyze()
    
    # Stage 4: AST Transformer (Soul Schema Emission) - STUBBED
    transformer = ASTTransformer(validated_tree)
    ast = transformer.transform()
    
    return ast


def main():
    """CLI entry point - parse ritual and emit JSON to stdout"""
    if len(sys.argv) < 2:
        print("Usage: parse_to_json_ast.py <ritual_path> [--debug-tokens]", file=sys.stderr)
        sys.exit(1)
    
    ritual_path = sys.argv[1]
    debug_tokens = "--debug-tokens" in sys.argv
    
    try:
        # Debug mode: show tokens
        if debug_tokens:
            ritual_file = Path(ritual_path)
            source = ritual_file.read_text(encoding='utf-8')
            lexer = Lexer(source, filename=str(ritual_file))
            tokens = lexer.tokenize()
            
            print("🔮 LEXER TOKEN STREAM:", file=sys.stderr)
            print("=" * 80, file=sys.stderr)
            for token in tokens:
                print(f"  {token}", file=sys.stderr)
            print("=" * 80, file=sys.stderr)
            print(f"TOTAL TOKENS: {len(tokens)}", file=sys.stderr)
            print("", file=sys.stderr)
        
        ast = parse_ritual(ritual_path)
        # Emit JSON to stdout (captured by Rust VM)
        json.dump(ast, sys.stdout, indent=2)
        sys.exit(0)
    
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        print(f"PARSE ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
