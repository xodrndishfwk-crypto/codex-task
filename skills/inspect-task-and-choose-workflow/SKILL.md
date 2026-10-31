---
name: inspect-task-and-choose-workflow
description: 과제 설명과 제공 파일을 조사하고 데이터 분석, 규칙 기반 문서 심사, 코드 수정, 웹 제작 중 알맞은 작업 흐름을 선택할 때 사용한다.
---

# Inspect Task and Choose Workflow

구현 전에 과제 README, 제출물, 기존 파일, 실행 방법을 확인한다. 필요하면 `python codex-task/kit.py scan .`으로 파일 구조를 요약한다.

## 분류

- 데이터 파일과 분석 결과가 중심이면 데이터 분석 흐름
- 기존 코드의 오류나 변경 요청이 중심이면 코드 수정 흐름
- 실행 가능한 화면과 사용자 동작이 중심이면 웹 서비스 흐름
- 입력 파일 변환이나 보고서가 중심이면 파일·문서 처리 흐름
- 둘 이상이면 제출물의 중요도와 위험을 기준으로 작은 흐름으로 나눈다.

## 공통 시작

1. `list-required-results-and-rules`와 `prepare-clear-business-questions`로 사실, 질문, 수용 기준을 정리한다.
2. `plan-small-steps-and-checks`와 `plan-time-and-stop-points`로 검증 가능한 순서를 만든다.
3. 과제 유형에 필요한 지침만 추가로 읽는다.
4. 기존 기술 스택과 제공 데이터를 우선하며 범위를 임의로 확장하지 않는다.

분류가 불명확하면 가장 비싼 구현을 시작하지 말고 제출물과 성공 기준부터 확인한다.
