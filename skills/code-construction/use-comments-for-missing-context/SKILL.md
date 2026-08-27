---
name: use-comments-for-missing-context
description: "Uses comments for intent and rationale that code structure cannot convey, not to narrate what the code does. Use for a workaround for a specific third-party bug, a business rule that only makes sense given a regulation or contract term, a security or performance constraint invisible in the code, or a deliberate deviation from the codebase's usual pattern. Not when restructuring would make the same fact self-evident, where the fix is name-for-meaning or write-code-at-the-level-of-intent, and not for decision records and system context docs (see document-decisions-and-system-context)."
license: MIT
---

# Use Comments for Missing Context

## Intent

Use comments and documentation to communicate intent, rationale, constraints, and non-obvious context that cannot be made sufficiently clear through code structure alone.

## Procedure

1. First improve names, structure, and interfaces.
2. Identify information that still cannot be inferred safely from the code.
3. Document why the decision exists, what constraint it satisfies, or what invariant must remain true.
4. Keep the comment adjacent to the behavior it explains.
5. Update or remove comments when the behavior changes.

## Decision rules

- Prefer self-documenting structure for ordinary behavior.
- Comments should add information rather than restate syntax.
- Rationale and constraints are usually more valuable than line-by-line narration.
- Treat stale comments as defects because they create false understanding.

## Anti-patterns

- Comments that merely translate code into English.
- Long comments compensating for a poorly structured function.
- Comments that describe an old implementation after the code changed.
- Hiding a confusing API behind a large usage comment instead of improving the API when improvement is feasible.

## Exceptions and trade-offs

- A comment that merely narrates what the next line does adds maintenance burden with no benefit; only rationale and context comments earn their cost.
- Comments referencing external tickets, RFCs, or incidents can go stale as fast as the systems they describe — prefer linking to a durable record over restating transient details inline.
- Doc-comments that double as generated API documentation face a different audience (external consumers) than an inline implementation comment, and should be held to that audience's bar.

## Verification

- Does the comment answer a question the code cannot answer?
- Is the rationale still true?
- Would changing the implementation leave the comment semantically correct?
- Is the comment shorter than the code change needed to make the same fact obvious, when such a change is practical?
