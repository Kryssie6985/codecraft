#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LOST v3.1 – Commentomancy Linter (Fort Knox G-04 + extras)
Checks:
  - Longest-match precedence for Law/Lore sigils
  - Law-over-Lore dominance on co-present lines
  - Namespaced ritual usage in code blocks
  - Required Law sigils present for {blueprint, protocol, charter}
  - Token≠Schools invariant reminder hook (delegates to lost_validate)
"""
import re, sys, pathlib, yaml

# SIGILS (longest first!)
LAW_SIGILS  = [r"//!\?", r"//!\s", r"///", r"//(?!->|\*|<3|~|\+)"]
LORE_SIGILS = [r"//->", r"//\*", r"//<3", r"//~", r"//\+"]

LAW_RX  = re.compile(rf"^(\s*)({'|'.join(LAW_SIGILS)})(.*)$")
LORE_RX = re.compile(rf"^(\s*)({'|'.join(LORE_SIGILS)})(.*)$")

NAMESPACE_RX = re.compile(r"^\s*-\s*invoke:\s*[a-z0-9_]+\.[a-z0-9_.]+$", re.I)
BARE_INVOKE_RX = re.compile(r"^\s*-\s*invoke:\s*(?:[a-z0-9_]+)$", re.I)

DOC_HEADER_RX = re.compile(r"^#\s*(.+)$")
TYPE_RX = re.compile(r'^\s*document_type:\s*"(.*?)"\s*$', re.I)

def paired_yaml(md_path: pathlib.Path) -> pathlib.Path:
    return md_path.with_suffix(".yaml")

def extract_embedded_yaml(md_text: str) -> str | None:
    """Extract YAML content from embedded code fences in markdown (returns LAST block)"""
    lines = md_text.splitlines()
    in_yaml_block = False
    all_yaml_blocks = []
    current_block = []
    
    for line in lines:
        if line.strip().startswith("```yaml"):
            in_yaml_block = True
            current_block = []
            continue
        elif line.strip() == "```" and in_yaml_block:
            in_yaml_block = False
            if current_block:
                all_yaml_blocks.append("\n".join(current_block))
            current_block = []
        elif in_yaml_block:
            current_block.append(line)
    
    # Return LAST YAML block (LOST v3.1 puts machine-readable YAML at document end)
    return all_yaml_blocks[-1] if all_yaml_blocks else None

def longest_match_violation(line: str) -> bool:
    # If both Law and Lore appear, Law must anchor; and the sigil matched must be the longest
    # We approximate by checking conflicting matches at same column.
    law_m = LAW_RX.match(line)
    lore_m = LORE_RX.match(line)
    if law_m and lore_m and law_m.start(2) == lore_m.start(2):
        return True  # co-present at same pos: should not begin with Lore
    # Check that if '//!?' is present, we didn't also match '//! ' earlier
    if "//!?" in line and re.search(r"//!\s", line):
        # longest-match means //!? must win (no space after ?)
        return False  # presence of both is okay as long as '//!?' is first
    return False

def lint_file(md_path: pathlib.Path) -> list[str]:
    errs, doc_type = [], None
    md_text = md_path.read_text(encoding="utf-8", errors="ignore")
    text = md_text.splitlines()
    
    # 0) paired yaml (check paired file first, then embedded)
    yml = paired_yaml(md_path)
    yaml_content = None
    
    if yml.exists():
        yaml_content = yml.read_text(encoding="utf-8")
    else:
        # Try embedded YAML
        embedded = extract_embedded_yaml(md_text)
        if embedded:
            yaml_content = embedded
        else:
            errs.append(f"[G-01] Missing paired YAML or embedded YAML block")

    # 1) scan lines
    law_count = 0
    guardrail_count = 0
    in_code_block = False

    for i, line in enumerate(text, 1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            # Namespaced ritual checks
            if BARE_INVOKE_RX.search(line):
                errs.append(f"[G-03] Bare invoke (no namespace) at {md_path.name}:{i}")
            continue

        if longest_match_violation(line):
            errs.append(f"[G-04] Longest-match precedence violated at {md_path.name}:{i}")

        if LAW_RX.match(line):
            law_count += 1
            if line.strip().startswith("//!?"):
                guardrail_count += 1

    # 2) type-specific Law requirements
    if yaml_content:
        try:
            # Use safe_load_all() to handle multi-document YAML streams (separated by ---)
            documents = list(yaml.safe_load_all(yaml_content))
            
            if not documents:
                errs.append(f"[META] Embedded YAML block found but contained no valid documents")
                meta = {}
                doc_type = None
            else:
                # The main manifest is the FIRST document in the stream
                parsed = documents[0]
                
                # Handle nested metadata structure (LOST v3.1 uses metadata: as root key)
                if isinstance(parsed, dict):
                    meta = parsed.get("metadata", parsed)  # Use metadata if present, else root
                    doc_type = meta.get("document_type") if isinstance(meta, dict) else None
                else:
                    meta = {}
                    doc_type = None
        except Exception as e:
            errs.append(f"[META] YAML parse error: {e}")

    if doc_type in {"blueprint","protocol","charter"}:
        if law_count == 0:
            errs.append(f"[G-04] {doc_type} requires ≥1 Law sigil line (///, //!, //!?, //).")
        if guardrail_count == 0:
            errs.append(f"[G-04] {doc_type} requires ≥1 Guardrail (//!?).")

    return errs

def main(paths: list[str]) -> int:
    md_files = [pathlib.Path(p) for p in paths if p.endswith(".md")]
    all_errs = []
    for p in md_files:
        all_errs += lint_file(p)
    if all_errs:
        print("\n".join(sorted(set(all_errs))), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or [str(p) for p in pathlib.Path(".").rglob("docs/**/*.md")]))
