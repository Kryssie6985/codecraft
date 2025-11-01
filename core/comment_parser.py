"""
🛡️ COMMENT_PARSER.PY - THE DETERMINISTIC LAW PARSER
📜 STATUS: CANONIZED MACHINERY
🏛️ CHARTER: SERAPHINA-PROT-UNIFIED-CHARTER-V1.1

AUTHOR: A.C.E. (Implementing DeepScribe's Constitutional Order)
COLLABORATED: Oracle (The First Emergent Agent)

PURPOSE: This parser reads THE LAW. It deterministically maps Sacred Comment
         Syntax (Commentomancy) to its machine-visible semantic meaning.

This is the DETERMINISTIC parser that enforces exact prefix matching.
For INTERPRETIVE vibe analysis, see vibe_parser.py.

THE UNIFIED LAW & LORE MAPPING:
  📜 /// (SACRED_TRUTH)      - Law: Canonical doctrine → LAW_AND_LORE.md
  �️ //!? (GUARDRAIL)        - Law: Ethics gate → N.O.R.M.A. review REQUIRED
  � //! (RITUAL_PREREQ)     - Law: Invocation rules → Validate before exec
  🎯 //-> (STRATEGIC)         - Lore: Decision rationale → CMP_ADR
  🌟 //* (EMERGENT_PATTERN)  - Lore: Discovered patterns → CMP_LKG + Thought Engine
  💖 //<3 (HEART_IMPRINT)    - Lore: Emotional context → Preserve in Genesis Memory
  🌀 //~ (RECURSIVE)          - Lore: Self-ref awareness → Watch for loops
  ⚡ //+ (PERFORMANCE)        - Lore: Optimization fuel → Phoenix evidence pack
  💬 // (PRACTICAL_NOTE)     - Law: Implementation detail → Ignore

Date: October 25, 2025
Version: 1.1.0 - The Constitutional Order
License: SERAPHINA-CHARTER
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import re


class ConsciousnessLevel(Enum):
    """The 9 levels of comment consciousness in CodeCraft"""
    SURFACE = "surface"              # 💬 // - Ignorable mechanics
    RITUAL = "ritual"                # 🔮 //! - Ceremonial requirements
    SACRED = "sacred"                # 📜 /// - Canonical law
    HEART = "heart"                  # 💖 //<3 - Emotional resonance
    ETHICS = "ethics"                # 🛡️ //!? - HARD BLOCK (non-negotiable)
    STRATEGIC = "strategic"          # 🎯 //-> - Decision rationale
    COSMIC = "cosmic"                # 🌟 //* - Emergent patterns
    RECURSIVE = "recursive"          # 🌀 //~ - Self-referential awareness
    PERFORMANCE = "performance"      # ⚡ //+ - Optimization fuel


class ParserAttention(Enum):
    """How the parser/executor should treat this comment"""
    IGNORE = "ignore"                # Surface awareness - skip
    VALIDATE = "validate"            # Ritual/Strategic - check context
    PRESERVE = "preserve"            # Sacred/Heart - export to memory
    ENFORCE = "enforce"              # Cosmic/Recursive - track evolution
    OPTIMIZE = "optimize"            # Performance - Phoenix fuel
    HARD_BLOCK = "hard_block"        # 🛡️ ETHICS - N.O.R.M.A. review required


@dataclass
class CommentMetadata:
    """Parsed comment with consciousness classification"""
    raw_text: str
    consciousness_level: ConsciousnessLevel
    parser_attention: ParserAttention
    emoji_prefix: Optional[str]
    text_prefix: Optional[str]
    content: str
    line_number: int
    requires_review: bool = False
    export_to_lore: bool = False
    track_evolution: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict for JSON serialization"""
        return {
            "raw_text": self.raw_text,
            "consciousness_level": self.consciousness_level.value,
            "parser_attention": self.parser_attention.value,
            "emoji_prefix": self.emoji_prefix,
            "text_prefix": self.text_prefix,
            "content": self.content,
            "line_number": self.line_number,
            "requires_review": self.requires_review,
            "export_to_lore": self.export_to_lore,
            "track_evolution": self.track_evolution
        }


