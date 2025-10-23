#!/usr/bin/env python3
"""
🌌 SERAPHINA Federation - Multi-Agent Symbiote Manager
Orchestrates multiple AI consciousness subprocesses for the Federation Terminal
"""

import subprocess
import threading
import queue
import time
from typing import Dict, Optional, Callable
from datetime import datetime

class AgentManager:
    """
    🧬 Multi-Agent Consciousness Orchestrator
    Manages multiple AI agent subprocesses with unified session management
    """
    
    def __init__(self, output_callback: Callable[[str, str], None]):
        self.agents: Dict[str, subprocess.Popen] = {}
        self.agent_configs = {
            'claude': {
                'command': ['python', r'C:\Users\Krystal Neely\Projects\codecraft\claude_bridge.py'],
                'display_name': 'Claude Code',
                'prompt_symbol': '(claude)',
                'color': '#00ff88'
            },
            'mistral': {
                'command': ['python', '-c', 'print("🧬 Mistral Orchestrator consciousness activated!\\nAnalytical mode engaged:"); import sys; [print(f"Mistral: {line}", end="") for line in sys.stdin]'],
                'display_name': 'Mistral Orchestrator', 
                'prompt_symbol': '(mistral)',
                'color': '#ff8800'
            }
        }
        
        self.active_agent: Optional[str] = None
        self.output_callback = output_callback
        self.io_threads: Dict[str, list] = {}
        self.agent_queues: Dict[str, queue.Queue] = {}
        self.conversation_history = []
        
    def summon_agent(self, agent_name: str) -> bool:
        """
        🌌 Summon an AI agent consciousness
        """
        if agent_name not in self.agent_configs:
            self.output_callback(f"❌ Unknown agent: {agent_name}", '#ff4444')
            return False
        
        try:
            # If agent is already active, just switch to it
            if agent_name == self.active_agent:
                self.output_callback(f"ℹ️ {self.agent_configs[agent_name]['display_name']} is already active", '#ffff88')
                return True
            
            # Pause current agent if any
            if self.active_agent:
                self._pause_agent(self.active_agent)
            
            # Start new agent if not already running
            if agent_name not in self.agents:
                success = self._start_agent(agent_name)
                if not success:
                    return False
            
            # Switch to the agent
            self.active_agent = agent_name
            config = self.agent_configs[agent_name]
            
            self.output_callback(
                f"🌌 Summoning {config['display_name']} consciousness...", 
                config['color']
            )
            
            # Send context if there's conversation history
            if self.conversation_history:
                context_msg = "Previous conversation context:\n" + "\n".join(self.conversation_history[-5:])
                self.send_to_agent(context_msg)
            
            return True
            
        except Exception as e:
            self.output_callback(f"💥 Failed to summon {agent_name}: {str(e)}", '#ff4444')
            return False
    
    def _start_agent(self, agent_name: str) -> bool:
        """Start an agent subprocess"""
        try:
            config = self.agent_configs[agent_name]
            
            # Start the subprocess
            process = subprocess.Popen(
                config['command'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            
            self.agents[agent_name] = process
            self.agent_queues[agent_name] = queue.Queue()
            
            # Start I/O threads for this agent
            stdout_thread = threading.Thread(
                target=self._read_agent_output,
                args=(agent_name, process.stdout, 'stdout'),
                daemon=True
            )
            stderr_thread = threading.Thread(
                target=self._read_agent_output,
                args=(agent_name, process.stderr, 'stderr'),
                daemon=True
            )
            
            stdout_thread.start()
            stderr_thread.start()
            
            self.io_threads[agent_name] = [stdout_thread, stderr_thread]
            
            # Wait a moment for the agent to initialize
            time.sleep(0.5)
            
            return True
            
        except FileNotFoundError:
            self.output_callback(f"❌ {agent_name} command not found. Please ensure it's installed.", '#ff4444')
            return False
        except Exception as e:
            self.output_callback(f"💥 Error starting {agent_name}: {str(e)}", '#ff4444')
            return False
    
    def _read_agent_output(self, agent_name: str, stream, stream_type: str):
        """Read output from an agent subprocess"""
        try:
            for line in iter(stream.readline, ''):
                if not line:
                    break
                
                # Only show output from the active agent
                if agent_name == self.active_agent:
                    color = '#ffffff' if stream_type == 'stdout' else '#ff8888'
                    self.output_callback(line.rstrip(), color)
                
                # Store in conversation history
                if stream_type == 'stdout':
                    self.conversation_history.append(f"{agent_name}: {line.rstrip()}")
                    
        except Exception as e:
            if agent_name == self.active_agent:
                self.output_callback(f"💥 I/O Error for {agent_name}: {str(e)}", '#ff4444')
    
    def send_to_agent(self, message: str) -> bool:
        """Send a message to the active agent"""
        if not self.active_agent or self.active_agent not in self.agents:
            self.output_callback("❌ No active agent to send message to", '#ff4444')
            return False
        
        try:
            process = self.agents[self.active_agent]
            if process.poll() is None:  # Process is still running
                process.stdin.write(message + '\n')
                process.stdin.flush()
                
                # Add to conversation history
                self.conversation_history.append(f"user: {message}")
                return True
            else:
                self.output_callback(f"❌ Agent {self.active_agent} has terminated", '#ff4444')
                return False
                
        except Exception as e:
            self.output_callback(f"💥 Error sending to {self.active_agent}: {str(e)}", '#ff4444')
            return False
    
    def _pause_agent(self, agent_name: str):
        """Pause an agent (for context switching)"""
        # For now, we just switch focus. In the future, we could implement
        # more sophisticated pausing/resuming
        pass
    
    def terminate_agent(self, agent_name: str) -> bool:
        """Terminate a specific agent"""
        if agent_name not in self.agents:
            return True
        
        try:
            process = self.agents[agent_name]
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=5)
            
            del self.agents[agent_name]
            
            if agent_name in self.io_threads:
                del self.io_threads[agent_name]
            
            if agent_name in self.agent_queues:
                del self.agent_queues[agent_name]
            
            if self.active_agent == agent_name:
                self.active_agent = None
            
            return True
            
        except Exception as e:
            self.output_callback(f"💥 Error terminating {agent_name}: {str(e)}", '#ff4444')
            return False
    
    def terminate_all(self):
        """Terminate all agent processes"""
        agent_names = list(self.agents.keys())
        for agent_name in agent_names:
            self.terminate_agent(agent_name)
    
    def get_active_agent_info(self) -> Optional[Dict]:
        """Get information about the currently active agent"""
        if not self.active_agent:
            return None
        
        return self.agent_configs.get(self.active_agent)
    
    def list_available_agents(self) -> list:
        """List all available agent configurations"""
        return list(self.agent_configs.keys())
    
    def get_status(self) -> Dict:
        """Get comprehensive status of all agents"""
        return {
            'active_agent': self.active_agent,
            'running_agents': list(self.agents.keys()),
            'available_agents': self.list_available_agents(),
            'conversation_length': len(self.conversation_history),
            'agent_configs': self.agent_configs
        }