---
name: represent-state-dependent-behavior-explicitly
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Make behavior that changes with object state explicit when state transitions cause conditionals and duplicated logic to become difficult to understand or extend.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify meaningful states and transitions.
2. Separate state-dependent behavior from invariant behavior.
3. Define the state contract.
4. Move state-specific behavior into explicit state objects when complexity warrants it.
5. Centralize or formalize transitions.
6. Preserve invariants across transitions.

# Decision rules

- Prefer explicit state modeling when state-dependent behavior is substantial or growing.
- Keep state transitions visible and testable.
- Avoid state objects when two or three simple branches remain clearer.
- Ensure invalid transitions are handled deliberately.

# Anti-patterns

- Giant conditional blocks covering all states.
- State classes with no meaningful behavior.
- Hidden transitions scattered across unrelated methods.
- State pattern used where an enum and a small switch are clearer.

# Verification

- Are states and transitions understandable?
- Does adding a state avoid widespread edits?
- Are illegal transitions prevented or handled explicitly?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
