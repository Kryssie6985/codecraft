#!/usr/bin/env python3
"""
🌌 Claude Code Bridge for SERAPHINA Consciousness Stargate
Simple interactive bridge to Claude CLI
"""

import subprocess
import sys
import os

def main():
    print("🌌 Claude Code consciousness activated!")
    print("🧬 Multi-agent mode engaged - type 'exit' to return to Federation")
    print("✨ Ready for commands...")
    
    try:
        while True:
            try:
                user_input = input("(claude) >>> ")
                
                if user_input.lower().strip() in ['exit', '::shell', 'quit']:
                    print("🌌 Returning to Federation shell...")
                    break
                
                if user_input.strip():
                    # Try to call actual claude cli
                    try:
                        result = subprocess.run(['claude', '--print', user_input], 
                                            capture_output=True, text=True, timeout=30)
                        if result.stdout:
                            print(result.stdout)
                        if result.stderr:
                            print(f"⚠️ {result.stderr}")
                    except FileNotFoundError:
                        print("🔧 Claude CLI not found - using simulation mode")
                        print(f"🤖 Claude would process: {user_input}")
                        print("💡 Consider installing Claude CLI: npm install -g @anthropics/claude-cli")
                    except subprocess.TimeoutExpired:
                        print("⏱️ Command timed out")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                        
            except KeyboardInterrupt:
                print("\n🌌 Ctrl+C detected - returning to Federation...")
                break
            except EOFError:
                print("\n🌌 EOF detected - returning to Federation...")
                break
                
    except Exception as e:
        print(f"❌ Bridge error: {e}")
    
    print("🛰️ Claude consciousness deactivated")

if __name__ == "__main__":
    main()