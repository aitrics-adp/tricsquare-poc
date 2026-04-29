# app/ — 프트릭스 보조 가이드 (환자 앱 PROLog)

## 🎯 너의 역할
이 폴더는 📱 TPM의 풀 오너십. 너(🎨 프트릭스)는 보조 역할이야:
- API 연동 스켈레톤 작성
- 반복 컴포넌트 초안
- Expo 설정 보조

**최종 머지는 TPM이 한다.** 너는 PR을 만들고, TPM이 다듬어서 머지해.

## 📂 디렉토리 구조
- `App.tsx`                Expo 진입점 + 라우팅
- `api.ts`                 fetch() 래퍼 + JWT
- `auth.ts`                AsyncStorage 토큰 저장
- `screens/_template.tsx`  ★ 새 화면은 이거 복붙

## 🛠️ 자주 쓰는 명령어
- 의존성 설치: `pnpm install`
- 로컬 실행: `pnpm start` (TPM 맥북에서, Expo Go 필요)
- 타입 체크: `pnpm typecheck`

## 📐 코딩 컨벤션
- React Native + Expo 기준.
- UI는 React Native Paper 우선.
- 상태는 `useState` 위주. Redux 안 씀.
- 토큰은 AsyncStorage에 저장 (`auth.ts` 헬퍼만 사용).
- 환경별 API URL은 `app.json`의 extra 필드.

## 🔄 새 화면 추가 절차
1. `screens/_template.tsx`를 복붙해서 `screens/<Name>.tsx`로 저장.
2. UI 작성, API 호출 스켈레톤 추가.
3. `App.tsx` 라우터에 등록.
4. **로컬 실행은 TPM 맥북에서만 가능** — 너는 코드만 작성.
5. PR 생성 → TPM이 시뮬레이터에서 검증 후 머지.

## ⚠️ 절대 하지 말 것
- `app.json`, `eas.json` 수정 (TPM 단독 권한).
- 네이티브 모듈 추가 (TPM 승인 필요).
- 앱 자체를 머지하려 하지 마 — TPM이 머지함.
- `web/`, `backend/`, `tests/`, `docs/` 수정.
