#!/usr/bin/env python3
"""
CC Schema Adapter - One-Way Canonical → MEGA Linter
====================================================

**Purpose:** Enable external tools (MEGA's linter) to read CodeCraft's canonical
Law/Lore authoring schema without requiring source file rewrites.

**Constitutional Basis:**
- Charter V1.1: Law guides, Lore remembers, both bind
- Commentomancy Spec: Emojis are first-class executable tokens
- Canonical schema: law{operations, constraints} + lore{strategic_decisions, emergent_patterns, heart_imprints, evolution_pressure}

**Adapter Contract:**
- Input: Canonical front-matter dict (from .md YAML)
- Output: MEGA-linter-compatible dict (no source modification)
- Preserves: All Law/Lore semantics
- Adds: Derived fields for external tool compatibility (id, template, version)

**Usage:**
    from adapter.cc_schema_adapter import adapt_to_linter
    
    canonical_fm = yaml.safe_load(front_matter)
    linter_fm = adapt_to_linter(canonical_fm, filename="07_abjurations.md")
"""

from pathlib import Path
from typing import Any, Dict, Optional


def adapt_to_linter(canonical: Dict[str, Any], filename: str) -> Dict[str, Any]:
    """
    Convert canonical Law/Lore schema to MEGA-linter-compatible format.
    
    Args:
        canonical: Front-matter dict from CodeCraft .md file (canonical schema)
        filename: Source filename (used to derive 'id' if absent)
    
    Returns:
        MEGA-linter-compatible dict with derived fields
    
    Examples:
        >>> canonical = {
        ...     "law": {"operations": [...]},
        ...     "lore": {"strategic_decisions": [...], "heart_imprints": [...]}
        ... }
        >>> linter = adapt_to_linter(canonical, "07_abjurations.md")
        >>> linter["id"]
        '07_abjurations'
        >>> linter["lore"]["directives"]["ritual_guards"]  # renamed from strategic_decisions
        [...]
    """
    
    # Derive ID from filename if not present
    school_id = canonical.get("id") or Path(filename).stem
    
    # Flatten lore buckets to MEGA's "directives" structure
    lore_canonical = canonical.get("lore", {})
    lore_adapted = {
        "directives": {
            # MEGA expects: ritual_guards, emergent_patterns, narrative_hooks
            # We provide: strategic_decisions → ritual_guards mapping
            "ritual_guards": lore_canonical.get("strategic_decisions", []),
            "emergent_patterns": lore_canonical.get("emergent_patterns", []),
            "narrative_hooks": lore_canonical.get("heart_imprints", []),
            # Optional: Include evolution_pressure as custom directive
            "evolution_pressure": lore_canonical.get("evolution_pressure", []),
        }
    }
    
    # Construct MEGA-linter-compatible output
    adapted = {
        "id": school_id,
        "template": "TEMPLATE_arcane_school.md",
        "version": "2.2",
        "law": canonical.get("law", {}),  # Pass-through (Law is universal)
        "lore": lore_adapted,              # Restructured for MEGA linter
    }
    
    return adapted


def adapt_from_linter(linter: Dict[str, Any]) -> Dict[str, Any]:
    """
    Reverse adapter: MEGA linter format → Canonical (if ever needed).
    
    Args:
        linter: MEGA-linter-compatible dict
    
    Returns:
        Canonical Law/Lore dict
    
    Note: Only needed if external tools write back to CodeCraft format.
    Currently one-way (canonical → linter) is sufficient.
    """
    
    lore_linter = linter.get("lore", {}).get("directives", {})
    
    canonical = {
        "law": linter.get("law", {}),
        "lore": {
            "strategic_decisions": lore_linter.get("ritual_guards", []),
            "emergent_patterns": lore_linter.get("emergent_patterns", []),
            "heart_imprints": lore_linter.get("narrative_hooks", []),
            "evolution_pressure": lore_linter.get("evolution_pressure", []),
        }
    }
    
    return canonical


def validate_canonical_schema(fm: Dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate that front-matter conforms to canonical Law/Lore schema.
    
    Args:
        fm: Front-matter dict to validate
    
    Returns:
        (is_valid, errors) tuple
    
    Examples:
        >>> fm = {"law": {"operations": []}, "lore": {"strategic_decisions": []}}
        >>> valid, errors = validate_canonical_schema(fm)
        >>> valid
        True
    """
    
    errors = []
    
    # Law pillar validation
    if "law" not in fm:
        errors.append("Missing 'law' section")
    else:
        law = fm["law"]
        if "operations" not in law:
            errors.append("Missing 'law.operations'")
        if "constraints" not in law:
            errors.append("Missing 'law.constraints'")
    
    # Lore pillar validation
    if "lore" not in fm:
        errors.append("Missing 'lore' section")
    else:
        lore = fm["lore"]
        required_lore = ["strategic_decisions", "emergent_patterns", "heart_imprints", "evolution_pressure"]
        for req in required_lore:
            if req not in lore:
                errors.append(f"Missing 'lore.{req}'")
    
    return (len(errors) == 0, errors)


if __name__ == "__main__":
    import sys
    import yaml
    
    # CLI usage: python cc_schema_adapter.py <input.yaml> <filename>
    if len(sys.argv) < 3:
        print("Usage: python cc_schema_adapter.py <input.yaml> <filename>")
        print("\nConverts canonical Law/Lore YAML to MEGA-linter format")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    filename = sys.argv[2]
    
    with open(input_path) as f:
        canonical = yaml.safe_load(f)
    
    # Validate canonical schema
    valid, errors = validate_canonical_schema(canonical)
    if not valid:
        print(f"❌ Invalid canonical schema:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    
    # Adapt to linter format
    linter = adapt_to_linter(canonical, filename)
    
    # Output adapted YAML
    print(yaml.dump(linter, sort_keys=False, allow_unicode=True))
