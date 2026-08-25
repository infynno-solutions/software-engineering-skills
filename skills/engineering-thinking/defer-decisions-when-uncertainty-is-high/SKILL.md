---
name: defer-decisions-when-uncertainty-is-high
description: Avoid irreversible or expensive commitments when the relevant requirements, constraints, or change patterns are not yet well understood. The goal is not indecision. The goal is to preserve useful options until evidence justifies commitment. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Defer Decisions When Uncertainty Is High

## Intent

Avoid irreversible or expensive commitments when the relevant requirements, constraints, or change patterns are not yet well understood.

The goal is not indecision. The goal is to preserve useful options until evidence justifies commitment.

## Apply when

Use this skill when:

- requirements are unstable
- system scale is uncertain
- future implementation choices are genuinely open
- an abstraction is being proposed mainly for hypothetical reuse
- a technology choice creates significant lock-in

## Procedure

1. Identify the decision that would create commitment.
2. Determine what uncertainty affects that decision.
3. Identify the cheapest way to learn more.
4. Prefer a design that keeps credible alternatives open if learning is cheap and commitment is expensive.
5. Commit once evidence or requirements make the decision meaningful.

## Decision rules

- Defer details that do not need to be decided yet.
- Do not confuse keeping options open with building every option now.
- Use boundaries and abstractions when they preserve important choices at reasonable cost.
- When the uncertainty is low and the cost of delay is high, decide rather than over-engineer the decision process.

## Anti-patterns

- Building plugin architectures for hypothetical providers.
- Introducing generic interfaces with no demonstrated variation.
- Selecting infrastructure solely because it may be needed at unknown future scale.
- Delaying a decision when the required evidence is already sufficient.

## Verification

The agent should be able to state:

- what is uncertain
- why commitment is costly
- what option remains open
- what future information would justify commitment


## Related skills

- ENG-03 Identify the Shape of Change
- ENG-08 Prefer the Simplest Adequate Solution
- ENG-10 Revisit Decisions as Context Changes
- MOD-12 Manage Abstraction Debt
