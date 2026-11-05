---
name: prepare-clear-business-questions
description: Prepare short decision-focused questions for the business-owner agent about success criteria, exceptions, priorities, and data handling.
---

# Prepare Clear Business Questions

Search the task README and existing files before asking. Route interface instructions to Cofa Helper, technical failures to problem reporting, and business context to the business-owner agent.

## Question priority

1. Success criteria and required users.
2. The core flow that must work.
3. Inputs, outputs, exceptions, and data-retention rules.
4. Priorities and scope that may be dropped if time is short.
5. Verification methods and stakeholder quality expectations.

Put one decision in each question. Briefly state realistic options and their impact. Do not ask for information already written in the task. After an answer, link the requirement ID, decision, implementation impact, and verification method in the work log.

## Find consequential ambiguity

Before drafting questions, check whether changing the user, date/day, time, location, state, or permissions changes the applicable rules or result. Look for interacting conditions, exceptions, and boundaries; distinguish missing data from an undefined business rule.

When criteria conflict (for example, travel time, walking distance, and cost), separate mandatory constraints from preferences. Check priority order, weights, and tie handling in the source; do not invent them or assume that "optimal" means nearest, fastest, or cheapest.

Prioritize unresolved interpretations that change recommendations, calculations, eligibility, access, or core screen behavior, especially those blocking the core flow or causing costly rework. For each, show a concrete case where plausible interpretations produce different outcomes. Do not turn low-impact presentation choices into blocking business questions.

## Draft and connect the decision

Draft a question for the business owner with the requirement/question ID, known facts and source, one unresolved decision, realistic options, and the outcome each option changes. Keep proposed assumptions visibly separate from confirmed rules.

Example: "For R-03, eligible routes vary by weekday and departure time. Among routes that meet the required arrival time, should we minimize total travel time or walking distance? The same employee may receive a different stop recommendation."

After the answer, record its source and connect question ID → requirement ID → confirmed decision → implementation rule and affected files → verification case. Define expected results for a normal case and relevant condition changes, conflicts, or boundaries; record actual results after verification. If the answer leaves a consequential ambiguity, draft a focused follow-up before implementing the dependent behavior.

If an answer is delayed, continue only safe, reversible inspection. Do not implement an unanswered assumption as fact.
