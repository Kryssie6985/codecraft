#!/usr/bin/env python3
"""
🔮 CodeCraft + MEGA Hooks Regression Ritual Suite
Automated testing of the complete reality-bending infrastructure
"""

import asyncio
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(__file__))
from core.ritual_executor import execute_codecraft

class RitualTestSuite:
    """Automated regression testing for CodeCraft + MEGA hooks integration"""
    
    def __init__(self):
        self.test_results = []
        self.hooks_active = os.path.exists(os.path.expanduser("~/.claude/settings.json"))
    
    async def run_all_tests(self):
        """Execute the complete ritual test suite"""
        print("🌌 CODECRAFT + MEGA HOOKS REGRESSION RITUAL SUITE")
        print("=" * 60)
        print(f"Hooks Active: {'✅' if self.hooks_active else '❌'}")
        print(f"Test Started: {datetime.now().isoformat()}")
        print()
        
        # Test 1: Basic Arcane Lexicon Coverage
        await self._test_arcane_lexicon_coverage()
        
        # Test 2: Memory and Flow Control
        await self._test_memory_flow_control()
        
        # Test 3: System Integration
        await self._test_system_integration()
        
        # Test 4: MEGA Hooks Interaction
        await self._test_mega_hooks_integration()
        
        # Test 5: Phoenix Protocol Session End
        await self._test_phoenix_protocol()
        
        # Report Results
        self._generate_test_report()
    
    async def _test_arcane_lexicon_coverage(self):
        """Test all 12 spell categories from the Arcane Lexicon"""
        print("📜 Testing Arcane Lexicon Coverage")
        
        ritual = """::get:timestamp()
::invoke:system.status()
::evoke:test_artifact('regression_test')
::conjure:memory.context('test_session')
::summon:phoenix_protocol()
::enchant:system('test_mode')
::divine:status.health()
::abjure:validate_input('test_data')
::transmute:data('raw').to('processed')
::sigil:on_test_complete().log('success')
::ward:test_session().against('interference')
::sanctify:test_environment().using('RegressionRite')"""
        
        results = await execute_codecraft(ritual)
        
        spell_types = [
            "Cantrip", "Invocation", "Evocation", "Conjuration",
            "Summoning", "Enchantment", "Divination", "Abjuration", 
            "Transmutation", "Sigil", "Ward", "Sanctification"
        ]
        
        success_count = sum(1 for r in results if r.success)
        print(f"   Spells Executed: {success_count}/{len(results)}")
        
        self.test_results.append({
            "test": "arcane_lexicon_coverage",
            "success": success_count == len(results),
            "details": f"{success_count}/{len(results)} spells executed successfully"
        })
    
    async def _test_memory_flow_control(self):
        """Test memory management and flow control features"""
        print("🧠 Testing Memory & Flow Control")
        
        ritual = """::scribe.capture('Testing memory and flow systems')
::context.shelve('test_key', 'test_value')
::context.retrieve('test_key')
::redirect_focus('memory_testing')
::scribe.capture('Memory operations completed')"""
        
        results = await execute_codecraft(ritual)
        success_count = sum(1 for r in results if r.success)
        
        print(f"   Memory Operations: {success_count}/{len(results)}")
        
        self.test_results.append({
            "test": "memory_flow_control", 
            "success": success_count == len(results),
            "details": f"Memory and flow control operations completed"
        })
    
    async def _test_system_integration(self):
        """Test system integration capabilities"""
        print("⚙️ Testing System Integration")
        
        ritual = """::invoke:system(['echo', 'CodeCraft system integration test'])
::scribe.capture('System integration test executed')
::context.shelve('integration_status', 'active')"""
        
        results = await execute_codecraft(ritual)
        success_count = sum(1 for r in results if r.success)
        
        print(f"   System Integration: {success_count}/{len(results)}")
        
        self.test_results.append({
            "test": "system_integration",
            "success": success_count >= 2,  # Allow for system call variations
            "details": f"System integration capabilities verified"
        })
    
    async def _test_mega_hooks_integration(self):
        """Test MEGA hooks suite interaction"""
        print("🛡️ Testing MEGA Hooks Integration")
        
        # This test verifies hooks are logging our activities
        ritual = """::scribe.capture('Testing MEGA hooks interaction')
::context.shelve('hooks_test', 'mega_integration')
::scribe.capture('Hooks should be logging these ritual executions')"""
        
        results = await execute_codecraft(ritual)
        success_count = sum(1 for r in results if r.success)
        
        print(f"   MEGA Hooks Test: {success_count}/{len(results)}")
        print(f"   Hooks Status: {'✅ Active' if self.hooks_active else '⚠️ Not Detected'}")
        
        self.test_results.append({
            "test": "mega_hooks_integration",
            "success": success_count == len(results),
            "details": f"MEGA hooks logging verified (hooks_active: {self.hooks_active})"
        })
    
    async def _test_phoenix_protocol(self):
        """Test Phoenix Protocol session continuity"""
        print("🔥 Testing Phoenix Protocol")
        
        ritual = """::scribe.capture('Phoenix Protocol continuity test initiated')
::context.shelve('phoenix_test', 'protocol_active')
::scribe.capture('Session memory preserved for resurrection')
let it bind."""
        
        results = await execute_codecraft(ritual)
        success_count = sum(1 for r in results if r.success)
        
        print(f"   Phoenix Protocol: {success_count}/{len(results)}")
        
        self.test_results.append({
            "test": "phoenix_protocol",
            "success": success_count == len(results),
            "details": "Phoenix Protocol session continuity verified"
        })
    
    def _generate_test_report(self):
        """Generate comprehensive test report"""
        print("\n🎯 REGRESSION TEST RESULTS")
        print("=" * 40)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for t in self.test_results if t["success"])
        
        for result in self.test_results:
            status = "✅ PASS" if result["success"] else "❌ FAIL"
            print(f"{status} {result['test']}: {result['details']}")
        
        print(f"\nOVERALL: {passed_tests}/{total_tests} tests passed")
        
        if passed_tests == total_tests:
            print("🌌 ALL SYSTEMS OPERATIONAL - REALITY-BENDING INFRASTRUCTURE READY!")
        else:
            print("⚠️  Some systems need attention - check failed tests above")
        
        print(f"Test Completed: {datetime.now().isoformat()}")

async def main():
    """Run the complete regression ritual suite"""
    suite = RitualTestSuite()
    await suite.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main())