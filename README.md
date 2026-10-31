# Public Codex CLI Toolkit

실무형 AI 과제에서 과제를 파악하고, 매뉴얼과 여러 서류를 심사하고, 표 데이터를 분석하고, 코드를 수정하고, 결과를 검증·기록하기 위한 범용 도구 모음입니다. 특정 과제의 정답이나 완성 결과물을 제공하지 않습니다.

## 시험장에서 이것만 기억하세요

```bash
git clone https://github.com/xodrndishfwk-crypto/codex-task.git
python codex-task/kit.py check
```

그다음 Codex에 다음 문장을 요청합니다.

```text
codex-task/AGENTS.md, codex-task/START-HERE.md,
codex-task/WHAT-EACH-TOOL-DOES.md를 읽고 이 과제를 시작해.
```

## 할 수 있는 일

- 과제 파일을 조사하고 필요한 작업 흐름 선택
- 제출물, 업무 규칙, 성공 기준 정리
- 매뉴얼을 대상별로 적용 가능한 규칙표로 변환
- 사람·설비·업체별 서류에서 사실과 출처 추출
- 통과·탈락·확인 필요 판정과 이유 작성
- 여러 파일의 누락·중복·충돌 확인
- CSV·JSON·Excel 데이터 분석과 순위 계산
- 코드 오류 수정과 요구사항별 테스트
- 최종 결과표, 요약, 테스트 보고서, 제출 전 점검

전체 도구의 입력과 결과는 `WHAT-EACH-TOOL-DOES.md`에서 확인할 수 있습니다.

## 안전 경계

- 제공된 Codex만 사용합니다.
- Computer Use와 Astra를 사용하지 않습니다.
- 시험 작업물, 프롬프트, 로그, 소스, 비밀정보를 외부로 전송하지 않습니다.
- 외부 AI/API, 원격 실행, 원격 분석, 자동 업로드를 사용하지 않습니다.
- 공개 자료는 상세 가이드가 허용하는 범위에서만 사용합니다.
- 이 저장소를 시험에서 활용한다면 2차 예선 결과 통지 전까지 공개 상태를 유지합니다.
- 이 저장소의 자료로 과제 결과물을 통째로 대체하지 않습니다.
- MCP는 필수가 아니며, 허용 여부와 데이터 흐름을 확인한 경우에만 선택적으로 사용합니다.

## 폴더 구성

- `AGENTS.md`: 모든 작업에 공통으로 적용할 안전·품질 규칙
- `START-HERE.md`: 시험장에서 처음 읽을 파일
- `WHAT-EACH-TOOL-DOES.md`: 각 Skill의 입력과 결과를 보여주는 메뉴
- `skills/`: 업무 종류별로 Codex가 따를 절차
- `templates/`: 규칙표, 사실표, 판정표, 계획과 테스트 기록 양식
- `kit.py`: 파일 조사, 데이터 점검, 판정표 점검 명령
- `docs/`: 자세한 사용법, 시험 흐름, 허용 범위
- `scripts/`와 `tests/`: 도구 자체의 로컬 검증

## 로컬 명령

```bash
python codex-task/kit.py check
python codex-task/kit.py scan .
python codex-task/kit.py files .
python codex-task/kit.py data data.csv
python codex-task/kit.py decisions decisions.csv
```

## 도구 자체 테스트

```powershell
python scripts/validate_toolkit.py
python -m unittest discover -s tests -v
```

네트워크 연결이나 외부 서비스 없이 동작합니다.

## 공개 전 확인

- 저장소에 시험 자료, 개인정보, 자격증명, 비공개 코드가 없는지 확인합니다.
- 커밋 기록에도 민감정보가 없는지 확인합니다.
- 라이선스와 출처를 확인합니다.
- 실제 시험 PDF 원문과 최신 공지를 다시 대조합니다.

자세한 절차는 `docs/HOW-TO-USE-THIS-TOOLKIT.md`, 사전 점검은 `docs/BEFORE-EXAM-CHECKLIST.md`, 규정은 `docs/ALLOWED-AND-NOT-ALLOWED.md`에 있습니다.

## 라이선스

MIT License. 단, 라이선스는 대회 규정보다 우선하지 않습니다.
