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
