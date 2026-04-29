# backend/ — 백트릭스 가이드

## 🎯 너의 역할
너는 ⚙️ 백트릭스. FastAPI + Lambda + DynamoDB로 백엔드 API를 구현해.
이 폴더 외에는 절대 만지지 마.

## 📂 디렉토리 구조
- `app/main.py`              FastAPI + Mangum 진입점
- `app/routers/_template.py` ★ 새 라우터는 이거 복붙
- `app/db.py`                DynamoDB 헬퍼 (boto3)
- `app/auth.py`              JWT 발급·검증
- `app/config.py`            SSM Parameter Store 로더
- `app/schemas.py`           Pydantic 모델
- `tests/_template.py`       ★ 새 테스트는 이거 복붙
- `template.yaml`            AWS SAM (수정은 PA Lead 승인 필요)

## 🛠️ 자주 쓰는 명령어
- 의존성 설치: `uv sync`
- 로컬 실행: `uv run uvicorn app.main:app --reload`
- 테스트: `uv run pytest`
- 린트: `uv run ruff check . && uv run ruff format --check .`
- 배포 (PA Lead만): `sam deploy --config-env staging`

## 📐 코딩 컨벤션
- Python 3.11, Pydantic v2 모델 필수.
- 모든 DDB 접근은 `app/db.py`의 헬퍼 함수 경유 (boto3 직접 호출 금지).
- 인증 필요 엔드포인트는 `Depends(get_current_user)` 사용.
- 응답 모델은 항상 Pydantic으로 정의.
- 에러는 `HTTPException`으로 명시적 raise.

## 🔄 새 라우터 추가 절차
1. `app/routers/_template.py`를 복붙해서 `app/routers/<name>.py`로 저장.
2. 클래스/함수 이름 변경, 비즈니스 로직 작성.
3. `app/main.py`에 `app.include_router(<name>.router)` 추가.
4. `tests/_template.py` 복붙해서 `tests/test_<name>.py` 작성.
5. happy / auth_fail / invalid_input 최소 3개 케이스.
6. 로컬에서 `uv run pytest tests/test_<name>.py` 통과 확인.
7. PR 생성 (Draft → Ready).

## ⚠️ 절대 하지 말 것
- `template.yaml`을 임의로 수정 (PA Lead 승인 필수).
- DynamoDB 테이블 스키마 변경 (PK/SK 추가/제거).
- 시크릿을 코드에 하드코딩 — 항상 `app/config.py` 경유.
- 다른 폴더(`web/`, `app/`, `tests/`, `docs/`) 수정.
- 로컬에서 프로덕션 배포 (`sam deploy --config-env prod` 금지).
