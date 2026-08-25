---
name: continuously-improve-code-quality
description: "Treat every meaningful code change as an opportunity to preserve or improve the codebase's readability, correctness, and maintainability rather than allowing entropy to accumulate. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Continuously Improve Code Quality

## Intent

Treat every meaningful code change as an opportunity to preserve or improve the codebase's readability, correctness, and maintainability rather than allowing entropy to accumulate.

## Apply when

Use this skill when:

- adding a feature
- fixing a defect
- changing an API
- touching confusing code
- addressing a review finding
- performing routine maintenance

## Procedure

1. Understand the existing code before modifying it.
2. Make the smallest change that solves the current problem while preserving clarity.
3. Remove nearby accidental complexity when it is safe and directly relevant.
4. Keep the change behaviorally controlled and verifiable.
5. Avoid leaving newly introduced duplication, unclear names, dead code, or hidden coupling.
6. When a larger improvement is necessary, separate it into reviewable, verifiable increments.

## Decision rules

- Prefer opportunistic improvement over allowing known problems to spread, but keep unrelated cleanup from obscuring the primary change.
- Refactoring should preserve observable behavior unless the task explicitly changes behavior.
- Do not use "cleanup" as justification for uncontrolled scope expansion.
- Code quality is a long-term engineering concern, not a final polishing stage.

## Anti-patterns

- "We'll clean it up later" when the current change would make the problem materially worse.
- Combining unrelated formatting, architecture, and feature changes into one opaque patch.
- Leaving obvious defects in code that is already being modified without assessing the risk of improvement.

## Verification

- Is the touched code at least as understandable as before?
- Did the change avoid increasing unnecessary coupling or duplication?
- Are behavior changes separated from structural improvements where practical?
- Can reviewers identify the purpose and safety of the change?


## Related skills

- ENG-10 Revisit Decisions as Context Changes
- CODE-05 Minimize Function and Class Complexity
- CODE-11 Write for the Maintainer
- REFACTOR-01 Refactor in Small Steps
