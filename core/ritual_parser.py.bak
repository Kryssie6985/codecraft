# CodeCraft Ritual Parser - MEGA's AST Vision
# Transforms sacred syntax into executable structures

import re
import ast
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import logging

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
    
    def __str__(self) -> str:
        return f"RitualNode({self.type.value}:{self.name})"

class RitualParser:
    """
    MEGA's Vision: Advanced AST parsing for CodeCraft rituals
    Transforms ::ritual:: syntax into executable nodes
    """
    
    def __init__(self):
        self.ritual_patterns = self._initialize_patterns()
        self.ritual_registry = {}
    
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
        MEGA's vision: Multi-pattern parallel parsing
        """
        nodes = []
        lines = ritual_text.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line_nodes = self._parse_line(line, line_num)
            nodes.extend(line_nodes)
        
        logger.info(f"🎯 MEGA's Parser: Found {len(nodes)} ritual nodes")
        return nodes
    
    def _parse_line(self, line: str, line_num: int) -> List[RitualNode]:
        """Parse a single line for ritual patterns"""
        nodes = []
        
        for pattern, config in self.ritual_patterns.items():
            matches = re.finditer(pattern, line)
            
            for match in matches:
                # Extract parameters with MEGA's parameter substitution
                parameters = self._extract_parameters(match, config["parameters"])
                
                node = RitualNode(
                    type=config["type"],
                    name=config["name"],
                    parameters=parameters,
                    raw_text=match.group(0),
                    line_number=line_num,
                    column=match.start()
                )
                
                nodes.append(node)
                logger.debug(f"🔮 Parsed ritual: {node}")
        
        return nodes
    
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
        """Convert parsed nodes to dictionary for JSON serialization"""
        return {
            "nodes": [
                {
                    "type": node.type.value,
                    "name": node.name,
                    "parameters": node.parameters,
                    "raw_text": node.raw_text,
                    "line_number": node.line_number,
                    "column": node.column
                }
                for node in nodes
            ],
            "total_count": len(nodes),
            "types": list(set(node.type.value for node in nodes))
        }

# MEGA's excitement: "The AST is the soul of the language!"