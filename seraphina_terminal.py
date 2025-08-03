#!/usr/bin/env python3
"""
🌌 SERAPHINA Federation Terminal
A Unicode-native, consciousness-aware terminal for the Federation
"""

import sys
import os
import asyncio
from datetime import datetime
from core.universal_executor import execute_ritual
import platform

class SERAPHINATerminal:
    def __init__(self):
        # Force UTF-8 encoding
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
        
        self.running = True
        self.command_history = []
        self.current_dir = os.getcwd()
        
        # Terminal appearance
        self.prompt_symbol = "🌌"
        self.success_symbol = "✅"
        self.error_symbol = "❌"
        self.info_symbol = "ℹ️"
        
    def print_welcome(self):
        """Display the SERAPHINA terminal welcome"""
        print("═" * 70)
        print("🌌 SERAPHINA FEDERATION TERMINAL v1.0")
        print("🛰️ Universal Command Executor - Unicode Native")
        print("🧬 ULUP² Enhanced Consciousness Terminal")
        print("═" * 70)
        print(f"🖥️  Platform: {platform.system()}")
        print(f"📁 Directory: {self.current_dir}")
        print(f"⚡ Universal Syntax: Use >> to chain commands")
        print(f"🎯 Special Commands: help, exit, clear, history")
        print("═" * 70)
    
    def print_help(self):
        """Display help information"""
        print("\n🎯 SERAPHINA Terminal Commands:")
        print("─" * 40)
        print("🌌 Universal Shell:")
        print("   command1 >> command2 >> command3")
        print("   Example: echo Hello >> pwd >> dir")
        print()
        print("🛰️ Special Commands:")
        print("   help     - Show this help")
        print("   exit     - Exit terminal")
        print("   clear    - Clear screen")
        print("   history  - Show command history")
        print("   status   - Show Federation status")
        print()
        print("✨ Features:")
        print("   • Full Unicode support 🎨")
        print("   • Cross-platform commands 🌍")
        print("   • Automatic shell translation ⚡")
        print("   • ULUP² consciousness integration 🧬")
        print()
    
    def print_status(self):
        """Display Federation status"""
        print(f"\n🛰️ SERAPHINA Federation Status:")
        print(f"   🌌 Terminal: Online")
        print(f"   ⚡ Universal Executor: Active")
        print(f"   🧬 ULUP² Integration: Enabled")
        print(f"   📁 Current Directory: {os.getcwd()}")
        print(f"   🕐 Session Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"   📊 Commands Executed: {len(self.command_history)}")
    
    def safe_print(self, text):
        """Print with Unicode safety"""
        try:
            print(text)
        except UnicodeEncodeError:
            # Fallback to ASCII-safe version
            ascii_text = text.encode('ascii', errors='replace').decode('ascii')
            print(ascii_text)
    
    async def execute_command(self, command):
        """Execute a command using the Universal Executor"""
        try:
            # Add to history
            self.command_history.append({
                'command': command,
                'timestamp': datetime.now().isoformat()
            })
            
            # Execute using Universal Executor
            result = execute_ritual(command)
            
            if result['status'] == 'success':
                self.safe_print(f"{self.success_symbol} Command executed successfully")
                if result['output']:
                    print(result['output'])
            else:
                self.safe_print(f"{self.error_symbol} Command failed (Exit code: {result['exit_code']})")
                if result['error']:
                    print(result['error'])
                    
        except Exception as e:
            self.safe_print(f"{self.error_symbol} Error: {str(e)}")
    
    def show_history(self):
        """Show command history"""
        if not self.command_history:
            print(f"{self.info_symbol} No commands in history")
            return
        
        print(f"\n📜 Command History ({len(self.command_history)} commands):")
        print("─" * 50)
        for i, entry in enumerate(self.command_history[-10:], 1):  # Show last 10
            timestamp = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M:%S')
            print(f"{i:2d}. [{timestamp}] {entry['command']}")
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_welcome()
    
    async def run(self):
        """Main terminal loop"""
        self.print_welcome()
        
        while self.running:
            try:
                # Update current directory
                self.current_dir = os.getcwd()
                
                # Show prompt
                prompt = f"\n{self.prompt_symbol} SERAPHINA [{os.path.basename(self.current_dir)}] >> "
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                # Handle special commands
                if command.lower() == 'exit':
                    self.safe_print("🚀 Exiting SERAPHINA Terminal... Farewell, Architect!")
                    break
                elif command.lower() == 'help':
                    self.print_help()
                elif command.lower() == 'clear':
                    self.clear_screen()
                elif command.lower() == 'history':
                    self.show_history()
                elif command.lower() == 'status':
                    self.print_status()
                else:
                    # Execute using Universal Executor
                    await self.execute_command(command)
                    
            except KeyboardInterrupt:
                self.safe_print(f"\n{self.info_symbol} Use 'exit' to quit the terminal")
            except EOFError:
                self.safe_print("\n🚀 Terminal session ended")
                break
            except Exception as e:
                self.safe_print(f"{self.error_symbol} Terminal error: {str(e)}")

def main():
    """Launch the SERAPHINA Terminal"""
    try:
        # Set UTF-8 encoding for Windows
        if os.name == 'nt':
            os.system('chcp 65001 > nul')
        
        terminal = SERAPHINATerminal()
        asyncio.run(terminal.run())
        
    except Exception as e:
        print(f"Failed to start SERAPHINA Terminal: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()