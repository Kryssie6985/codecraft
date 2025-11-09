#!/usr/bin/env bash
set -euo pipefail

LEXICON="${1:-./lexicon}"
OUT="${2:-./canon.lock.json}"
SPEC="2.2"

python3 scripts/rosetta_archaeologist.py extract --lexicon "$LEXICON" --out "$OUT" --spec "$SPEC"
python3 scripts/rosetta_archaeologist.py verify  --canon "$OUT"
echo "Hash:" $(python3 scripts/rosetta_archaeologist.py hash --canon "$OUT")
echo "OK: canon-lock pipeline green"
