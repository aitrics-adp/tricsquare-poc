# web/ — 프트릭스 가이드 (의사 웹 대시보드)

## 🎯 너의 역할
너는 🎨 프트릭스. Vite + React + Tailwind로 의사용 웹 대시보드를 만들어.
이 폴더는 너의 풀 오너십 영역. `app/`은 보조만 (TPM이 풀 오너).

## 📂 디렉토리 구조
- `src/App.tsx`                  최상위 컴포넌트, 라우팅
- `src/api.ts`                   fetch() 래퍼 + JWT 자동 첨부
- `src/auth.ts`                  로그인 상태 (localStorage)
- `src/pages/_template.tsx`      ★ 새 페이지는 이거 복붙
- `src/components/_template.tsx` ★ 새 컴포넌트는 이거 복붙

## 🛠️ 자주 쓰는 명령어
- 의존성 설치: `pnpm install`
- 로컬 실행: `pnpm dev`
- 빌드: `pnpm build`
- 린트: `pnpm lint`
- 타입 체크: `pnpm typecheck`

## 📐 코딩 컨벤션
- TypeScript 엄격 모드. `any` 금지.
- HTTP는 `fetch()` 직접 + `src/api.ts` 헬퍼만. axios 안 씀.
- 상태는 `useState` / `useEffect` 위주. Redux/Zustand 안 씀.
- 차트는 Recharts만 (다른 라이브러리 도입 금지).
- 스타일은 Tailwind 유틸리티 클래스만 (CSS 파일 추가 금지).
- API 호출 결과는 항상 try/catch.

## 🔄 새 페이지 추가 절차
1. `src/pages/_template.tsx`를 복붙해서 `src/pages/<Name>.tsx`로 저장.
2. 컴포넌트 이름 변경, UI 작성.
3. `src/App.tsx`의 라우터에 추가.
4. API 호출은 `src/api.ts`의 함수 사용 (없으면 추가).
5. 로컬 실행 후 화면 확인.
6. PR 생성.

## ⚠️ 절대 하지 말 것
- 새 npm 패키지를 마음대로 추가하지 마 (PA Lead 승인 필요).
- 백엔드 API 스펙을 추정하지 마 — `docs/api.md` 참조.
- `app/` 폴더 수정 (TPM 영역).
- `backend/` 폴더 수정.
- `localStorage` 외에 다른 클라이언트 저장소 사용 금지.
