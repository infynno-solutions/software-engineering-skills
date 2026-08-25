---
name: write-for-the-maintainer
description: Optimize code for the future engineer who must understand, debug, modify, review, or extend it rather than only for the author completing today's task. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Write for the Maintainer

## Intent

Optimize code for the future engineer who must understand, debug, modify, review, or extend it rather than only for the author completing today's task.

## Apply when

Use this skill for essentially all non-trivial production code, especially code expected to live for years or cross team boundaries.

## Procedure

1. Assume the reader does not know why the current implementation exists.
2. Make intent, contracts, assumptions, and non-obvious constraints discoverable.
3. Prefer stable conventions and predictable structures.
4. Minimize unnecessary coupling and cognitive load.
5. Leave the codebase in a state that makes the next change easier.

## Decision rules

- Readability is an engineering property, not decoration.
- Prefer consistency with the surrounding codebase unless an explicit improvement justifies deviation.
- Optimize for the lifetime cost of understanding and changing the code.
- Do not make code more abstract, generic, or clever solely to impress the author.

## Anti-patterns

- Code optimized only for the original author's familiarity.
- Clever shortcuts that reduce typing while increasing reading cost.
- Leaving known confusion because "it works."
- Ignoring repository conventions without a concrete reason.

## Verification

- Can an engineer unfamiliar with the change understand it from source and nearby documentation?
- Are the important assumptions discoverable?
- Is the code consistent with established local patterns?
- Did the change reduce or increase future maintenance effort?


## Related skills

- CODE-01 Write Code at the Level of Intent
- CODE-02 Name for Meaning
- CODE-12 Use Comments for Missing Context
- CODE-15 Continuously Improve Code Quality
