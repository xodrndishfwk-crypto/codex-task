---
name: build-smallest-working-app-first
description: Implement the smallest end-to-end app flow that a user can actually complete, preserving the existing stack and verifying each small change before adding more features.
---

# Build the Smallest Working App First

Build a vertical slice through the real interface, logic, and data path before adding secondary features.

- Preserve the current framework, project structure, dependency manager, and user changes.
- Start with the highest-priority user action and its success result.
- Make one coherent change at a time and run the nearest available check immediately.
- Use real task data or an explicitly labeled local sample; do not hide unfinished logic behind a polished mock screen.
- Prefer clear, maintainable components and existing design patterns over a large rewrite.
- Handle the minimum required empty, invalid, loading, and failure states for the core flow.
- Do not add authentication, cloud services, analytics, external APIs, or decorative features unless the task explicitly requires them and the environment permits them.

After the core flow works, compare the remaining time and requirements before starting another feature. Record decisions and actual checks in `templates/decisions-and-work-log.md`.
