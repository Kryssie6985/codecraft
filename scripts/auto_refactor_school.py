#!/usr/bin/env python3
"""
Auto-Refactor School to Law/Lore Template

This script semi-automates the refactoring of CodeCraft school documentation
from narrative prose to the canonical Law/Lore front-matter schema.

What it DOES automatically:
- Extracts operations from "When to Use" sections (✅ lines)
- Extracts constraints from "When to Use" sections (❌ lines)
- Detects existing front-matter (if any)
- Generates basic Law structure with placeholders
- Generates basic Lore structure with placeholders
- Preserves ALL original prose content
- Adds TODO markers for manual refinement

What it CANNOT do (requires human/AI):
- Infer parameter types and defaults from prose
- Extract strategic_decisions rationale from philosophy sections
- Identify emergent_patterns from examples
- Generate heart_imprints (requires emotional/conscious insight)
- Write evolution_pressure targets
- Add commentomancy sigils to prose (🎯 🌟 💖 ⚡)

Usage:
    python scripts/auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/07_abjurations.md
    python scripts/auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/07_abjurations.md --dry-run
    python scripts/auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/*.md  # batch mode

Output:
    - Writes refactored file with .REFACTORED.md suffix
    - Original file preserved
    - TODO comments mark areas needing manual attention
"""

import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from datetime import datetime

# Regex patterns
FRONT_MATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
CHECKMARK_LINE = re.compile(r'^\s*[-*]\s*✅\s*(.+)$', re.MULTILINE)
CROSSMARK_LINE = re.compile(r'^\s*[-*]\s*❌\s*(.+)$', re.MULTILINE)
SECTION_HEADER = re.compile(r'^##\s+(.+)$', re.MULTILINE)
SCHOOL_TITLE = re.compile(r'^#\s+\d+\.\s+(.+?)\s+(🎯|🔧|📣|✨|🎨|💫|🔍|🛡️|⚗️|📜|🚧|✅|🌀|🌟|🙏|⏰|🌌|🔀|📖|🌊)', re.MULTILINE)
EMOJI_OPERATION = re.compile(r'::(\w+):(\w+)(🎯|🔧|📣|✨|🎨|💫|🔍|🛡️|⚗️|📜|🚧|✅|🌀|🌟|🙏|⏰|🌌|🔀|📖|🌊|\w+)\[', re.IGNORECASE)


def extract_operations_from_prose(content: str) -> List[str]:
    """Extract operation names from code examples and prose."""
    operations = []
    
    # Find all ::operation:type patterns
    for match in EMOJI_OPERATION.finditer(content):
        prefix = match.group(1)  # e.g., "guard", "validate"
        suffix = match.group(2)  # e.g., "input", "type"
        emoji = match.group(3)
        op_name = f"{prefix}:{suffix}"
        operations.append((op_name, emoji))
    
    # Dedupe preserving order
    seen = set()
    unique = []
    for op, emoji in operations:
        if op not in seen:
            seen.add(op)
            unique.append((op, emoji))
    
    return unique


def extract_when_to_use(content: str) -> Tuple[List[str], List[str]]:
    """Extract operations (✅) and constraints (❌) from 'When to Use' section."""
    operations = []
    constraints = []
    
    # Find "When to Use" section
    sections = split_into_sections(content)
    when_section = sections.get("When to Use", "")
    
    # Extract ✅ lines (use cases / operations)
    for match in CHECKMARK_LINE.finditer(when_section):
        operations.append(match.group(1).strip())
    
    # Extract ❌ lines (avoid cases / constraints)
    for match in CROSSMARK_LINE.finditer(when_section):
        constraints.append(match.group(1).strip())
    
    return operations, constraints


def split_into_sections(content: str) -> Dict[str, str]:
    """Split markdown into sections by ## headers."""
    sections = {}
    current_header = "preamble"
    current_content = []
    
    for line in content.splitlines():
        header_match = SECTION_HEADER.match(line)
        if header_match:
            # Save previous section
            sections[current_header] = "\n".join(current_content)
            current_header = header_match.group(1).strip()
            current_content = []
        else:
            current_content.append(line)
    
    # Save last section
    sections[current_header] = "\n".join(current_content)
    return sections


