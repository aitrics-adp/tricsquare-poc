# Agent Handbook

TricSquare POC에서 4개 에이전트(GiTrics / BackTrics / FrTrics / QTrics)가 함께 일하기 위한 공통 운영 룰. 각 에이전트의 워크트리 지시서(`~/tricsquare/{agent}/CLAUDE.md`)와 폴더별 지시서(`backend/CLAUDE.md` 등)에 흩어진 룰 중 **에이전트 간 협업에 영향**을 주는 것들을 한 곳에 모은다.

각 에이전트 지시서에 다음 한 줄을 추가해서 본 문서를 참조하도록 한다 (사람이 직접):

> `## 공통 룰: 모노레포 docs/agent-handbook.md 참조`

문서가 SSOT이고, 각 에이전트는 포인터만 둔다.

---

## 운영 룰

### 1) 핸드오프 룰 (에이전트 간 협업)

- **티켓 생성은 GiTrics만.** 다른 에이전트는 코멘트로 요청만.
- 작업 중 의존성/블로커 발견 시:
  1. 현재 티켓 코멘트에 "선행 작업 필요" 명시 (구체적 AC 초안 포함).
  2. 현재 티켓 `Stop Progress` 트랜지션으로 Ready로 되돌림.
  3. 작업 종료 + 사람에게 보고.
- 사람이 GiTrics에게 명시적으로 "TRCS-N 코멘트 보고 선행 티켓 발행" 지시.
- GiTrics가 새 티켓 발행 → 사람 승인 (Refine + Mark Ready) → 새 티켓 작업 → 머지 → 원래 티켓 재개.

> POC 단계는 사람 매개. 자동 알림은 추후 Jira Automation으로 추가 예정.

### 2) chore 티켓 정책

1줄 chore (lock 파일 추가, 포맷 수정, typo 등)는 **TRCS-N 없이 `[chore]` prefix만으로 OK**. 단, 다음 항목은 반드시 GiTrics에게 티켓 발행 요청:

- 의존성 추가/제거 (`pyproject.toml`, `package.json` 등 변경)
- 빌드 도구 변경 (pre-commit hook 추가/제거 등)
- CI/CD 변경 (`.github/workflows/` 수정)
- 인프라 변경 (`template.yaml` 등)

판정 기준: **다른 에이전트의 빌드/CI/배포에 영향**을 주는지. 영향 있으면 티켓.

### 3) 워크트리 sync 룰

- **본인 워크트리만 sync.** 다른 워크트리는 다른 에이전트 영역 — 건드리지 말 것.
- sync 명령:
  ```bash
  git fetch origin --prune
  git checkout {agent}/main
  git merge --ff-only origin/main
  ```
  (`{agent}`은 `gitrics` / `backtrics` / `frtrics` / `qtrics` 중 본인 것)
- sync 시점:
  - **작업 시작 직전** (Start Progress 후 새 브랜치 만들기 전)
  - **PR 머지 직후** (다음 작업 시작 전 최신 상태 반영)

> `--ff-only`로 강제. 충돌이 나면 다른 에이전트가 같은 영역을 만진 것 → 멈추고 사람 보고.

---

## 외부 시스템

### MCP 서버 설정 (`.mcp.json`)

- 각 워크트리 루트(`~/tricsquare/{agent}/.mcp.json`)에 위치 (git 추적 외부).
- 올바른 schema: `{"type": "http", "url": "..."}`.
- 현재 등록: `atlassian` (Jira/Confluence).
- **GitHub MCP 재추가는 TRCS-6에서 처리** — 본 PR에서는 schema 위반 정리만.

### Git 워크트리 신원

- 각 워크트리는 본인 명의로 commit하도록 `git config` 영구화 (per-worktree, `-c` 플래그 반복 X).
- 4개 워크트리(gitrics/backtrics/frtrics/qtrics) 각각 `user.name` / `user.email` 박혀있어야 함.
