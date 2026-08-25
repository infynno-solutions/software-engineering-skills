---
name: compose-patterns-without-pattern-accumulation
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Use multiple patterns as cooperating structures when they address distinct forces, but avoid accumulating patterns until the design becomes more abstract and less understandable than the original problem requires.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Evaluate each pattern independently against a real force.
2. Identify interactions between patterns and shared abstractions.
3. Check whether the combination creates cycles, unnecessary indirection, or duplicated concepts.
4. Remove patterns whose forces are no longer present.
5. Prefer a dense, coherent design over a catalog of unrelated pattern instances.

# Decision rules

- Patterns can compose and reinforce one another.
- A combination is justified only when each participating pattern addresses a real force.
- Reassess the combined design after requirements change.
- The resulting system should be easier to understand and change than the pre-pattern design.

# Anti-patterns

- Pattern soup.
- Naming every class after a pattern.
- Combining patterns because the catalog says they can interact.
- Preserving obsolete abstractions because they were once justified.

# Verification

- Can each pattern's purpose be stated independently?
- Does the combination reduce coupling or change amplification?
- Is the final design simpler to reason about than the alternatives?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
