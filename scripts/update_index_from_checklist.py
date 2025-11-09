#!/usr/bin/env python3
import sys, yaml, datetime as dt, pathlib

def parse_blocks(text):
    blocks = []
    block = []
    for line in text.splitlines():
        if line.strip() == "":
            if block:
                blocks.append("\n".join(block))
                block = []
        else:
            block.append(line)
    if block:
        blocks.append("\n".join(block))
    return blocks

def main(checklist_path, out_md):
    text = pathlib.Path(checklist_path).read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    now = dt.datetime.now().isoformat(timespec="seconds")
    lines = []
    lines.append(f"# Lexicon Index — Auto‑Generated")
    lines.append(f"_Generated: {now}_\n")
    total = 0
    done = 0
    for block in blocks:
        b = block.strip()
        if not b or b.startswith("#"):
            continue
        name = b.split(":",1)[0].strip()
        total += 1
        status = "pending"; law = lore = ids = False
        for ln in b.splitlines():
            t = ln.strip()
            if t.startswith("status:"):
                status = t.split(":",1)[1].strip()
            elif t.startswith("law_conformant:"):
                law = t.split(":",1)[1].strip().lower()=="true"
            elif t.startswith("lore_present:"):
                lore = t.split(":",1)[1].strip().lower()=="true"
            elif t.startswith("ids_canonical:"):
                ids = t.split(":",1)[1].strip().lower()=="true"
        if status=="done" and law and lore and ids:
            done += 1
        emoji = "✅" if (status=="done" and law and lore and ids) else ("🟡" if status=="in_progress" else "⬜")
        lines.append(f"- {emoji} **{name}** — status: `{status}`, law:{law}, lore:{lore}, ids:{ids}")
    lines.append(f"\n**Progress:** {done}/{total} schools fully conformant")
    pathlib.Path(out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: update_index_from_checklist.py <school_refactor_checklist.yaml> <out.md>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
