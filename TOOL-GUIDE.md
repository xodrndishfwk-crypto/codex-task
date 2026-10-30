# 도구별 역할

긴 이름을 외울 필요 없이 아래 이름 하나를 골라 Codex에 말하면 됩니다.

| 이름 | 하는 일 | 이렇게 말하기 |
|---|---|---|
| `understand-task` | 과제와 파일을 보고 무엇을 해야 하는지 파악 | `understand-task를 읽고 과제부터 파악해` |
| `find-needs` | 요구사항, 제출물, 성공 기준을 정리 | `find-needs로 필요한 것을 정리해` |
| `make-questions` | 실무자 에이전트에게 물어볼 질문 작성 | `make-questions로 질문을 만들어줘` |
| `make-plan` | 구현 순서와 단계별 확인 방법 작성 | `make-plan으로 작업 순서를 정해줘` |
| `manage-time` | 남은 시간에 맞춰 범위와 중단 시점 조절 | `manage-time으로 시간 계획을 잡아줘` |
| `fix-errors` | 오류를 재현하고 원인을 찾아 수정 | `fix-errors로 이 오류를 조사해` |
| `check-result` | 결과가 요구사항을 충족하는지 확인 | `check-result로 결과를 검증해` |
| `write-report` | 실행법, 구현 내용, 테스트, 한계 정리 | `write-report로 제출 문서를 정리해` |
| `final-check` | 제출 전 빠진 내용과 설명 근거 점검 | `final-check로 마지막 점검해` |

## 기본 사용법

처음에는 하나를 직접 고르지 않아도 됩니다.

```text
codex-task/START-HERE.md를 읽고 시작해.
```

`START-HERE.md`가 먼저 `understand-task`를 읽고 상황에 맞는 기능을 고르게 합니다.

## 직접 고를 때

원하는 기능이 확실하면 파일 경로까지 말할 수 있습니다.

```text
codex-task/skills/make-questions/SKILL.md를 읽고 실무자에게 물어볼 질문을 만들어줘.
```

```text
codex-task/skills/check-result/SKILL.md를 읽고 현재 결과를 검증해.
```

Skill은 완성 결과물을 대신 만드는 버튼이 아니라, Codex가 해당 업무를 수행할 때 지킬 절차입니다.
