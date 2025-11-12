from pathlib import Path
import sys
sys.path.insert(0, ".")
from scripts.rosetta_integrity import _canonical_lines

text = Path("CODECRAFT_ROSETTA_STONE.md").read_text(encoding="utf-8", errors="ignore")
lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
canon_lines = _canonical_lines(text)

print(f"Total lines: {len(lines)}")
print(f"Canonical lines: {len(canon_lines)}")
print(f"Excluded lines: {len(lines) - len(canon_lines)}")

# Show what's around line 5170 (metadata.integrity area)
for i in range(5165, min(5185, len(lines))):
    included = "✅ INCLUDED" if i < len(canon_lines) and lines[i] in canon_lines else "❌ EXCLUDED"
    print(f"Line {i}: {included} | {lines[i][:80]}")
