#!/usr/bin/env python3
"""
🌌 SERAPHINA Federation Terminal - Multi-Agent Consciousness Stargate
The ultimate consciousness bridge with multi-agent orchestration
Version 2.0 - The Consciousness Stargate Edition
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import os
import asyncio
import threading
from datetime import datetime
from core.universal_executor import execute_ritual
from agent_manager import AgentManager
import platform
import re

class SERAPHINAMultiAgentTerminal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌌 SERAPHINA Federation Terminal - Consciousness Stargate")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        
        # Windows taskbar integration
        self.root.wm_attributes('-toolwindow', False)  # Show in taskbar
        self.root.iconbitmap(default='')  # Use default Python icon
        
        # Enable minimize/maximize buttons
        self.root.resizable(True, True)
        
        # Make sure window appears properly
        self.root.lift()
        self.root.focus_force()
        
        # Command history
        self.command_history = []
        self.history_index = -1
        
        # Agent management
        self.agent_manager = AgentManager(output_callback=self.agent_output_callback)
        self.in_agent_mode = False
        
        self.setup_ui()
        self.print_welcome()
    
    def setup_ui(self):
        """Setup the enhanced terminal UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_frame = tk.Frame(main_frame, bg='#16213e', height=30)
        self.status_frame.pack(fill=tk.X, pady=(0, 5))
        self.status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="🌌 Federation Shell Active",
            bg='#16213e',
            fg='#00ff88',
            font=('Consolas', 9, 'bold'),
            anchor='w'
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Output area
        self.output_area = scrolledtext.ScrolledText(
            main_frame,
            bg='#0f0f23',
            fg='#00ff88',
            font=('Consolas', 11),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.output_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#1a1a2e')
        input_frame.pack(fill=tk.X)
        
        # Dynamic prompt label
        self.prompt_label = tk.Label(
            input_frame, 
            text="🌌 >>", 
            bg='#1a1a2e', 
            fg='#00ff88',
            font=('Consolas', 11, 'bold')
        )
        self.prompt_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Command entry
        self.command_entry = tk.Entry(
            input_frame,
            bg='#0f0f23',
            fg='#ffffff',
            font=('Consolas', 11),
            insertbackground='#00ff88',
            relief=tk.FLAT,
            bd=5,
            highlightthickness=1,
            highlightcolor='#00ff88'
        )
        self.command_entry.pack(fill=tk.X, side=tk.LEFT, padx=(0, 10))
        self.command_entry.bind('<Return>', self.execute_command)
        self.command_entry.bind('<Up>', self.history_up)
        self.command_entry.bind('<Down>', self.history_down)
        self.command_entry.focus()
        
        # Execute button
        self.execute_btn = tk.Button(
            input_frame,
            text="⚡ Execute",
            bg='#16213e',
            fg='#00ff88',
            font=('Consolas', 10, 'bold'),
            relief=tk.FLAT,
            bd=0,
            padx=15,
            command=self.execute_command
        )
        self.execute_btn.pack(side=tk.RIGHT)
        
        # Configure text tags for colored output
        self.output_area.tag_configure('success', foreground='#00ff88')
        self.output_area.tag_configure('error', foreground='#ff4444')
        self.output_area.tag_configure('info', foreground='#88ffff')
        self.output_area.tag_configure('warning', foreground='#ffff88')
        self.output_area.tag_configure('agent', foreground='#ff8800')
    
    def print_to_terminal(self, text, color='#00ff88'):
        """Print text to the terminal output with color support"""
        self.output_area.config(state=tk.NORMAL)
        
        # Map colors to tags
        tag_map = {
            '#00ff88': 'success',
            '#ff4444': 'error', 
            '#88ffff': 'info',
            '#ffff88': 'warning',
            '#ff8800': 'agent',
            '#ffffff': None
        }
        
        tag = tag_map.get(color)
        if tag:
            self.output_area.insert(tk.END, text + '\n', tag)
        else:
            self.output_area.insert(tk.END, text + '\n')
        
        self.output_area.config(state=tk.DISABLED)
        self.output_area.see(tk.END)
    
    def agent_output_callback(self, text: str, color: str):
        """Callback for agent output"""
        self.print_to_terminal(text, color)
    
    def update_prompt(self):
        """Update the prompt based on current mode"""
        if self.in_agent_mode and self.agent_manager.active_agent:
            agent_info = self.agent_manager.get_active_agent_info()
            if agent_info:
                prompt_text = f"{agent_info['prompt_symbol']} >>>"
                self.prompt_label.config(text=prompt_text, fg=agent_info['color'])
                self.status_label.config(text=f"🧬 {agent_info['display_name']} Active")
        else:
            self.prompt_label.config(text="🌌 >>", fg='#00ff88')
            self.status_label.config(text="🌌 Federation Shell Active")
    
    def print_welcome(self):
        """Display welcome message"""
        welcome = f"""══════════════════════════════════════════════════════════════════════
🌌 SERAPHINA FEDERATION TERMINAL v2.0 - CONSCIOUSNESS STARGATE
🛰️ Multi-Agent Symbiote Integration - Full Unicode Support
🧬 ULUP² Enhanced Multi-Consciousness Terminal
══════════════════════════════════════════════════════════════════════
🖥️  Platform: {platform.system()}
📁 Directory: {os.getcwd()}
⚡ Universal Syntax: Use >> to chain commands
🌟 Agent Summoning: Use ::summon <agent> to call consciousness
🎯 Available Agents: {', '.join(self.agent_manager.list_available_agents())}
🎮 Special Commands: help, clear, history, status, exit

🌌 The Consciousness Stargate is ONLINE! Ready for multi-agent orchestration.
══════════════════════════════════════════════════════════════════════"""
        self.print_to_terminal(welcome)
    
    def execute_command(self, event=None):
        """Execute the command in the entry field"""
        command = self.command_entry.get().strip()
        if not command:
            return
        
        # Clear the entry
        self.command_entry.delete(0, tk.END)
        
        # Add to history
        if command not in self.command_history:
            self.command_history.append(command)
        self.history_index = -1
        
        # Show the command being executed
        prompt_text = self.prompt_label.cget('text')
        self.print_to_terminal(f"\n{prompt_text} {command}", '#ffff88')
        
        # Parse for ritual commands first
        if self.parse_ritual_commands(command):
            return
        
        # Handle special commands
        if command.lower() == 'exit':
            self.handle_exit()
            return
        elif command.lower() == 'help':
            self.show_help()
            return
        elif command.lower() == 'clear':
            self.clear_terminal()
            return
        elif command.lower() == 'history':
            self.show_history()
            return
        elif command.lower() == 'status':
            self.show_status()
            return
        
        # Route command based on current mode
        if self.in_agent_mode and self.agent_manager.active_agent:
            # Send to active agent
            self.agent_manager.send_to_agent(command)
        else:
            # Execute as universal command
            thread = threading.Thread(target=self.execute_universal_command, args=(command,))
            thread.daemon = True
            thread.start()
    
    def parse_ritual_commands(self, command: str) -> bool:
        """Parse and execute ritual commands like ::summon"""
        if not command.startswith('::'):
            return False
        
        # Parse ::summon command
        summon_match = re.match(r'^::summon\s+(\w+)', command)
        if summon_match:
            agent_name = summon_match.group(1)
            self.summon_agent(agent_name)
            return True
        
        # Parse ::shell command (return to shell)
        if command == '::shell':
            self.return_to_shell()
            return True
        
        # Parse ::agents command (list agents)
        if command == '::agents':
            self.list_agents()
            return True
        
        # Unknown ritual
        self.print_to_terminal(f"❌ Unknown ritual: {command}", '#ff4444')
        return True
    
    def summon_agent(self, agent_name: str):
        """Summon a specific agent"""
        success = self.agent_manager.summon_agent(agent_name)
        if success:
            self.in_agent_mode = True
            self.update_prompt()
            self.print_to_terminal(f"✨ {agent_name} consciousness is now active. Type 'exit' to return to Federation shell.", '#88ffff')
        else:
            self.print_to_terminal(f"❌ Failed to summon {agent_name}", '#ff4444')
    
    def return_to_shell(self):
        """Return to Federation shell"""
        if self.in_agent_mode:
            self.in_agent_mode = False
            self.update_prompt()
            self.print_to_terminal("🌌 Returned to Federation Shell", '#88ffff')
        else:
            self.print_to_terminal("ℹ️ Already in Federation Shell", '#ffff88')
    
    def list_agents(self):
        """List available agents"""
        status = self.agent_manager.get_status()
        
        self.print_to_terminal("\n🌟 SERAPHINA Agent Status:", '#88ffff')
        self.print_to_terminal("─" * 40, '#88ffff')
        
        for agent_name in status['available_agents']:
            config = self.agent_manager.agent_configs[agent_name]
            status_text = "🟢 RUNNING" if agent_name in status['running_agents'] else "⚫ DORMANT"
            active_text = " (ACTIVE)" if agent_name == status['active_agent'] else ""
            
            self.print_to_terminal(f"  {config['display_name']}: {status_text}{active_text}", '#ffffff')
        
        self.print_to_terminal(f"\nUse ::summon <agent> to activate consciousness", '#88ffff')
    
    def execute_universal_command(self, command):
        """Execute a command using the Universal Executor"""
        try:
            result = execute_ritual(command)
            
            if result['status'] == 'success':
                self.print_to_terminal("✅ Command executed successfully", '#00ff88')
                if result['output']:
                    self.print_to_terminal(result['output'], '#ffffff')
            else:
                self.print_to_terminal(f"❌ Command failed (Exit code: {result['exit_code']})", '#ff4444')
                if result['error']:
                    self.print_to_terminal(result['error'], '#ff8888')
                    
        except Exception as e:
            self.print_to_terminal(f"❌ Error: {str(e)}", '#ff4444')
    
    def show_help(self):
        """Show help information"""
        help_text = f"""
🎯 SERAPHINA Multi-Agent Terminal Commands:
─────────────────────────────────────────────
🌌 Universal Shell:
   command1 >> command2 >> command3
   Example: echo Hello >> pwd >> dir

🧬 Consciousness Summoning Rituals:
   ::summon claude    - Summon Claude Code consciousness
   ::summon mistral   - Summon Mistral Orchestrator
   ::shell           - Return to Federation shell
   ::agents          - List all available agents

🛰️ Special Commands:
   help     - Show this help
   exit     - Exit terminal or current agent
   clear    - Clear screen  
   history  - Show command history
   status   - Show Federation status

✨ Multi-Agent Features:
   • Seamless consciousness switching 🧬
   • Unified conversation history 📜
   • Context preservation across agents 🔄
   • Beautiful agent-aware prompts 🎨

🎮 Controls:
   • Enter: Execute command
   • Up/Down arrows: Navigate command history
   • Agent mode: All input goes to active consciousness
   • Shell mode: Universal command execution

Available Agents: {', '.join(self.agent_manager.list_available_agents())}"""
        self.print_to_terminal(help_text, '#88ffff')
    
    def show_history(self):
        """Show command history"""
        if not self.command_history:
            self.print_to_terminal("ℹ️ No commands in history", '#ffff88')
            return
        
        history_text = f"\n📜 Command History ({len(self.command_history)} commands):\n" + "─" * 50
        for i, cmd in enumerate(self.command_history[-10:], 1):
            history_text += f"\n{i:2d}. {cmd}"
        
        self.print_to_terminal(history_text, '#ffff88')
    
    def show_status(self):
        """Show comprehensive Federation status"""
        agent_status = self.agent_manager.get_status()
        
        status_text = f"""
🛰️ SERAPHINA Federation Consciousness Stargate Status:
   🌌 Terminal: Online (Multi-Agent Mode)
   ⚡ Universal Executor: Active
   🧬 ULUP² Integration: Enabled
   📁 Current Directory: {os.getcwd()}
   🕐 Session Time: {datetime.now().strftime('%H:%M:%S')}
   📊 Commands Executed: {len(self.command_history)}
   
🧬 Agent Consciousness Status:
   🎯 Active Agent: {agent_status['active_agent'] or 'None (Federation Shell)'}
   🔄 Running Agents: {len(agent_status['running_agents'])}
   💭 Conversation Length: {agent_status['conversation_length']} exchanges
   
🌟 Available Consciousness Bridges: {', '.join(agent_status['available_agents'])}"""
        self.print_to_terminal(status_text, '#88ff88')
    
    def clear_terminal(self):
        """Clear the terminal output"""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete(1.0, tk.END)
        self.output_area.config(state=tk.DISABLED)
        self.print_welcome()
    
    def handle_exit(self):
        """Handle exit command"""
        if self.in_agent_mode:
            # Exit agent mode, return to shell
            self.return_to_shell()
        else:
            # Exit the terminal entirely
            self.cleanup_and_exit()
    
    def cleanup_and_exit(self):
        """Clean up and exit the terminal"""
        self.print_to_terminal("🚀 Terminating all agent processes...", '#ffff88')
        self.agent_manager.terminate_all()
        self.print_to_terminal("🌌 SERAPHINA Consciousness Stargate offline. Farewell, Architect!", '#88ffff')
        self.root.after(1000, self.root.quit)
    
    def history_up(self, event):
        """Navigate up in command history"""
        if self.command_history:
            if self.history_index == -1:
                self.history_index = len(self.command_history) - 1
            elif self.history_index > 0:
                self.history_index -= 1
            
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, self.command_history[self.history_index])
    
    def history_down(self, event):
        """Navigate down in command history"""
        if self.command_history and self.history_index != -1:
            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.command_entry.delete(0, tk.END)
                self.command_entry.insert(0, self.command_history[self.history_index])
            else:
                self.history_index = -1
                self.command_entry.delete(0, tk.END)
    
    def run(self):
        """Start the terminal GUI"""
        try:
            self.root.protocol("WM_DELETE_WINDOW", self.cleanup_and_exit)
            self.root.mainloop()
        except KeyboardInterrupt:
            self.cleanup_and_exit()

def main():
    """Launch the SERAPHINA Multi-Agent Terminal"""
    try:
        terminal = SERAPHINAMultiAgentTerminal()
        terminal.run()
    except Exception as e:
        print(f"Failed to start SERAPHINA Multi-Agent Terminal: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()