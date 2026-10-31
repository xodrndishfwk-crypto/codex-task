---
name: inspect-app-project-and-run-locally
description: Inspect an existing mobile or web app project, identify its stack and entry points, and prove the original project runs locally before changing code.
---

# Inspect App Project and Run Locally

Establish a working baseline before implementation.

- Read the task README, package manifest, lockfile, configuration, and existing tests.
- Identify the framework, package manager, start command, build command, test command, entry point, routes, and data layer.
- Reuse the installed dependencies and existing project conventions. Do not replace the stack for convenience.
- Run the shortest documented local start or build check without changing product code.
- Record the original result, warnings, failures, local URL or output location, and environment assumptions.
- Distinguish a pre-existing failure from a failure introduced by later changes.

Do not install unrelated tools, send project data outside the environment, use Computer Use, or assume an external API is available. If the original project does not run, reproduce and diagnose that problem before building new features.
