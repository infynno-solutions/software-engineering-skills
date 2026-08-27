---
name: select-patterns-by-forces-and-consequences
description: "Compares two or more candidate patterns for an already-identified force by the coupling, object count, indirection, and runtime cost each introduces, rather than by familiarity or precedent. Use when choosing between Strategy and Template Method for a family of similar algorithms, or between Proxy and Facade for simplified or controlled access to something complex. Not for the earlier step of naming the force (see recognize-recurring-design-forces), auditing a design that already combines patterns (see compose-patterns-without-pattern-accumulation), or judging whether existing code has earned a pattern yet (see refactor-toward-patterns-when-justified)."
license: MIT
---

# Select Patterns by Forces and Consequences

## Intent
Choose a pattern by comparing the problem's forces, the structure it introduces, and its consequences. Pattern selection is a trade-off, not a popularity contest.

## Procedure
1. State the design problem and the desired qualities plainly: what should get easier (extensibility, testability, decoupling) and what constraints must hold (performance, team size, existing conventions).
2. Identify candidate pattern families that plausibly address the stated force — usually two or three, not the whole catalog.
3. Compare them on concrete axes: coupling introduced, flexibility gained, understandability for the team, object/class count, added indirection, and runtime implications (extra allocations, virtual dispatch, memory).
4. Check whether each candidate solves the dominant force identified in step 1, or merely adds machinery that looks appropriate without addressing it.
5. Select the simplest candidate with an acceptable consequence profile — not the most powerful or most "textbook-correct" one.
6. Document why alternatives were rejected when the choice is consequential enough that a future reader will wonder why the road not taken wasn't taken.

## Decision rules
- Prefer a pattern when it makes the specific, already-identified dominant force easier to manage — not because it's applicable in general.
- Evaluate both benefits and costs of each candidate explicitly; a pattern with a real benefit can still be the wrong choice if its cost (e.g., a new abstraction layer for a two-person team) outweighs it.
- Treat added indirection and new object relationships as real, non-free cognitive costs — every additional class or hop is something a future reader must hold in their head.
- Reconsider the pattern choice when requirements or constraints change; a comparison done a year ago may no longer favor the same candidate.

## Anti-patterns
- Choosing a pattern by familiarity — "I know Factory well, so I'll use Factory" — rather than by fit to the stated force.
- Applying a pattern because the codebase already uses it elsewhere, without checking that this instance shares the same force.
- Ignoring object count, indirection, or debugging complexity when comparing candidates, focusing only on theoretical flexibility.
- Treating catalog membership (it's in the GoF book, it's well-known) as proof of suitability for the case at hand.

## Exceptions and trade-offs
- When two candidates are genuinely close in fit, team familiarity is a legitimate tie-breaker — consistency with what the team already knows well can outweigh a marginal theoretical advantage.
- Runtime cost comparisons matter far more in hot paths (tight loops, high-throughput services) than in rarely-executed configuration or startup code; scale the rigor of the comparison to where the code actually runs.
- Documenting rejected alternatives has diminishing returns for low-stakes, easily-reversible choices — reserve written rationale for decisions that would be expensive to revisit later.

## Verification
- Is the dominant force the choice is meant to address stated explicitly, not just implied?
- Were meaningful alternatives actually considered and compared on concrete axes, not just the first pattern that came to mind?
- Are the consequences of the chosen pattern acceptable for this codebase's actual scale, team size, and constraints — not just acceptable in the abstract?
