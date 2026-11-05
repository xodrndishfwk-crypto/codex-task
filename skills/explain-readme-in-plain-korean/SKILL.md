---
name: explain-readme-in-plain-korean
description: Explain a task README and referenced specifications in plain Korean, producing a readable Markdown guide to the purpose, users, concrete workflow, inputs, outputs, requirements, and unresolved questions before implementation.
---

# Explain Task README in Plain Language

Help the user understand the work before discussing how to code it. Read the actual task README and relevant local files it references, following the source priority in `AGENTS.md`. Distinguish the exam task README from this toolkit's README. If the task source is missing or unreadable, identify the missing source and ask for it instead of inventing an assignment.

## Write the explanation

Create `reports/<task-name>/README-이해하기.md` in the task workspace during initial inspection, without a separate request. Link it from the inspection-stage report and in chat. Reuse the task's report directory; preserve user-authored files and use a new path on collision. Update the generated guide when an authoritative answer or source change alters the interpretation, recording the source and change.

Write in approachable Korean, starting with a short overview and then enough detail for someone unfamiliar with the domain:

1. **무엇을 하는 과제인가:** Explain the problem and intended outcome in everyday language, and why the result is useful. State when the purpose is not specified rather than guessing it.
2. **누가 언제 사용하는가:** Identify stated users, their situation, and goals. Explain unfamiliar business terms at first use.
3. **실제로 사용하는 과정:** Walk through one concrete user scenario step by step, showing user action, system processing, and visible result. For analysis or document tasks, follow a representative record from input to deliverable instead of inventing app screens.
4. **입력 → 처리 → 결과:** Map required data/files to business rules and expected outputs. Use a small table or simple text flow when helpful. A conceptual screen outline may explain stated steps, but must not become an invented UI requirement.
5. **반드시 지켜야 할 조건과 제출물:** Preserve mandatory requirements, units, dates, time rules, permissions, exceptions, constraints, and submission formats. Separate required work from explicitly optional work; do not add features to fill gaps.
6. **아직 정해지지 않은 내용:** List consequential ambiguities, missing data, and conflicts with the outcomes they could change. Route them to `prepare-clear-business-questions` and carry their question IDs into the stage report. Ask the user directly when their decision is required.
7. **핵심 용어와 이해 확인:** Briefly explain relevant terms and include a few self-check questions with answers grounded in the source. These support pre-implementation understanding, not predicted post-submission exam answers.

Use source file paths and headings or line locations beside important requirements so the user can check the original. Keep the overview readable before the detail; do not merely reorder README sentences or start with frameworks and code structure.

## Guard against invented clarity

Label illustrative people, numbers, and scenarios as `설명용 예시`; keep them separate from source requirements. If the outcome depends on an unanswered rule, show the alternatives or leave the result unresolved. Do not silently choose optimization priorities, thresholds, weights, or permissions. Distinguish source facts, explanation-only examples, and unanswered questions in ordinary language without certainty labels.

Before saving, compare the guide with the source: retain outcome-changing conditions and exceptions, verify that the scenario follows the stated rules, and ensure examples have not become requirements. Say which referenced material could not be checked. This is a readability and source-consistency review, not evidence that an implementation works.

Hand off to `list-required-results-and-rules` for formal requirement tracking and to the existing planning workflow for implementation. The explanation does not authorize new features or replace the original task instructions. No implementation, external service, network access, image generation, or browser automation is needed to produce it.
