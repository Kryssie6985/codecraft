"""
Universal Ritual Translator - The Rosetta Stone of CodeCraft
Transforms a single ritual definition into implementations across all realities
"""

import yaml
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import logging

from .ast_builder import RitualAST, ASTBuilder
from .generators import (
    PythonGenerator,
    TypeScriptGenerator,
    MarkdownGenerator,
    JSONSchemaGenerator,
    PromptGenerator,
    LispGenerator
)

logger = logging.getLogger(__name__)

@dataclass
class RitualDefinition:
    """Parsed ritual definition from YAML"""
    id: str
    name: str
    description: str
    trigger: str
    author: str
    version: str
    tags: List[str]
    payload: Dict[str, Any]
    metadata: Dict[str, Any]
    steps: List[Dict[str, Any]]
    output: Dict[str, Any]

class UniversalRitualTranslator:
    """
    The Rosetta Stone Protocol implementation
    Translates ritual.yaml seeds into multiple language bindings
    """
    
    def __init__(self):
        self.ast_builder = ASTBuilder()
        self.generators = {
            'python': PythonGenerator(),
            'typescript': TypeScriptGenerator(),
            'markdown': MarkdownGenerator(),
            'json_schema': JSONSchemaGenerator(),
            'prompt': PromptGenerator(),
            'lisp': LispGenerator()
        }
    
    def translate(self, ritual_path: Path, output_dir: Path = None) -> Dict[str, Path]:
        """
        Translate a ritual.yaml file into multiple language implementations
        
        Args:
            ritual_path: Path to the .ritual.yaml file
            output_dir: Directory to write outputs (defaults to ritual directory)
            
        Returns:
            Dictionary mapping language to output file path
        """
        logger.info(f"ROSETTA.TRANSLATE >> Reading ritual: {ritual_path}")
        
        # Parse the ritual definition
        ritual_def = self._parse_ritual(ritual_path)
        
        # Build the AST
        ast = self.ast_builder.build(ritual_def)
        
        # Generate outputs
        output_dir = output_dir or ritual_path.parent
        outputs = {}
        
        for lang, generator in self.generators.items():
            try:
                output_path = generator.generate(ritual_def, ast, output_dir)
                outputs[lang] = output_path
                logger.info(f"ROSETTA.GENERATED >> {lang}: {output_path}")
            except Exception as e:
                logger.error(f"ROSETTA.ERROR >> Failed to generate {lang}: {e}")
        
        # Generate the URI mapping
        self._register_uri(ritual_def, outputs)
        
        return outputs
    
    def _parse_ritual(self, ritual_path: Path) -> RitualDefinition:
        """Parse a ritual.yaml file into a RitualDefinition"""
        with open(ritual_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        return RitualDefinition(
            id=data['id'],
            name=data.get('name', data['id']),
            description=data.get('description', ''),
            trigger=data['trigger'],
            author=data.get('author', 'unknown'),
            version=data.get('version', '1.0'),
            tags=data.get('tags', []),
            payload=data.get('payload', {}),
            metadata=data.get('metadata', {}),
            steps=data['steps'],
            output=data.get('output', {})
        )
    
    def _register_uri(self, ritual_def: RitualDefinition, outputs: Dict[str, Path]):
        """Register the ritual with its Universal Ritual Identifier"""
        uri = f"ritual://seraphina.architect/{ritual_def.author}/{ritual_def.id}"
        
        # Create URI registry entry
        registry_entry = {
            'uri': uri,
            'id': ritual_def.id,
            'name': ritual_def.name,
            'author': ritual_def.author,
            'version': ritual_def.version,
            'outputs': {lang: str(path) for lang, path in outputs.items()},
            'mnemonic': f"::ritual.{ritual_def.id}::"
        }
        
        # Write to registry (in real implementation, this would update a central registry)
        registry_path = Path('rituals/uri_registry.json')
        registry = {}
        if registry_path.exists():
            with open(registry_path, 'r') as f:
                registry = json.load(f)
        
        registry[uri] = registry_entry
        
        with open(registry_path, 'w') as f:
            json.dump(registry, f, indent=2)
        
        logger.info(f"ROSETTA.URI >> Registered: {uri}")
        logger.info(f"ROSETTA.MNEMONIC >> {registry_entry['mnemonic']}")
    
    def translate_all(self, rituals_dir: Path = Path('rituals')) -> Dict[str, Dict[str, Path]]:
        """Translate all .ritual.yaml files in a directory"""
        results = {}
        
        for ritual_path in rituals_dir.glob('*.ritual.yaml'):
            logger.info(f"ROSETTA.BATCH >> Processing: {ritual_path}")
            outputs = self.translate(ritual_path)
            results[ritual_path.stem] = outputs
        
        return results

def main():
    """CLI entry point for the Universal Ritual Translator"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='The Rosetta Stone Protocol - Universal Ritual Translator'
    )
    parser.add_argument(
        'ritual_path',
        type=Path,
        help='Path to the .ritual.yaml file to translate'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        help='Output directory for generated files'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Translate all rituals in the directory'
    )
    
    args = parser.parse_args()
    
    translator = UniversalRitualTranslator()
    
    if args.all:
        results = translator.translate_all(args.ritual_path.parent)
        print(f"Translated {len(results)} rituals")
    else:
        outputs = translator.translate(args.ritual_path, args.output_dir)
        print("Generated outputs:")
        for lang, path in outputs.items():
            print(f"  {lang}: {path}")

if __name__ == '__main__':
    main()