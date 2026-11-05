---
name: write-result-and-test-report
description: Maintain stage progress reports and a final reproducible report covering implemented scope, user decisions, actual tests, and limitations.
---

# Write Result and Test Report

Enable a reviewer to reproduce execution and verification using only the workspace.

- Purpose and implemented scope.
- Prerequisites and local run commands.
- Important files and design decisions.
- Tests actually performed and their actual results.
- Known limitations, unfinished work, and needs-review items.
- Public sources and licenses used.

Do not claim a test that was not run or a feature that does not exist. Exclude secrets, personal data, full exam conversations, and unnecessary logs. Use external links only for necessary public sources.

## Maintain stage reports

Apply this procedure during work as well as at completion, following `AGENTS.md`. Use `templates/stage-progress-report.md` for a separate file per planned stage. Update it when the stage ends or a user decision or its resolution changes, and link the saved file in chat. On interruption, record the current state without claiming completion.

Summarize work, changed files, actual verification, and remaining work. Carry forward only issues that require the user's decision or confirmation, with stable question IDs and their status; preserve earlier answers and evidence links. Do not list routine troubles resolved independently. Keep necessary reproduction details in the existing work-log and test-evidence records.

Use the final stage file to consolidate implemented scope, run instructions, actual tests, limitations, and the final status of every important question, including unresolved impacts. Link earlier stage files instead of copying all logs.
