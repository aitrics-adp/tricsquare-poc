// 컴포넌트 템플릿. 새 컴포넌트는 이 파일을 복붙해 시작하세요.
// 파일명: src/components/<PascalCase>.tsx
// Props 타입을 명시하고 TS 엄격 모드를 통과해야 합니다.

type TemplateBadgeProps = {
  label: string;
};

export default function TemplateBadge({ label }: TemplateBadgeProps): JSX.Element {
  return (
    <span className="inline-flex items-center rounded bg-slate-100 px-2 py-1 text-sm text-slate-700">
      {label}
    </span>
  );
}
