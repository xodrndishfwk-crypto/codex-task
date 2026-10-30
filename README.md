# Public Codex CLI Toolkit

실무형 AI 과제에서 요구사항을 확인하고, 계획하고, 구현하고, 검증하고, 기록하기 위한 범용 Codex CLI 도구 모음입니다. 특정 과제의 정답이나 완성 결과물을 제공하지 않습니다.

## 안전 경계

- 제공된 Codex만 사용합니다.
- Computer Use와 Astra를 사용하지 않습니다.
- 시험 작업물, 프롬프트, 로그, 소스, 비밀정보를 외부로 전송하지 않습니다.
- 외부 AI/API, 원격 실행, 원격 분석, 자동 업로드를 사용하지 않습니다.
- 공개 자료는 상세 가이드가 허용하는 범위에서만 사용합니다.
- 이 저장소를 시험에서 활용한다면 2차 예선 결과 통지 전까지 공개 상태를 유지합니다.
- 이 저장소의 자료로 과제 결과물을 통째로 대체하지 않습니다.
- MCP는 필수가 아니며, 허용 여부와 데이터 흐름을 확인한 경우에만 선택적으로 사용합니다.

## 구성

```text
.
|-- AGENTS.md
|-- skills/
|   |-- requirements/SKILL.md
|   |-- planning/SKILL.md
|   |-- debugging/SKILL.md
|   |-- testing/SKILL.md
|   |-- documentation/SKILL.md
|   |-- stakeholder-interview/SKILL.md
|   |-- timeboxed-execution/SKILL.md
|   `-- final-defense/SKILL.md
|-- templates/
|   |-- requirements.md
|   |-- plan.md
|   |-- validation-report.md
|   |-- submission-checklist.md
|   |-- worklog.md
|   `-- final-defense-notes.md
|-- scripts/
|   `-- validate_toolkit.py
|-- tests/
|   `-- test_validate_toolkit.py
`-- docs/
    |-- USAGE.md
    |-- EXAM-STRATEGY.md
    |-- PRETRIAL-CHECKLIST.md
    |-- ALLOWED-USE-REVIEW.md
    `-- MCP-OPTIONAL.md
```

## 빠른 시작

1. 저장소를 공개 상태로 준비하고 시험 규정의 허용 범위를 다시 확인합니다.
2. 과제 작업 공간에 필요한 파일만 복사하거나 공개 저장소에서 허용된 방식으로 가져옵니다.
3. Codex에 `AGENTS.md`를 읽고 따르도록 요청합니다.
4. `templates/requirements.md`로 사실, 가정, 질문, 수용 기준을 구분합니다.
5. 필요한 Skill만 사용해 계획, 구현, 디버깅, 테스트, 문서화를 진행합니다.
6. `worklog.md`에 본인이 내린 결정과 검증 근거를 짧게 남깁니다.
7. 로컬에서 검증합니다.

```powershell
python scripts/validate_toolkit.py
python -m unittest discover -s tests -v
```

네트워크 연결이나 외부 서비스 없이 동작합니다.

## 권장 프롬프트

```text
AGENTS.md와 관련 SKILL.md를 먼저 읽어라. 과제 원문을 사실의 기준으로 삼고,
모호한 요구사항은 업무 담당자에게 물을 질문으로 분리하라. 외부 전송,
Computer Use, Astra, 제3자 AI/API는 사용하지 마라. 작은 단계로 구현하고
각 단계의 로컬 검증 결과와 남은 한계를 기록하라.
```

## 공개 전 확인

- 저장소에 시험 자료, 개인정보, 자격증명, 비공개 코드가 없는지 확인합니다.
- 커밋 기록에도 민감정보가 없는지 확인합니다.
- 라이선스와 출처를 확인합니다.
- 실제 시험 PDF 원문과 최신 공지를 다시 대조합니다.

세부 절차는 `docs/USAGE.md`, 사전 점검은 `docs/PRETRIAL-CHECKLIST.md`, 규정 해석과 확인 필요 사항은 `docs/ALLOWED-USE-REVIEW.md`에 있습니다.

## 라이선스

MIT License. 단, 라이선스는 대회 규정보다 우선하지 않습니다.