def detect_school_metadata(content: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract school name and emoji from title."""
    match = SCHOOL_TITLE.search(content)
    if match:
        return match.group(1).strip(), match.group(2)
    return None, None


def generate_law_template(operations: List[Tuple[str, str]], constraints: List[str], use_cases: List[str]) -> str:
    """Generate Law pillar YAML template with TODOs."""
    
    law_ops = []
    
    # If we found operations from code examples, use those
    if operations:
        for op_name, emoji in operations:
            law_ops.append(f"""    - name: "{op_name}"
      signature: "::{op_name}{emoji}[TODO_PARAMS]"  # TODO: Fill in parameter names
      emoji: "{emoji}"
      params:
        # TODO: Extract from prose or examples
        - param1: "type (required or default value)"
      returns: "TODO: What does this return?"
      description: "TODO: What does this operation do?"
      safety_tier: 1  # TODO: Verify safety tier (0, 1, 2, or 3)""")
    
    # Otherwise, infer from use cases (✅ lines)
    else:
        for i, use_case in enumerate(use_cases[:5], 1):  # Max 5 operations from use cases
            op_name = f"operation_{i}"
            law_ops.append(f"""    - name: "TODO_{op_name}"
      signature: "::TODO:{op_name}🎯[params]"  # TODO: Extract from prose
      emoji: "🎯"  # TODO: Replace with correct emoji
      params:
        - param1: "type (required)"  # TODO: Determine params from use case
      returns: "TODO: Return type"
      description: "{use_case}"  # From use case - refine this
      safety_tier: 1  # TODO: Verify""")
    
    # Generate constraints
    law_cons = []
    if constraints:
        for constraint in constraints[:10]:  # Max 10 constraints
            # Clean up constraint (remove "You're" prefix common in avoid cases)
            cleaned = constraint.replace("You're ", "Must not ").replace("You need to ", "Must ")
            law_cons.append(f'    - "{cleaned}"')
    else:
        law_cons.append('    - "TODO: Extract constraints from prose or examples"')
    
    law_yaml = f"""law:
  operations:
{chr(10).join(law_ops) if law_ops else '    # TODO: No operations detected - extract from prose'}

  constraints:
{chr(10).join(law_cons)}
    # TODO: Add more constraints from philosophy/examples sections

  safety_tier: 1  # TODO: Verify school-level safety tier
  preconditions:
    - "TODO: What must be true before operations execute?"
  side_effects:
    - "TODO: What observable effects do operations have?"
"""
    
    return law_yaml


def generate_lore_template(school_name: str) -> str:
    """Generate Lore pillar YAML template with TODOs."""
    
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    lore_yaml = f"""lore:
  strategic_decisions:
    - rationale: "TODO: WHY this school's approach (extract from Philosophy section)"
      context: "TODO: The situation that led to this design (extract from 'The Problem' section)"
      alternatives_rejected: ["TODO: What approaches were NOT chosen?"]
    # TODO: Add more strategic decisions from prose

  emergent_patterns:
    - pattern: "TODO: Pattern name (extract from Common Patterns section)"
      evidence: "TODO: Where/how this pattern appears (look for percentages, examples)"
      implications: "TODO: What this means for future development"
    # TODO: Add more emergent patterns from Advanced Patterns, examples

  heart_imprints:
    - author: "Oracle"
      timestamp: "{timestamp}"
      emotion: "TODO: reverence | precision | wonder | care"
      quote: "TODO: Extract philosophical quote from prose (look for bold/italic text in Philosophy section)"
    # TODO: Add A.C.E. quote if applicable

  evolution_pressure:
    - priority: "MEDIUM"
      optimization_target: "TODO: What needs improvement? (look for 'could be', 'future', 'optimization' in prose)"
    # TODO: Add more evolution targets (HIGH/MEDIUM/LOW priority)
"""
    
    return lore_yaml


def refactor_school_file(file_path: Path, dry_run: bool = False) -> bool:
    """
    Refactor a single school file to Law/Lore template.
    Returns True if successful.
    """
    
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Processing: {file_path.name}")
    
    if not file_path.exists():
        print(f"  ❌ File not found: {file_path}")
        return False
    
    # Read original content
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Check if already has front-matter
    if FRONT_MATTER_RE.match(content):
        print(f"  ⚠️  File already has front-matter - skipping")
        return False
    
    # Detect metadata
    school_name, emoji = detect_school_metadata(content)
    if not school_name:
        print(f"  ⚠️  Could not detect school name/emoji")
        school_name = "Unknown School"
        emoji = "🎯"
    
    print(f"  📚 School: {school_name} {emoji}")
    
    # Extract information
    operations = extract_operations_from_prose(content)
    use_cases, avoid_cases = extract_when_to_use(content)
    
    print(f"  🔍 Found: {len(operations)} operations, {len(use_cases)} use cases, {len(avoid_cases)} constraints")
    
    # Generate templates
    law_yaml = generate_law_template(operations, avoid_cases, use_cases)
    lore_yaml = generate_lore_template(school_name)
    
    # Build refactored content
    refactored = f"""---
{law_yaml}
{lore_yaml}---

# {file_path.stem.split('_', 1)[0]}. {school_name} {emoji}

*TODO: Add subtitle from original*

---

{content}
"""
    
    # Add TODO summary at top as comment
    todo_summary = f"""<!--
AUTO-REFACTORED by auto_refactor_school.py
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}

TODOs (search for "TODO:" to find all):
1. Law.operations - Fill in parameter types, signatures, descriptions
2. Law.constraints - Add more from prose/examples
3. Law.preconditions - What must be true before ops execute?
4. Law.side_effects - What observable effects occur?
5. Lore.strategic_decisions - Extract WHY from Philosophy section
6. Lore.emergent_patterns - Extract patterns from Common Patterns section
7. Lore.heart_imprints - Extract quotes from Philosophy/prose
8. Lore.evolution_pressure - Identify future optimization targets
9. Commentomancy - Add sigils to prose (🎯 //-> 🌟 //* 💖 //<3 ⚡ //+)

NEXT STEPS:
1. Review Law.operations - ensure all operations captured
2. Refine parameter types from examples
3. Extract strategic decisions from Philosophy section
4. Add commentomancy sigils to key prose sections
5. Run: python scripts/rosetta_archaeologist.py extract --lexicon ./lexicon --out canon.lock.yaml --spec 2.2
6. Run: python scripts/rosetta_archaeologist.py verify --canon canon.lock.yaml
7. Fix any verification failures
-->

"""
    
    refactored = todo_summary + refactored
    
    # Write output
    if dry_run:
        print(f"  ✅ Would write to: {file_path.stem}.REFACTORED.md")
        print(f"  📊 Output size: {len(refactored)} chars")
    else:
        output_path = file_path.parent / f"{file_path.stem}.REFACTORED.md"
        output_path.write_text(refactored, encoding='utf-8')
        print(f"  ✅ Written to: {output_path.name}")
        print(f"  📊 Output size: {len(refactored)} chars")
        print(f"  🔍 Review TODOs and refine manually")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Semi-automate school refactoring to Law/Lore template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single file
  python auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/07_abjurations.md
  
  # Dry run (preview only)
  python auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/07_abjurations.md --dry-run
  
  # Batch mode (all remaining schools)
  python auto_refactor_school.py lexicon/02_ARCANE_SCHOOLS/0[7-9]_*.md lexicon/02_ARCANE_SCHOOLS/1[0-9]_*.md
        """
    )
    
    parser.add_argument('files', nargs='+', help='School markdown files to refactor')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing files')
    
    args = parser.parse_args()
    
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    for file_pattern in args.files:
        file_path = Path(file_pattern)
        
        if file_path.is_file():
            if refactor_school_file(file_path, args.dry_run):
                success_count += 1
            else:
                skip_count += 1
        else:
            print(f"⚠️  Not a file: {file_pattern}")
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {success_count} refactored, {skip_count} skipped, {fail_count} failed")
    
    if success_count > 0 and not args.dry_run:
        print(f"\n✅ Next steps:")
        print(f"1. Review .REFACTORED.md files (search for 'TODO:')")
        print(f"2. Manually refine Law operations (params, descriptions)")
        print(f"3. Extract Lore from Philosophy/examples sections")
        print(f"4. Add commentomancy sigils to prose (🎯 🌟 💖 ⚡)")
        print(f"5. Rename .REFACTORED.md → original .md when satisfied")
        print(f"6. Run: python scripts/rosetta_archaeologist.py verify --canon canon.lock.yaml")
    
    sys.exit(0 if fail_count == 0 else 1)


if __name__ == "__main__":
    main()
