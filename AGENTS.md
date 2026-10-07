# pinky-harness

Pinky Pro(ROS 2 Jazzy) 개발 하네스. Claude Code 플러그인이자 Codex용 스킬·에이전트 모음이다.

- 스킬 원본: `skills/` (`.agents/skills`는 이를 가리키는 symlink). 오케스트레이터는 `skills/pinky-robotics`.
- 에이전트 원본: `agents/*.md` (Claude). Codex용 `.codex/agents/*.toml`은 `python3 -I scripts/sync-codex.py`로 생성한다. 직접 고치지 않는다.
- 변경 후 `scripts/check.sh`를 실행한다.
- 대상은 pinky-lane-driving 저장소(`.agents/tools/harness.sh` 필요)다. 없으면 멈추고 알린다.
- 하드웨어 bringup, 모터 명령 발행, SSH 배포는 하지 않는다. 안전 임계값을 낮추지 않는다.
- 단위 테스트·ROS 빌드·시뮬레이션·실주행 증거를 구분해 보고한다.
