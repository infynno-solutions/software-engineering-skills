---
name: encapsulate-algorithmic-variation
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Separate an algorithm or policy that varies from the context that uses it, so strategies can be selected, replaced, or extended without rewriting the stable context.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify the algorithmic decision point.
2. Determine whether alternative algorithms share a meaningful contract.
3. Define the smallest strategy interface.
4. Implement each algorithm independently.
5. Inject or compose the selected strategy.
6. Keep selection policy separate from algorithm implementation.

# Decision rules

- Use Strategy when algorithm variation is meaningful and the context can stay stable.
- Template Method is useful when the invariant algorithm skeleton should remain in a base abstraction.
- Prefer composition when runtime replacement or low coupling matters.
- Do not create a strategy hierarchy for a single stable algorithm.

# Anti-patterns

- Boolean flags selecting unrelated algorithms.
- Strategy interfaces with methods unrelated to the varying behavior.
- A strategy abstraction that merely renames one existing function call.
- Putting selection logic inside every strategy.

# Verification

- Can the context operate without knowing concrete algorithm details?
- Can a strategy be replaced independently?
- Is the interface smaller than the variation it represents?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
