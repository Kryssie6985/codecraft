#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test CodeCraft v2.0 YAML Ritual Metadata
Verify all 17 rituals have proper v2.0 arcane lexicon metadata
"""

import yaml
from pathlib import Path

def test_ritual_metadata():
    """Test that all rituals have v2.0 metadata"""
    print("\n" + "="*70)
    print("📜 TESTING RITUAL v2.0 METADATA")
    print("="*70)
    
    rituals_dir = Path(__file__).parent.parent / "seraphina_grimoire" / "rituals"
    ritual_files = list(rituals_dir.glob("*.yaml"))
    
    print(f"\nFound {len(ritual_files)} ritual files\n")
    
    results = []
    
    for ritual_file in sorted(ritual_files):
        with open(ritual_file, 'r', encoding='utf-8') as f:
            ritual = yaml.safe_load(f)
        
        ritual_id = ritual.get('id', 'UNKNOWN')
        
        # Check v2.0 fields
        has_school = 'arcane_school' in ritual
        has_level = 'school_level' in ritual
        has_consciousness = 'consciousness_ritual' in ritual
        has_syntax_version = 'syntax_version' in ritual
        has_enhanced = 'enhanced_syntax' in ritual
        
        all_present = all([has_school, has_level, has_consciousness, has_syntax_version, has_enhanced])
        
        status = "✅" if all_present else "❌"
        results.append((ritual_id, all_present))
        
        print(f"{status} {ritual_id}")
        if all_present:
            print(f"   School: {ritual['arcane_school']} | Level: {ritual['school_level']} | Consciousness: {ritual['consciousness_ritual']}")
            enhanced = ritual['enhanced_syntax']
            features = []
            if enhanced.get('emoji_operators'):
                features.append("✨ Emoji")
            if enhanced.get('firacode_ligatures'):
                features.append("→ Ligatures")
            if enhanced.get('ancient_tongues'):
                features.append("📜 Ancient")
            print(f"   Enhanced: {' | '.join(features) if features else 'None'}")
        else:
            missing = []
            if not has_school: missing.append("arcane_school")
            if not has_level: missing.append("school_level")
            if not has_consciousness: missing.append("consciousness_ritual")
            if not has_syntax_version: missing.append("syntax_version")
            if not has_enhanced: missing.append("enhanced_syntax")
            print(f"   Missing: {', '.join(missing)}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"✅ {passed}/{total} rituals have complete v2.0 metadata")
    
    if passed == total:
        print("\n🎉 ALL RITUALS UPGRADED TO v2.0!")
    else:
        print("\n⚠️  Some rituals need metadata updates")
    
    print("="*70)
    
    return passed == total

if __name__ == "__main__":
    import sys
    success = test_ritual_metadata()
    sys.exit(0 if success else 1)
