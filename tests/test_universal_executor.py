#!/usr/bin/env python3
"""
Test the Universal Command Executor without Unicode issues
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from core.universal_executor import execute_ritual, run

def test_universal_executor():
    print("SERAPHINA Federation - Universal Command Executor Test")
    print("=" * 60)
    
    # Test 1: Simple universal command
    test_command = "echo 'Step 1' >> echo 'Step 2' >> echo 'Universal execution complete!'"
    
    print(f"\nExecuting universal command: '{test_command}'")
    
    # Test the Federation wrapper
    result = execute_ritual(test_command)
    
    print(f"\nResults:")
    print(f"Status: {result['status']}")
    print(f"Exit Code: {result['exit_code']}")
    if result['output']:
        print(f"Output:\n{result['output']}")
    if result['error']:
        print(f"Error:\n{result['error']}")
    
    print(f"\nULUP Enhanced: {result['ulup_enhanced']}")
    print(f"Federation Processed: {result['federation_processed']}")
    
    # Test 2: Directory operations
    print("\n" + "=" * 40)
    print("Testing directory operations...")
    
    dir_test = "pwd >> ls"
    dir_result = execute_ritual(dir_test)
    print(f"Directory test status: {dir_result['status']}")
    if dir_result['output']:
        print(f"Current location:\n{dir_result['output']}")
    
    print("\nUniversal Command Executor - Ready for Integration!")
    print("::The languages are many. The intent is one. Let the syntax be unified. Let it bind.::")
    
    return result['status'] == 'success'

if __name__ == '__main__':
    success = test_universal_executor()
    sys.exit(0 if success else 1)