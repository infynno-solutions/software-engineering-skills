---
name: prefer-the-simplest-adequate-solution
description: "Choose a solution that satisfies the actual requirements while introducing as little unnecessary complexity, indirection, and speculative flexibility as practical. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Prefer the Simplest Adequate Solution

## Intent

Choose a solution that satisfies the actual requirements while introducing as little unnecessary complexity, indirection, and speculative flexibility as practical.

## Apply when

Use this skill during:

- design selection
- architecture proposals
- abstraction decisions
- framework selection
- refactoring plans
- reliability improvements

## Procedure

1. Establish the actual requirements and constraints.
2. Identify the simplest design that can satisfy them.
3. List additional machinery introduced by more elaborate alternatives.
4. Keep an elaborate option only when it buys a requirement, meaningful risk reduction, or a justified future-change benefit.

## Decision rules

- Simplicity means fewer unnecessary concepts, not merely fewer lines of code.
- Do not reject necessary complexity simply because it is complicated.
- Do not add flexibility without a credible change driver.
- A simple design that is wrong is not preferable to a more complex design that satisfies a real requirement.

## Anti-patterns

- Abstraction for abstraction's sake.
- Framework-driven architecture.
- Configurability without a known configuration need.
- Premature optimization.
- “Enterprise” layering that increases navigation without isolating meaningful concerns.

## Verification

Ask:

- What requirement justifies each major abstraction or mechanism?
- Can one or more layers be removed without violating a requirement?
- Does the extra machinery reduce total lifecycle cost?


## Related skills

- ENG-04 Manage Essential vs Accidental Complexity
- ENG-05 Evaluate Engineering Trade-offs
- ENG-07 Defer Decisions When Uncertainty Is High