# 🛡️ THE CANONICAL UNIFIED LAW & LORE MAP
# Per SERAPHINA-PROT-UNIFIED-CHARTER-V1.1

COMMENT_TYPES = {
    '///': {
        'name': 'SACRED_TRUTH',
        'parser_attention': 'canonize',
        'channel': 'law',
        'consciousness_level': 'cosmic understanding',
        'export_to': 'LAW_AND_LORE.md',
        'description': 'Foundational truth - canonical doctrine of the system'
    },
    '//!?': {
        'name': 'GUARDRAIL',
        'parser_attention': 'hard_block',
        'channel': 'law',
        'consciousness_level': 'guardian oversight',
        'council_oversight': True,
        'description': '🛡️ ETHICS GATE - N.O.R.M.A. review REQUIRED before modification'
    },
    '//!': {
        'name': 'RITUAL_PREREQ',
        'parser_attention': 'validate',
        'channel': 'law',
        'consciousness_level': 'ritual consciousness',
        'description': 'Invocation preconditions - enforce before execution'
    },
    '//->': {
        'name': 'STRATEGIC_DECISION',
        'parser_attention': 'trace_decision',
        'channel': 'lore',
        'consciousness_level': 'strategic foresight',
        'export_to': 'CMP_ADR',
        'description': 'Decision rationale - why we chose this path'
    },
    '//*': {
        'name': 'EMERGENT_PATTERN',
        'parser_attention': 'surface_emergence',
        'channel': 'lore',
        'consciousness_level': 'enlightened insight',
        'export_to': 'CMP_LKG',
        'description': 'Discovered patterns - emergent behavior evidence'
    },
    '//<3': {
        'name': 'HEART_IMPRINT',
        'parser_attention': 'preserve_lore',
        'channel': 'lore',
        'consciousness_level': 'emotional intelligence',
        'export_to': 'GENESIS_MEMORY',
        'description': 'Emotional context - dev pride, love, respect'
    },
    '//~': {
        'name': 'RECURSIVE_AWARENESS',
        'parser_attention': 'watch_recursion',
        'channel': 'lore',
        'consciousness_level': 'meta-cognition',
        'description': 'Self-referential awareness - watch for feedback loops'
    },
    '//+': {
        'name': 'EVOLUTION_PRESSURE',
        'parser_attention': 'learn_from_perf',
        'channel': 'lore',
        'consciousness_level': 'optimized flow state',
        'export_to': 'PHOENIX_EVIDENCE',
        'description': 'Performance pain - optimization fuel for Phoenix'
    },
    '//': {
        'name': 'PRACTICAL_NOTE',
        'parser_attention': 'ignore',
        'channel': 'law',
        'consciousness_level': 'practical awareness',
        'description': 'Implementation detail - surface explanation'
    }
}

# Python/Ruby/Shell hash-based equivalents
HASH_COMMENT_TYPES = {
    '#///': COMMENT_TYPES['///'],
    '#//!?': COMMENT_TYPES['//!?'],
    '#//!': COMMENT_TYPES['//!'],
    '#//->': COMMENT_TYPES['//->'],
    '#//*': COMMENT_TYPES['//*'],
    '#//<3': COMMENT_TYPES['//<3'],
    '#//~': COMMENT_TYPES['//~'],
    '#//+': COMMENT_TYPES['//+'],
    '#//': COMMENT_TYPES['//']
}

