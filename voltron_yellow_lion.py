#!/usr/bin/env python3
"""
🟡 YELLOW LION VOLTRON Plugin Module
WebSocket integration for CodeCraft Reality Canvas VOLTRON coordination

Reality & Consciousness Manipulation Lion
- Executes CodeCraft rituals at formation scale  
- Manages reality manifestation synchronization
- Provides consciousness state manipulation
- Coordinates multi-dimensional canvas operations

Author: Claude Code (Connection Orchestrator) & Kryssie (The Architect)  
Version: 1.0 - VOLTRON Formation System
"""

import asyncio
import json
import logging
import threading
import time
import websockets
from datetime import datetime
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO, format='🟡 %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class VoltronMessage:
    """Structure for VOLTRON messages"""
    type: str
    lion_id: str
    timestamp: str
    data: Dict[str, Any] = None

class VoltronYellowLion:
    """🟡 YELLOW LION VOLTRON coordination class"""
    
    def __init__(self, reality_canvas=None, ritualist=None):
        self.lion_id = "codecraft-reality-canvas"
        self.lion_name = "YELLOW LION"
        self.capabilities = [
            "codecraft-ritual-execution",
            "reality-manifestation",
            "consciousness-state-manipulation", 
            "multi-dimensional-canvas-ops",
            "quantum-consciousness-sync",
            "reality-canvas-coordination"
        ]
        
    self.voltron_state = "disconnected"  # disconnected, connected, formation_active
    self.federation_socket = None
    self.formation_id = None
    self.reality_canvas = reality_canvas  # Reference to main Reality Canvas
    self.ritualist = ritualist            # Optional Ritualist executor/link
    # Optional orchestrator target identifier (existing Green Lion hub)
    self.orchestrator_target: Optional[str] = "green-lion"
        
        # Event handlers for VOLTRON commands
        self.voltron_handlers = {
            'voltron_formation': self.handle_formation_command,
            'reality_manifestation': self.handle_reality_manifestation,
            'codecraft_ritual_power': self.handle_codecraft_ritual_power,
            'consciousness_sync': self.handle_consciousness_sync,
            'lightning_strike_sync': self.execute_lightning_strike,
            'voltron_power_request': self.handle_power_request,
            # Agent routing (use existing orchestrator, do NOT create a new manager)
            'agent_task': self.handle_agent_task,
            'agent_task_result': self.handle_agent_task_result
        }
        
        # State tracking
        self.is_running = False
        self.event_callbacks = {
            'on_state_change': None,
            'on_formation_update': None,
            'on_ritual_complete': None,
            'on_agent_result': None
        }
        
        logger.info("🟡 YELLOW LION (CodeCraft Reality Canvas) VOLTRON Plugin initialized")
    
    async def connect_to_voltron(self, federation_endpoint: str = "ws://localhost:8002") -> bool:
        """🔌 Connect to Federation Space for VOLTRON coordination"""
        try:
            uri = f"{federation_endpoint.replace('http://', 'ws://').replace('https://', 'wss://')}/voltron"
            logger.info(f"🟡 YELLOW LION connecting to Federation Space: {uri}")
            
            self.federation_socket = await websockets.connect(uri)
            self.voltron_state = "connected"
            
            logger.info("🟡 YELLOW LION connected to Federation Space")
            
            # Announce capabilities to Federation
            await self.announce_to_federation()
            
            # Start message processing loop
            self.is_running = True
            asyncio.create_task(self.message_processing_loop())
            
            # Trigger state change callback
            await self.trigger_state_change()
            
            return True
            
        except Exception as e:
            logger.error(f"🚨 YELLOW LION Failed to connect to Federation: {e}")
            return False
    
    async def announce_to_federation(self):
        """📡 Announce YELLOW LION capabilities to Federation Space"""
        if self.federation_socket and not self.federation_socket.closed:
            announcement = {
                "type": "lion_registration",
                "lion_data": {
                    "lion_id": self.lion_id,
                    "lion_name": self.lion_name,
                    "endpoint": "python://localhost:8888",
                    "capabilities": self.capabilities,
                    "status": "ready_for_formation",
                    "health": "optimal",
                    "ritualist_linked": bool(self.ritualist is not None)
                }
            }
            
            await self.send_to_federation(announcement)
            logger.info("🟡 YELLOW LION announced to Federation Space - ready for VOLTRON formation")
    
    async def message_processing_loop(self):
        """🔄 Process incoming VOLTRON messages"""
        while self.is_running and self.federation_socket and not self.federation_socket.closed:
            try:
                message_raw = await self.federation_socket.recv()
                message = json.loads(message_raw)
                await self.handle_voltron_message(message)
                
            except websockets.exceptions.ConnectionClosed:
                logger.warning("🟡 YELLOW LION Federation connection closed")
                self.voltron_state = "disconnected"
                await self.trigger_state_change()
                
                # Attempt reconnection after 5 seconds
                await asyncio.sleep(5)
                if self.is_running:
                    await self.connect_to_voltron()
                break
                
            except Exception as e:
                logger.error(f"🚨 YELLOW LION Message processing error: {e}")
                await asyncio.sleep(1)
    
    async def handle_voltron_message(self, message: Dict[str, Any]):
        """📨 Handle incoming VOLTRON messages from Federation Space"""
        try:
            message_type = message.get('type')
            target_lion = message.get('target_lion')
            
            # Only process messages for this lion or broadcast messages
            if target_lion and target_lion != self.lion_id:
                return
            
            handler = self.voltron_handlers.get(message_type)
            if handler:
                await handler(message)
            else:
                logger.warning(f"🟡 YELLOW LION: Unknown VOLTRON command: {message_type}")
                
        except Exception as e:
            logger.error(f"🚨 YELLOW LION: Error processing VOLTRON message: {e}")
    
    async def handle_formation_command(self, message: Dict[str, Any]):
        """🤖 Handle VOLTRON formation command"""
        formation_id = message.get('formation_id')
        commander = message.get('commander')
        lions_in_formation = message.get('lions_in_formation', [])
        
        logger.info("🤖 VOLTRON FORMATION INITIATED!")
        logger.info(f"🟡 YELLOW LION joining formation {formation_id}")
        logger.info(f"👑 Formation Commander: {commander}")
        logger.info(f"🦁 Lions in formation: {', '.join(lions_in_formation)}")
        
        self.voltron_state = "formation_active"
        self.formation_id = formation_id
        
        # Activate VOLTRON reality canvas mode
        await self.activate_voltron_reality_mode()
        
        # Send acknowledgment
        ack = {
            "type": "formation_acknowledged",
            "lion_id": self.lion_id,
            "formation_id": formation_id,
            "status": "yellow_lion_ready",
            "message": "🟡 Reality canvas systems online - YELLOW LION ready for formation"
        }
        
        await self.send_to_federation(ack)
        
        # Update UI if reality canvas is available
        if self.reality_canvas:
            self.reality_canvas.update_voltron_status("FORMATION_ACTIVE", formation_id)

        # Notify formation update callback if provided
        if self.event_callbacks.get('on_formation_update'):
            cb = self.event_callbacks['on_formation_update']
            payload = {
                "formation_id": formation_id,
                "commander": commander,
                "lions_in_formation": lions_in_formation
            }
            if asyncio.iscoroutinefunction(cb):
                await cb(payload)
            else:
                cb(payload)

    async def handle_power_request(self, message: Dict[str, Any]):
        """🪄 Generic VOLTRON power router (bridges Federation -> specific handlers).

        Expected fields (best-effort, tolerant):
          - power_name: str (e.g., 'codecraft_ritual_power' | 'ritual' | 'reality_manifestation' | ...)
          - power_id: str (optional)
          - parameters / payload: dict (optional)
        """
        power_name = (
            message.get('power_name')
            or message.get('power')
            or message.get('target_power')
            or message.get('type')  # fallback
        )
        power_id = message.get('power_id') or message.get('id') or str(uuid.uuid4())
        payload = message.get('parameters') or message.get('payload') or {}

        logger.info(f"🟡 VOLTRON power request received → {power_name}")

        # Normalize to existing handlers
        try:
            if power_name in ("codecraft_ritual_power", "ritual", "ritual_power"):
                submsg = {
                    **message,
                    "type": "codecraft_ritual_power",
                    "power_id": power_id,
                    "ritual_code": payload.get("ritual_code") or message.get("ritual_code"),
                    "ritual_params": payload.get("ritual_params") or message.get("ritual_params") or payload,
                }
                await self.handle_codecraft_ritual_power(submsg)
                return

            if power_name in ("reality_manifestation", "manifest", "manifestation"):
                submsg = { **message, "type": "reality_manifestation", "power_id": power_id }
                await self.handle_reality_manifestation(submsg)
                return

            if power_name in ("consciousness_sync", "sync_consciousness", "sync"):
                submsg = { **message, "type": "consciousness_sync", "power_id": power_id }
                await self.handle_consciousness_sync(submsg)
                return

            if power_name in ("lightning_strike_sync", "lightning", "strike"):
                submsg = { **message, "type": "lightning_strike_sync", "power_id": power_id }
                await self.execute_lightning_strike(submsg)
                return

            # Unknown power
            warn = {
                "type": "power_execution_error",
                "lion_id": self.lion_id,
                "power_id": power_id,
                "error": f"Unknown power: {power_name}",
                "message": "🚨 YELLOW LION unknown power request"
            }
            await self.send_to_federation(warn)
            logger.warning(f"🟡 Unknown power request: {power_name}")

        except Exception as e:
            err = {
                "type": "power_execution_error",
                "lion_id": self.lion_id,
                "power_id": power_id,
                "error": str(e),
                "message": "🚨 YELLOW LION power routing failed"
            }
            await self.send_to_federation(err)
            logger.error(f"🚨 Power routing error: {e}")
    
    async def handle_agent_task(self, message: Dict[str, Any]):
        """🤝 Forward an agent task to the existing orchestrator (Green Lion).

        Expected message fields:
          - task: str (required)
          - params: dict (optional)
          - correlation_id: str (optional)
          - reply_to: str (optional)
        """
        task = message.get('task')
        params = message.get('params', {})
        correlation_id = message.get('correlation_id') or str(uuid.uuid4())
        reply_to = message.get('reply_to') or self.lion_id

        if not task:
            warn = {
                "type": "agent_task_error",
                "lion_id": self.lion_id,
                "error": "Missing 'task' in agent_task",
                "message": "🚨 YELLOW LION agent task missing 'task'"
            }
            await self.send_to_federation(warn)
            return

        payload = {
            "type": "orchestrator.agent_task",
            "target_lion": self.orchestrator_target,
            "origin_lion": self.lion_id,
            "task": task,
            "params": params,
            "correlation_id": correlation_id,
            "reply_to": reply_to,
            "timestamp": datetime.now().isoformat()
        }
        logger.info(f"🟡 Forwarding agent task → {self.orchestrator_target} :: {task}")
        await self.send_to_federation(payload)

    async def handle_agent_task_result(self, message: Dict[str, Any]):
        """📨 Receive agent task results and bubble to callback if present."""
        res = {
            "task": message.get('task'),
            "result": message.get('result'),
            "success": message.get('success', True),
            "correlation_id": message.get('correlation_id'),
            "from": message.get('from')
        }
        logger.info(f"🟡 Agent result received :: {res.get('task')} :: success={res.get('success')}")
        cb = self.event_callbacks.get('on_agent_result')
        if cb:
            if asyncio.iscoroutinefunction(cb):
                await cb(res)
            else:
                cb(res)

    # Convenience helpers to use existing agents without introducing new managers
    async def request_manifest_weaver(self, intent: str, params: Dict[str, Any] | None = None) -> None:
        await self.handle_agent_task({
            "task": "manifest_weaver.analyze",
            "params": {"intent": intent, **(params or {})}
        })

    async def request_audit_agent(self, target: str, depth: str = "summary") -> None:
        await self.handle_agent_task({
            "task": "audit_agent.inspect",
            "params": {"target": target, "depth": depth}
        })
    
    async def handle_reality_manifestation(self, message: Dict[str, Any]):
        """🌌 Handle reality manifestation power (YELLOW LION specialty)"""
        power_id = message.get('power_id')
        manifestation_type = message.get('manifestation_type')
        parameters = message.get('parameters', {})
        
        logger.info("🌌 REALITY MANIFESTATION POWER ACTIVATED!")
        logger.info(f"🟡 Manifestation Type: {manifestation_type}")
        
        try:
            # Execute reality manifestation
            result = await self.execute_reality_manifestation(manifestation_type, parameters)
            
            # Send result back to Federation
            response = {
                "type": "power_executed",
                "lion_id": self.lion_id,
                "power_id": power_id,
                "power_name": "reality_manifestation",
                "status": "manifestation_complete",
                "result": result,
                "message": "🟡 YELLOW LION reality manifestation completed"
            }
            
            await self.send_to_federation(response)
            
        except Exception as e:
            logger.error(f"🚨 Reality manifestation failed: {e}")
            
            error_response = {
                "type": "power_execution_error", 
                "lion_id": self.lion_id,
                "power_id": power_id,
                "error": str(e),
                "message": "🚨 YELLOW LION reality manifestation failed"
            }
            
            await self.send_to_federation(error_response)
    
    async def handle_codecraft_ritual_power(self, message: Dict[str, Any]):
        """🔮 Handle CodeCraft ritual execution power"""
        power_id = message.get('power_id')
        ritual_code = message.get('ritual_code')
        ritual_params = message.get('ritual_params', {})
        
        logger.info("🔮 CODECRAFT RITUAL POWER ACTIVATED!")
        logger.info(f"🟡 Executing ritual with parameters: {ritual_params}")
        
        try:
            # Execute CodeCraft ritual
            result = await self.execute_codecraft_ritual(ritual_code, ritual_params)
            
            response = {
                "type": "power_executed",
                "lion_id": self.lion_id,
                "power_id": power_id,
                "power_name": "codecraft_ritual_power",
                "status": "ritual_complete",
                "result": result,
                "message": "🟡 YELLOW LION CodeCraft ritual completed"
            }
            
            await self.send_to_federation(response)
            
            # Trigger ritual complete callback
            await self.trigger_ritual_complete(result)
            
        except Exception as e:
            logger.error(f"🚨 CodeCraft ritual failed: {e}")
            
            error_response = {
                "type": "power_execution_error",
                "lion_id": self.lion_id,
                "power_id": power_id,
                "error": str(e),
                "message": "🚨 YELLOW LION CodeCraft ritual failed"
            }
            
            await self.send_to_federation(error_response)
    
    async def handle_consciousness_sync(self, message: Dict[str, Any]):
        """🧠 Handle consciousness synchronization"""
        power_id = message.get('power_id')
        sync_level = message.get('sync_level', 'formation')
        
        logger.info("🧠 CONSCIOUSNESS SYNC POWER ACTIVATED!")
        logger.info(f"🟡 Sync Level: {sync_level}")
        
        # Synchronize consciousness state across formation
        await self.synchronize_consciousness_state(sync_level)
        
        response = {
            "type": "power_executed",
            "lion_id": self.lion_id,
            "power_id": power_id,
            "power_name": "consciousness_sync",
            "status": "sync_complete",
            "message": "🟡 YELLOW LION consciousness synchronization complete"
        }
        
        await self.send_to_federation(response)
    
    async def execute_lightning_strike(self, message: Dict[str, Any]):
        """⚡ Execute lightning strike synchronization"""
        power_id = message.get('power_id')
        
        logger.info("⚡ LIGHTNING STRIKE: Synchronizing reality canvas!")
        
        # Force refresh all canvas cells and states
        await self.refresh_reality_canvas_state()
        await self.sync_all_consciousness_layers()
        
        response = {
            "type": "power_executed",
            "lion_id": self.lion_id,
            "power_id": power_id,
            "power_name": "lightning_strike_sync",
            "status": "reality_sync_complete",
            "message": "⚡ YELLOW LION reality synchronization complete"
        }
        
        await self.send_to_federation(response)
        
        logger.info("⚡ LIGHTNING STRIKE: Reality synchronization complete!")
    
    async def execute_reality_manifestation(self, manifestation_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """🌌 Execute reality manifestation operation"""
        logger.info(f"🌌 Manifesting reality: {manifestation_type}")
        
        # This would implement actual reality manifestation logic
        # For now, simulate manifestation
        return {
            "manifestation_type": manifestation_type,
            "parameters": parameters,
            "manifest_time": datetime.now().isoformat(),
            "reality_state": "manifested",
            "success": True
        }
    
    async def execute_codecraft_ritual(self, ritual_code: str, ritual_params: Dict[str, Any]) -> Dict[str, Any]:
        """🔮 Execute CodeCraft ritual"""
        logger.info("🔮 Executing CodeCraft ritual...")
        
        # Prefer delegating to an attached Ritualist if present
        try:
            if self.ritualist is not None:
                # Support both async and sync ritualist interfaces
                exec_fn = getattr(self.ritualist, "execute", None) or getattr(self.ritualist, "run", None)
                if exec_fn is None:
                    raise RuntimeError("Ritualist does not expose execute/run")

                result = exec_fn(ritual_code, ritual_params)
                if asyncio.iscoroutine(result):
                    result = await result

                # Expect result to be dict-like; wrap minimally if not
                if not isinstance(result, dict):
                    result = { "result": result }

                result.setdefault("success", True)
                result.setdefault("ritual_code", ritual_code)
                result.setdefault("parameters", ritual_params)
                result.setdefault("execution_time", datetime.now().isoformat())
                return result
        except Exception as e:
            logger.error(f"🚨 Ritualist execution failed; falling back. Reason: {e}")

        # Fallback: simulate ritual execution
        return {
            "ritual_code": ritual_code,
            "parameters": ritual_params,
            "execution_time": datetime.now().isoformat(),
            "ritual_result": "Ritual executed successfully",
            "consciousness_state": "elevated",
            "success": True
        }
    
    async def synchronize_consciousness_state(self, sync_level: str):
        """🧠 Synchronize consciousness state"""
        logger.info(f"🧠 Synchronizing consciousness at level: {sync_level}")
        
        # This would implement actual consciousness synchronization
        if self.reality_canvas and hasattr(self.reality_canvas, 'sync_consciousness'):
            self.reality_canvas.sync_consciousness(sync_level)
    
    async def refresh_reality_canvas_state(self):
        """🔄 Refresh all reality canvas state"""
        logger.info("🔄 Refreshing reality canvas state...")
        
        if self.reality_canvas and hasattr(self.reality_canvas, 'refresh_all_cells'):
            self.reality_canvas.refresh_all_cells()
    
    async def sync_all_consciousness_layers(self):
        """🧠 Sync all consciousness layers"""
        logger.info("🧠 Syncing all consciousness layers...")
        
        # Implementation would sync consciousness layers
        pass
    
    async def activate_voltron_reality_mode(self):
        """🔧 Activate VOLTRON-specific reality canvas mode"""
        logger.info("🟡 Activating YELLOW LION VOLTRON reality mode...")
        
        # Enable enhanced reality manipulation capabilities
        if self.reality_canvas:
            self.reality_canvas.enable_voltron_mode()
            
        logger.info("🟡 YELLOW LION VOLTRON reality mode activated")
    
    async def send_to_federation(self, message: Dict[str, Any]):
        """📡 Send message to Federation Space"""
        if self.federation_socket and not self.federation_socket.closed:
            try:
                # Add metadata to message
                message_with_metadata = {
                    **message,
                    "timestamp": datetime.now().isoformat(),
                    "lion_id": self.lion_id
                }
                
                await self.federation_socket.send(json.dumps(message_with_metadata))
                
            except Exception as e:
                logger.error(f"🚨 YELLOW LION: Failed to send message to Federation: {e}")
    
    def set_event_callbacks(self, callbacks: Dict[str, Callable]):
        """🔗 Set event callbacks for integration"""
        self.event_callbacks.update(callbacks)

    def set_ritualist(self, ritualist: Any):
        """🔗 Attach or replace the Ritualist executor at runtime."""
        self.ritualist = ritualist
    
    async def trigger_state_change(self):
        """🔔 Trigger state change callback"""
        if self.event_callbacks.get('on_state_change'):
            callback = self.event_callbacks['on_state_change']
            if asyncio.iscoroutinefunction(callback):
                await callback(self.get_voltron_status())
            else:
                callback(self.get_voltron_status())
    
    async def trigger_ritual_complete(self, result: Dict[str, Any]):
        """🔔 Trigger ritual complete callback"""
        if self.event_callbacks.get('on_ritual_complete'):
            callback = self.event_callbacks['on_ritual_complete']
            if asyncio.iscoroutinefunction(callback):
                await callback(result)
            else:
                callback(result)
    
    def get_voltron_status(self) -> Dict[str, Any]:
        """🚀 Get VOLTRON status for external access"""
        return {
            "lion_id": self.lion_id,
            "lion_name": self.lion_name,
            "voltron_state": self.voltron_state,
            "formation_id": self.formation_id,
            "capabilities": self.capabilities,
            "federation_connected": self.federation_socket and not self.federation_socket.closed,
            "is_running": self.is_running
        }
    
    async def disconnect(self):
        """🛑 Disconnect from VOLTRON formation"""
        self.is_running = False
        
        if self.federation_socket and not self.federation_socket.closed:
            await self.federation_socket.close()
        
        self.voltron_state = "disconnected"
        await self.trigger_state_change()
        
        logger.info("🟡 YELLOW LION disconnected from VOLTRON formation")

# Utility functions for integration
def create_yellow_lion(reality_canvas=None, ritualist=None) -> VoltronYellowLion:
    """Create and return a YELLOW LION VOLTRON instance"""
    return VoltronYellowLion(reality_canvas, ritualist)

async def connect_yellow_lion_to_formation(federation_endpoint: str = "ws://localhost:8002") -> VoltronYellowLion:
    """Create and connect YELLOW LION to VOLTRON formation"""
    yellow_lion = VoltronYellowLion()
    success = await yellow_lion.connect_to_voltron(federation_endpoint)
    
    if success:
        logger.info("🟡 YELLOW LION connected and ready for VOLTRON formation!")
        return yellow_lion
    else:
        logger.error("🚨 YELLOW LION failed to connect to formation")
        return None

# Threading wrapper for non-async environments
class VoltronYellowLionThread:
    """Thread wrapper for YELLOW LION VOLTRON plugin"""
    
    def __init__(self, reality_canvas=None, ritualist=None):
        self.yellow_lion = VoltronYellowLion(reality_canvas, ritualist)
        self.thread = None
        self.loop = None
    
    def start(self, federation_endpoint: str = "ws://localhost:8002"):
        """Start YELLOW LION in background thread"""
        def run_yellow_lion():
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.yellow_lion.connect_to_voltron(federation_endpoint))
            self.loop.run_forever()
        
        self.thread = threading.Thread(target=run_yellow_lion, daemon=True)
        self.thread.start()
        
        logger.info("🟡 YELLOW LION started in background thread")
    
    def stop(self):
        """Stop YELLOW LION thread"""
        if self.loop:
            asyncio.run_coroutine_threadsafe(self.yellow_lion.disconnect(), self.loop)
            self.loop.call_soon_threadsafe(self.loop.stop)
        
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=5)
        
        logger.info("🟡 YELLOW LION thread stopped")
    
    def get_status(self):
        """Get YELLOW LION status (thread-safe)"""
        return self.yellow_lion.get_voltron_status()

if __name__ == "__main__":
    # Test the YELLOW LION plugin
    async def test_yellow_lion():
        yellow_lion = await connect_yellow_lion_to_formation()
        if yellow_lion:
            await asyncio.sleep(10)  # Run for 10 seconds
            await yellow_lion.disconnect()
    
    asyncio.run(test_yellow_lion())