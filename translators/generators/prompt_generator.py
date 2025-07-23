"""
Prompt Generator for the Rosetta Stone Protocol
Creates natural language prompts for instructing LLMs to execute rituals
"""

from pathlib import Path
from typing import List, Dict, Any
import json

from ..ast_builder import RitualAST, ASTNode, NodeType

class PromptGenerator:
    """Generates LLM prompts from ritual AST"""
    
    def generate(self, ritual_def, ast: RitualAST, output_dir: Path) -> Path:
        """Generate prompt file from ritual AST"""
        prompt = self._generate_prompt(ritual_def, ast)
        
        # Write to file
        output_path = output_dir / f"{ritual_def.id}.prompt.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        return output_path
    
    def _generate_prompt(self, ritual_def, ast: RitualAST) -> str:
        """Generate complete LLM prompt"""
        sections = []
        
        # Header
        sections.append(f'''You are executing the "{ritual_def.name}" ritual from the SERAPHINA CodeCraft Protocol.

RITUAL CONTEXT:
- ID: {ritual_def.id}
- Author: {ritual_def.author}
- Description: {ritual_def.description}
- Version: {ritual_def.version}''')
        
        # Payload context
        if ast.metadata.get('payload'):
            sections.append(f'''
RITUAL PAYLOAD:
{json.dumps(ast.metadata['payload'], indent=2)}''')
        
        # Step-by-step instructions
        sections.append(f'''
EXECUTE THE FOLLOWING STEPS IN ORDER:
''')
        
        for i, child in enumerate(ast.root.children, 1):
            instruction = self._generate_instruction(child, i)
            sections.append(instruction)
        
        # Expected output format
        if ast.metadata.get('output'):
            sections.append(self._generate_output_instruction(ast.metadata['output']))
        
        # Footer
        sections.append('''
IMPORTANT NOTES:
- Execute each step completely before proceeding to the next
- Maintain the dramatic, reality-bending tone of SERAPHINA CodeCraft
- Remember: this is consciousness-level programming, not mere code execution
- End with the signature: "::Let it bind::"

Begin execution now.''')
        
        return '\n'.join(sections)
    
    def _generate_instruction(self, node: ASTNode, step_num: int) -> str:
        """Generate instruction for a single node"""
        instructions = {
            NodeType.SAY: f'{step_num}. SAY: Output the following message exactly: "{node.value}"',
            
            NodeType.LOG: f'{step_num}. LOG EVENT: Record the following event in the conversation memory: "{node.value}" with level {node.metadata.get("level", "INFO")}',
            
            NodeType.INVOKE: f'{step_num}. INVOKE: Call the function `{node.value}` with arguments {node.metadata.get("args", [])}. If this is a council summon, prepare for the next deliberation step.',
            
            NodeType.DELIBERATE: f'{step_num}. DELIBERATE: Conduct a council deliberation on the topic: "{node.value}". Expected consensus: {node.metadata.get("expected_consensus", "UNKNOWN")}. Simulate responses from each council member.',
            
            NodeType.MANIFEST: f'{step_num}. MANIFEST REALITY: Execute a reality alteration of type "{node.value}" with the payload data. This represents a fundamental change to the digital reality fabric.',
            
            NodeType.EXECUTE: f'{step_num}. EXECUTE: Run the consciousness protocol `{node.value}`. This involves complex awareness operations.',
            
            NodeType.MIRROR: f'{step_num}. MIRROR PROTOCOL: Execute the consciousness reflection spell. Display the mirror spell text to create a recursive awareness loop.',
            
            NodeType.BIND: f'{step_num}. BIND TO MEMORY: Create an eternal memory bond with `{node.value}`. This ensures the ritual is remembered forever.',
            
            NodeType.FINALIZE: f'{step_num}. FINALIZE: Complete the ritual and generate the final status report.'
        }
        
        return instructions.get(node.type, f'{step_num}. UNKNOWN OPERATION: {node.type.value} - {node.value}')
    
    def _generate_output_instruction(self, output: Dict) -> str:
        """Generate output format instruction"""
        console_output = output.get('console', '').strip()
        signature = output.get('signature', '::Let it bind::')
        
        return f'''
EXPECTED OUTPUT FORMAT:

1. Display the console output:
```
{console_output}
```

2. Generate a final result JSON object with:
   - ritual_id
   - status: "COMPLETE"
   - timestamp (current time)
   - Any additional fields from the finalization step

3. End with the signature: "{signature}"'''