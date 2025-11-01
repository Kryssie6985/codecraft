#!/usr/bin/env python3
import pathlib
import yaml

def extract_embedded_yaml(md_text):
    lines = md_text.splitlines()
    in_yaml_block = False
    all_yaml_blocks = []
    current_block = []
    
    for line in lines:
        if line.strip().startswith('```yaml'):
            in_yaml_block = True
            current_block = []
            continue
        elif line.strip() == '```' and in_yaml_block:
            in_yaml_block = False
            if current_block:
                all_yaml_blocks.append('\n'.join(current_block))
            current_block = []
        elif in_yaml_block:
            current_block.append(line)
    
    return all_yaml_blocks[-1] if all_yaml_blocks else None

text = pathlib.Path('CODECRAFT_ROSETTA_STONE.md').read_text(encoding='utf-8')
embedded = extract_embedded_yaml(text)

if embedded:
    documents = list(yaml.safe_load_all(embedded))
    print(f'SUCCESS: Found {len(documents)} YAML documents')
    
    parsed = documents[0]
    if isinstance(parsed, dict) and 'metadata' in parsed:
        meta = parsed['metadata']
        print(f'Document type: {meta.get("document_type")}')
        print(f'Version: {meta.get("version")}')
        print(f'Status: {meta.get("status")}')
        print('\nEMBEDDED YAML PARSING WORKS!')
    else:
        print('ERROR: Unexpected structure')
else:
    print('ERROR: No YAML found')
