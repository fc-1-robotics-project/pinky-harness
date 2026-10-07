# pinky-harness

Pinky Pro(ROS 2 Jazzy) 개발용 Claude Code 플러그인 겸 Codex 스킬·에이전트 모음. [revfactory/harness](https://github.com/revfactory/harness) v2 방식으로 만들었다.

| 구성 | 역할 |
| --- | --- |
| `agents/lane-perception-dev` | 세그멘테이션 → 지면 투영 → 주행 경로 |
| `agents/drive-control-dev` | Pure Pursuit, 속도 제한, 횡단보도/장애물 상태기계, watchdog |
| `agents/nav2-dev` | SLAM, AMCL, Nav2 파라미터·런치, Gazebo, 목표 주행 |
| `agents/robot-safety-reviewer` | 읽기 전용 안전 검토 (PASS / FAIL / BLOCKED) |
| `skills/pinky-robotics` | 오케스트레이터 (개발 → 검토 → 최대 3회 수정) |
| `skills/lane-perception`, `drive-control`, `nav2-driving` | 영역별 작업 방법 |

## 설치

```shell
/plugin marketplace add ~/ros/pinky-harness
/plugin install pinky-harness@pinky-harness-marketplace
```

GitHub: `/plugin marketplace add fc-1-robotics-project/pinky-harness`.

## Codex 설치

```shell
git clone git@github.com:fc-1-robotics-project/pinky-harness.git ~/pinky-harness
# 스킬 (사용자 전역)
mkdir -p ~/.agents && ln -s ~/pinky-harness/skills ~/.agents/skills   # 이미 있으면 하위 폴더만 링크
# 커스텀 에이전트
mkdir -p ~/.codex/agents && ln -s ~/pinky-harness/.codex/agents/*.toml ~/.codex/agents/
```

또는 대상 저장소에 `.agents/skills`, `.codex/agents`를 복사/링크한다.

| | Claude Code | Codex |
| --- | --- | --- |
| 지침 | `CLAUDE.md` (→ `AGENTS.md` symlink) | `AGENTS.md` |
| 스킬 | `skills/` (플러그인) | `.agents/skills` (→ `skills/` symlink) |
| 에이전트 | `agents/*.md` (원본) | `.codex/agents/*.toml` (생성물) |

`agents/*.md`를 고치면 `python3 -I scripts/sync-codex.py`로 TOML을 다시 만들고 `scripts/check.sh`로 확인한다.
Codex 런타임에서의 동작은 아직 시험하지 않았다 (형식만 공식 문서 기준).

## 전제

pinky-lane-driving 저장소 루트에서 쓴다 (`.agents/tools/harness.sh` 필요). 중간 산출물은 `.agents/output/harness/`에 쓴다.
에이전트는 하드웨어 bringup, 모터 명령, SSH 배포를 실행하지 않는다.
