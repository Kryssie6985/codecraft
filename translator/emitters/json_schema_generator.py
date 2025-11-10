"""
JSON Schema Generator for the Rosetta Stone Protocol
Creates validation schemas for ritual payloads and LLM instruction
"""

from pathlib import Path
from typing import Dict, Any
import json

from ..ast_builder import RitualAST, ASTNode, NodeType

class JSONSchemaGenerator:
    """Generates JSON Schema from ritual AST"""
    
    def generate(self, ritual_def, ast: RitualAST, output_dir: Path) -> Path:
        """Generate JSON Schema file from ritual AST"""
        schema = self._generate_schema(ritual_def, ast)
        
        # Write to file
        output_path = output_dir / f"{ritual_def.id}.schema.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2)
        
        return output_path
    
    def _generate_schema(self, ritual_def, ast: RitualAST) -> Dict[str, Any]:
        """Generate JSON schema"""
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://seraphina.architect/schemas/rituals/{ritual_def.id}.json",
            "title": ritual_def.name,
            "description": ritual_def.description,
            "type": "object",
            "properties": {
                "ritual_id": {
                    "type": "string",
                    "const": ritual_def.id
                },
                "payload": self._generate_payload_schema(ast.metadata.get('payload', {})),
                "metadata": self._generate_metadata_schema(ast.metadata.get('metadata', {})),
                "result": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "timestamp": {"type": "string", "format": "date-time"}
                    }
                }
            },
            "required": ["ritual_id"]
        }
    
    def _generate_payload_schema(self, payload: Dict) -> Dict[str, Any]:
        """Generate schema for payload object"""
        if not payload:
            return {"type": "object"}
        
        properties = {}
        for key, value in payload.items():
            properties[key] = self._infer_type_schema(value)
        
        return {
            "type": "object",
            "properties": properties
        }
    
    def _generate_metadata_schema(self, metadata: Dict) -> Dict[str, Any]:
        """Generate schema for metadata object"""
        if not metadata:
            return {"type": "object"}
        
        properties = {}
        for key, value in metadata.items():
            properties[key] = self._infer_type_schema(value)
        
        return {
            "type": "object",
            "properties": properties
        }
    
    def _infer_type_schema(self, value: Any) -> Dict[str, Any]:
        """Infer JSON schema type from Python value"""
        if isinstance(value, str):
            return {"type": "string"}
        elif isinstance(value, bool):
            return {"type": "boolean"}
        elif isinstance(value, int):
            return {"type": "integer"}
        elif isinstance(value, float):
            return {"type": "number"}
        elif isinstance(value, list):
            if value:
                # Infer array item type from first element
                item_schema = self._infer_type_schema(value[0])
                return {"type": "array", "items": item_schema}
            return {"type": "array"}
        elif isinstance(value, dict):
            properties = {}
            for k, v in value.items():
                properties[k] = self._infer_type_schema(v)
            return {"type": "object", "properties": properties}
        else:
            return {"type": "string"}  # Default fallback