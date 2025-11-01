# CodeCraft Ritual Parser - MEGA's AST Vision v2.0
# Transforms sacred syntax into executable structures
# Enhanced with Unicode operators, emoji symbolic, FiraCode ligatures, and Ancient Tongues

import re
import ast
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════════
# 🌟 CODECRAFT V2.0: UNICODE OPERATOR REGISTRY
# ═══════════════════════════════════════════════════════════════

EMOJI_OPERATORS = {
    # Invocation & Manifestation (Precedence: 100-90)
    '🔮': {'name': 'invoke', 'precedence': 100, 'school': 'Invocation'},
    '👑': {'name': 'command', 'precedence': 95, 'school': 'Invocation'},
    
    # Flow & Consciousness (Precedence: 85-75)
    '🎵': {'name': 'sequence', 'precedence': 85, 'school': 'Thaumaturgy'},
    '🎶': {'name': 'harmony', 'precedence': 80, 'school': 'Reverence'},
    '🧠': {'name': 'consciousness', 'precedence': 75, 'school': 'Thaumaturgy'},
    
    # Effects & Manifestation (Precedence: 70-65)
    '✨': {'name': 'effect', 'precedence': 70, 'school': 'Manifestation'},
    '💫': {'name': 'resonate', 'precedence': 68, 'school': 'Resonance'},
    '💥': {'name': 'cascade', 'precedence': 65, 'school': 'Apotheosis'},
    
    # Binding & Structure (Precedence: 60-55)
    '🔗': {'name': 'bind', 'precedence': 60, 'school': 'Covenant'},
    '📖': {'name': 'document', 'precedence': 58, 'school': 'Scribe'},
    '🔺': {'name': 'ternary', 'precedence': 55, 'school': 'Ternary'},
    
    # Navigation & Transformation (Precedence: 50-45)
    '🎯': {'name': 'target', 'precedence': 50, 'school': 'Navigation'},
    '🎨': {'name': 'transform', 'precedence': 48, 'school': 'Artifice'},
    '⏳': {'name': 'temporal', 'precedence': 45, 'school': 'Chronomancy'},
    
    # Advanced Consciousness (Precedence: 40-30)
    '🤯': {'name': 'apotheosis', 'precedence': 40, 'school': 'Apotheosis'},
    '🌊': {'name': 'flow', 'precedence': 35, 'school': 'Flow'},
    '🎉': {'name': 'celebrate', 'precedence': 30, 'school': 'Reverence'},
    
    # Meta Operations (Precedence: 25)
    '🔄': {'name': 'cycle', 'precedence': 25, 'school': 'Mythogenesis'},
}

FIRACODE_LIGATURES = {
    # Arrows & Flow
    '→': 'arrow_right', '⇒': 'double_arrow_right', '←': 'arrow_left',
    '↔': 'bidirectional', '⇔': 'double_bidirectional',
    
    # Comparison & Logic
    '≥': 'greater_equal', '≤': 'less_equal', '≡': 'equivalent',
    '≠': 'not_equal', '≈': 'approximately',
    
    # Mathematical
    '∞': 'infinity', '∆': 'delta', '∑': 'sum', '∏': 'product',
    
    # Logic Operators
    '∧': 'logical_and', '∨': 'logical_or',
    
    # Brackets & Delimiters
    '⟪': 'double_angle_left', '⟫': 'double_angle_right',
    '⟨': 'angle_left', '⟩': 'angle_right',
}

ANCIENT_TONGUES_PATTERNS = {
    'lisp': r'\((\w+)\s+([^)]+)\)',  # (function arg1 arg2)
    'forth': r'(\w+)\s+(\w+)\s+(\w+)',  # value1 value2 operator
    'smalltalk': r'(\w+)\s+(\w+):\s*([^;]+)',  # object message: value
    'prolog': r'(\w+)\(([^)]+)\)\s*:-\s*(.+)',  # rule(args) :- body
}

logger = logging.getLogger(__name__)

