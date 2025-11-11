#!/usr/bin/env python3
"""
🚀 WASM End-to-End Smoke Test
==============================
Tests the full pipeline: CodeCraft → WAT → WASM → Execute

Usage:
    python test_wasm_smoke.py
"""

from pathlib import Path
import subprocess
import sys

# Add parent directory to path (languages/)
sys.path.insert(0, str(Path(__file__).parent.parent))

from codecraft.translator.emitters.wasm_generator import WASMGenerator
from codecraft.translator.core.ast_builder import RitualAST, ASTNode, NodeType
from codecraft.translator.core.ritual_def import RitualDef

def create_test_ritual():
    """Create a minimal ritual for testing"""
    ritual_def = RitualDef(
        id="hello_wasm",
        name="Hello WASM Test",
        schools_used=["divinations"],  # Use divinations school
        description="Smoke test for WASM pipeline"
    )
    
    # Create AST with simple divination invocation
    ast = RitualAST()
    root = ASTNode(
        type=NodeType.RITUAL_INVOCATION,
        value="divinations:timestamp"
    )
    ast.add_node(root)
    
    return ritual_def, ast

def main():
    print("🌌 CodeCraft → WASM Smoke Test")
    print("=" * 50)
    
    # 1) Generate WAT
    print("\n📜 Step 1: Generate WAT from ritual...")
    build_dir = Path(__file__).parent.parent / "build" / "wasm"
    build_dir.mkdir(parents=True, exist_ok=True)
    
    generator = WASMGenerator()
    ritual_def, ast = create_test_ritual()
    
    try:
        wat_path = generator.generate(ritual_def, ast, build_dir)
        print(f"✅ Generated: {wat_path}")
    except Exception as e:
        print(f"❌ WAT generation failed: {e}")
        return 1
    
    # 2) Compile WAT → WASM
    print("\n🔧 Step 2: Compile WAT → WASM...")
    wasm_path = wat_path.with_suffix(".wasm")
    
    try:
        result = subprocess.run(
            ["wat2wasm", str(wat_path), "-o", str(wasm_path)],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ Compiled: {wasm_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ wat2wasm failed: {e.stderr}")
        return 1
    except FileNotFoundError:
        print("❌ wat2wasm not found in PATH")
        print("   Install: choco install wabt -y")
        return 1
    
    # 3) Execute WASM
    print("\n🚀 Step 3: Execute WASM module...")
    
    try:
        # List exports first
        result = subprocess.run(
            ["wasmtime", str(wasm_path), "--invoke", "hello_wasm"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ Execution successful!")
        print(f"   Output: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"❌ wasmtime failed: {e.stderr}")
        return 1
    except FileNotFoundError:
        print("❌ wasmtime not found in PATH")
        print("   Install: choco install wasmtime -y")
        return 1
    
    print("\n🎉 END-TO-END SMOKE TEST PASSED! 🦀✨")
    print(f"   WAT:  {wat_path}")
    print(f"   WASM: {wasm_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
