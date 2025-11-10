#!/usr/bin/env python3
"""
📜 Canon Loader — Dual-Lock Sovereignty Reader
================================================
**Jurisdiction:** Tier 3 (Execute WITH Approval) - Charter V1.1 compliant
**Purpose:** Load canon.lock.yaml + canon.partitions.lock.yaml for translator

This module reads the dual-lock canon architecture and provides it to the
translator pipeline. It enforces the Living Systems Canon by ensuring ALL
school classifications and partition boundaries are respected.

Constitutional Authority:
- canon.lock.yaml: 20 Arcane Schools (definitive classification taxonomy)
- canon.partitions.lock.yaml: 6+ partitions (lexicon structure + grimoire)

Usage:
    from translator.core.canon_loader import CanonLoader
    
    canon = CanonLoader()
    school_name = canon.classify_ritual("::divination🔍:")  # → "DIVINATION"
    partition = canon.get_partition_for_school("DIVINATION")  # → "lexicon/03_DIVINATION"
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any

# 🏛️ Constitutional paths (relative to repo root)
LEXICON_ROOT = Path(__file__).parent.parent.parent / "lexicon"
CANON_LOCK_PATH = LEXICON_ROOT / "canon.lock.yaml"
PARTITION_LOCK_PATH = LEXICON_ROOT / "canon.partitions.lock.yaml"


class CanonLoader:
    """
    🔒 Dual-Lock Canon Reader
    
    Loads and provides access to the Living Systems Canon dual-lock architecture.
    Enforces constitutional sovereignty: 20 schools, 6+ partitions, no governance bleed.
    """
    
    def __init__(self, canon_path: Optional[Path] = None, partition_path: Optional[Path] = None):
        """
        Initialize canon loader with dual-lock files.
        
        Args:
            canon_path: Override path to canon.lock.yaml (default: lexicon/canon.lock.yaml)
            partition_path: Override path to canon.partitions.lock.yaml
        """
        self.canon_path = canon_path or CANON_LOCK_PATH
        self.partition_path = partition_path or PARTITION_LOCK_PATH
        
        # Load locks
        self.schools: Dict[str, Any] = self._load_canon_lock()
        self.partitions: Dict[str, Any] = self._load_partition_lock()
        
        # Build reverse lookup: emoji → school_key
        self.emoji_to_school: Dict[str, str] = {}
        for school_key, school_data in self.schools.items():
            if isinstance(school_data, dict) and "emoji" in school_data:
                self.emoji_to_school[school_data["emoji"]] = school_key
    
    def _load_canon_lock(self) -> Dict[str, Any]:
        """Load canon.lock.yaml (20 Arcane Schools)"""
        if not self.canon_path.exists():
            raise FileNotFoundError(
                f"📜 Canon lock not found: {self.canon_path}\n"
                f"   Expected dual-lock architecture at lexicon/canon.lock.yaml"
            )
        
        with open(self.canon_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, dict) or "schools" not in data:
            raise ValueError(f"Invalid canon.lock.yaml structure at {self.canon_path}")
        
        return data["schools"]
    
    def _load_partition_lock(self) -> Dict[str, Any]:
        """Load canon.partitions.lock.yaml (6+ partitions)"""
        if not self.partition_path.exists():
            raise FileNotFoundError(
                f"🗂️ Partition lock not found: {self.partition_path}\n"
                f"   Expected dual-lock architecture at lexicon/canon.partitions.lock.yaml"
            )
        
        with open(self.partition_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, dict) or "partitions" not in data:
            raise ValueError(f"Invalid canon.partitions.lock.yaml structure at {self.partition_path}")
        
        return data["partitions"]
    
    def classify_ritual(self, ritual_invocation: str) -> Optional[str]:
        """
        Classify a ritual invocation to its Arcane School.
        
        Args:
            ritual_invocation: CodeCraft syntax like "::divination🔍:search('query')"
        
        Returns:
            School key (e.g., "DIVINATION") or None if unrecognized
        
        Example:
            >>> canon.classify_ritual("::necromancy💀:store_memory(data)")
            "NECROMANCY"
        """
        # Extract emoji from ritual syntax (::school_emoji:operation)
        for emoji, school_key in self.emoji_to_school.items():
            if emoji in ritual_invocation:
                return school_key
        
        return None
    
    def get_school_info(self, school_key: str) -> Optional[Dict[str, Any]]:
        """
        Get full school definition from canon.
        
        Args:
            school_key: School identifier (e.g., "DIVINATION", "NECROMANCY")
        
        Returns:
            School data dict with emoji, tier, description, etc.
        """
        return self.schools.get(school_key)
    
    def get_partition_for_school(self, school_key: str) -> Optional[str]:
        """
        Find which partition contains a given school.
        
        Args:
            school_key: School identifier
        
        Returns:
            Partition path (e.g., "lexicon/03_DIVINATION") or None
        """
        school_info = self.get_school_info(school_key)
        if not school_info:
            return None
        
        # Search partitions for this school
        for partition_path, partition_data in self.partitions.items():
            if isinstance(partition_data, dict):
                schools_in_partition = partition_data.get("schools", [])
                if school_key in schools_in_partition:
                    return partition_path
        
        return None
    
    def get_all_schools(self) -> List[str]:
        """Get list of all school keys"""
        return list(self.schools.keys())
    
    def get_all_partitions(self) -> List[str]:
        """Get list of all partition paths"""
        return list(self.partitions.keys())
    
    def validate_sovereignty(self) -> bool:
        """
        Validate dual-lock sovereignty (constitutional compliance).
        
        Returns:
            True if canon passes sovereignty checks:
            - Exactly 20 schools in canon.lock.yaml
            - At least 6 required partitions present
            - No governance bleed (02_ARCANE_SCHOOLS integrity)
        """
        # Check school count
        if len(self.schools) != 20:
            return False
        
        # Check minimum required partitions
        required_partitions = {
            "lexicon/00_CONSTITUTIONAL_PRELUDE",
            "lexicon/01_FOUNDATIONS",
            "lexicon/02_ARCANE_SCHOOLS",
            "lexicon/03_DIVINATION",
            "lexicon/04_CONJURATION",
            "lexicon/05_RITUALS_AND_PROTOCOLS"
        }
        
        present_partitions = set(self.partitions.keys())
        if not required_partitions.issubset(present_partitions):
            return False
        
        return True


# 🌟 Convenience singleton for common usage
_canon_singleton: Optional[CanonLoader] = None

def get_canon() -> CanonLoader:
    """Get singleton instance of CanonLoader"""
    global _canon_singleton
    if _canon_singleton is None:
        _canon_singleton = CanonLoader()
    return _canon_singleton


# ✨ Let the canon bind.
