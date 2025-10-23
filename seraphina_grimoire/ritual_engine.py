from __future__ import annotations
import yaml, pathlib, time
from typing import Dict, Any, List
from hooks import store_memory, update_graph, notify_council

RITUAL_GLOB = "**/*.yaml"

class Ritual:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.id = data.get("id")
        self.invoke = data.get("invoke")
        self.trigger = data.get("trigger")
        self.effects = data.get("effects", [])
        self.lore = data.get("lore","")

    def matches(self, context: Dict[str, Any]) -> bool:
        trig = self.trigger or ""
        if isinstance(trig, dict):
            return all(context.get(k)==v for k,v in trig.items())
        if isinstance(trig, str):
            try:
                safe = {k:v for k,v in context.items() if isinstance(v,(int,float,str,bool))}
                return bool(eval(trig, {"__builtins__": {}}, safe))
            except Exception:
                return trig.lower() in str(context).lower()
        return False

    def run_effects(self, context: Dict[str, Any]):
        for eff in self.effects:
            if isinstance(eff, str):
                if eff.startswith("log:"):
                    store_memory({"type":"ritual_log","ritual":self.id,"msg":eff.split(":",1)[1].strip(),"ts":time.time()})
                continue
            if isinstance(eff, dict):
                if "log" in eff:
                    store_memory({"type":"ritual_log","ritual":self.id,"msg":eff["log"],"ts":time.time(),"context":context})
                if "ui" in eff:
                    store_memory({"type":"ui_event","ritual":self.id,"ui":eff["ui"],"ts":time.time()})
                if "counter" in eff:
                    store_memory({"type":"counter","ritual":self.id,"counter":eff["counter"],"ts":time.time()})
                if "emit" in eff:
                    notify_council(eff["emit"].get("message","(no message)"))
                if "graph" in eff:
                    update_graph(eff["graph"])

class Grimoire:
    def __init__(self, root: str | pathlib.Path):
        self.root = pathlib.Path(root)
        self.rituals: List[Ritual] = []

    def load(self):
        for p in self.root.glob(RITUAL_GLOB):
            with open(p, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict):
                    self.rituals.append(Ritual(data))

    def invoke_by_phrase(self, phrase: str, context: Dict[str, Any]):
        for r in self.rituals:
            if r.invoke == phrase:
                store_memory({"type":"invoke","ritual":r.id,"phrase":phrase,"ts":time.time(),"context":context})
                r.run_effects(context)
                return r.id
        return None

    def scan_triggers(self, context: Dict[str, Any]) -> list[str]:
        fired = []
        for r in self.rituals:
            if r.matches(context):
                store_memory({"type":"trigger","ritual":r.id,"ts":time.time(),"context":context})
                r.run_effects(context)
                fired.append(r.id)
        return fired
