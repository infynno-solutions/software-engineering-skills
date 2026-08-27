---
name: write-code-at-the-level-of-intent
description: "Makes code express what the system is trying to do rather than low-level mechanics. Use when an order-processing function is full of raw HTTP calls and serialization details that bury the business rule it is actually implementing. Not when the issue is encapsulating a boundary other code depends on (see encapsulate-implementation-details), when poor naming alone is the problem on an otherwise well-structured routine (see name-for-meaning), or when separating a decision from its mechanism architecturally (see separate-policy-from-details)."
license: MIT
---

# Write Code at the Level of Intent

## Intent

Make source code communicate what the system is trying to accomplish without forcing the reader to reconstruct the design from low-level implementation details.

## Procedure

1. State the behavior in domain or problem terms.
2. Separate the purpose of the operation from the mechanism used to implement it.
3. Prefer names, functions, abstractions, and structure that expose the purpose directly.
4. Hide incidental implementation details behind the smallest useful interface.
5. Re-read the resulting code as a maintainer who does not know the implementation history.

## Decision rules

- Prefer code that describes intent over code that exposes incidental mechanics.
- Use abstractions when they reduce cognitive load or hide details that readers do not need.
- Do not add abstraction merely to rename trivial code or create another layer of indirection.
- Domain terminology is usually preferable to infrastructure terminology when the operation is domain-driven.

## Anti-patterns

- Leaking database, framework, serialization, or transport details into business-level code when they are not part of the business concept.
- Names such as `process`, `handle`, or `doThing` when a more precise intent is available.
- Requiring readers to mentally simulate low-level steps to discover the purpose of a function.

## Exceptions and trade-offs

- Infrastructure code — a driver, a serializer, the framework glue itself — is legitimately expressed in mechanism-level terms; this skill applies to code expressing domain or business intent, not to the plumbing underneath it.
- Introducing a domain vocabulary or abstraction layer has a real cost when the codebase is small or short-lived; don't build a domain model for a five-line script.
- Occasionally a "low-level" detail is exactly what a reader needs to trust the code, such as in a performance-sensitive routine — intent-level language should not hide information the reader genuinely needs.

## Verification

- Can a reader summarize the code's purpose from names and structure?
- Can most implementation details be ignored while understanding the behavior?
- Does the code use the problem domain where appropriate?
- Would changing an implementation detail force unrelated readers to relearn the behavior?
