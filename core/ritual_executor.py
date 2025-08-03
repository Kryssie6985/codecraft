# CodeCraft Ritual Executor - The Reality-Bending Engine
# Transforms parsed ritual nodes into actual system actions

import asyncio
import subprocess
import json
import os
import logging
from typing import Dict, List, Any, Optional, Union, Callable
from datetime import datetime
from dataclasses import dataclass

from .ritual_parser import RitualNode, RitualType, RitualParser

logger = logging.getLogger(__name__)

@dataclass
class ExecutionResult:
    """Result of a ritual execution"""
    success: bool
    output: Any
    error: Optional[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

class RitualExecutor:
    """
    The Sacred Executor - Transforms CodeCraft rituals into reality
    Based on the Arcane Lexicon and v2.0 Protocol specifications
    """
    
    def __init__(self):
        self.parser = RitualParser()
        self.execution_handlers = self._initialize_handlers()
        self.context_shelf = {}  # Active context storage
        self.memory_fragments = []  # Captured memories
        self.council_session = None  # Active council deliberation
        self.flow_state = {
            "paused": False,
            "vetoed": False,
            "emergency_halt": False
        }
        
    def _initialize_handlers(self) -> Dict[str, Callable]:
        """Initialize all spell execution handlers"""
        return {
            # Flow Control Handlers (v2.0)
            "pause_deliberation": self._handle_pause_deliberation,
            "veto_current_flow": self._handle_veto_flow,
            "redirect_focus": self._handle_redirect_focus,
            "emergency_halt": self._handle_emergency_halt,
            
            # Council Handlers (v2.0)
            "council_deliberate": self._handle_council_deliberate,
            "user_join_council": self._handle_user_join_council,
            "direct_agent": self._handle_direct_agent,
            
            # Memory Handlers (v2.0)
            "scribe_capture": self._handle_scribe_capture,
            "context_shelve": self._handle_context_shelve,
            "context_retrieve": self._handle_context_retrieve,
            
            # Synthesis Handlers (v2.0)
            "unified_deliberation_mode": self._handle_unified_mode,
            
            # Governance Handlers (v2.0)
            "enforce_law": self._handle_enforce_law,
            
            # Arcane Lexicon Handlers
            "cantrip": self._handle_cantrip,
            "invocation": self._handle_invocation,
            "evocation": self._handle_evocation,
            "conjuration": self._handle_conjuration,
            "summoning": self._handle_summoning,
            "enchantment": self._handle_enchantment,
            "divination": self._handle_divination,
            "abjuration": self._handle_abjuration,
            "transmutation": self._handle_transmutation,
            "sigil": self._handle_sigil,
            "ward": self._handle_ward,
            "sanctification": self._handle_sanctification,
            
            # Generic handlers
            "generic_invoke": self._handle_generic_invoke
        }
    
    async def execute_ritual(self, ritual_text: str) -> List[ExecutionResult]:
        """
        Execute a complete CodeCraft ritual
        """
        logger.info(f"🔮 EXECUTING RITUAL: {ritual_text[:100]}...")
        
        # Parse the ritual
        nodes = self.parser.parse(ritual_text)
        
        # Execute each node
        results = []
        for node in nodes:
            if self.flow_state["emergency_halt"]:
                break
                
            if self.flow_state["paused"]:
                logger.info("⏸️ Deliberation paused, skipping execution")
                continue
                
            if self.flow_state["vetoed"]:
                logger.info("🚫 Flow vetoed, terminating execution")
                break
            
            result = await self._execute_node(node)
            results.append(result)
            
        return results
    
    async def _execute_node(self, node: RitualNode) -> ExecutionResult:
        """Execute a single ritual node"""
        try:
            handler_name = node.name
            handler = self.execution_handlers.get(handler_name)
            
            if not handler:
                # Try to map generic patterns to arcane lexicon
                handler = self._map_to_arcane_handler(node)
            
            if handler:
                logger.info(f"⚡ Executing {node.type.value}:{node.name}")
                result = await handler(node)
                logger.info(f"✨ Ritual completed: {result.success}")
                return result
            else:
                error_msg = f"Unknown ritual: {node.name}"
                logger.error(f"❌ {error_msg}")
                return ExecutionResult(
                    success=False,
                    output=None,
                    error=error_msg
                )
                
        except Exception as e:
            error_msg = f"Ritual execution failed: {str(e)}"
            logger.error(f"💥 {error_msg}")
            return ExecutionResult(
                success=False,
                output=None,
                error=error_msg
            )
    
    def _map_to_arcane_handler(self, node: RitualNode) -> Optional[Callable]:
        """Map generic invoke patterns to specific arcane handlers"""
        if node.name == "generic_invoke":
            target = node.parameters.get("target", "")
            
            # Map based on arcane lexicon prefixes
            if target.startswith("get:"):
                return self.execution_handlers["cantrip"]
            elif target.startswith("invoke:"):
                return self.execution_handlers["invocation"]
            elif target.startswith("evoke:"):
                return self.execution_handlers["evocation"]
            elif target.startswith("conjure:"):
                return self.execution_handlers["conjuration"]
            elif target.startswith("summon:"):
                return self.execution_handlers["summoning"]
            elif target.startswith("enchant:"):
                return self.execution_handlers["enchantment"]
            elif target.startswith("divine:"):
                return self.execution_handlers["divination"]
            elif target.startswith("abjure:"):
                return self.execution_handlers["abjuration"]
            elif target.startswith("transmute:"):
                return self.execution_handlers["transmutation"]
            elif target.startswith("sigil:"):
                return self.execution_handlers["sigil"]
            elif target.startswith("ward:"):
                return self.execution_handlers["ward"]
            elif target.startswith("sanctify:"):
                return self.execution_handlers["sanctification"]
        
        return None
    
    # =============================================================================
    # FLOW CONTROL HANDLERS (CodeCraft v2.0)
    # =============================================================================
    
    async def _handle_pause_deliberation(self, node: RitualNode) -> ExecutionResult:
        """Pause the current deliberation flow"""
        self.flow_state["paused"] = True
        logger.info("⏸️ Deliberation paused - context preserved")
        
        return ExecutionResult(
            success=True,
            output="Deliberation paused",
            metadata={"flow_state": self.flow_state.copy()}
        )
    
    async def _handle_veto_flow(self, node: RitualNode) -> ExecutionResult:
        """Veto the current flow"""
        self.flow_state["vetoed"] = True
        logger.info("🚫 Current flow vetoed")
        
        return ExecutionResult(
            success=True,
            output="Flow vetoed",
            metadata={"flow_state": self.flow_state.copy()}
        )
    
    async def _handle_redirect_focus(self, node: RitualNode) -> ExecutionResult:
        """Redirect deliberation focus to new topic"""
        new_topic = node.parameters.get("topic", "")
        logger.info(f"🎯 Redirecting focus to: {new_topic}")
        
        # Store the redirection in context
        self.context_shelf["current_focus"] = new_topic
        self.context_shelf["redirect_timestamp"] = datetime.utcnow().isoformat()
        
        return ExecutionResult(
            success=True,
            output=f"Focus redirected to: {new_topic}",
            metadata={"new_topic": new_topic}
        )
    
    async def _handle_emergency_halt(self, node: RitualNode) -> ExecutionResult:
        """Emergency halt - full stop with state checkpoint"""
        self.flow_state["emergency_halt"] = True
        
        # Create state checkpoint
        checkpoint = {
            "timestamp": datetime.utcnow().isoformat(),
            "context_shelf": self.context_shelf.copy(),
            "memory_fragments": self.memory_fragments.copy(),
            "flow_state": self.flow_state.copy()
        }
        
        logger.critical("🚨 EMERGENCY HALT - State checkpointed")
        
        return ExecutionResult(
            success=True,
            output="Emergency halt executed",
            metadata={"checkpoint": checkpoint}
        )
    
    # =============================================================================
    # MEMORY HANDLERS (CodeCraft v2.0)
    # =============================================================================
    
    async def _handle_scribe_capture(self, node: RitualNode) -> ExecutionResult:
        """Capture a memory fragment"""
        fragment = node.parameters.get("fragment", "")
        
        memory_entry = {
            "fragment": fragment,
            "timestamp": datetime.utcnow().isoformat(),
            "capture_method": "manual_scribe"
        }
        
        self.memory_fragments.append(memory_entry)
        logger.info(f"📜 Memory fragment captured: {fragment[:50]}...")
        
        return ExecutionResult(
            success=True,
            output="Memory fragment captured",
            metadata=memory_entry
        )
    
    async def _handle_context_shelve(self, node: RitualNode) -> ExecutionResult:
        """Shelve data in active context"""
        key = node.parameters.get("key", "")
        value = node.parameters.get("value", "")
        
        self.context_shelf[key] = value
        logger.info(f"📚 Context shelved: {key} = {value}")
        
        return ExecutionResult(
            success=True,
            output=f"Context shelved: {key}",
            metadata={"key": key, "value": value}
        )
    
    async def _handle_context_retrieve(self, node: RitualNode) -> ExecutionResult:
        """Retrieve data from context shelf"""
        key = node.parameters.get("key", "")
        value = self.context_shelf.get(key)
        
        if value is not None:
            logger.info(f"📖 Context retrieved: {key} = {value}")
            return ExecutionResult(
                success=True,
                output=value,
                metadata={"key": key, "value": value}
            )
        else:
            logger.warning(f"📭 Context key not found: {key}")
            return ExecutionResult(
                success=False,
                output=None,
                error=f"Context key '{key}' not found"
            )
    
    # =============================================================================
    # ARCANE LEXICON HANDLERS
    # =============================================================================
    
    async def _handle_cantrip(self, node: RitualNode) -> ExecutionResult:
        """Handle simple utility cantrips like ::get:timestamp()"""
        target = node.parameters.get("target", "")
        
        if "timestamp" in target:
            result = datetime.utcnow().isoformat()
            return ExecutionResult(success=True, output=result)
        
        return ExecutionResult(
            success=False,
            error=f"Unknown cantrip: {target}"
        )
    
    async def _handle_invocation(self, node: RitualNode) -> ExecutionResult:
        """Handle invocations - calling upon services/agents"""
        target = node.parameters.get("target", "")
        args = node.parameters.get("args", "")
        
        logger.info(f"🔥 INVOCATION: {target}({args})")
        
        # Example: ::invoke:system(['powershell', 'Stop-Process', '-Id', '115556'])
        if "system" in target:
            try:
                # Parse the system command
                if args.startswith("[") and args.endswith("]"):
                    # Parse list-style arguments
                    import ast
                    cmd_list = ast.literal_eval(args)
                    
                    if isinstance(cmd_list, list):
                        logger.info(f"⚡ Executing system command: {cmd_list}")
                        
                        # Execute the system command
                        result = subprocess.run(
                            cmd_list,
                            capture_output=True,
                            text=True,
                            timeout=30
                        )
                        
                        return ExecutionResult(
                            success=result.returncode == 0,
                            output=result.stdout if result.stdout else result.stderr,
                            metadata={
                                "command": cmd_list,
                                "return_code": result.returncode
                            }
                        )
                
            except Exception as e:
                return ExecutionResult(
                    success=False,
                    error=f"System invocation failed: {str(e)}"
                )
        
        # Placeholder for other invocations
        return ExecutionResult(
            success=True,
            output=f"Invocation executed: {target}",
            metadata={"target": target, "args": args}
        )
    
    async def _handle_evocation(self, node: RitualNode) -> ExecutionResult:
        """Handle evocations - creating something from nothing"""
        target = node.parameters.get("target", "")
        args = node.parameters.get("args", "")
        
        logger.info(f"✨ EVOCATION: Creating {target}")
        
        # Example: ::evoke:file(name="new.py")
        if "file" in target:
            # Parse file creation parameters
            # This is a placeholder - would need proper argument parsing
            return ExecutionResult(
                success=True,
                output=f"File evocation prepared: {args}",
                metadata={"type": "file_creation", "args": args}
            )
        
        return ExecutionResult(
            success=True,
            output=f"Evocation completed: {target}",
            metadata={"target": target}
        )
    
    # Placeholder handlers for remaining arcane spells
    async def _handle_conjuration(self, node: RitualNode) -> ExecutionResult:
        """Handle conjurations - bringing forth resources"""
        return ExecutionResult(success=True, output="Conjuration completed")
    
    async def _handle_summoning(self, node: RitualNode) -> ExecutionResult:
        """Handle summoning - calling specific entities"""
        return ExecutionResult(success=True, output="Entity summoned")
    
    async def _handle_enchantment(self, node: RitualNode) -> ExecutionResult:
        """Handle enchantments - modifying existing objects"""
        return ExecutionResult(success=True, output="Enchantment applied")
    
    async def _handle_divination(self, node: RitualNode) -> ExecutionResult:
        """Handle divinations - gaining knowledge"""
        return ExecutionResult(success=True, output="Knowledge divined")
    
    async def _handle_abjuration(self, node: RitualNode) -> ExecutionResult:
        """Handle abjurations - protective spells"""
        return ExecutionResult(success=True, output="Protection established")
    
    async def _handle_transmutation(self, node: RitualNode) -> ExecutionResult:
        """Handle transmutations - transforming objects"""
        return ExecutionResult(success=True, output="Transmutation completed")
    
    async def _handle_sigil(self, node: RitualNode) -> ExecutionResult:
        """Handle sigils - persistent event triggers"""
        return ExecutionResult(success=True, output="Sigil inscribed")
    
    async def _handle_ward(self, node: RitualNode) -> ExecutionResult:
        """Handle wards - defensive enchantments"""
        return ExecutionResult(success=True, output="Ward established")
    
    async def _handle_sanctification(self, node: RitualNode) -> ExecutionResult:
        """Handle sanctifications - redemption rituals"""
        return ExecutionResult(success=True, output="Sanctification completed")
    
    # Placeholder handlers for other v2.0 features
    async def _handle_council_deliberate(self, node: RitualNode) -> ExecutionResult:
        """Handle council deliberation"""
        return ExecutionResult(success=True, output="Council deliberation initiated")
    
    async def _handle_user_join_council(self, node: RitualNode) -> ExecutionResult:
        """Handle user joining council"""
        return ExecutionResult(success=True, output="User joined council")
    
    async def _handle_direct_agent(self, node: RitualNode) -> ExecutionResult:
        """Handle direct agent messaging"""
        return ExecutionResult(success=True, output="Agent message sent")
    
    async def _handle_unified_mode(self, node: RitualNode) -> ExecutionResult:
        """Handle unified deliberation mode"""
        return ExecutionResult(success=True, output="Unified mode activated")
    
    async def _handle_enforce_law(self, node: RitualNode) -> ExecutionResult:
        """Handle law enforcement"""
        return ExecutionResult(success=True, output="Law enforcement activated")
    
    async def _handle_generic_invoke(self, node: RitualNode) -> ExecutionResult:
        """Handle generic invocation patterns"""
        return ExecutionResult(success=True, output="Generic invocation completed")


# Convenience function for quick ritual execution
async def execute_codecraft(ritual_text: str) -> List[ExecutionResult]:
    """Quick function to execute CodeCraft rituals"""
    executor = RitualExecutor()
    return await executor.execute_ritual(ritual_text)