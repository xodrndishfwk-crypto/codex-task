---
name: plan-small-steps-and-checks
description: Break confirmed requirements into small work steps and define the expected result and local verification method for every step.
---

# Plan Small Steps and Checks

Order the plan by verifiable outcomes rather than by vague implementation phases.

- For every step, state the files or area to change, expected result, and command or observation that will verify it.
- Resolve high-impact uncertainty early.
- Preserve the existing structure and user changes.
- Do not depend on network access, external transmission, Computer Use, Astra, or another AI or API.
- Prefer a plan that still works without MCP.
- Before deletion, large rewrites, or data conversion, check impact and recovery options.

Use `templates/step-by-step-work-plan.md`. Update both the plan and its evidence when new facts are discovered.

## Stage reports

Follow the stage-report rules in `AGENTS.md` without waiting for a separate reporting request. Reuse the inspection report already started for this task. Give each remaining verifiable stage a stable number, name, completion criterion, and report path under `reports/<task-name>/`; do not create a report per command. Use `templates/stage-progress-report.md` for each stage and reserve the final stage for the consolidated result.

Save the current stage report before moving to the next stage, including actual checks and the latest state of carried-forward question IDs. A decision that requires the user's answer blocks dependent behavior, not unrelated work; a stage with no such decision needs no extra approval.
