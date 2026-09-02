---
name: simplify-conditionals-and-control-flow
description: "Reduces nested, duplicated, or state-dependent conditionals in existing code to something verifiable by inspection, via guard clauses and consolidation. Use for a method nested three or more levels deep, a boolean expression repeated across many methods of a class, or a type-code switch duplicated at several call sites that grows with every new type. Not when the fix is a full pattern such as Strategy or State (see refactor-toward-patterns-when-justified first), and not for writing clear conditionals in code being authored now (see simplify-conditional-logic)."
license: MIT
---

# Simplify Conditionals and Control Flow

## Intent
Reduce complicated conditionals and state-dependent branching by extracting logic, clarifying predicates, or applying polymorphism where justified.

## Procedure
1. Identify the shape of the complexity: deep nesting, duplicated conditions across branches, a repeated type-code switch, or a boolean expression hard to parse at a glance.
2. For deeply nested conditionals guarding invalid or edge cases, apply guard clauses to flatten the main-path logic to one level.
3. For a large conditional expression, extract it into a well-named predicate function so the condition reads as a sentence, such as `isEligibleForDiscount(order)` instead of the raw boolean expression.
4. For branches that do almost the same thing with a small variation, consolidate duplicate code inside each branch, leaving only the true point of variation different.
5. For a type-code switch repeated at multiple call sites, first check whether polymorphism is justified — if the same switch recurs in three or more places it's likely worth replacing; if it appears once, extracting a named function may be enough.
6. Re-read the flattened or decomposed result and confirm each branch answers one question, not several ANDed together.

## Decision rules
- Prefer guard clauses over nested if/else when the nested branches represent early exits or error cases rather than symmetric alternatives.
- Extract a named predicate whenever a boolean expression combines more than two conditions or mixes `&&`/`||` in a way that requires parentheses to disambiguate.
- Consolidate branches only when they actually express the same rule with a parameterized difference — don't force two genuinely different rules into one branch with an added flag.
- Reach for polymorphism only when the same type-code check recurs across multiple methods or files; a single local switch is often clearest left as a switch.

## Anti-patterns
- Flattening a guard-clause refactor so aggressively that the function has several separate early returns with unrelated error messages, making the actual success path harder to find.
- Extracting a predicate function with a name that just restates the code, such as `isXAndY`, instead of naming the domain concept it represents.
- Replacing a single, rarely-changing switch statement with a full class hierarchy, adding files and indirection for no reduction in real complexity.
- Consolidating two conditional branches that look similar but encode different business rules, silently changing behavior for one of them.

## Exceptions and trade-offs
- A switch statement over a truly closed, stable set of cases, such as the seven days of the week, rarely benefits from polymorphism — the "open for extension" argument for patterns doesn't apply.
- In extremely performance-sensitive code, guard-clause early returns and predicate extraction have no real cost, but polymorphic dispatch may, so weigh that if profiling shows it matters.

## Verification
- Confirm the flattened or decomposed conditional produces identical results to the original for every existing test case, including edge cases at each boundary.
- Confirm nesting depth is reduced without hiding an error case that the original code handled explicitly.
- Confirm any newly extracted predicate function is exercised directly by a test, not only indirectly through the caller.
