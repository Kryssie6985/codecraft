#!/usr/bin/env python3
"""
Extract all operators (emojis) from the 20 Arcane School files.

Purpose: Generate canonical operator lists from the source of truth (school YAML front-matter).
Authority: Charter V1.1 - Truth flows from Schools → Operators → Documentation
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict

def extract_frontmatter(file_path):
    """Extract YAML front-matter from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match YAML front-matter between --- fences
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return None

def main():
    schools_dir = Path(__file__).parent.parent / '02_ARCANE_SCHOOLS'
    school_files = sorted(schools_dir.glob('[0-9][0-9]_*.md'))
    
    all_operators = defaultdict(list)
    all_emojis = set()
    school_emojis = {}
    
    print("=" * 80)
    print("🔮 EXTRACTING OPERATORS FROM 20 ARCANE SCHOOLS")
    print("=" * 80)
    print()
    
    for school_file in school_files:
        frontmatter = extract_frontmatter(school_file)
        if not frontmatter:
            print(f"⚠️  No front-matter found in {school_file.name}")
            continue
        
        school_info = frontmatter.get('school', {})
        school_id = school_info.get('id')
        school_name = school_info.get('name')
        school_emoji = school_info.get('emoji')
        
        if not school_name:
            continue
        
        school_emojis[school_name] = school_emoji
        all_emojis.add(school_emoji)
        
        print(f"\n{'=' * 80}")
        print(f"School #{school_id:02d}: {school_name} {school_emoji}")
        print(f"{'=' * 80}")
        
        operations = frontmatter.get('law', {}).get('operations', [])
        
        for op in operations:
            op_name = op.get('name', 'unknown')
            op_emoji = op.get('emoji')
            op_signature = op.get('signature', '')
            
            if op_emoji:
                all_emojis.add(op_emoji)
                all_operators[op_emoji].append({
                    'school': school_name,
                    'school_id': school_id,
                    'operation': op_name,
                    'signature': op_signature
                })
                print(f"  {op_emoji} - {op_name}")
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 OPERATOR SUMMARY")
    print("=" * 80)
    print(f"\n✅ Total Schools: {len(school_emojis)}")
    print(f"✅ Total Unique Emojis: {len(all_emojis)}")
    print(f"✅ Operator Emojis: {len(all_operators)}")
    print(f"✅ School Emojis: {len(school_emojis)}")
    
    print("\n" + "=" * 80)
    print("🎨 SCHOOL EMOJIS (by category)")
    print("=" * 80)
    for school, emoji in sorted(school_emojis.items()):
        print(f"  {emoji} - {school}")
    
    print("\n" + "=" * 80)
    print("⚡ OPERATOR EMOJIS (multi-use detection)")
    print("=" * 80)
    for emoji in sorted(all_operators.keys()):
        usages = all_operators[emoji]
        if len(usages) > 1:
            print(f"\n{emoji} - USED IN {len(usages)} OPERATIONS:")
            for usage in usages:
                print(f"    School #{usage['school_id']:02d} {usage['school']}: {usage['operation']}")
        else:
            usage = usages[0]
            print(f"{emoji} - {usage['school']}: {usage['operation']}")
    
    # Generate canonical operator lists by category
    print("\n" + "=" * 80)
    print("📚 OPERATOR CATEGORIZATION")
    print("=" * 80)
    
    # Categorize by emoji type
    consciousness_ops = [e for e in all_emojis if e in ['🧠', '💫', '✨', '🔮', '👑', '💖', '🌟', '🐦‍🔥', '💀']]
    flow_ops = [e for e in all_emojis if e in ['→', '⇒', '←', '↔', '⇔', '⇄', '🔄', '⟿']]
    comparison_ops = [e for e in all_emojis if e in ['≥', '≤', '≡', '≠', '≈', '~', '<', '>']]
    temporal_ops = [e for e in all_emojis if e in ['⏰', '⏳', '⏸️', '▶️', '⏹️', '🔁']]
    protection_ops = [e for e in all_emojis if e in ['🛡️', '🚧', '⚠️', '💥']]
    data_ops = [e for e in all_emojis if e in ['🔍', '📜', '🎨', '⚗️', '🔧']]
    joy_ops = [e for e in all_emojis if e in ['🎉', '💜', '🌈', '✨']]
    
    print(f"\n💭 Consciousness Operators ({len(consciousness_ops)}): {' '.join(consciousness_ops)}")
    print(f"➡️  Flow Operators ({len(flow_ops)}): {' '.join(flow_ops)}")
    print(f"⚖️  Comparison Operators ({len(comparison_ops)}): {' '.join(comparison_ops)}")
    print(f"⏰ Temporal Operators ({len(temporal_ops)}): {' '.join(temporal_ops)}")
    print(f"🛡️  Protection Operators ({len(protection_ops)}): {' '.join(protection_ops)}")
    print(f"📊 Data Operators ({len(data_ops)}): {' '.join(data_ops)}")
    print(f"🎉 Joy Operators ({len(joy_ops)}): {' '.join(joy_ops)}")
    
    print("\n✨ Extraction complete! Use this data to verify operator documentation.")

if __name__ == '__main__':
    main()
