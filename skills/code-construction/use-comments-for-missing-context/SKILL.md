---
name: use-comments-for-missing-context
description: "Use comments and documentation to communicate intent, rationale, constraints, and non-obvious context that cannot be made sufficiently clear through code structure alone. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Use Comments for Missing Context

## Intent

Use comments and documentation to communicate intent, rationale, constraints, and non-obvious context that cannot be made sufficiently clear through code structure alone.

## Apply when

Use this skill when code depends on:

- non-obvious business rules
- unusual constraints
- compatibility requirements
- security assumptions
- performance constraints
- deliberate deviations from normal patterns
- external behavior that the code alone cannot explain

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

## Verification

- Does the comment answer a question the code cannot answer?
- Is the rationale still true?
- Would changing the implementation leave the comment semantically correct?
- Is the comment shorter than the code change needed to make the same fact obvious, when such a change is practical?


## Related skills

- CODE-01 Write Code at the Level of Intent
- CODE-02 Name for Meaning
- CODE-11 Write for the Maintainer
