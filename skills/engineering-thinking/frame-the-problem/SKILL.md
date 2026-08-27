---
name: frame-the-problem
description: "Establishes the actual problem, desired outcome, and relevant context before an implementation is chosen. Use when a ticket says add a Redis cache here and it is unclear what problem caching solves, when a bug report describes a symptom such as the button is slow that may trace to a different root cause, or when a request names a technology or pattern before the underlying need is stated. Not when the problem is already framed and the open question is which quality attributes bound the solution (see identify-requirements-and-constraints), or when several candidate designs need comparing (see iterate-design-before-committing, evaluate-engineering-trade-offs)."
license: MIT
---

# Frame the Problem

## Intent

Understand the problem, desired outcome, and relevant context before selecting an implementation.

The agent should solve the stated engineering problem rather than prematurely optimizing for a particular implementation, pattern, framework, or technology.

## Procedure

1. State the problem in domain terms.
2. State the desired observable outcome.
3. Identify the affected users, components, workflows, and operational constraints.
4. Separate known facts from assumptions.
5. Identify what is explicitly required versus merely suggested by the current implementation.
6. Identify important unknowns.
7. Only then enumerate candidate solutions.

## Decision rules

- Do not start from a preferred technology and retrofit a problem around it.
- Do not treat an existing implementation detail as a requirement without evidence.
- If the problem definition is unstable, prefer an incremental investigation over a large irreversible design.
- A problem that cannot yet be stated clearly may need exploration before implementation.

## Anti-patterns

- Jumping directly from ticket text to code changes.
- Choosing a pattern because it is familiar rather than because the forces require it.
- Treating the current architecture as the definition of the problem.
- Designing for hypothetical requirements that have not been established.

## Exceptions and trade-offs

- For a genuinely trivial change (a typo fix, a one-line config tweak), full problem framing is wasted motion — apply judgment about scale before invoking the full procedure.
- An incident in progress may require a stabilizing action before the problem is fully framed; frame the problem for the follow-up fix even if the immediate mitigation was reflexive.
- Framing is not the same as gathering every possible fact — stop once the problem, outcome, and material constraints are stated, rather than turning it into open-ended research.

## Verification

Before implementation, the agent should be able to answer:

- What exact problem is being solved?
- What observable result determines success?
- What constraints matter?
- Which assumptions remain uncertain?

If these cannot be answered, continue analysis rather than making a large design commitment.
