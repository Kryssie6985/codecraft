#!/usr/bin/env python3
"""
Simple test for Universal Command Executor
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from core.universal_executor import execute_ritual

def main():
    print("Testing Universal Command Executor...")
    
    # Simple test command
    cmd = "echo Hello >> echo World >> echo Done"
    print(f"Command: {cmd}")
    
    result = execute_ritual(cmd)
    
    print(f"Status: {result['status']}")
    print(f"Exit Code: {result['exit_code']}")
    
    if result['output']:
        print("Output:")
        print(result['output'])
    
    if result['error'] and result['error'].strip():
        print("Error:")
        # Safe print without Unicode issues
        try:
            print(result['error'])
        except UnicodeEncodeError:
            print(result['error'].encode('utf-8', errors='replace').decode('utf-8'))
    
    print(f"ULUP Enhanced: {result['ulup_enhanced']}")
    print("Test complete!")

if __name__ == '__main__':
    main()