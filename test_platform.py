import platform
from core.universal_executor import get_shell_config

print(f"Platform system: {platform.system()}")
print(f"Platform system (lower): {platform.system().lower()}")

shell_exe, chain_op, use_shell = get_shell_config()
print(f"Shell executable: {shell_exe}")
print(f"Chain operator: {chain_op}")
print(f"Use shell flag: {use_shell}")

# Test a simple command directly
import subprocess
try:
    result = subprocess.run("echo Hello", shell=True, capture_output=True, text=True)
    print(f"Direct test - Exit code: {result.returncode}")
    print(f"Direct test - Output: {result.stdout.strip()}")
    print(f"Direct test - Error: {result.stderr.strip()}")
except Exception as e:
    print(f"Direct test failed: {e}")