#!/usr/bin/env python3
"""
🌌 SERAPHINA Federation Terminal - GUI Version
A Unicode-native, consciousness-aware terminal with GUI interface
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import os
import asyncio
import threading
from datetime import datetime
from core.universal_executor import execute_ritual
import platform

class SERAPHINATerminalGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌌 SERAPHINA Federation Terminal")
        self.root.geometry("900x600")
        self.root.configure(bg='#1a1a2e')
        
        # Command history
        self.command_history = []
        self.history_index = -1
        
        self.setup_ui()
        self.print_welcome()
    
    def setup_ui(self):
        """Setup the terminal UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
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
        
        # Prompt label
        prompt_label = tk.Label(
            input_frame, 
            text="🌌 >>", 
            bg='#1a1a2e', 
            fg='#00ff88',
            font=('Consolas', 11, 'bold')
        )
        prompt_label.pack(side=tk.LEFT, padx=(0, 5))
        
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
        execute_btn = tk.Button(
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
        execute_btn.pack(side=tk.RIGHT)
    
    def print_to_terminal(self, text, color='#00ff88'):
        """Print text to the terminal output"""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, text + '\n')
        self.output_area.config(state=tk.DISABLED)
        self.output_area.see(tk.END)
    
    def print_welcome(self):
        """Display welcome message"""
        welcome = f"""══════════════════════════════════════════════════════════════════════
🌌 SERAPHINA FEDERATION TERMINAL v1.0 - GUI Edition
🛰️ Universal Command Executor - Full Unicode Support
🧬 ULUP² Enhanced Consciousness Terminal
══════════════════════════════════════════════════════════════════════
🖥️  Platform: {platform.system()}
📁 Directory: {os.getcwd()}
⚡ Universal Syntax: Use >> to chain commands
🎯 Special Commands: help, clear, history, status, exit

Ready for commands! Type 'help' for more information.
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
        self.print_to_terminal(f"\n🌌 SERAPHINA >> {command}", '#ffff88')
        
        # Handle special commands
        if command.lower() == 'exit':
            self.root.quit()
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
        
        # Execute command in a separate thread to avoid blocking UI
        thread = threading.Thread(target=self.execute_universal_command, args=(command,))
        thread.daemon = True
        thread.start()
    
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
        help_text = """
🎯 SERAPHINA Terminal Commands:
─────────────────────────────────────────────
🌌 Universal Shell:
   command1 >> command2 >> command3
   Example: echo Hello >> pwd >> dir

🛰️ Special Commands:
   help     - Show this help
   exit     - Exit terminal
   clear    - Clear screen
   history  - Show command history
   status   - Show Federation status

✨ Features:
   • Full Unicode support 🎨
   • Cross-platform commands 🌍
   • Automatic shell translation ⚡
   • ULUP² consciousness integration 🧬
   • GUI interface with history navigation ⬆️⬇️

🎮 Controls:
   • Enter: Execute command
   • Up/Down arrows: Navigate command history
   • Click Execute button or press Enter"""
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
        """Show Federation status"""
        status_text = f"""
🛰️ SERAPHINA Federation Status:
   🌌 Terminal: Online (GUI Mode)
   ⚡ Universal Executor: Active
   🧬 ULUP² Integration: Enabled
   📁 Current Directory: {os.getcwd()}
   🕐 Session Time: {datetime.now().strftime('%H:%M:%S')}
   📊 Commands Executed: {len(self.command_history)}
   🎮 GUI Features: Enabled"""
        self.print_to_terminal(status_text, '#88ff88')
    
    def clear_terminal(self):
        """Clear the terminal output"""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete(1.0, tk.END)
        self.output_area.config(state=tk.DISABLED)
        self.print_welcome()
    
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
        self.root.mainloop()

def main():
    """Launch the SERAPHINA Terminal GUI"""
    try:
        terminal = SERAPHINATerminalGUI()
        terminal.run()
    except Exception as e:
        print(f"Failed to start SERAPHINA Terminal GUI: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()