---
name: compose-and-augment-object-behavior
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Build richer behavior by composing objects rather than creating increasingly large inheritance hierarchies, especially when optional responsibilities should be combined dynamically.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify behavior that can be layered or combined.
2. Define a stable component contract.
3. Compose behavior through objects.
4. Keep each wrapper/decorator focused.
5. For tree-like structures, distinguish leaf and composite behavior through a coherent common contract.
6. Validate the resulting object graph remains understandable.

# Decision rules

- Prefer composition when responsibilities combine independently.
- Decorator is useful for dynamically adding responsibilities while preserving an interface.
- Composite is useful when clients should treat individual objects and compositions uniformly.
- Do not use wrappers if they merely obscure a single direct call.

# Anti-patterns

- Deep decorator chains that are impossible to inspect.
- Composite interfaces with meaningless operations for leaves.
- Wrappers that accidentally change contracts.
- Composition used without documenting important object relationships.

# Verification

- Can each composed responsibility be understood independently?
- Does the composed object preserve the expected contract?
- Is the runtime object graph still debuggable?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