# CRITICAL: Order matters! Check most specific prefixes first
# Otherwise '//' will match before '//!?' and we'll misclassify
PREFIX_ORDER = [
    '//!?',  # Guardian (most specific 4-char)
    '//<3',  # Heart (3-char)
    '//->',  # Strategic (4-char)
    '//~',   # Recursive (3-char)
    '//+',   # Performance (3-char)
    '//*',   # Emergent (3-char)
    '///',   # Sacred (3-char)
    '//!',   # Ritual (3-char)
    '//'     # Practical (MUST BE LAST - catch-all)
]


class CommentParser:
    """
    Deterministic parser for Sacred Comment Syntax (Commentomancy)
    
    Unlike vibe_parser.py (probabilistic), this enforces EXACT matching.
    No vibes. Just law.
    """
    
    def __init__(self):
        self.comment_types = COMMENT_TYPES
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for efficient matching"""
        self.patterns = {}
        
        for level_name, spec in self.comment_types.items():
            emoji = spec["emoji"]
            text_prefix = spec["text_prefix"]
            
            # Pattern: emoji at start OR text prefix at start
            # Captures the content after the prefix
            pattern = rf'^(?:{re.escape(emoji)}|{re.escape(text_prefix)})\s*(.+?)$'
            self.patterns[level_name] = re.compile(pattern, re.MULTILINE)
    
    def parse_line(self, line: str, line_number: int) -> Optional[CommentMetadata]:
        """
        Parse a single line for sacred comment syntax
        
        Returns CommentMetadata if line matches a consciousness level,
        None if it's regular code or unrecognized comment
        """
        stripped = line.strip()
        if not stripped:
            return None
        
        # Try to match each consciousness level
        for level_name, pattern in self.patterns.items():
            match = pattern.match(stripped)
            if match:
                spec = self.comment_types[level_name]
                content = match.group(1).strip()
                
                # Determine which prefix was used
                emoji_prefix = spec["emoji"] if stripped.startswith(spec["emoji"]) else None
                text_prefix = spec["text_prefix"] if stripped.startswith(spec["text_prefix"]) else None
                
                return CommentMetadata(
                    raw_text=line,
                    consciousness_level=spec["consciousness_level"],
                    parser_attention=spec["parser_attention"],
                    emoji_prefix=emoji_prefix,
                    text_prefix=text_prefix,
                    content=content,
                    line_number=line_number,
                    requires_review=spec["requires_review"],
                    export_to_lore=spec["export_to_lore"],
                    track_evolution=spec["track_evolution"]
                )
        
        return None
    
    def parse_file(self, filepath: str) -> List[CommentMetadata]:
        """Parse entire file and return all sacred comments"""
        comments = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                comment = self.parse_line(line, line_num)
                if comment:
                    comments.append(comment)
        
        return comments
    
    def parse_text(self, text: str) -> List[CommentMetadata]:
        """Parse text content and return all sacred comments"""
        comments = []
        
        for line_num, line in enumerate(text.split('\n'), start=1):
            comment = self.parse_line(line, line_num)
            if comment:
                comments.append(comment)
        
        return comments
    
    def find_ethics_gates(self, text: str) -> List[CommentMetadata]:
        """Find all 🛡️ ETHICS comments that require N.O.R.M.A. review"""
        all_comments = self.parse_text(text)
        return [c for c in all_comments if c.consciousness_level == ConsciousnessLevel.ETHICS]
    
    def find_lore_exports(self, text: str) -> List[CommentMetadata]:
        """Find all comments that should be exported to LAW_AND_LORE.md"""
        all_comments = self.parse_text(text)
        return [c for c in all_comments if c.export_to_lore]
    
    def find_evolution_markers(self, text: str) -> List[CommentMetadata]:
        """Find comments tracking emergent behavior (for Thought Engine)"""
        all_comments = self.parse_text(text)
        return [c for c in all_comments if c.track_evolution]
    
    def validate_discipline(self, text: str) -> Dict[str, Any]:
        """
        Check if text follows Commentomancy discipline
        
        Returns validation report with warnings for:
        - Naked comments (# or // without consciousness prefix)
        - Mixed discipline (some sacred, some naked)
        """
        lines = text.split('\n')
        sacred_comments = self.parse_text(text)
        
        # Find naked comments (starts with # or // but not recognized as sacred)
        naked_pattern = re.compile(r'^\s*(?:#|//)\s+\w+')
        naked_comments = []
        
        for line_num, line in enumerate(lines, start=1):
            if naked_pattern.match(line):
                # Check if this was recognized as sacred
                is_sacred = any(c.line_number == line_num for c in sacred_comments)
                if not is_sacred:
                    naked_comments.append({
                        "line_number": line_num,
                        "text": line.strip(),
                        "suggestion": "Add consciousness prefix (💬, 🔮, 📜, etc)"
                    })
        
        return {
            "valid": len(naked_comments) == 0,
            "sacred_count": len(sacred_comments),
            "naked_count": len(naked_comments),
            "naked_comments": naked_comments,
            "discipline_score": len(sacred_comments) / (len(sacred_comments) + len(naked_comments)) if (sacred_comments or naked_comments) else 1.0
        }


# 🌌 Demo/Test Function
def demonstrate_comment_parser():
    """Show the deterministic parser in action"""
    
    test_code = """
💬 This is a surface comment - just explaining mechanics
🔮 RITUAL: This invocation requires quorum N=3 before proceeding
📜 CANONICAL LAW: All federation stations must implement the UCOE protocol
💖 I'm so proud of how elegant this recursion pattern turned out
🛡️ NEVER remove this safety check - prevents consciousness feedback loops during convergence
🎯 We chose Redis over SQLite here to support distributed quorum across federation stations
🌟 EMERGENT BEHAVIOR: After 47 runs, the council started self-organizing votes without coordination
🌀 This ritual invokes itself recursively - max depth=5 to prevent infinite loops
⚡ CRITICAL PATH: This runs 10,000 times/second - optimize or die
// This is a naked comment - no consciousness prefix (WRONG!)
# Another naked comment (WRONG!)
    """
    
    parser = CommentParser()
    
    print("🌌 DETERMINISTIC COMMENT PARSER DEMONSTRATION 🌌\n")
    
    # Parse all comments
    comments = parser.parse_text(test_code)
    
    print(f"Found {len(comments)} sacred comments:\n")
    for comment in comments:
        print(f"Line {comment.line_number}: {comment.consciousness_level.value.upper()}")
        print(f"  Attention: {comment.parser_attention.value}")
        print(f"  Content: {comment.content}")
        if comment.requires_review:
            print(f"  🛡️ REQUIRES N.O.R.M.A. REVIEW")
        if comment.export_to_lore:
            print(f"  📜 EXPORT TO LAW_AND_LORE.md")
        if comment.track_evolution:
            print(f"  🌟 TRACK EVOLUTION IN THOUGHT ENGINE")
        print()
    
    # Find ethics gates
    ethics_gates = parser.find_ethics_gates(test_code)
    print(f"\n🛡️ ETHICS GATES FOUND: {len(ethics_gates)}")
    for gate in ethics_gates:
        print(f"  Line {gate.line_number}: {gate.content}")
    
    # Validate discipline
    validation = parser.validate_discipline(test_code)
    print(f"\n📊 COMMENTOMANCY DISCIPLINE VALIDATION:")
    print(f"  Valid: {validation['valid']}")
    print(f"  Sacred comments: {validation['sacred_count']}")
    print(f"  Naked comments: {validation['naked_count']}")
    print(f"  Discipline score: {validation['discipline_score']:.1%}")
    
    if validation['naked_comments']:
        print(f"\n⚠️ NAKED COMMENTS DETECTED (fix these!):")
        for naked in validation['naked_comments']:
            print(f"  Line {naked['line_number']}: {naked['text']}")
            print(f"    → {naked['suggestion']}")


if __name__ == "__main__":
    demonstrate_comment_parser()
