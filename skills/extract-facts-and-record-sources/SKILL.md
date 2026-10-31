---
name: extract-facts-and-record-sources
description: 각 대상의 PDF, 표, 문서에서 규칙 판단에 필요한 사실만 추출하고 원본 파일과 페이지 또는 행 위치를 함께 기록할 때 사용한다.
---

# Extract Facts and Record Sources

`rule-checklist`에서 요구하는 정보만 대상별로 추출한다.

- 값, 단위, 날짜, 상태를 원문 표현과 함께 보존한다.
- 모든 값에 파일 경로와 페이지, 표 행, 셀 같은 위치를 연결한다.
- 값이 없으면 `없음`, 읽을 수 없으면 `확인 불가`, 서로 다르면 `충돌`로 구분한다.
- 빈칸을 0이나 `아니오`로 해석하지 않는다.
- 표본 대상을 골라 추출값을 원본과 수동 대조한다.

결과는 `templates/facts-with-sources.md`에 기록한다. 추출과 판정은 분리해 사실을 먼저 고정한다.
