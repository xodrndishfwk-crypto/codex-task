---
name: test-results-against-requirements
description: Verify that the completed result satisfies every requirement and acceptance criterion using local tests and manual checks, and record evidence.
---

# Test Results Against Requirements

Map at least one verification method to every requirement.

- Run fast static checks and unit tests first.
- Check the core user flow, invalid inputs, and boundary conditions.
- Do not delete or weaken existing tests to make them pass.
- Record commands, actual results, failure counts, skipped checks, and reasons.
- Prefer verification that is reproducible without external network access.
- Do not use browser automation or Computer Use.

When a test is impossible, record substitute evidence and the remaining risk in `templates/test-results-and-evidence.md`.
