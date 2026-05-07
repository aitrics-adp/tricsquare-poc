# tricsquare-poc — 모노레포 가이드

## 🎯 이 프로젝트는?
AITRICS 트릭스퀘어 PRO 수집 MVP. 환자가 증상을 제출하고, 의사가 본다.

## 👥 조직 구조
- **PA팀 리드 (백상헌, @aitrics-shbaek)** — Terraform, AWS 리소스, SAM 배포, OIDC. 인프라 전담. 코드 리뷰 안 함.
- **AF팀 리드 (정주용, @aitrics-jyjeong)** — PRD 작성, 4 에이전트 개발 지시, PR 리뷰/머지 권한자.
- **IF팀 리드 (박진우, @aitrics-jinwoopark)** — ML/AI Framework. 모델 서빙, 추론 파이프라인.
- **4 AI 에이전트** — AF팀 리드 지시에 따라 개발 실행. commit까지만, push/PR은 사람.

## 🗂️ 폴더별 담당 에이전트
- `backend/` → ⚙️ 백트릭스
- `web/` → 🎨 프트릭스 (풀 오너)
- `app/` → AF팀 리드 (풀 오너), 🎨 프트릭스 (보조)
- `tests/` → 🧪 큐트릭스
- `docs/` → 🧭 기트릭스
- `.github/` → 🧭 기트릭스
- `template.yaml`, Terraform, AWS → PA팀 리드 전담 (인프라)

## ⚠️ 절대 규칙
1. 너의 담당 폴더 외에는 **절대** 수정하지 마.
2. 새 기능은 항상 해당 폴더의 `_template.X`를 복붙해서 시작해.
3. 커밋 전 `pre-commit run --all-files` 통과 확인.
4. PR 제목은 `[TRCS-N] type: 한 줄 요약` 형식.
5. DynamoDB 스키마 변경은 PA팀 리드 승인 없이 금지.
6. AF팀 리드의 PR 리뷰 없이 main 머지 금지.
7. 비용 발생 작업 (sam deploy, AWS 리소스 생성)은 PA팀 리드에게 요청.

## 🔗 더 알아야 할 것
- 폴더별 상세는 그 폴더의 `CLAUDE.md`를 봐.
- 데이터 모델: `docs/data-model.md`
- API 스펙: `docs/api.md`
- 더 깊은 컨텍스트: Confluence "🚀 트릭스퀘어 MVP" 트리

## 🚫 토큰 절약을 위해 절대 하지 말 것
- 다른 폴더 파일을 호기심으로 읽지 마.
- 프로젝트 전체를 스캔하려 하지 마. 필요한 파일만 봐.
- 기존 패턴을 추론하려 하지 마. `_template.X`가 정답이야.

## 📣 Slack 보고 규칙
- **작업 커밋 완료 시**: `$SLACK_WEBHOOK_URL`로 `[에이전트명] ✅ TRCS-N 작업 설명 — commit 완료, push 대기` 전송
- **블로커 발견 시**: `$SLACK_WEBHOOK_URL`로 `[에이전트명] 🛑 TRCS-N 블로커: 설명` 전송
- 전송은 `curl` 명령으로, `username`은 `$AGENT_NAME` 사용
- `#tricsquare-infra` (`$SLACK_WEBHOOK_INFRA`)는 **PA팀 리드 전용**, 에이전트 사용 금지
