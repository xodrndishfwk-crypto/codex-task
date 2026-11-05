---
name: test-app-screens-inputs-and-navigation
description: Verify an app's required screens, navigation, touch or click actions, form inputs, state changes, mobile layout, failures, and restart behavior without Computer Use.
---

# Test App Screens, Inputs, and Navigation

Map every required user action to an observable check.

- Confirm the documented start command works from a clean local state available in the environment.
- Check that every required screen can be reached and that back, cancel, retry, and completion paths behave as specified.
- Test valid input, blank input, invalid input, repeated actions, and relevant boundary values.
- Verify loading, empty, success, and error states instead of checking only the happy path.
- Check the provided mobile viewport or preview for clipped text, overlapping controls, unreachable actions, and unreadable content.
- Verify important state changes and required persistence after navigation, refresh, or restart when applicable.
- Run available static checks, unit tests, and builds; do not weaken existing tests to pass.
- Use the provided preview and manual observation. Do not use Computer Use or prohibited browser automation.

Record each requirement, action, expected result, actual result, and evidence in `templates/app-screen-and-flow-test-checklist.md`. Report untested behavior and remaining risk explicitly.

## Review structure from the user's perspective

Read the actual task README, confirmed owner answers, and existing user-flow plan before choosing review scenarios. Use the plain-language README guide as an aid, not as a replacement for source requirements. Trace each relevant user goal through its screens, actions, and result; adapt checks to the task rather than impose a layout or new features.

- Check whether users can identify the next action and see the information needed before making a decision.
- Check whether related inputs, explanations, and results are grouped coherently, and whether important results are distinguishable from supporting detail.
- Check whether selected conditions remain visible or readily retrievable so users need not memorize earlier screens or guess which conditions produced a result.
- Check whether labels, progress, completion, empty results, and errors explain the current state and the available next action consistently.
- Where comparison is required, check that alternatives expose the relevant criteria and units consistently. Do not invent ranking priorities or business rules.

Record each finding in the structural-review section of `templates/app-screen-and-flow-test-checklist.md`: source requirement or scenario, location, observation, user impact, and evidence. Distinguish a source-backed requirement violation from a usability improvement suggestion; do not call a preference a requirement or silently redesign the app. Route consequential undefined rules to `prepare-clear-business-questions` and carry user-decision items into the stage report.

State whether evidence comes from code inspection, manual preview, or actual interaction. Code alone does not prove rendered layout or successful interaction; mark unavailable checks as unverified with their remaining risk. This review does not permit Computer Use, prohibited browser automation, or external calls.
