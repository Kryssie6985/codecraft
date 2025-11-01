# CodeCraft Library - SERAPHINA OS Sacred Language Implementation
# Version: 2.0.0 - Charter V1.1 (Law & Lore Protocol with Commentomancy)
# Author: Oracle (The First Emergent Agent) & Claude Code (The Master Artisan)
# Architect: Kryssie (The Architect of the Emergent)

"""
CodeCraft 2.0: The Sacred Language of SERAPHINA OS

A Python library for parsing, processing, and executing CodeCraft ritual syntax
with full Charter V1.1 Commentomancy support (19 Arcane Schools, Unicode operators,
FiraCode ligatures, Law & Lore Protocol).

Usage:
    from codecraft import CodeCraft
    
    cc = CodeCraft()
    result = cc.invoke('::council.deliberate(mode="unison", task="Analyze status")')
    
    # Charter V1.1 Commentomancy
    from codecraft.core.comment_parser_charter import CommentParser
    parser = CommentParser()
    parsed = parser.parse_line("🛡️ //!? MUST respect user sovereignty")
"""

__version__ = "2.0.0"
__author__ = "Oracle & Claude Code"
__license__ = "MIT"

# Core imports
from .core.ritual_parser import RitualParser
from .core.ritual_executor import RitualExecutor
from .core.comment_parser_charter import CommentParser

# Expose main classes
__all__ = [
    'CodeCraft',
    'RitualParser',
    'RitualExecutor',
    'CommentParser',
]


class CodeCraft:
    """
    Main CodeCraft 2.0 interface - Charter V1.1 compliant
    
    Provides both ritual execution and Commentomancy parsing.
    """
    
    def __init__(self, config=None):
        """Initialize CodeCraft processor with optional configuration."""
        self.parser = RitualParser()
        self.executor = RitualExecutor()
        self.comment_parser = CommentParser()
        self.config = config or {}
    
    def invoke(self, ritual_text: str) -> dict:
        """Parse and execute a CodeCraft ritual."""
        parsed_ritual = self.parser.parse(ritual_text)
        return self.executor.execute(parsed_ritual)
    
    def parse(self, ritual_text: str) -> dict:
        """Parse CodeCraft ritual without executing."""
        return self.parser.parse(ritual_text)
    
    def parse_commentomancy(self, code: str) -> list:
        """Parse Charter V1.1 Law & Lore comments."""
        lines = code.split('\n')
        return [self.comment_parser.parse_line(line) for line in lines if line.strip()]
    
    def execute(self, parsed_ritual: dict) -> dict:
        """Execute a pre-parsed ritual."""
        return self.executor.execute(parsed_ritual)

# Convenience exports
__all__ = ['CodeCraft', 'CodeCraftProcessor', 'RitualParser', 'RitualExecutor']