
import textwrap, subprocess, sys, pathlib

def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

def test_validator_accepts_minimal(tmp_path):
    md = tmp_path/"02_invocations.md"
    md.write_text(textwrap.dedent('''
    # 02 - Invocations

    ```json LAW
    {"axioms":["A"],"operators":["op"],"constraints":["c"]}
    ```

    ```json LORE
    {"archetype":"Invoker","notes":["ok"]}
    ```
    '''))
    schema = pathlib.Path("validators/school_schema.json")
    exe = pathlib.Path("validators/validate_school.py")
    out = run([sys.executable, str(exe), str(md), "--schema", str(schema)])
    assert "OK:" in out.stdout
