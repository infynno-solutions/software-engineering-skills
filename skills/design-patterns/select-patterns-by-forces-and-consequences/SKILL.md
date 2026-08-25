---
name: select-patterns-by-forces-and-consequences
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Choose a pattern by comparing the problem's forces, the structure it introduces, and its consequences. Pattern selection is a trade-off, not a popularity contest.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. State the design problem and desired qualities.
2. Identify candidate pattern families.
3. Compare coupling, flexibility, understandability, object count, indirection, and runtime implications.
4. Check whether the pattern solves the dominant force or merely adds machinery.
5. Select the simplest candidate with an acceptable consequence profile.
6. Document why alternatives were rejected when the choice is consequential.

# Decision rules

- Prefer a pattern when it makes the important force easier to manage.
- Evaluate both benefits and costs.
- Treat added indirection and object relationships as real cognitive costs.
- Reconsider the pattern when requirements or constraints change.

# Anti-patterns

- Choosing patterns by familiarity.
- Applying patterns because a codebase already uses them elsewhere.
- Ignoring object count, indirection, or debugging complexity.
- Treating catalog membership as proof of suitability.

# Verification

- Is the dominant force explicit?
- Are meaningful alternatives considered?
- Are consequences acceptable for the codebase's scale and constraints?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
