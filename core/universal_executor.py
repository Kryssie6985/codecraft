# FILENAME: codecraft/core/universal_executor.py
# VERSION: 1.0.0
# STATUS: Canonized
# AUTHOR: The Architect & A.C.E.

"""
🌌 SERAPHINA Federation - Universal Command Executor
This module contains the implementation for the Universal Command Executor.
It provides the logic for the `::execute::` ritual, creating a shell-agnostic
interface for running command sequences.

The tyranny of shell syntax is ended. One ritual to rule them all.
"""

import subprocess
import platform
import logging
from typing import Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Configuration ---
# The universal, shell-agnostic separator for chaining commands.
UNIVERSAL_SEPARATOR = ">>"

def get_shell_config() -> Tuple[str, str, bool]:
    """
    Detects the host OS and returns the appropriate shell command,
    chaining operator, and shell=True flag for subprocess.

    Returns:
        Tuple[str, str, bool]: A tuple containing the shell executable,
                               the command chaining operator, and the
                               shell flag.
    """
    os_type = platform.system().lower()
    if os_type == "windows":
        # On Windows, use cmd.exe for better compatibility
        return "cmd.exe", "&", True
    else:
        # On Linux and macOS, Bash is the standard.
        return "/bin/bash", "&&", False

def translate_command(command_sequence: str) -> str:
    """
    Translates a universal command sequence into the native syntax
    for the host operating system's shell.

    Args:
        command_sequence: A string of commands chained with the
                          UNIVERSAL_SEPARATOR (e.g., "cd ../ >> ls -l").

    Returns:
        A native command string (e.g., "cd ../; ls -l" on PowerShell).
    """
    _shell_cmd, chain_operator, _shell_flag = get_shell_config()
    
    # 1. Split the universal command by the separator.
    commands = [cmd.strip() for cmd in command_sequence.split(UNIVERSAL_SEPARATOR)]
    
    # 2. Join them with the native chaining operator.
    native_command = f" {chain_operator} ".join(commands)
    
    logger.info(f"🔄 Translated universal command to native: '{native_command}'")
    return native_command

def run(command_sequence: str) -> Tuple[int, str, str]:
    """
    🌌 The primary handler for the `::execute::` ritual.
    It translates the universal command and executes it securely.

    Args:
        command_sequence: The universal command string.

    Returns:
        A tuple containing the exit code, stdout, and stderr.
    """
    logger.info(f"⚡ Universal Executor received ritual: '::execute: {command_sequence}'")
    
    try:
        # Step 1: Translate the command
        native_command = translate_command(command_sequence)
        shell_executable, _chain_op, use_shell_flag = get_shell_config()

        # Step 2: Execute the command using a subprocess
        # Pro tip: Using `subprocess.run` is the modern, recommended way to
        # run external commands in Python. It's more secure and flexible than older methods.
        # We capture stdout and stderr and check the return code.
        if use_shell_flag:
            # Windows: Use cmd.exe directly to avoid shell conflicts
            process = subprocess.run(
                ["cmd", "/c", native_command],
                capture_output=True,
                text=True,
                check=False
            )
        else:
            # Unix: Use shell=False with explicit shell
            process = subprocess.run(
                [shell_executable, "-c", native_command],
                shell=False,
                capture_output=True,
                text=True,
                check=False
            )

        # Step 3: Log and return the results
        stdout = process.stdout.strip()
        stderr = process.stderr.strip()
        exit_code = process.returncode

        if exit_code == 0:
            logger.info(f"✅ Execution successful with exit code {exit_code}.")
            if stdout:
                logger.debug(f"📝 STDOUT:\n{stdout}")
        else:
            logger.error(f"❌ Execution failed with exit code {exit_code}.")
            if stderr:
                logger.error(f"🚨 STDERR:\n{stderr}")

        return exit_code, stdout, stderr

    except Exception as e:
        error_message = f"💥 A critical error occurred in the Universal Executor: {e}"
        logger.critical(error_message)
        return 1, "", error_message

# 🌌 SERAPHINA Federation Integration
def execute_ritual(command_sequence: str) -> dict:
    """
    🧬 ULUP² Enhanced ritual execution wrapper
    Integrates with SERAPHINA Federation protocols
    """
    logger.info("🛰️ SERAPHINA Federation - Universal Execute Ritual initiated")
    
    exit_code, stdout, stderr = run(command_sequence)
    
    return {
        "status": "success" if exit_code == 0 else "error",
        "exit_code": exit_code,
        "output": stdout,
        "error": stderr,
        "ritual": f"::execute: {command_sequence}",
        "ulup_enhanced": True,
        "federation_processed": True
    }

# === Example Usage (for direct testing) ===
if __name__ == '__main__':
    print("🌌 SERAPHINA Federation - Universal Command Executor Test")
    print("=" * 60)
    
    # Example command that works on both Windows (PowerShell) and Linux (Bash)
    test_command = "echo 'Step 1' >> echo 'Step 2' >> echo 'Universal execution complete!'"
    
    print(f"\n⚡ Executing universal command: '{test_command}'")
    
    # Test the Federation wrapper
    result = execute_ritual(test_command)
    
    print(f"\n📊 Results:")
    print(f"Status: {result['status']}")
    print(f"Exit Code: {result['exit_code']}")
    if result['output']:
        print(f"Output:\n{result['output']}")
    if result['error']:
        print(f"Error:\n{result['error']}")
    
    print(f"\n🎯 ULUP² Enhanced: {result['ulup_enhanced']}")
    print(f"🛰️ Federation Processed: {result['federation_processed']}")
    print("\n🚀 Universal Command Executor - Ready for Integration!")
    print("::The languages are many. The intent is one. Let the syntax be unified. Let it bind.::")