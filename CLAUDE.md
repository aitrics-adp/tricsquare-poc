# tricsquare-poc — 모노레포 가이드

## 🎯 이 프로젝트는?
AITRICS 트릭스퀘어 PRO 수집 MVP. 환자가 증상을 제출하고, 의사가 본다.

## 🗂️ 폴더별 담당 에이전트
- `backend/` → ⚙️ 백트릭스
- `web/`     → 🎨 프트릭스 (풀 오너)
- `app/`     → 📱 TPM (풀 오너), 🎨 프트릭스 (보조)
- `tests/`   → 🧪 큐트릭스
- `docs/`    → 🧭 기트릭스
- `.github/`, `template.yaml` → PA Lead (사람) 전담

## ⚠️ 절대 규칙
1. 너의 담당 폴더 외에는 **절대** 수정하지 마.
2. 새 기능은 항상 해당 폴더의 `_template.X`를 복붙해서 시작해.
3. 커밋 전 `pre-commit run --all-files` 통과 확인.
4. PR 제목은 `[TRIC-N] 한 줄 요약` 형식.
5. DynamoDB 스키마 변경은 PA Lead 승인 없이 금지.

## 🔗 더 알아야 할 것
- 폴더별 상세는 그 폴더의 `CLAUDE.md`를 봐.
- 데이터 모델: `docs/data-model.md`
- API 스펙: `docs/api.md`
- 더 깊은 컨텍스트: Confluence "🚀 트릭스퀘어 MVP" 트리

## 🚫 토큰 절약을 위해 절대 하지 말 것
- 다른 폴더 파일을 호기심으로 읽지 마.
- 프로젝트 전체를 스캔하려 하지 마. 필요한 파일만 봐.
- 기존 패턴을 추론하려 하지 마. `_template.X`가 정답이야.
