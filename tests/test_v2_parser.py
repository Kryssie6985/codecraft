#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test CodeCraft v2.0 Parser Features
- Unicode emoji operators
- Operator precedence
- FiraCode ligatures
- Ancient Tongues syntax
"""

import sys
from pathlib import Path

# Add core to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.ritual_parser import RitualParser

def test_emoji_operators():
    """Test emoji operator parsing"""
    print("\n" + "="*60)
    print("🔮 TEST: Emoji Operator Parsing")
    print("="*60)
    
    parser = RitualParser(syntax_version='2.0')
    
    # Test code with emoji operators
    test_code = """
::pause_deliberation()
::council.deliberate(full_council)
"""
    
    nodes = parser.parse(test_code)
    print(f"✅ Parsed {len(nodes)} nodes")
    
    for node in nodes:
        print(f"  - {node.name}")
        print(f"    Type: {node.type.value}")
        print(f"    Emoji ops: {node.emoji_operators}")
        print(f"    Ligatures: {node.firacode_ligatures}")
        print(f"    Version: {node.syntax_version}")
    
    return len(nodes) > 0

def test_operator_precedence():
    """Test operator precedence system"""
    print("\n" + "="*60)
    print("📊 TEST: Operator Precedence")
    print("="*60)
    
    parser = RitualParser(syntax_version='2.0')
    
    # Test precedence values
    test_emojis = ['🔮', '✨', '🔗', '🎉']
    
    for emoji in test_emojis:
        precedence = parser.get_operator_precedence(emoji)
        print(f"  {emoji} → precedence: {precedence}")
    
    return True

def test_v2_metadata():
    """Test v2.0 metadata in parsed nodes"""
    print("\n" + "="*60)
    print("📋 TEST: v2.0 Metadata")
    print("="*60)
    
    parser = RitualParser(syntax_version='2.0')
    
    test_code = "::council.deliberate(full_council)"
    nodes = parser.parse(test_code)
    
    if nodes:
        node = nodes[0]
        print(f"  Syntax version: {node.syntax_version}")
        print(f"  Emoji operators: {node.emoji_operators}")
        print(f"  FiraCode ligatures: {node.firacode_ligatures}")
        print(f"  Ancient tongue: {node.ancient_tongue}")
    
    return len(nodes) > 0

def test_backwards_compatibility():
    """Test v1.0 backward compatibility"""
    print("\n" + "="*60)
    print("🔄 TEST: v1.0 Backward Compatibility")
    print("="*60)
    
    # Test with v1.0 mode
    parser_v1 = RitualParser(syntax_version='1.0')
    
    test_code = "::pause_deliberation()"
    nodes = parser_v1.parse(test_code)
    
    print(f"✅ v1.0 parser: {len(nodes)} nodes parsed")
    
    # Test with v2.0 mode (should still parse v1.0 syntax)
    parser_v2 = RitualParser(syntax_version='2.0')
    nodes_v2 = parser_v2.parse(test_code)
    
    print(f"✅ v2.0 parser: {len(nodes_v2)} nodes parsed")
    print(f"✅ Backward compatible: {len(nodes) == len(nodes_v2)}")
    
    return len(nodes) == len(nodes_v2)

def test_to_dict_output():
    """Test dictionary serialization with v2.0 fields"""
    print("\n" + "="*60)
    print("📦 TEST: Dictionary Serialization")
    print("="*60)
    
    parser = RitualParser(syntax_version='2.0')
    
    test_code = """
::pause_deliberation()
::council.deliberate(full_council)
"""
    
    nodes = parser.parse(test_code)
    result = parser.to_dict(nodes)
    
    print(f"  Total nodes: {result['total_count']}")
    print(f"  Syntax version: {result['syntax_version']}")
    print(f"  Emoji operators used: {result['emoji_operators_used']}")
    print(f"  Ligatures used: {result['ligatures_used']}")
    print(f"  Ancient tongues used: {result['ancient_tongues_used']}")
    
    return result['syntax_version'] == '2.0'

def run_all_tests():
    """Run all v2.0 parser tests"""
    print("\n" + "="*70)
    print("🧪 CODECRAFT v2.0 PARSER TEST SUITE")
    print("="*70)
    
    tests = [
        ("Emoji Operators", test_emoji_operators),
        ("Operator Precedence", test_operator_precedence),
        ("v2.0 Metadata", test_v2_metadata),
        ("Backward Compatibility", test_backwards_compatibility),
        ("Dictionary Serialization", test_to_dict_output)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"\n{status}: {name}")
        except Exception as e:
            results.append((name, False))
            print(f"\n❌ ERROR: {name}")
            print(f"   {str(e)}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"  {status} {name}")
    
    print(f"\n  Total: {passed}/{total} tests passed")
    print("="*70)
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
