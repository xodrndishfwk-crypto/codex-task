---
name: define-app-users-screens-and-core-flow
description: Convert app requirements into named users, required screens, screen states, navigation, and one testable end-to-end core user flow before coding.
---

# Define App Users, Screens, and Core Flow

Describe the smallest complete experience that satisfies the task.

- Name the primary user and the goal they must complete.
- List required screens and the purpose of each screen.
- For every screen, define entry conditions, visible information, available actions, next destination, and success feedback.
- Include loading, empty, invalid-input, error, and completed states where relevant.
- Separate required screens from optional polish or ideas not requested by the task.
- Connect each screen and action to a requirement and an observable acceptance check.
- Resolve business ambiguity through `prepare-clear-business-questions` instead of inventing behavior.

Record the result in `templates/app-user-flow-and-screen-plan.md`. Keep the flow small enough to build and verify within the available time.
