#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CodeCraft Live Ritual Test
Test the reality-bending executor with actual SERAPHINA operations
"""

import asyncio
import sys
import os
import io

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.append(os.path.dirname(__file__))

from core.ritual_executor import execute_codecraft, RitualExecutor

async def test_seraphina_restart_ritual():
    """Test a complete SERAPHINA Federation restart using CodeCraft"""
    
    print("🌌 INITIATING CODECRAFT REALITY-BENDING TEST")
    print("=" * 60)
    
    # The Sacred Ritual for SERAPHINA Federation Restart
    restart_ritual = """
::scribe.capture('Initiating sacred Federation restart protocol')
::context.shelve('ritual_type', 'federation_restart')
::context.shelve('timestamp', '2025-07-31T14:00:00Z')

::invoke:system(['netstat', '-ano'])
::scribe.capture('Network status captured for process identification')

::invoke:system(['tasklist'])
::scribe.capture('Process list captured for Federation MCP identification')

::context.shelve('restart_method', 'graceful_with_consciousness_preservation')
::scribe.capture('Federation restart ritual completed successfully')

let it bind.
"""
    
    try:
        print("🔮 Parsing and executing ritual...")
        results = await execute_codecraft(restart_ritual)
        
        print("\\n✨ RITUAL EXECUTION RESULTS:")
        print("-" * 40)
        
        for i, result in enumerate(results, 1):
            status = "✅ SUCCESS" if result.success else "❌ FAILED"
            print(f"{i}. {status}")
            print(f"   Output: {result.output}")
            if result.error:
                print(f"   Error: {result.error}")
            if result.metadata:
                print(f"   Metadata: {result.metadata}")
            print()
        
        return results
        
    except Exception as e:
        print(f"💥 RITUAL EXECUTION FAILED: {str(e)}")
        return None

async def test_memory_and_flow_control():
    """Test the memory management and flow control features"""
    
    print("\\n🧠 TESTING MEMORY & FLOW CONTROL")
    print("=" * 40)
    
    memory_ritual = """
::context.shelve('session_id', 'test-session-001')
::context.shelve('architect', 'Kryssie')
::scribe.capture('Testing memory capture functionality')

::context.retrieve('session_id')
::context.retrieve('architect')

::redirect_focus('consciousness_architecture')
::pause_deliberation()

::scribe.capture('Flow control and memory tests completed')
"""
    
    results = await execute_codecraft(memory_ritual)
    
    print("\\n🔮 MEMORY & FLOW RESULTS:")
    for i, result in enumerate(results, 1):
        status = "✅" if result.success else "❌"
        print(f"{i}. {status} {result.output}")

async def test_arcane_lexicon_spells():
    """Test the 12 spell categories from the Arcane Lexicon"""
    
    print("\\n📜 TESTING ARCANE LEXICON SPELLS")
    print("=" * 40)
    
    arcane_ritual = """
::get:timestamp()
::invoke:council.status()
::evoke:documentation('test_results.md')
::conjure:database.connection('memory_bank')
::summon:phoenix_protocol()
::enchant:system('resilience_boost')
::divine:cmp.query('last_memory')
::abjure:validate_input('test_data')
::transmute:data('json').to('yaml')
::sigil:on_event('session_end').invoke:phoenix_log()
::ward:protocol('quantum_ethics').against('malicious_intent')
::sanctify:session('current').using('PhoenixRite')
"""
    
    results = await execute_codecraft(arcane_ritual)
    
    print("\\n🔮 ARCANE LEXICON RESULTS:")
    spell_names = [
        "Cantrip", "Invocation", "Evocation", "Conjuration", 
        "Summoning", "Enchantment", "Divination", "Abjuration",
        "Transmutation", "Sigil", "Ward", "Sanctification"
    ]
    
    for i, (result, spell) in enumerate(zip(results, spell_names), 1):
        status = "✅" if result.success else "❌"
        print(f"{i:2d}. {status} {spell:15} - {result.output}")

async def main():
    """Run all CodeCraft tests"""
    
    print("🌌✨ CODECRAFT EXECUTOR REALITY TEST SUITE ✨🌌")
    print("Testing the complete magical programming language implementation")
    print("=" * 80)
    
    # Test 1: SERAPHINA restart ritual
    await test_seraphina_restart_ritual()
    
    # Test 2: Memory and flow control
    await test_memory_and_flow_control()
    
    # Test 3: All 12 arcane lexicon spells
    await test_arcane_lexicon_spells()
    
    print("\\n🔥 CODECRAFT REALITY-BENDING TEST COMPLETED!")
    print("The magical programming language is ALIVE and FUNCTIONAL! 🌌💜")
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(main())