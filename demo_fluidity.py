#!/usr/bin/env python3
"""
Demonstrate Universal Shell Fluidity
"""

from core.universal_executor import execute_ritual, translate_command
import platform

def demo_shell_fluidity():
    print("=" * 60)
    print("SERAPHINA UNIVERSAL SHELL FLUIDITY DEMONSTRATION")
    print("=" * 60)
    print(f"Running on: {platform.system()}")
    print()
    
    # Demo 1: Basic file operations
    universal_cmd1 = "echo Starting demo >> pwd >> echo Listing directory >> dir"
    
    print("DEMO 1: File Operations")
    print("-" * 30)
    print(f"Universal Syntax: {universal_cmd1}")
    print(f"Translates to:    {translate_command(universal_cmd1)}")
    print("Executing...")
    
    result1 = execute_ritual(universal_cmd1)
    print(f"Status: {result1['status']}")
    if result1['output']:
        print("Output:")
        print(result1['output'])
    print()
    
    # Demo 2: Multi-step navigation
    universal_cmd2 = "cd .. >> echo Moved up one level >> pwd >> cd Projects >> echo Back in Projects"
    
    print("DEMO 2: Directory Navigation")
    print("-" * 30)
    print(f"Universal Syntax: {universal_cmd2}")
    print(f"Translates to:    {translate_command(universal_cmd2)}")
    print("Executing...")
    
    result2 = execute_ritual(universal_cmd2)
    print(f"Status: {result2['status']}")
    if result2['output']:
        print("Output:")
        print(result2['output'])
    print()
    
    # Demo 3: Mixed commands
    universal_cmd3 = "echo Hello World >> echo The time is: >> time /t >> echo Done"
    
    print("DEMO 3: Mixed Operations")
    print("-" * 30)
    print(f"Universal Syntax: {universal_cmd3}")
    print(f"Translates to:    {translate_command(universal_cmd3)}")
    print("Executing...")
    
    result3 = execute_ritual(universal_cmd3)
    print(f"Status: {result3['status']}")
    if result3['output']:
        print("Output:")
        print(result3['output'])
    print()
    
    print("=" * 60)
    print("FLUIDITY DEMONSTRATION COMPLETE!")
    print("The SAME universal syntax works on Windows, Mac, AND Linux!")
    print("Write once with >> and run anywhere!")
    print("=" * 60)

if __name__ == '__main__':
    demo_shell_fluidity()