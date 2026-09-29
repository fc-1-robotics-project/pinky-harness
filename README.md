# pinky-harness

Pinky Pro(ROS 2 Jazzy) 개발용 Claude Code 플러그인. [revfactory/harness](https://github.com/revfactory/harness) v2 방식으로 만들었다.

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

GitHub에 올린 뒤에는 `/plugin marketplace add <owner>/pinky-harness`.

## 전제

pinky-lane-driving 저장소 루트에서 쓴다 (`.agents/tools/harness.sh` 필요). 중간 산출물은 `.agents/output/harness/`에 쓴다.
에이전트는 하드웨어 bringup, 모터 명령, SSH 배포를 실행하지 않는다.
