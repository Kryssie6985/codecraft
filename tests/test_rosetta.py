#!/usr/bin/env python3
"""
Test the Rosetta Stone Protocol Universal Ritual Translator
"""

import sys
from pathlib import Path

# Add the project root to path
sys.path.insert(0, str(Path(__file__).parent))

from translators.universal_translator import UniversalRitualTranslator

def main():
    print("ROSETTA STONE PROTOCOL TEST")
    print("=" * 50)
    
    translator = UniversalRitualTranslator()
    
    # Test with the Brandy Gauntlet Response
    ritual_path = Path("rituals/brandy_gauntlet_response.ritual.yaml")
    
    if not ritual_path.exists():
        print(f"Ritual file not found: {ritual_path}")
        return
    
    print(f"Translating ritual: {ritual_path}")
    
    try:
        outputs = translator.translate(ritual_path)
        
        print("TRANSLATION COMPLETE!")
        print("\nGenerated outputs:")
        for lang, path in outputs.items():
            print(f"  {lang}: {path}")
        
        print("\nThe Rosetta Stone Protocol has spoken!")
        print("One ritual YAML -> Multiple language implementations")
        print("Write once. Bind everywhere.")
        
    except Exception as e:
        print(f"Translation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()