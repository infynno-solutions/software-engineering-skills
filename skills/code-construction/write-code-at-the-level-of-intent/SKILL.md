---
name: write-code-at-the-level-of-intent
description: Make source code communicate what the system is trying to accomplish without forcing the reader to reconstruct the design from low-level implementation details. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Write Code at the Level of Intent

## Intent

Make source code communicate what the system is trying to accomplish without forcing the reader to reconstruct the design from low-level implementation details.

## Apply when

Use this skill when:

- implementing new behavior
- reviewing an unfamiliar function or class
- translating a design into code
- choosing between a domain-level abstraction and a low-level mechanism
- deciding whether extraction or naming would improve readability

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

## Verification

- Can a reader summarize the code's purpose from names and structure?
- Can most implementation details be ignored while understanding the behavior?
- Does the code use the problem domain where appropriate?
- Would changing an implementation detail force unrelated readers to relearn the behavior?


## Related skills

- CODE-02 Name for Meaning
- CODE-10 Encapsulate Implementation Details
- CODE-11 Write for the Maintainer
- CODE-05 Minimize Function and Class Complexity
