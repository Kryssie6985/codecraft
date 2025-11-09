
#!/usr/bin/env python3
# Validates a template-conformant school Markdown by extracting LAW/LORE fenced blocks
# in JSON or YAML and enforcing schema.

import sys, re, json, hashlib, argparse, pathlib

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

from jsonschema import validate, Draft7Validator

LAW_TAGS = ("law", "LAW")
LORE_TAGS = ("lore", "LORE")
FENCE = re.compile(r"```(\w+)?\s*(LAW|LORE)\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)

def parse_blocks(text):
    blocks = []
    for m in FENCE.finditer(text):
        lang = (m.group(1) or "").lower()
        tag = m.group(2).lower()
        body = m.group(3).strip()
        blocks.append((tag, lang, body))
    return blocks

def load_obj(lang, body):
    if lang in ("json",""):
        return json.loads(body)
    if lang in ("yaml","yml"):
        if yaml is None:
            raise RuntimeError("PyYAML not installed")
        return yaml.safe_load(body)
    # attempt JSON then YAML fallback
    try:
        return json.loads(body)
    except Exception:
        if yaml is None:
            raise
        return yaml.safe_load(body)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown_file")
    ap.add_argument("--schema", default="validators/school_schema.json")
    args = ap.parse_args()

    p = pathlib.Path(args.markdown_file)
    text = p.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    law = lore = None
    for tag, lang, body in blocks:
        if tag in LAW_TAGS:
            law = load_obj(lang, body)
        elif tag in LORE_TAGS:
            lore = load_obj(lang, body)

    if not (law and lore):
        print("ERROR: Missing LAW and/or LORE fenced blocks", file=sys.stderr)
        sys.exit(2)

    schema = json.loads(pathlib.Path(args.schema).read_text(encoding="utf-8"))
    school_id = p.stem
    payload = {
        "id": re.sub(r"[^a-z0-9_]+","_", school_id.lower()),
        "name": school_id.replace("_"," ").title(),
        "version": "0.1",
        "law": law,
        "lore": lore,
    }
    v = Draft7Validator(schema)
    errs = sorted(v.iter_errors(payload), key=lambda e: e.path)
    if errs:
        print("ERROR: Schema validation failed:", file=sys.stderr)
        for e in errs:
            path = ".".join(map(str,e.path))
            print(f"  - {path}: {e.message}", file=sys.stderr)
        sys.exit(3)

    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
    print("OK:", p.name)
    print("sha256:", digest)
    print(json.dumps(payload, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
