# 여기서 시작

파일 이름을 외울 필요가 없습니다.

## Codex에 보낼 첫 요청

```text
codex-task/AGENTS.md, codex-task/START-HERE.md,
codex-task/WHAT-EACH-TOOL-DOES.md를 읽고 이 과제를 시작해.
과제 설명과 제공 파일을 먼저 조사하고, 해야 할 일과 제출물을 정리한 다음
필요한 Skill만 골라서 사용해. 아직 큰 구현은 시작하지 말고
성공 기준, 확인할 질문, 검증 방법부터 보여줘.
```

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
