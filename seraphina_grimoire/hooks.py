import json, time

def store_memory(event: dict):
    print("[CMP] store_memory:", json.dumps(event, ensure_ascii=False))

def update_graph(changes: dict):
    print("[LKG] update_graph:", json.dumps(changes, ensure_ascii=False))

def notify_council(msg: str):
    print("[COUNCIL]", msg)
