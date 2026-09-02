---
name: recognize-recurring-design-forces
description: "Analyzes a design problem for what varies, what must stay stable, and who must know about whom, before any pattern name is chosen. Use at the start of a design conversation when a tangle of conditionals or references leaves the underlying pressure unclear, or when someone proposes let's use a Strategy here before anyone has articulated what actually varies. Not once the force is named and candidates are being compared (see select-patterns-by-forces-and-consequences), nor for auditing a design that already stacks patterns (see compose-patterns-without-pattern-accumulation)."
license: MIT
---

# Recognize Recurring Design Forces

## Intent
Design-pattern use starts with recognizing a recurring design problem and the forces around it, not with searching for a pattern name. Inspect what varies, what must remain stable, who must know about whom, how objects collaborate, and what consequences the current structure creates.

## Procedure
1. Describe the problem in plain language without naming a pattern — what is hard to change, test, or extend right now, and why.
2. Identify the forces and constraints at play: performance, testability, team ownership boundaries, expected future changes.
3. Identify what varies (and how often) versus what should remain stable — this is usually the single most important distinction for choosing any structure.
4. Identify the collaborators involved and the dependency relationships between them: who calls whom, who constructs whom, who needs to be notified of what.
5. Look for a known pattern family only after the forces above are clear enough to state in one or two sentences each.

## Decision rules
- A pattern is justified by a recurring problem and its forces, not by novelty or by wanting to use a pattern.
- Prefer the smallest known structure that addresses the actual forces identified — don't reach for the most powerful pattern that could apply.
- If the problem is not recurring (a one-off case) or the forces are weak (unlikely to matter again), a simpler, more direct design may be better than any pattern.
- Do not force a GoF pattern onto a problem merely because its name or example superficially resembles the situation at hand.

## Anti-patterns
- Pattern-first design: starting from "we should use a Factory here" instead of from the actual construction problem.
- Pattern-name matching without understanding consequences — picking a pattern because the current code resembles a textbook example, not because the forces match.
- Treating a pattern as a finished architecture rather than a partial answer to one recognized force among several.
- Assuming every point of variation in a codebase deserves its own abstraction, regardless of how likely that variation is to actually be exercised.

## Exceptions and trade-offs
- Spending time naming forces explicitly has a cost; for a small, low-stakes, easily-reversible piece of code, it may be faster to just write the direct implementation and revisit if it becomes painful.
- Not every design problem maps cleanly onto a catalog pattern — the honest outcome of this analysis is sometimes "no pattern is needed here," which is a legitimate and valuable result, not a failure to find one.
- Junior engineers may need more explicit prompting to separate "what varies" from "what's just complicated"; complexity alone isn't a force that calls for a pattern.

## Verification
- Can the problem and its forces be stated independently of any pattern name, in language a non-pattern-fluent teammate would understand?
- Is there a clear, stated reason the eventually-chosen structure addresses those specific forces?
- Are the consequences of the chosen structure — added indirection, new abstractions, coupling shifts — made explicit rather than assumed to be net-positive?
