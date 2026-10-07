#!/usr/bin/env bash
# 하네스 정합성 검사: 에이전트/TOML 동기화, SKILL frontmatter, AGENTS.md/CLAUDE.md, symlink
cd "$(dirname "$0")/.." || exit 1
fail=0
python3 -I scripts/sync-codex.py --check || fail=1
for f in skills/*/SKILL.md; do
  grep -q '^name:' "$f" && grep -q '^description:' "$f" || { echo "BAD frontmatter $f"; fail=1; }
done
[ -f AGENTS.md ] || { echo "missing AGENTS.md"; fail=1; }
[ "$(readlink CLAUDE.md)" = AGENTS.md ] || { echo "CLAUDE.md must symlink AGENTS.md"; fail=1; }
[ -f .agents/skills/pinky-robotics/SKILL.md ] || { echo ".agents/skills symlink broken"; fail=1; }
[ $fail = 0 ] && echo "check OK"
exit $fail
