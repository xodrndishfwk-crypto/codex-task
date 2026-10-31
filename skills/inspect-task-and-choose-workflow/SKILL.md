---
name: inspect-task-and-choose-workflow
description: Inspect the task description and provided files, then choose the relevant workflow for data analysis, document review, code changes, app building, or mixed work.
---

# Inspect Task and Choose Workflow

Before implementation, inspect the task README, required deliverables, existing files, and run instructions. Use `python codex-task/kit.py scan .` when a compact file summary helps.

## Classify the task

- Choose data analysis when data files and analytical findings are central.
- Choose code repair or extension when an existing project and change request are central.
- Choose app building when a working interface and user actions are central.
- Choose document processing when file transformation, policy review, or reports are central.
- For mixed work, split it into smaller flows by deliverable importance and risk.

## Common start

1. Use `list-required-results-and-rules` and `prepare-clear-business-questions` to separate facts, questions, and acceptance criteria.
2. Use `plan-small-steps-and-checks` and `plan-time-and-stop-points` to create a verifiable order.
3. Read only the additional instructions needed for the selected workflow.
4. Prefer the existing technology and provided data. Do not expand product scope without a stated requirement.

If classification is unclear, confirm deliverables and success criteria before starting the most expensive implementation.
