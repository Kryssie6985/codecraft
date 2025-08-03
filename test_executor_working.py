#!/usr/bin/env python3
"""
Working test for Universal Command Executor using Windows Command Prompt directly
"""

import subprocess
import platform

def test_windows_commands():
    print("Testing Windows Command Execution...")
    
    # Test 1: Direct Windows command
    try:
        # Force use of Windows cmd.exe
        result = subprocess.run(
            ["cmd", "/c", "echo Hello & echo World & echo Done"],
            capture_output=True,
            text=True,
            shell=False
        )
        
        print(f"Status: {'SUCCESS' if result.returncode == 0 else 'ERROR'}")
        print(f"Exit Code: {result.returncode}")
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Error:\n{result.stderr}")
            
    except Exception as e:
        print(f"Exception: {e}")
    
    # Test 2: Universal command translation
    print("\n" + "="*40)
    print("Testing Universal Command Translation...")
    
    universal_cmd = "echo Step1 >> echo Step2 >> echo Complete"
    native_cmd = universal_cmd.replace(" >> ", " & ")
    
    print(f"Universal: {universal_cmd}")
    print(f"Native: {native_cmd}")
    
    try:
        result = subprocess.run(
            ["cmd", "/c", native_cmd],
            capture_output=True,
            text=True,
            shell=False
        )
        
        print(f"Status: {'SUCCESS' if result.returncode == 0 else 'ERROR'}")
        print(f"Output:\n{result.stdout}")
        
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
    test_windows_commands()