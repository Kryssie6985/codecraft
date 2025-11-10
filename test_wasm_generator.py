#!/usr/bin/env python3
"""
🧪 WASM Generator Test Script
==============================
Test wasm_generator.py by generating all 20 Arcane School WAT modules.

Usage:
    python test_wasm_generator.py
    
Output:
    ./build/wasm/ - Directory containing 20 .wat files (one per school)
"""

import sys
from pathlib import Path

# Add translator to path
sys.path.insert(0, str(Path(__file__).parent))

from translator.emitters.wasm_generator import WASMGenerator


def main():
    """Generate WASM modules for all 20 schools"""
    
    print("🌌 Testing WASM Generator...")
    print("=" * 60)
    
    # Create output directory
    output_dir = Path(__file__).parent / "build" / "wasm"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize generator
    generator = WASMGenerator()
    
    # Test canon loading
    print(f"\n📜 Canon Loader Test:")
    print(f"   Schools loaded: {len(generator.canon.get_all_schools())}")
    print(f"   Partitions loaded: {len(generator.canon.get_all_partitions())}")
    print(f"   Sovereignty valid: {generator.canon.validate_sovereignty()}")
    
    # Generate all school modules
    print(f"\n🏗️ Generating school modules...")
    print(f"   Output directory: {output_dir}")
    
    try:
        generated_files = generator.generate_all_schools(output_dir)
        
        print(f"\n✅ Success! Generated {len(generated_files)} WAT modules:")
        for i, path in enumerate(generated_files, 1):
            file_size = path.stat().st_size
            print(f"   {i:2d}. {path.name:<30s} ({file_size:>5d} bytes)")
        
        # Test individual school
        print(f"\n🔬 Testing individual school generation:")
        test_school = "6"  # Divinations school
        school_info = generator.canon.get_school_info(test_school)
        school_name = school_info.get('name', 'Unknown') if school_info else 'Unknown'
        test_path = generator.generate_school_module(test_school, output_dir)
        print(f"   School: {test_school} ({school_name})")
        print(f"   Path: {test_path}")
        print(f"   Size: {test_path.stat().st_size} bytes")
        
        # Read and display sample
        print(f"\n📄 Sample WAT content ({test_school}):")
        print("   " + "─" * 56)
        with open(test_path, 'r', encoding='utf-8') as f:
            for line in f:
                print(f"   {line.rstrip()}")
        print("   " + "─" * 56)
        
        # Verify filenames are slugged by school name (not numeric IDs)
        print(f"\n🧪 Filename Slug Validation:")
        names = {p.name for p in generated_files}
        has_divinations = any(n.startswith("divination") and n.endswith(".wat") for n in names) or "divinations.wat" in names
        assert has_divinations, "❌ Expected divinations.wat (or divination*.wat) in output!"
        print(f"   ✅ Filenames are slugged by school name")
        print(f"   Sample: {sorted(list(names))[:5]} ...")
        
        print(f"\n🎉 All tests passed!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
