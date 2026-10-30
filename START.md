# 여기서 시작

시험에서는 복잡한 파일명을 외울 필요가 없습니다.

## Codex에 보낼 첫 요청

```text
/tmp/codex-task/START.md를 읽고 이 과제를 시작해.
과제 README와 기존 파일을 먼저 조사하고, 과제 유형을 분류한 다음
필요한 지침만 읽어. 아직 큰 구현은 시작하지 말고 요구사항,
실무자에게 물을 질문, 성공 기준, 검증 계획부터 보여줘.
```

## 사람이 기억할 명령

```bash
# 도구 자체 확인
python /tmp/codex-task/kit.py check

# 현재 과제 구조 파악
python /tmp/codex-task/kit.py scan .

# CSV 또는 JSON 데이터 빠른 조사
python /tmp/codex-task/kit.py data 데이터파일.csv
```

명령이 기억나지 않으면 다음만 실행합니다.

```bash
python /tmp/codex-task/kit.py
```

## 과제 유형별 안내

Codex는 `skills/task-router/SKILL.md`를 이용해 먼저 과제를 분류합니다.

| 과제 유형 | 우선 확인 |
|---|---|
| 데이터 분석 | 파일 구조, 행·열, 결측, 중복, 기본 통계, 집계 기준 |
| 코드 수정 | 재현 방법, 기대 결과, 실제 오류, 관련 테스트 |
| 웹 서비스 | 핵심 사용자 흐름, 실행 포트, Browser 동작, 오류 입력 |
| 파일·문서 처리 | 입력 형식, 변환 규칙, 원문 근거, 전후 검증 |
| 복합 과제 | 가장 중요한 제출물과 위험부터 작은 단계로 분리 |

## 공통 안전 규칙

- 과제 README와 최신 공식 안내가 가장 우선입니다.
- 실무자 에이전트에는 업무 맥락을 묻습니다.
- Cofa Helper에는 화면과 제출 방법을 묻습니다.
- 외부 전송, Git Push, 개인 파일 업로드, Astra, Computer Use, 별도 AI/API를 사용하지 않습니다.
- 제출 후 서술형은 AI 없이 본인이 직접 답합니다.
