#!/usr/bin/env python3
"""
🎃 CodeCraft School Validation - CI Guardrails

Version: 1.1
Date: October 31, 2025
Authority: MEGA's Token≠Schools Invariant + Fort Knox Integration
Purpose: Prevent version drift between grammar and canonical YAML

CRITICAL: This script enforces the 19-school invariant across all documentation.
MEGA's Fort Knox Pack: CI-ready with --ci flag for GitHub Actions integration.
"""

import yaml
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple

# ANSI colors for output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def load_canonical_yaml(yaml_path: Path) -> Dict:
    """Load the canonical schools YAML file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def check_1_unique_schools_count(data: Dict) -> Tuple[bool, str]:
    """
    CHECK 1: Verify unique(canonical names) == 19
    
    Invariant: len(set(token_to_school_mapping.values())) == 19
    """
    print(f"\n{Colors.BLUE}CHECK 1: Unique Schools Count{Colors.RESET}")
    
    token_mapping = data.get('token_to_school_mapping', {})
    unique_schools = set(token_mapping.values())
    expected_count = data['metadata']['total_schools']
    
    if len(unique_schools) != expected_count:
        return False, f"❌ FAIL: Found {len(unique_schools)} unique schools, expected {expected_count}"
    
    print(f"{Colors.GREEN}✅ PASS: {len(unique_schools)} unique schools (matches metadata){Colors.RESET}")
    return True, "PASS"

def check_2_token_grammar_sync(data: Dict, ebnf_path: Path) -> Tuple[bool, str]:
    """
    CHECK 2: Verify YAML grammar_tokens matches EBNF school_name tokens
    
    Ensures grammar and YAML stay in sync.
    """
    print(f"\n{Colors.BLUE}CHECK 2: Token-Grammar Sync{Colors.RESET}")
    
    yaml_tokens = set(data.get('grammar_tokens', []))
    
    # Extract tokens from EBNF school_name rule
    with open(ebnf_path, 'r', encoding='utf-8') as f:
        ebnf_content = f.read()
    
    # Find school_name rule (multi-line with | separators)
    pattern = r'school_name\s*=\s*((?:"[^"]+"\s*\|?\s*)+)'
    match = re.search(pattern, ebnf_content, re.MULTILINE | re.DOTALL)
    
    ebnf_tokens = set()
    if match:
        tokens_section = match.group(1)
        # Extract all quoted tokens
        token_pattern = r'"([^"]+)"'
        ebnf_tokens = set(re.findall(token_pattern, tokens_section))
    
    if yaml_tokens != ebnf_tokens:
        missing_in_yaml = ebnf_tokens - yaml_tokens
        missing_in_ebnf = yaml_tokens - ebnf_tokens
        msg = []
        if missing_in_yaml:
            msg.append(f"Missing in YAML: {missing_in_yaml}")
        if missing_in_ebnf:
            msg.append(f"Missing in EBNF: {missing_in_ebnf}")
        return False, f"❌ FAIL: Token mismatch\n" + "\n".join(msg)
    
    print(f"{Colors.GREEN}✅ PASS: {len(yaml_tokens)} tokens match between YAML and EBNF{Colors.RESET}")
    return True, "PASS"

def check_3_no_wrong_school_count(repo_root: Path, data: Dict) -> Tuple[bool, str]:
    """
    CHECK 3: Verify no file claims wrong school count (e.g., "20 schools")
    
    Searches for incorrect school count claims in documentation.
    """
    print(f"\n{Colors.BLUE}CHECK 3: No Wrong School Count Claims{Colors.RESET}")
    
    expected_count = data['metadata']['total_schools']
    wrong_counts = [18, 20, 21]  # Common mistakes
    
    issues = []
    
    # Search markdown files in grammar directory
    grammar_dir = repo_root / 'languages' / 'codecraft' / 'lexicon' / 'grammar'
    
    if not grammar_dir.exists():
        return False, f"❌ FAIL: Grammar directory not found: {grammar_dir}"
    
    md_files = list(grammar_dir.glob('*.md'))
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for wrong_count in wrong_counts:
                if re.search(rf'\b{wrong_count}\s+(?:Arcane\s+)?Schools?\b', content, re.IGNORECASE):
                    issues.append(f"{md_file.name}: Claims '{wrong_count} schools' (should be {expected_count})")
        except Exception as e:
            issues.append(f"{md_file.name}: Error reading file: {e}")
    
    # Check EBNF header
    ebnf_path = grammar_dir / 'lexicon.ebnf'
    
    if not ebnf_path.exists():
        return False, f"❌ FAIL: EBNF file not found: {ebnf_path}"
    
    try:
        with open(ebnf_path, 'r', encoding='utf-8') as f:
            ebnf_content = f.read()
        
        for wrong_count in wrong_counts:
            if re.search(rf'for\s+{wrong_count}\s+Arcane\s+Schools', ebnf_content):
                issues.append(f"lexicon.ebnf: Header claims '{wrong_count} Arcane Schools' (should be {expected_count})")
    except Exception as e:
        return False, f"❌ FAIL: Error reading lexicon.ebnf: {e}"
    
    if issues:
        msg = f"❌ FAIL: Found incorrect school count claims:\n" + "\n".join(f"  - {issue}" for issue in issues)
        print(msg)
        return False, msg
    
    print(f"{Colors.GREEN}✅ PASS: No files claim wrong school count (checked {len(md_files)} .md files){Colors.RESET}")
    return True, "PASS"

def check_4_token_mapping_completeness(data: Dict) -> Tuple[bool, str]:
    """
    CHECK 4: Verify all grammar tokens have mappings
    
    Ensures no orphaned tokens exist.
    """
    print(f"\n{Colors.BLUE}CHECK 4: Token Mapping Completeness{Colors.RESET}")
    
    grammar_tokens = set(data.get('grammar_tokens', []))
    mapped_tokens = set(data.get('token_to_school_mapping', {}).keys())
    
    if grammar_tokens != mapped_tokens:
        missing = grammar_tokens - mapped_tokens
        extra = mapped_tokens - grammar_tokens
        msg = []
        if missing:
            msg.append(f"Tokens without mapping: {missing}")
        if extra:
            msg.append(f"Mapped tokens not in grammar: {extra}")
        return False, f"❌ FAIL: Token mapping incomplete\n" + "\n".join(msg)
    
    print(f"{Colors.GREEN}✅ PASS: All {len(grammar_tokens)} tokens have mappings{Colors.RESET}")
    return True, "PASS"

def main():
    """Run all validation checks."""
    print(f"\n{Colors.BOLD}🎃 CodeCraft School Validation - CI Guardrails{Colors.RESET}")
    print(f"{Colors.BOLD}{'=' * 60}{Colors.RESET}\n")
    
    # Determine paths
    script_dir = Path(__file__).parent
    yaml_path = script_dir / 'schools.canonical.yaml'
    ebnf_path = script_dir / 'lexicon.ebnf'
    repo_root = script_dir.parent.parent.parent.parent  # infrastructure/languages/codecraft/lexicon/grammar -> infrastructure
    
    # Load canonical YAML
    try:
        data = load_canonical_yaml(yaml_path)
    except Exception as e:
        print(f"{Colors.RED}❌ FATAL: Could not load {yaml_path}: {e}{Colors.RESET}")
        sys.exit(1)
    
    # Run checks
    checks = [
        check_1_unique_schools_count(data),
        check_2_token_grammar_sync(data, ebnf_path),
        check_3_no_wrong_school_count(repo_root, data),
        check_4_token_mapping_completeness(data),
    ]
    
    # Summary
    print(f"\n{Colors.BOLD}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}SUMMARY{Colors.RESET}\n")
    
    passed = sum(1 for success, _ in checks if success)
    total = len(checks)
    
    if passed == total:
        print(f"{Colors.GREEN}{Colors.BOLD}✅ ALL CHECKS PASSED ({passed}/{total}){Colors.RESET}")
        print(f"\n{Colors.GREEN}Canon is locked. 19 Arcane Schools verified. 🔒✨{Colors.RESET}\n")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}❌ {total - passed} CHECK(S) FAILED ({passed}/{total} passed){Colors.RESET}")
        print(f"\n{Colors.YELLOW}Fix the issues above and run again.{Colors.RESET}\n")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CodeCraft Canon Validation')
    parser.add_argument('--ci', action='store_true', help='CI mode (no colors, machine-readable output)')
    args = parser.parse_args()
    
    # Disable colors in CI mode
    if args.ci:
        Colors.GREEN = Colors.RED = Colors.YELLOW = Colors.BLUE = Colors.RESET = Colors.BOLD = ''
    
    main()
