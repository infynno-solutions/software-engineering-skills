---
name: separate-abstraction-from-implementation
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Allow an abstraction and its implementation to evolve independently when both dimensions vary, instead of encoding the variation in inheritance or conditional logic.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify two independent axes of variation.
2. Separate the abstraction from the implementation contract.
3. Define the implementation interface.
4. Connect the abstraction to implementations through composition/delegation.
5. Verify each axis can evolve independently.
6. Keep the number of combinations manageable.

# Decision rules

- Bridge is justified by genuinely independent dimensions of variation.
- Prefer composition/delegation when inheritance would couple the axes.
- Use only when the second axis is real enough to justify the abstraction.
- Avoid introducing Bridge merely because inheritance exists.

# Anti-patterns

- Cartesian explosion of subclasses.
- Bridge with only one stable implementation and no credible second axis.
- Abstraction and implementation still changing together despite the supposed separation.

# Verification

- Can either axis change without multiplying subclasses?
- Are both abstractions meaningful?
- Did the bridge reduce dependency coupling rather than add ceremony?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
