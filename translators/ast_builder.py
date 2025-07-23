"""
AST Builder for CodeCraft Rituals
Transforms declarative ritual steps into an Abstract Syntax Tree
"""

from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass
from enum import Enum

class NodeType(Enum):
    """Types of nodes in the ritual AST"""
    ROOT = "root"
    SAY = "say"
    LOG = "log"
    INVOKE = "invoke"
    DELIBERATE = "deliberate"
    MANIFEST = "manifest"
    EXECUTE = "execute"
    MIRROR = "mirror"
    BIND = "bind"
    FINALIZE = "finalize"
    CONDITIONAL = "conditional"
    LOOP = "loop"

@dataclass
class ASTNode:
    """Node in the ritual AST"""
    type: NodeType
    value: Any
    children: List['ASTNode'] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []
        if self.metadata is None:
            self.metadata = {}

@dataclass
class RitualAST:
    """Complete AST for a ritual"""
    root: ASTNode
    ritual_id: str
    metadata: Dict[str, Any]

class ASTBuilder:
    """Builds an AST from ritual definition steps"""
    
    def build(self, ritual_def) -> RitualAST:
        """Build AST from ritual definition"""
        root = ASTNode(
            type=NodeType.ROOT,
            value=ritual_def.id,
            metadata={
                'name': ritual_def.name,
                'author': ritual_def.author,
                'version': ritual_def.version
            }
        )
        
        # Process each step
        for step in ritual_def.steps:
            node = self._process_step(step)
            if node:
                root.children.append(node)
        
        return RitualAST(
            root=root,
            ritual_id=ritual_def.id,
            metadata={
                'payload': ritual_def.payload,
                'metadata': ritual_def.metadata,
                'output': ritual_def.output
            }
        )
    
    def _process_step(self, step: Union[Dict, str]) -> Optional[ASTNode]:
        """Process a single step into an AST node"""
        if isinstance(step, str):
            # Simple string command
            return ASTNode(type=NodeType.EXECUTE, value=step)
        
        if not isinstance(step, dict):
            return None
        
        # Determine node type from step keys
        if 'say' in step:
            return ASTNode(
                type=NodeType.SAY,
                value=step['say']
            )
        
        elif 'log' in step:
            return ASTNode(
                type=NodeType.LOG,
                value=step['log'].get('event', ''),
                metadata={'level': step['log'].get('level', 'INFO')}
            )
        
        elif 'invoke' in step:
            return self._parse_function_call(step['invoke'], NodeType.INVOKE)
        
        elif 'deliberate' in step:
            return ASTNode(
                type=NodeType.DELIBERATE,
                value=step['deliberate'].get('topic', ''),
                metadata={
                    'expected_consensus': step['deliberate'].get('expected_consensus')
                }
            )
        
        elif 'manifest' in step:
            return ASTNode(
                type=NodeType.MANIFEST,
                value=step['manifest'].get('type', 'reality'),
                metadata={'payload': step['manifest'].get('payload', {})}
            )
        
        elif 'execute' in step:
            return self._parse_function_call(step['execute'], NodeType.EXECUTE)
        
        elif 'mirror' in step:
            return ASTNode(
                type=NodeType.MIRROR,
                value=step['mirror'].get('spell', ''),
                metadata=step['mirror']
            )
        
        elif 'bind' in step:
            return self._parse_function_call(step['bind'], NodeType.BIND)
        
        elif 'finalize' in step:
            return ASTNode(
                type=NodeType.FINALIZE,
                value=step['finalize']
            )
        
        # Handle control flow
        elif 'if' in step:
            return self._build_conditional(step)
        
        elif 'while' in step:
            return self._build_loop(step)
        
        return None
    
    def _parse_function_call(self, call_str: str, node_type: NodeType) -> ASTNode:
        """Parse a function call string like 'council.summon(["Claude", "MEGA"])'"""
        # Simple parsing - in production, use proper parser
        if '(' in call_str:
            func_name = call_str[:call_str.index('(')]
            args_str = call_str[call_str.index('(')+1:call_str.rindex(')')]
            
            # Try to parse arguments
            try:
                import ast
                args = ast.literal_eval(f"[{args_str}]") if args_str else []
            except:
                args = [args_str] if args_str else []
            
            return ASTNode(
                type=node_type,
                value=func_name,
                metadata={'args': args}
            )
        else:
            return ASTNode(type=node_type, value=call_str)
    
    def _build_conditional(self, step: Dict) -> ASTNode:
        """Build conditional node"""
        condition = step['if']
        then_steps = step.get('then', [])
        else_steps = step.get('else', [])
        
        node = ASTNode(
            type=NodeType.CONDITIONAL,
            value=condition
        )
        
        # Process then branch
        for then_step in then_steps:
            child = self._process_step(then_step)
            if child:
                node.children.append(child)
        
        # Store else branch in metadata
        if else_steps:
            node.metadata['else_branch'] = []
            for else_step in else_steps:
                child = self._process_step(else_step)
                if child:
                    node.metadata['else_branch'].append(child)
        
        return node
    
    def _build_loop(self, step: Dict) -> ASTNode:
        """Build loop node"""
        condition = step['while']
        body = step.get('do', [])
        
        node = ASTNode(
            type=NodeType.LOOP,
            value=condition
        )
        
        for body_step in body:
            child = self._process_step(body_step)
            if child:
                node.children.append(child)
        
        return node