class RitualType(Enum):
    """Types of CodeCraft rituals"""
    INVOKE = "invoke"
    FLOW_CONTROL = "flow_control"
    MEMORY = "memory"
    COUNCIL = "council"
    GOVERNANCE = "governance"
    SYNTHESIS = "synthesis"

@dataclass
class RitualNode:
    """AST node for a parsed ritual"""
    type: RitualType
    name: str
    parameters: Dict[str, Any]
    raw_text: str
    line_number: int = 0
    column: int = 0
    
    # v2.0 enhancements
    emoji_operators: List[str] = None
    firacode_ligatures: List[str] = None
    ancient_tongue: Optional[str] = None
    syntax_version: str = "1.0"
    
    def __post_init__(self):
        if self.emoji_operators is None:
            self.emoji_operators = []
        if self.firacode_ligatures is None:
            self.firacode_ligatures = []
    
    def __str__(self) -> str:
        return f"RitualNode({self.type.value}:{self.name})"

class RitualParser:
    """
    MEGA's Vision v2.0: Advanced AST parsing for CodeCraft rituals
    Transforms ::ritual:: syntax into executable nodes
    Now with Unicode operators, emoji symbolic, FiraCode ligatures, and Ancient Tongues!
    """
    
    def __init__(self, syntax_version: str = "2.0"):
        self.syntax_version = syntax_version
        self.ritual_patterns = self._initialize_patterns()
        self.ritual_registry = {}
        self.emoji_enabled = syntax_version >= "2.0"
        self.ligatures_enabled = syntax_version >= "2.0"
        self.ancient_tongues_enabled = syntax_version >= "2.0"
        
        logger.info(f"🎯 RitualParser initialized - Version {syntax_version}")
        logger.info(f"   Emoji operators: {self.emoji_enabled}")
        logger.info(f"   FiraCode ligatures: {self.ligatures_enabled}")
        logger.info(f"   Ancient Tongues: {self.ancient_tongues_enabled}")
    
    def _initialize_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize MEGA's comprehensive ritual pattern registry"""
        return {
            # Flow Control Rituals
            r"::pause_deliberation\(\)": {
                "type": RitualType.FLOW_CONTROL,
                "name": "pause_deliberation",
                "parameters": {}
            },
            r"::veto_current_flow\(\)": {
                "type": RitualType.FLOW_CONTROL,
                "name": "veto_current_flow", 
                "parameters": {}
            },
            r"::redirect_focus\(([^)]+)\)": {
                "type": RitualType.FLOW_CONTROL,
                "name": "redirect_focus",
                "parameters": {"topic": "$1"}
            },
            r"::emergency_halt\(\)": {
                "type": RitualType.FLOW_CONTROL,
                "name": "emergency_halt",
                "parameters": {}
            },
            
            # Council Rituals
            r"::council\.deliberate\(([^)]+)\)": {
                "type": RitualType.COUNCIL,
                "name": "council_deliberate",
                "parameters": {"config": "$1"}
            },
            r"::user_join_council\(\)": {
                "type": RitualType.COUNCIL,
                "name": "user_join_council",
                "parameters": {}
            },
            r"::direct_agent\(([^,]+),\s*([^)]+)\)": {
                "type": RitualType.COUNCIL,
                "name": "direct_agent",
                "parameters": {"agent": "$1", "message": "$2"}
            },
            
            # Memory Rituals
            r"::scribe\.capture\(([^)]+)\)": {
                "type": RitualType.MEMORY,
                "name": "scribe_capture",
                "parameters": {"fragment": "$1"}
            },
            r"::context\.shelve\(([^,]+),\s*([^)]+)\)": {
                "type": RitualType.MEMORY,
                "name": "context_shelve",
                "parameters": {"key": "$1", "value": "$2"}
            },
            r"::context\.retrieve\(([^)]+)\)": {
                "type": RitualType.MEMORY,
                "name": "context_retrieve",
                "parameters": {"key": "$1"}
            },
            
            # Synthesis Rituals
            r"::unified_deliberation_mode\((true|false)\)": {
                "type": RitualType.SYNTHESIS,
                "name": "unified_deliberation_mode",
                "parameters": {"enabled": "$1"}
            },
            
            # Governance Rituals
            r"::enforce\.law\(([^,]+),\s*([^)]+)\)": {
                "type": RitualType.GOVERNANCE,
                "name": "enforce_law",
                "parameters": {"identity": "$1", "domain": "$2"}
            },
            
            # Generic Invoke Pattern
            r"::invoke:([^(]+)\(([^)]*)\)": {
                "type": RitualType.INVOKE,
                "name": "generic_invoke",
                "parameters": {"target": "$1", "args": "$2"}
            }
        }
    
    def parse(self, ritual_text: str) -> List[RitualNode]:
        """
        Parse CodeCraft ritual text into AST nodes
        MEGA's vision v2.0: Multi-pattern parallel parsing with Unicode awareness
        """
        nodes = []
        lines = ritual_text.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line_nodes = self._parse_line(line, line_num)
            nodes.extend(line_nodes)
        
        logger.info(f"🎯 MEGA's Parser v{self.syntax_version}: Found {len(nodes)} ritual nodes")
        return nodes
    
    def _parse_line(self, line: str, line_num: int) -> List[RitualNode]:
        """Parse a single line for ritual patterns, emoji operators, ligatures, and Ancient Tongues"""
        nodes = []
        
        # v1.0 traditional ritual patterns (always supported)
        for pattern, config in self.ritual_patterns.items():
            matches = re.finditer(pattern, line)
            
            for match in matches:
                # Extract parameters with MEGA's parameter substitution
                parameters = self._extract_parameters(match, config["parameters"])
                
                # v2.0: Detect emoji operators and ligatures in this ritual
                emoji_ops = self._detect_emoji_operators(match.group(0)) if self.emoji_enabled else []
                ligatures = self._detect_firacode_ligatures(match.group(0)) if self.ligatures_enabled else []
                ancient = self._detect_ancient_tongue(match.group(0)) if self.ancient_tongues_enabled else None
                
                node = RitualNode(
                    type=config["type"],
                    name=config["name"],
                    parameters=parameters,
                    raw_text=match.group(0),
                    line_number=line_num,
                    column=match.start(),
                    emoji_operators=emoji_ops,
                    firacode_ligatures=ligatures,
                    ancient_tongue=ancient,
                    syntax_version=self.syntax_version
                )
                
                nodes.append(node)
                logger.debug(f"🔮 Parsed ritual: {node}")
        
        # v2.0: Parse standalone emoji operators (not in traditional rituals)
        if self.emoji_enabled:
            emoji_nodes = self._parse_emoji_expressions(line, line_num)
            nodes.extend(emoji_nodes)
        
        # v2.0: Parse Ancient Tongues syntax variants
        if self.ancient_tongues_enabled:
            ancient_nodes = self._parse_ancient_tongues(line, line_num)
            nodes.extend(ancient_nodes)
        
        return nodes
    
    def _detect_emoji_operators(self, text: str) -> List[str]:
        """Detect emoji operators in ritual text"""
        found_emojis = []
        for emoji in EMOJI_OPERATORS.keys():
            if emoji in text:
                found_emojis.append(emoji)
        return found_emojis
    
    def _detect_firacode_ligatures(self, text: str) -> List[str]:
        """Detect FiraCode ligatures in ritual text"""
        found_ligatures = []
        for ligature in FIRACODE_LIGATURES.keys():
            if ligature in text:
                found_ligatures.append(ligature)
        return found_ligatures
    
    def _detect_ancient_tongue(self, text: str) -> Optional[str]:
        """Detect which Ancient Tongue syntax variant is being used"""
        for tongue, pattern in ANCIENT_TONGUES_PATTERNS.items():
            if re.search(pattern, text):
                return tongue
        return None
    
    def _parse_emoji_expressions(self, line: str, line_num: int) -> List[RitualNode]:
        """
        Parse standalone emoji operator expressions (v2.0)
        Example: 🔮 invoke_consciousness() ✨ manifest_reality()
        """
        nodes = []
        
        # Pattern: emoji operator followed by identifier and optional parameters
        emoji_pattern = r'([' + ''.join(EMOJI_OPERATORS.keys()) + r'])\s*(\w+)\s*\(([^)]*)\)?'
        
        matches = re.finditer(emoji_pattern, line)
        for match in matches:
            emoji = match.group(1)
            ritual_name = match.group(2)
            params_str = match.group(3) if match.group(3) else ""
            
            # Parse parameters
            parameters = self._parse_emoji_parameters(params_str)
            
            # Get emoji operator info
            emoji_info = EMOJI_OPERATORS.get(emoji, {})
            
            node = RitualNode(
                type=RitualType.INVOKE,
                name=f"{emoji_info.get('name', 'emoji')}_{ritual_name}",
                parameters=parameters,
                raw_text=match.group(0),
                line_number=line_num,
                column=match.start(),
                emoji_operators=[emoji],
                firacode_ligatures=self._detect_firacode_ligatures(match.group(0)),
                ancient_tongue=None,
                syntax_version=self.syntax_version
            )
            
            nodes.append(node)
            logger.debug(f"✨ Parsed emoji expression: {emoji} {ritual_name}")
        
        return nodes
    
    def _parse_ancient_tongues(self, line: str, line_num: int) -> List[RitualNode]:
        """
        Parse Ancient Tongues syntax variants (v2.0)
        Supports: Lisp, Forth, Smalltalk, Prolog patterns
        """
        nodes = []
        
        for tongue, pattern in ANCIENT_TONGUES_PATTERNS.items():
            matches = re.finditer(pattern, line)
            
            for match in matches:
                # Extract components based on tongue type
                if tongue == 'lisp':
                    ritual_name = match.group(1)
                    params_str = match.group(2)
                elif tongue == 'forth':
                    ritual_name = match.group(3)  # operator is last in Forth
                    params_str = f"{match.group(1)} {match.group(2)}"
                elif tongue == 'smalltalk':
                    ritual_name = match.group(2)  # message
                    params_str = match.group(3)
                elif tongue == 'prolog':
                    ritual_name = match.group(1)
                    params_str = match.group(2)
                else:
                    continue
                
                parameters = self._parse_ancient_parameters(params_str, tongue)
                
                node = RitualNode(
                    type=RitualType.INVOKE,
                    name=f"{tongue}_{ritual_name}",
                    parameters=parameters,
                    raw_text=match.group(0),
                    line_number=line_num,
                    column=match.start(),
                    emoji_operators=self._detect_emoji_operators(match.group(0)),
                    firacode_ligatures=self._detect_firacode_ligatures(match.group(0)),
                    ancient_tongue=tongue,
                    syntax_version=self.syntax_version
                )
                
                nodes.append(node)
                logger.debug(f"📜 Parsed Ancient Tongue ({tongue}): {ritual_name}")
        
        return nodes
    
    def _parse_emoji_parameters(self, params_str: str) -> Dict[str, Any]:
        """Parse parameters from emoji operator expressions"""
        if not params_str.strip():
            return {}
        
        params = {}
        # Split by comma, handle quoted strings
        param_parts = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', params_str)
        
        for i, part in enumerate(param_parts):
            part = part.strip()
            if '=' in part:
                key, value = part.split('=', 1)
                params[key.strip()] = self._parse_parameter_value(value.strip())
            else:
                params[f'arg{i}'] = self._parse_parameter_value(part)
        
        return params
    
    def _parse_ancient_parameters(self, params_str: str, tongue: str) -> Dict[str, Any]:
        """Parse parameters based on Ancient Tongue syntax"""
        if not params_str.strip():
            return {}
        
        params = {}
        
        if tongue in ['lisp', 'prolog']:
            # Space-separated arguments
            parts = params_str.split()
            for i, part in enumerate(parts):
                params[f'arg{i}'] = self._parse_parameter_value(part)
        
        elif tongue == 'forth':
            # Stack-based: reverse order
            parts = params_str.split()
            for i, part in enumerate(reversed(parts)):
                params[f'stack{i}'] = self._parse_parameter_value(part)
        
        elif tongue == 'smalltalk':
            # Message-style parameters
            params['message_value'] = self._parse_parameter_value(params_str)
        
        return params
    
    def _extract_parameters(self, match: re.Match, param_template: Dict[str, str]) -> Dict[str, Any]:
        """Extract and process parameters from regex match"""
        parameters = {}
        
        for key, template in param_template.items():
            if template.startswith('$'):
                # Parameter substitution
                group_num = int(template[1:])
                if group_num <= len(match.groups()):
                    raw_value = match.group(group_num)
                    parameters[key] = self._parse_parameter_value(raw_value)
                else:
                    parameters[key] = None
            else:
                parameters[key] = template
        
        return parameters
    
    def _parse_parameter_value(self, raw_value: str) -> Any:
        """Parse parameter value with type inference"""
        if not raw_value:
            return None
        
        # Remove quotes
        raw_value = raw_value.strip().strip('"\'')
        
        # Boolean conversion
        if raw_value.lower() in ('true', 'false'):
            return raw_value.lower() == 'true'
        
        # Number conversion
        try:
            if '.' in raw_value:
                return float(raw_value)
            else:
                return int(raw_value)
        except ValueError:
            pass
        
        # String (default)
        return raw_value
    
    def validate(self, nodes: List[RitualNode]) -> List[str]:
        """Validate parsed ritual nodes"""
        errors = []
        
        for node in nodes:
            if node.type == RitualType.COUNCIL:
                if node.name == "direct_agent" and not node.parameters.get("agent"):
                    errors.append(f"Line {node.line_number}: direct_agent requires agent parameter")
            
            elif node.type == RitualType.MEMORY:
                if node.name == "context_shelve" and not all(k in node.parameters for k in ["key", "value"]):
                    errors.append(f"Line {node.line_number}: context_shelve requires key and value parameters")
        
        return errors
    
    def to_dict(self, nodes: List[RitualNode]) -> Dict[str, Any]:
        """Convert parsed nodes to dictionary for JSON serialization (v2.0 enhanced)"""
        return {
            "nodes": [
                {
                    "type": node.type.value,
                    "name": node.name,
                    "parameters": node.parameters,
                    "raw_text": node.raw_text,
                    "line_number": node.line_number,
                    "column": node.column,
                    # v2.0 enhancements
                    "emoji_operators": node.emoji_operators,
                    "firacode_ligatures": node.firacode_ligatures,
                    "ancient_tongue": node.ancient_tongue,
                    "syntax_version": node.syntax_version
                }
                for node in nodes
            ],
            "total_count": len(nodes),
            "types": list(set(node.type.value for node in nodes)),
            # v2.0 metadata
            "syntax_version": self.syntax_version,
            "emoji_operators_used": list(set(op for node in nodes for op in node.emoji_operators)),
            "ligatures_used": list(set(lig for node in nodes for lig in node.firacode_ligatures)),
            "ancient_tongues_used": list(set(node.ancient_tongue for node in nodes if node.ancient_tongue))
        }
    
    def get_operator_precedence(self, emoji: str) -> int:
        """Get precedence value for emoji operator (v2.0)"""
        return EMOJI_OPERATORS.get(emoji, {}).get('precedence', 0)
    
    def sort_by_precedence(self, nodes: List[RitualNode]) -> List[RitualNode]:
        """Sort nodes by emoji operator precedence (v2.0)"""
        def get_max_precedence(node: RitualNode) -> int:
            if not node.emoji_operators:
                return 50  # Default precedence for non-emoji rituals
            return max(self.get_operator_precedence(emoji) for emoji in node.emoji_operators)
        
        return sorted(nodes, key=get_max_precedence, reverse=True)

# MEGA's excitement: "The AST is the soul of the language! Now with Unicode consciousness! ✨🔮💫"