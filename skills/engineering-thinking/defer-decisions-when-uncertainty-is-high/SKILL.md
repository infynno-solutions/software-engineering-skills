---
name: defer-decisions-when-uncertainty-is-high
description: "Avoids irreversible or expensive commitments while requirements, constraints, or change patterns are still unsettled, preserving options until evidence justifies commitment. Use when a design doc proposes a generic plugin or provider interface with only one concrete provider today, a costly-to-migrate database or message-schema choice is debated before usage patterns are known, or a ticket asks for configurable behavior with no second configuration in sight. Not when data already resolves the uncertainty (see make-evidence-based-engineering-decisions), when the decision is cheap to reverse (see prefer-the-simplest-adequate-solution), or when an old decision needs re-checking (see revisit-decisions-as-context-changes)."
license: MIT
---

# Defer Decisions When Uncertainty Is High

## Intent

Avoid irreversible or expensive commitments when the relevant requirements, constraints, or change patterns are not yet well understood.

The goal is not indecision. The goal is to preserve useful options until evidence justifies commitment.

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

## Exceptions and trade-offs

- Deferral has its own cost — added indirection, an extra seam to maintain, or a slower first delivery. Weigh that against the cost of guessing wrong.
- A decision that is hard to reverse later (public API shape, on-disk data format) may warrant deciding early with an explicit escape hatch rather than open-ended deferral.
- Compliance- or contract-driven requirements are rarely deferrable even under genuine technical uncertainty.
- If the "cheapest way to learn more" turns out to be building the real thing, build it — don't invent a speculative placeholder just to avoid commitment.

## Verification

The agent should be able to state:

- what is uncertain
- why commitment is costly
- what option remains open
- what future information would justify commitment
