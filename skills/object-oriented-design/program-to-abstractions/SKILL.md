---
name: program-to-abstractions
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Reduce implementation dependencies by expressing collaboration through an abstraction that captures what the consumer actually needs.

# When to apply

Use when:

- multiple implementations can satisfy the same client need;
- infrastructure should be replaceable;
- an algorithm or policy varies independently of its consumer;
- dependency direction is causing unnecessary coupling;
- tests benefit from a stable seam.

# Procedure

1. Identify the client's actual required behavior.
2. Define the smallest meaningful contract for that behavior.
3. Make the consumer depend on the contract.
4. Make concrete implementations satisfy that contract.
5. Put construction/wiring at the appropriate composition boundary.
6. Verify that the abstraction corresponds to a real variation or dependency boundary.

# Decision rules

- Abstract the client-facing behavior, not every concrete class.
- Let the consumer's needs shape the interface.
- Use an abstraction when it reduces meaningful implementation coupling or isolates a genuine point of variation.
- Keep concrete instantiation at a boundary rather than spreading it throughout business logic.

# Anti-patterns

- Interfaces for every class by default.
- "IUserService", "IThingManager", etc. that simply mirror one implementation.
- Abstractions whose names describe implementation technology instead of client behavior.
- Abstracting before there is a meaningful reason for substitution or dependency inversion.

# Verification

A good abstraction should let the consumer:

- remain unaware of concrete implementation details;
- express its intent without construction knowledge;
- accept another implementation without changing its own behavior;
- keep the contract smaller than the implementation.

# Source basis

GoF's "Program to an interface, not an implementation" reduces implementation dependencies. Clean Architecture shows how polymorphism can invert source-code dependencies so higher-level policy does not depend directly on lower-level details.
