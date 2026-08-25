---
name: identify-requirements-and-constraints
description: "Make the boundaries of an engineering problem explicit before choosing a solution. The agent should distinguish what the system must do from constraints imposed by the environment and from assumptions that may later change. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Identify Requirements and Constraints

## Intent

Make the boundaries of an engineering problem explicit before choosing a solution.

The agent should distinguish what the system must do from constraints imposed by the environment and from assumptions that may later change.

## Apply when

Use this skill when:

- a task has incomplete or conflicting requirements
- an implementation choice depends on performance, reliability, deployment, compatibility, or team constraints
- a design needs to balance several quality attributes
- a requirement may be inferred from existing behavior rather than explicitly stated

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

## Verification

The agent should produce a concise problem model containing:

- requirements
- important quality attributes
- constraints
- assumptions
- open questions


## Related skills

- ENG-01 Frame the Problem Before Designing the Solution
- ENG-05 Evaluate Engineering Trade-offs
- ENG-07 Defer Decisions When Uncertainty Is High
