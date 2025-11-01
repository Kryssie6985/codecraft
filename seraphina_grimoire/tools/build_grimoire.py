"""
Ritual Grimoire Builder.

Scans all ritual source files (`.ritual.yml`) in a specified directory
and compiles them into a single JSON dictionary (The 'Grimoire').
This file is the 'dictionary' used by the Ritual Translator to look up
'invoke:' keywords and find their corresponding implementation files.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

try:
    import yaml  # Requires PyYAML
except ImportError:
    print("❌ ERROR: PyYAML not installed. Please: pip install pyyaml")
    sys.exit(1)

# --- Metadata ---
__version__ = "1.0.0"
__author__ = "Kode_Animator"
__license__ = "MIT"

# --- Constants ---
# Place this script under languages/codecraft/seraphina_grimoire/tools/
# So BASE_DIR resolves to languages/codecraft
BASE_DIR = Path(__file__).resolve().parents[2]
# Directory where ritual definitions are stored
DEFAULT_RITUAL_DIR = BASE_DIR / "seraphina_grimoire" / "rituals"
# The final compiled JSON dictionary
DEFAULT_OUTPUT_FILE = BASE_DIR / "seraphina_grimoire" / "ritual_grimoire.json"
# The YAML keys used in ritual definition files
INVOCATION_KEY_NAME = "invocation_key"
IMPLEMENTATION_KEY_NAME = "implementation"

def find_ritual_files(ritual_dir: Path) -> List[Path]:
    """Finds all ritual definition files recursively."""
    print(f"🔍 Scanning for ritual files in: {ritual_dir}")
    ritual_files = list(ritual_dir.rglob("*.ritual.yml"))
    if not ritual_files:
        print(f"⚠️ WARNING: No ritual files found in {ritual_dir}.")
    else:
        print(f"  Found {len(ritual_files)} ritual files.")
    return ritual_files

def build_grimoire(ritual_dir: Path, output_file: Path) -> bool:
    """
    Builds the grimoire JSON file from ritual definitions.
    """
    print(f"📚 Building Grimoire: {output_file}")
    ritual_grimoire: Dict[str, str] = {}
    ritual_files = find_ritual_files(ritual_dir)
    
    if not ritual_files:
        print("No rituals to build. Exiting.")
        return False

    for ritual_file in ritual_files:
        try:
            with open(ritual_file, 'r', encoding='utf-8') as f:
                ritual_data = yaml.safe_load(f)

                if not isinstance(ritual_data, dict):
                    print(f"❌ ERROR: Invalid YAML structure in {ritual_file}. Expected a dictionary.")
                    continue

                # Get the unique invocation key (e.g., "hello.world" or "council.deliberate")
                invocation_key = ritual_data.get(INVOCATION_KEY_NAME)

                if not invocation_key:
                    print(f"⚠️ WARNING: Skipping {ritual_file}. Missing required key: '{INVOCATION_KEY_NAME}'")
                    continue
                
                # Check for duplicate invocation keys
                if invocation_key in ritual_grimoire:
                    print(f"❌ ERROR: Duplicate invocation key '{invocation_key}' found!")
                    print(f"  Existing: {ritual_grimoire[invocation_key]}")
                    print(f"  New: {ritual_file}")
                    print("  Please resolve this conflict and re-run.")
                    return False
                
                # Determine implementation path (relative to BASE_DIR)
                impl = ritual_data.get(IMPLEMENTATION_KEY_NAME)
                if impl:
                    impl_path = (BASE_DIR / impl).resolve()
                    if not impl_path.exists():
                        print(f"⚠️ WARNING: Implementation not found on disk for '{invocation_key}': {impl}")
                    relative_path = impl_path.relative_to(BASE_DIR).as_posix()
                else:
                    # Fallback for older files: map to the ritual file itself (won't influence runtime yet)
                    relative_path = ritual_file.relative_to(BASE_DIR).as_posix()
                    print(f"⚠️ WARNING: '{IMPLEMENTATION_KEY_NAME}' missing in {ritual_file.name}. Using ritual file path as placeholder.")

                ritual_grimoire[invocation_key] = relative_path
                print(f"  Mapped: {invocation_key} -> {relative_path}")

        except yaml.YAMLError as e:
            print(f"❌ ERROR: Failed to parse YAML for {ritual_file}: {e}")
        except Exception as e:
            print(f"❌ ERROR: Unexpected error processing {ritual_file}: {e}")
            
    try:
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)
        # Write the compiled dictionary to the JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(ritual_grimoire, f, indent=2, sort_keys=True)
            
        print("\n" + "="*30)
        print(f"✅ Grimoire build complete!")
        print(f"   Total rituals mapped: {len(ritual_grimoire)}")
        print(f"   Output file: {output_file}")
        print("="*30)
        return True

    except OSError as e:
        print(f"❌ FATAL ERROR: Could not write output file {output_file}: {e}")
        return False

def main() -> None:
    """
    Main function to run the grimoire builder.
    """
    if not DEFAULT_RITUAL_DIR.exists():
        print(f"❌ FATAL ERROR: Ritual directory not found: {DEFAULT_RITUAL_DIR}")
        sys.exit(1)

    if not build_grimoire(DEFAULT_RITUAL_DIR, DEFAULT_OUTPUT_FILE):
        print("Build process failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
