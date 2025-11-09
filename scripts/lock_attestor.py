#!/usr/bin/env python3
"""
canon-lock attestor
See docs/README.md for usage.
"""
import argparse, hashlib, pathlib, sys, re, datetime as dt

PARTITIONS = ["schools","foundations","parameters","syntax_variants","operators","grammar"]

def file_sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def try_yaml(path: pathlib.Path):
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return None

def heuristic_counts(text: str):
    counts = {}
    for part in PARTITIONS:
        m = re.search(rf"(?m)^\s*{part}\s*:\s*(\n|$)", text)
        if not m:
            counts[part] = 0
            continue
        start = m.end()
        nxt = re.search(r"(?m)^\w[\w_]*\s*:\s*(\n|$)", text[start:])
        block = text[start: start + (nxt.start() if nxt else len(text))]
        counts[part] = len(re.findall(r"(?m)^\s*-\s", block))
    return counts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default="canon.lock.yaml")
    args = ap.parse_args()

    p = pathlib.Path(args.path)
    if not p.exists():
        print(f"ERROR: {p} not found", file=sys.stderr); sys.exit(2)

    sha = file_sha(p)
    size = p.stat().st_size
    text = p.read_text(encoding="utf-8", errors="ignore")

    data = try_yaml(p)
    if isinstance(data, dict):
        counts = {}
        for part in PARTITIONS:
            v = data.get(part)
            counts[part] = (len(v) if isinstance(v, (list, dict)) else 0)
    else:
        counts = heuristic_counts(text)

    stamp = dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        f"canon.attest.ts: {stamp}",
        f"canon.path: {p}",
        f"canon.sha256: {sha}",
        f"canon.bytes: {size}",
        "partitions:",
    ] + [f"  {k}: {counts.get(k,0)}" for k in PARTITIONS]

    receipt = "\n".join(lines) + "\n"
    print(receipt)

    receipts_dir = p.parent/"receipts"
    receipts_dir.mkdir(parents=True, exist_ok=True)
    out = receipts_dir/f"canon_attest_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    out.write_text(receipt, encoding="utf-8")
    print(f"wrote: {out}")

if __name__ == "__main__":
    main()
