---
name: find-and-fix-code-errors
description: Reproduce a code or test failure, narrow down the cause, apply the smallest relevant fix, and rerun regression checks.
---

# Find and Fix Code Errors

1. Reproduce the failure with the shortest local procedure.
2. Record the expected and actual results exactly.
3. Inspect recent changes, inputs, environment, and boundary conditions.
4. Test one cause hypothesis at a time.
5. Apply the smallest change that directly addresses the confirmed cause.
6. Rerun the reproduction test and relevant regression tests.

Do not upload logs or data to an external service. Do not use remote analysis, web-executed code, or another AI reviewer. If the failure cannot be reproduced, record the environment and unknowns and do not report success.
