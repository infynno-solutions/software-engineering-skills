---
name: identify-requirements-and-constraints
description: "Makes the boundaries of a problem explicit, separating what the system must do from environmental constraints and from assumptions that may later change. Use when an acceptance criterion says must be fast or must scale with no number attached, when two quality attributes pull in opposite directions and the design must name which one wins, or when a rate limit, deployment target, or supported browser was assumed but never confirmed. Not when the problem itself is still unclear (see frame-the-problem first), or when requirements are clear and competing designs need comparing (see evaluate-engineering-trade-offs)."
license: MIT
---

# Identify Requirements and Constraints

## Intent

Make the boundaries of an engineering problem explicit before choosing a solution.

The agent should distinguish what the system must do from constraints imposed by the environment and from assumptions that may later change.

## Procedure

Classify information into four buckets:

1. **Required behavior** — what must be true from the user's or system's perspective.
2. **Quality constraints** — performance, reliability, security, maintainability, usability, or similar properties that materially constrain the solution.
3. **Environmental constraints** — language/runtime, deployment model, existing interfaces, organizational constraints, or compatibility requirements.
4. **Assumptions and unknowns** — beliefs that need confirmation or may change.

Then identify conflicts between constraints.

## Decision rules

- Do not promote an assumption into a requirement without evidence.
- Do not optimize one quality attribute while silently violating another important constraint.
- Where requirements conflict, make the trade-off explicit rather than hiding it in implementation details.
- Use the smallest set of constraints necessary to explain the required behavior and acceptable solution space.

## Anti-patterns

- “The existing code does it this way, so the requirement must be that way.”
- Treating implementation constraints as permanent product requirements.
- Ignoring operational or deployment constraints until after design.
- Using vague words such as “fast” or “scalable” without identifying what they mean in context.

## Exceptions and trade-offs

- Not every constraint needs to be surfaced — chasing every conceivable quality attribute for a small change produces an over-specified problem model that nobody reads.
- Where a constraint genuinely cannot be confirmed in the available time, label it an assumption and proceed rather than blocking on it indefinitely.
- Conflicting constraints do not always need to be resolved up front — sometimes surfacing the conflict for the requester to arbitrate is the correct outcome of this step.

## Verification

The agent should produce a concise problem model containing:

- requirements
- important quality attributes
- constraints
- assumptions
- open questions
