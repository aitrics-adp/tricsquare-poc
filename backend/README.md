# backend — TricSquare PRO 수집 API

FastAPI + AWS Lambda + DynamoDB 기반 백엔드. Mangum이 ASGI ↔ Lambda 어댑터 역할.

## 디렉터리

```
backend/
├── app/
│   ├── main.py            FastAPI + Mangum 진입점
│   ├── config.py          pydantic-settings (env / SSM)
│   ├── db.py              DynamoDB 헬퍼 (boto3 직접 호출 금지)
│   ├── auth.py            JWT 발급 / 검증 (POC HS256)
│   ├── schemas.py         공통 Pydantic 베이스
│   └── routers/
│       └── _template.py   ★ 새 라우터는 이거 복붙
├── tests/
│   └── _template.py       ★ 새 테스트는 이거 복붙
├── pyproject.toml         uv 패키지 + ruff/mypy/pytest 설정
└── README.md
```

`template.yaml`(SAM)은 PA Lead 전담이라 본 디렉터리에 별도 추가됨.

## 자주 쓰는 명령

```bash
# 의존성 설치 (개발)
uv sync

# 로컬 개발 서버
uv run uvicorn app.main:app --reload

# 테스트
uv run pytest

# 린트 / 포맷
uv run ruff check .
uv run ruff format --check .

# 타입 체크
uv run mypy

# 모든 pre-commit 훅 실행
pre-commit run --all-files
```

## 새 라우터 추가 절차

1. `app/routers/_template.py` → `app/routers/<feature>.py` 복사.
2. prefix/tag 변경, 비즈니스 로직 작성. DDB는 `app.db` 헬퍼 경유.
3. `app/main.py`에 `app.include_router(<feature>.router)` 추가.
4. `tests/_template.py` → `tests/test_<feature>.py` 복사.
5. happy / auth_fail / invalid_input 최소 3 케이스 작성.
6. `uv run pytest tests/test_<feature>.py` 통과 확인.
7. `pre-commit run --all-files` 통과 후 PR.

## 컨벤션 요약

- Python 3.11, Pydantic v2 모델 필수.
- DDB 접근은 `app/db.py` 헬퍼만 사용 (직접 boto3 금지).
- 인증 필요 엔드포인트: `Depends(get_current_user)`.
- 응답은 항상 `response_model` 명시.
- 에러는 `HTTPException`으로 명시적 raise.

## 타입 체크

`pyproject.toml`의 mypy 설정은 현재 모더레이트(strict 미적용). `disallow_untyped_defs`/`check_untyped_defs`만 켜져 있음. 기능 모듈이 안정화되면 `strict = true`로 ratchet 예정.

pre-commit의 mypy 훅은 `^backend/(app|tests)/` 경로만 검사하며, 다른 영역(web/, app/, docs/)에는 영향 없음.

## 보안 / 데이터

- 시크릿은 코드 하드코딩 금지. `app/config.py` 경유 (env / SSM).
- POC 단계에선 합성 데이터만 사용. 실제 환자 데이터 절대 금지.
- `template.yaml` 수정은 PA Lead 승인 필수.
- DDB 테이블 스키마 변경(PK/SK)은 PA Lead 승인 필수.

## 관련 문서

- 루트 `CLAUDE.md` — 모노레포 전체 가이드.
- `backend/CLAUDE.md` — BackTrics 에이전트 운영 룰.
- `docs/data-model.md` — DDB 모델.
- `docs/api.md` — API 스펙.
