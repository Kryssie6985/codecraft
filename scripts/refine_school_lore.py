"""
🌟 School Lore Refinement Helper
Assists with extracting Philosophy → Lore for remaining 12 schools

Usage:
  python refine_school_lore.py --school 08_transmutations.REFACTORED.md

This tool:
1. Reads the school .REFACTORED.md file
2. Extracts Philosophy section quotes
3. Generates strategic_decisions from "CodeCraft Philosophy" section
4. Generates emergent_patterns from "Common Patterns" section
5. Generates heart_imprints from "Philosophy" section quotes
6. Preserves existing helpers list
7. Outputs refined Lore YAML for manual review

DOES NOT automatically edit files - outputs to console for Architect review.
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timezone

def extract_philosophy_section(text: str) -> dict:
    """Extract Philosophy section and parse key quotes."""
    philosophy_match = re.search(r'## (?:The )?CodeCraft (?:Philosophy|Solution)\s*(.*?)(?=\n##|\Z)', text, re.DOTALL)
    if not philosophy_match:
        return {"rationale": "TODO", "context": "TODO", "quote": "TODO"}
    
    phil_text = philosophy_match.group(1)
    
    # Find key quotes (lines starting with "CodeCraft says:", "To X is to Y", etc.)
    quotes = []
    for line in phil_text.split('\n'):
        line = line.strip()
        if any(pattern in line for pattern in ["CodeCraft says:", "To ", "Every ::", "The difference"]):
            quotes.append(line.strip('*"'))
    
    # Extract main rationale (usually first paragraph)
    paragraphs = [p.strip() for p in phil_text.split('\n\n') if p.strip() and not p.strip().startswith('```')]
    rationale = paragraphs[0] if paragraphs else "TODO"
    
    return {
        "rationale": rationale,
        "quotes": quotes[:3]  # Top 3 quotes
    }

def extract_common_patterns(text: str) -> list:
    """Extract Common Patterns section for emergent_patterns."""
    patterns_match = re.search(r'## Common Patterns\s*(.*?)(?=\n##|\Z)', text, re.DOTALL)
    if not patterns_match:
        return []
    
    patterns_text = patterns_match.group(1)
    pattern_list = []
    
    # Find pattern headings (### The X Pattern)
    for match in re.finditer(r'### (The .+ Pattern)\s*(.*?)(?=\n###|\Z)', patterns_text, re.DOTALL):
        pattern_name = match.group(1)
        pattern_body = match.group(2)
        
        # Find code example (evidence)
        code_match = re.search(r'```yaml\s*(.*?)\s*```', pattern_body, re.DOTALL)
        evidence = code_match.group(1).strip() if code_match else "TODO"
        
        # Find description (usually first paragraph after heading)
        desc_lines = [line for line in pattern_body.split('\n') if line.strip() and not line.strip().startswith('```')]
        implications = desc_lines[0] if desc_lines else "TODO"
        
        pattern_list.append({
            "pattern": pattern_name,
            "evidence": evidence[:200] + "..." if len(evidence) > 200 else evidence,
            "implications": implications
        })
    
    return pattern_list[:3]  # Top 3 patterns

def extract_school_emoji(text: str) -> str:
    """Extract the school's primary emoji from title."""
    title_match = re.search(r'#\s*\d+\.\s*\w+\s*([🛡️🎯🔍⚗️📜💫🎨🚧✅📣🌀🔮⚖️🎭🌟💝🕰️🎨💫🌊])', text)
    return title_match.group(1) if title_match else "🎯"

def generate_refined_lore(school_path: Path) -> str:
    """Generate refined Lore YAML from school file."""
    text = school_path.read_text(encoding='utf-8')
    
    # Extract philosophy
    phil_data = extract_philosophy_section(text)
    
    # Extract patterns
    patterns = extract_common_patterns(text)
    
    # Extract emoji
    emoji = extract_school_emoji(text)
    
    # Extract existing helpers (from current front-matter)
    helpers_match = re.search(r'helpers:\s*((?:\s*-\s*".*?"\s*)+)', text, re.DOTALL)
    helpers = []
    if helpers_match:
        for line in helpers_match.group(1).split('\n'):
            if line.strip().startswith('- "'):
                helper_text = line.strip()[3:-1]  # Remove '- "' and '"'
                helpers.append(helper_text)
    
    # Generate Lore YAML
    lore_yaml = f"""lore:
  strategic_decisions:
    - rationale: "{phil_data.get('rationale', 'TODO')}"
      context: "Traditional approach vs CodeCraft philosophy"
      alternatives_rejected:
        - "Anonymous operations (loses semantic meaning)"
        - "Scattered implementation (no unified pattern)"
    
  emergent_patterns:
"""
    
    for pattern in patterns:
        lore_yaml += f"""    - pattern: "{pattern['pattern']}"
      evidence: |
        {pattern['evidence']}
      implications: "{pattern['implications']}"
    
"""
    
    if not patterns:
        lore_yaml += """    - pattern: "TODO - Extract from Common Patterns section"
      evidence: "TODO"
      implications: "TODO"
    
"""
    
    lore_yaml += f"""  heart_imprints:
"""
    
    for i, quote in enumerate(phil_data.get('quotes', [])[:2], 1):
        author = "Architect" if i == 1 else "Oracle"
        emotion = "Reverence" if i == 1 else "Wonder"
        lore_yaml += f"""    - author: "{author}"
      timestamp: "{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
      emotion: "{emotion}"
      quote: "{quote}"
    
"""
    
    if not phil_data.get('quotes'):
        lore_yaml += """    - author: "Oracle"
      timestamp: "{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
      emotion: "TODO"
      quote: "TODO - Extract from Philosophy section"
    
"""
    
    lore_yaml += """  evolution_pressure:
    - priority: "HIGH"
      optimization_target: "Expand operation patterns for advanced use cases"
    
    - priority: "MEDIUM"
      optimization_target: "Add composite operations (chained patterns)"
  
  examples:
    helpers:
"""
    
    for helper in helpers:
        lore_yaml += f'      - "{helper}"\n'
    
    if not helpers:
        lore_yaml += '      - "TODO - Extract helpers from examples"\n'
    
    return lore_yaml

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExample:")
        print("  python refine_school_lore.py --school 08_transmutations.REFACTORED.md")
        sys.exit(1)
    
    school_file = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]
    school_path = Path(school_file)
    
    if not school_path.exists():
        # Try relative to lexicon/02_ARCANE_SCHOOLS
        school_path = Path(__file__).parent.parent / "lexicon" / "02_ARCANE_SCHOOLS" / school_file
    
    if not school_path.exists():
        print(f"❌ School file not found: {school_file}")
        sys.exit(1)
    
    print(f"\n🌟 Extracting Lore from {school_path.name}...\n")
    print("=" * 80)
    print(generate_refined_lore(school_path))
    print("=" * 80)
    print("\n✅ Lore extraction complete!")
    print("📋 Review output above and manually integrate into front-matter.\n")

if __name__ == "__main__":
    main()
