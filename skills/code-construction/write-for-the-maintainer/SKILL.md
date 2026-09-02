---
name: write-for-the-maintainer
description: "The umbrella judgment call for optimizing code for the future engineer who must read, debug, or extend it. Use when choosing between an obscure one-liner and a few clearer lines, or when deciding whether to follow local convention or a technically nicer pattern that would stand out from everything around it. When the concrete lever is naming, comments, or structural cohesion, the narrower skills (name-for-meaning, use-comments-for-missing-context, design-cohesive-functions, design-cohesive-classes) are more actionable; reach for this one to weigh the overall trade-off."
license: MIT
---

# Write for the Maintainer

## Intent

Optimize code for the future engineer who must understand, debug, modify, review, or extend it rather than only for the author completing today's task.

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

## Exceptions and trade-offs

- A genuine one-off script or throwaway spike does not warrant the same investment — judge by expected lifetime and audience, not as a universal rule.
- Matching local convention sometimes conflicts with an objectively better pattern; prefer consistency unless the deviation is clearly justified and documented.
- Optimizing purely for a hypothetical future maintainer can itself produce speculative complexity — the standard is a competent engineer unfamiliar with today's context, not defense against every imaginable future need.

## Verification

- Can an engineer unfamiliar with the change understand it from source and nearby documentation?
- Are the important assumptions discoverable?
- Is the code consistent with established local patterns?
- Did the change reduce or increase future maintenance effort?
