# 여기서 시작

파일 이름을 외울 필요가 없습니다.

## Codex에 보낼 첫 요청

```text
codex-task/AGENTS.md와 codex-task/START-HERE.md를 읽고 시작해.
```

## Codex가 이어서 수행할 시작 절차

사용자가 위 두 파일을 읽고 시작하라고 하면 아래 절차를 별도 요청 없이 수행한다. 아래 경로는 이 도구 모음 폴더를 기준으로 한다.

1. 실제 과제 README와 제공 파일을 먼저 확인한다. 과제 폴더의 README가 시험 명세이며, 이 도구 모음의 README는 사용 설명이다. 과제 README를 찾지 못하거나 후보가 여러 개라 구분할 수 없으면 확인하고 추측하지 않는다.
2. `skills/explain-readme-in-plain-korean/SKILL.md`를 읽고 과제 작업 공간에 `reports/<작업명>/README-이해하기.md`를 작성한다. 업무 목적·사용자·사용 예시·필수 조건·제출물·미정 사항을 쉽게 설명하고 채팅에 문서 링크와 핵심 내용을 보여준다.
3. `skills/inspect-task-and-choose-workflow/SKILL.md`를 따라 요구사항·중요 질문·성공 기준·검증 방법·단계별 계획을 정리한다. 2단계에서 만든 설명 문서는 재사용하고, `WHAT-EACH-TOOL-DOES.md`와 필요한 Skill은 Codex가 찾아 읽는다. 사용자에게 내부 경로를 추가로 지정하도록 요구하지 않는다.
4. `AGENTS.md`의 단계별 진행보고 규칙에 따라 조사 보고서를 저장하고 링크를 보여준다. 중요한 질문은 채팅에서도 직접 묻는다. 시작 요청만 받은 시점에는 조사·설명·계획을 먼저 보여주고 구현을 시작하지 않는다.
5. 사용자가 구현 진행을 지시하면 확정된 조건에 따라 구현·검증하고 단계별 보고와 마지막 최종보고까지 이어간다. 이후 매 단계 승인을 반복해서 요구하지 않으며, 사용자 판단이 필요한 사안은 기존 질문 절차로 처리한다.

기존 파일과 사용자 작성 문서를 보존하고, 실제 시험 지침과 과제별 제출 조건을 우선한다.

## 사람이 실행할 수 있는 간단한 명령

```bash
# 도구 자체 확인
python codex-task/kit.py check

# 현재 과제의 파일 종류와 구조 파악
python codex-task/kit.py scan .

# 모든 입력 파일의 경로·형식·크기 목록
python codex-task/kit.py files .

# CSV 또는 JSON 데이터 빠른 조사
python codex-task/kit.py data 데이터파일.csv

# 대상별 판정 CSV에 이유와 근거가 빠졌는지 확인
python codex-task/kit.py decisions 판정결과.csv
```

명령이 기억나지 않으면 `python codex-task/kit.py`만 실행합니다.

## 과제 유형별로 먼저 쓸 도구

| 과제 유형 | 먼저 사용할 Skill |
|---|---|
| 모바일·웹 애플리케이션 개발 | `inspect-app-project-and-run-locally` → `define-app-users-screens-and-core-flow` → `build-smallest-working-app-first` → `connect-app-data-storage-and-state` → `test-app-screens-inputs-and-navigation` |
| 매뉴얼 기준으로 여러 사람·설비·업체 심사 | `list-and-group-input-files` → `turn-manual-into-rule-checklist` → `extract-facts-and-record-sources` → `apply-rules-and-explain-each-decision` |
| CSV·Excel 데이터 분석 | `analyze-table-data-and-find-patterns` → `build-result-table-and-short-summary` |
| 여러 파일의 값 대조 | `find-missing-duplicate-or-conflicting-data` |
| 점수 계산과 우선순위 | `rank-items-and-explain-the-order` |
| 기존 코드 오류 수정 | `find-and-fix-code-errors` → `test-results-against-requirements` |
| 복합 과제 | `inspect-task-and-choose-workflow`로 가장 중요한 결과부터 나누기 |

## 공통 안전 규칙

- 과제 README와 최신 공식 안내가 가장 우선입니다.
- 실무자 에이전트에는 업무 기준과 모호한 예외를 묻습니다.
- Cofa Helper에는 화면과 제출 방법을 묻습니다.
- 외부 전송, Git Push, 개인 파일 업로드, Astra, Computer Use, 별도 AI/API를 사용하지 않습니다.
- 제출 후 서술형은 AI 없이 본인이 직접 답합니다.
