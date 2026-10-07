"""agents/*.md (Claude 원본) -> .codex/agents/*.toml 생성. 사용: python3 -I scripts/sync-codex.py [--check]"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
out = root / ".codex" / "agents"
check = "--check" in sys.argv
bad = 0
for md in sorted((root / "agents").glob("*.md")):
    m = re.match(r"---\n(.*?)\n---\n(.*)", md.read_text(), re.S)
    meta = dict(re.findall(r'^(name|description|tools):\s*"?(.*?)"?\s*$', m[1], re.M))
    body = m[2].strip().replace("${CLAUDE_PLUGIN_ROOT}/", "")
    assert "'''" not in body, md
    ro = "Edit" not in meta["tools"]
    toml = (
        f'name = {json.dumps(meta["name"])}\n'
        f'description = {json.dumps(meta["description"], ensure_ascii=False)}\n'
        f'sandbox_mode = "{"read-only" if ro else "workspace-write"}"\n'
        f'model_reasoning_effort = "high"\n'
        f"developer_instructions = '''\n{body}\n'''\n"
    )
    dst = out / f"{md.stem}.toml"
    if check:
        if not dst.exists() or dst.read_text() != toml:
            print("STALE", dst.name); bad += 1
    else:
        dst.write_text(toml)
sys.exit(bad)
