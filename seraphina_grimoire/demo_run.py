from ritual_engine import Grimoire

if __name__ == "__main__":
    g = Grimoire("rituals")
    g.load()
    g.invoke_by_phrase("::(╯°□°)╯︵ ┻━┻::", {"serendipity_score": 1.0, "agent":"claude"})
    fired = g.scan_triggers({"serendipity_score": 2.0, "ternary_revelation": True})
    print("Fired:", fired)
