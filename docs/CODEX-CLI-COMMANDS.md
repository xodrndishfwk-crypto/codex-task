# Bash에서 사용하는 Codex 명령어

과제 폴더에서 실행하는 Codex CLI 명령어와 용도를 정리한 참고 문서다. 설치 버전에 따라 지원하는 명령어와 옵션이 다를 수 있으므로 실제 환경에서는 `codex --help`와 각 명령어의 `--help`를 확인한다. 시험에서는 제공된 환경과 공식 지침을 우선한다.

## 기본 명령어

| 명령어 | 용도 |
|---|---|
| `codex` | 현재 폴더에서 대화형 Codex 시작 |
| `codex "요청 내용"` | 첫 요청을 넣고 대화형 Codex 시작 |
| `codex -C /path/to/project` | 지정한 폴더를 작업 위치로 사용 |
| `codex resume` | 이전 대화를 목록에서 골라 이어가기 |
| `codex resume --last` | 가장 최근 대화 이어가기 |
| `codex fork --last` | 최근 대화를 분기해 새 대화로 시작 |
| `codex --help` | 전체 명령어와 옵션 확인 |
| `codex --version` | 설치 버전 확인 |
| `codex resume --help` | 특정 명령어의 자세한 사용법 확인 |

`codex`는 새 대화를 시작하고, `codex resume`는 이전 대화의 맥락을 이어간다.

## 상황에 따라 사용하는 명령어

| 명령어 | 용도 |
|---|---|
| `codex --no-alt-screen` | 터미널 스크롤 기록을 유지하는 방식으로 실행 |
| `codex -s read-only "요청 내용"` | 읽기 전용으로 조사하도록 실행 |
| `codex -i screenshot.png "이 화면을 설명해줘"` | 시작 요청에 로컬 이미지 첨부 |
| `codex review` | 코드 리뷰를 비대화형으로 실행 |
| `codex exec "요청 내용"` | 요청을 비대화형으로 실행하고 종료 |
| `codex login` | 로그인 |
| `codex logout` | 로그아웃 |

읽기 전용 모드에서는 설명 문서나 진행보고 MD를 저장하는 작업도 제한된다. 이 도구 모음의 문서 생성 흐름을 사용할 때는 일반 `codex`로 시작한다.

## 이 도구 모음으로 시작하기

실제 과제 README와 제공 파일이 있는 과제 폴더에서, `codex-task/`를 가져온 상태로 실행한다.

```bash
codex "codex-task/AGENTS.md와 codex-task/START-HERE.md를 읽고 시작해."
```

이미 Codex 대화창이 열려 있다면 Bash에서 다시 실행할 필요 없이 대화창에 다음 문장을 입력한다.

```text
codex-task/AGENTS.md와 codex-task/START-HERE.md를 읽고 시작해.
```

시작 절차는 실제 과제 README 조사, `README-이해하기.md` 작성·제시, 중요 질문과 작업 계획, 조사 보고서 작성으로 연결된다. 구현은 이후 진행 지시에 따라 이어간다.

터미널을 닫았다가 기존 작업으로 돌아오려면 다음 명령어로 대화를 선택한다.

```bash
codex resume
```

## 도움말 확인 예시

```bash
codex --help
codex exec --help
codex review --help
codex resume --help
```

## 출처와 확인 범위

- [공식 Codex CLI 명령어 문서](https://learn.chatgpt.com/docs/cli/reference)
- 2026-11-05 현재 작업 환경의 `codex --help`와 대조했다. 시험 환경의 설치 버전에서 모든 명령어를 실행해 검증한 것은 아니다.
