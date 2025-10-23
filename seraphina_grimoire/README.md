# SERAPHINA — Living Grimoire (Starter Kit)

This turns the **Ritual Grimoire** into machine-readable manifests plus a tiny ritual engine.
Wire it to your **CMP Memory MCP** (left brain) and **LKG MCP** (right brain).

## Pieces
- `rituals/*.yaml` — ritual manifests (id, invoke, trigger, effects, lore)
- `ritual_engine.py` — minimal loader + dispatcher + stub hooks for CMP + LKG
- `hooks.py` — replace stubs to call your real CMP/LKG endpoints or MCP tools
- `demo_run.py` — quick demo invoking a few rituals with sample context
