# 각 도구로 무엇을 할 수 있는지

이름을 외우지 않아도 됩니다. 이 파일을 Codex에 읽으라고 하면 과제에 필요한 도구를 고를 수 있습니다.

## 과제를 시작하고 계획할 때

| 이름 | 입력 | 나오는 결과 |
|---|---|---|
| `explain-readme-in-plain-korean` | 시험 과제 README와 참조 명세 | 목적·사용자·사용 예시·입력과 결과·필수 조건을 쉽게 설명한 한국어 MD |
| `inspect-task-and-choose-workflow` | 과제 설명과 전체 파일 | 과제 유형과 사용할 작업 흐름 |
| `list-required-results-and-rules` | 과제 원문과 담당자 답변 | 제출물·요구사항·제한사항·성공 기준 목록 |
| `prepare-clear-business-questions` | 아직 모호한 업무 조건 | 실무자에게 물을 짧고 결정 가능한 질문 |
| `plan-small-steps-and-checks` | 확정된 요구사항 | 단계별 작업과 각 단계의 확인 방법 |
| `plan-time-and-stop-points` | 제한 시간과 남은 작업 | 시간 배분과 새 기능을 멈출 시점 |

## 매뉴얼과 여러 서류를 처리할 때

| 이름 | 입력 | 나오는 결과 |
|---|---|---|
| `list-and-group-input-files` | 여러 사람·설비·업체의 파일 | 대상별 파일 목록과 누락·중복 목록 |
| `turn-manual-into-rule-checklist` | 매뉴얼·규정 PDF | 조건·예외·출처가 있는 규칙 체크리스트 |
| `extract-facts-and-record-sources` | 대상별 서류와 규칙표 | 판단에 필요한 사실과 원본 위치 표 |
| `apply-rules-and-explain-each-decision` | 규칙표와 사실표 | 대상별 통과·탈락·확인 필요 판정과 이유 |
| `find-missing-duplicate-or-conflicting-data` | 서로 연결된 여러 파일·표 | 누락·중복·충돌·연결 실패 검토 목록 |

## 데이터를 분석하고 결과를 만들 때

| 이름 | 입력 | 나오는 결과 |
|---|---|---|
| `analyze-table-data-and-find-patterns` | CSV·JSON·Excel 표 | 결측·중복·집계·비교·추세·이상값 분석 |
| `rank-items-and-explain-the-order` | 평가 대상과 점수 규칙 | 순위·점수·순위 이유·확인 필요 사항 |
| `build-result-table-and-short-summary` | 분석·판정 결과 | 대상별 상세표·전체 집계·짧은 요약 |

## 모바일·웹 애플리케이션을 만들 때

| 이름 | 입력 | 나오는 결과 |
|---|---|---|
| `inspect-app-project-and-run-locally` | 기존 앱 프로젝트 | 기술 구성·실행법·수정 전 실행 결과 |
| `define-app-users-screens-and-core-flow` | 앱 요구사항 | 핵심 사용자·필수 화면·화면 이동 계획 |
| `build-smallest-working-app-first` | 화면 계획과 기존 코드 | 처음부터 끝까지 동작하는 최소 핵심 기능 |
| `connect-app-data-storage-and-state` | 화면·입력·데이터 요구사항 | 저장·상태 변화·빈 화면·오류 처리가 연결된 앱 |
| `test-app-screens-inputs-and-navigation` | 완성 앱과 요구사항 | 화면·입력·이동·모바일 배치 테스트 결과 |

## 코드를 고치고 제출을 준비할 때

| 이름 | 입력 | 나오는 결과 |
|---|---|---|
| `find-and-fix-code-errors` | 실패하는 코드나 테스트 | 재현 결과·원인·최소 수정·회귀 테스트 |
| `test-results-against-requirements` | 완성 결과와 요구사항 | 요구사항별 통과 여부와 테스트 증거 |
| `write-result-and-test-report` | 구현·분석·테스트 기록 | 실행법·결정·테스트·한계 보고서 |
| `check-everything-before-submit` | 전체 제출물과 작업 기록 | 빠진 것과 마지막 수정 항목 목록 |

## 가장 쉬운 사용법

```text
codex-task/START-HERE.md와 codex-task/WHAT-EACH-TOOL-DOES.md를 읽고,
이 과제에 필요한 도구만 골라서 사용해.
```

원하는 도구가 확실하면 경로를 직접 말해도 됩니다.

```text
codex-task/skills/turn-manual-into-rule-checklist/SKILL.md를 읽고
제공된 매뉴얼을 판정 규칙표로 만들어줘.
```

앱 개발 과제라면 다음처럼 요청할 수 있습니다.

```text
codex-task/skills/inspect-app-project-and-run-locally/SKILL.md와
codex-task/skills/define-app-users-screens-and-core-flow/SKILL.md를 읽고
기존 앱을 실행한 다음 핵심 화면과 사용자 흐름을 정리해줘.
```

Skill은 결과물을 대신 제공하는 프로그램이 아니라 Codex가 업무를 정확하고 같은 방식으로 수행하도록 돕는 절차입니다.
