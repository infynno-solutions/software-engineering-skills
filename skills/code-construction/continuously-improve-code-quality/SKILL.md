---
name: continuously-improve-code-quality
description: "The ongoing discipline of leaving nearby code better on each change, rather than only shipping the fix. Use when fixing a bug in a function you are already reading closely, when the same duplication or misnamed concept keeps reappearing across unrelated changes, or when a reviewer flags an adjacent problem fixable in the same pass. Not to justify a stand-alone large rewrite disconnected from a real change (see refactor-in-small-safe-steps, separate-feature-work-from-refactoring), and not when the question is whether one function or class is readable in isolation (see name-for-meaning, minimize-function-and-class-complexity)."
license: MIT
---

# Continuously Improve Code Quality

## Intent

Treat every meaningful code change as an opportunity to preserve or improve the codebase's readability, correctness, and maintainability rather than allowing entropy to accumulate.

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

## Exceptions and trade-offs

- Code scheduled for imminent deletion or replacement is usually not worth improving beyond what the current task requires.
- Under incident or hotfix pressure, deliberately deferring improvement — with a tracked follow-up — can be the correct call over risking a larger diff mid-incident.
- Large structural improvements should land as separate, reviewable commits rather than folded into the triggering change, even though both count as "improving quality."

## Verification

- Is the touched code at least as understandable as before?
- Did the change avoid increasing unnecessary coupling or duplication?
- Are behavior changes separated from structural improvements where practical?
- Can reviewers identify the purpose and safety of the change?
