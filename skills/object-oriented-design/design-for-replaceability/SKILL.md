---
name: design-for-replaceability
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Use stable contracts and controlled collaboration boundaries so legitimate implementation changes remain localized.

# When to apply

Consider replaceability when:

- infrastructure vendors may change;
- algorithms have multiple valid implementations;
- a component is expected to evolve independently;
- code needs a test seam because the real implementation is slow or external;
- a current implementation is blocking an important future change.

# Procedure

1. Identify the replacement scenario that matters.
2. Determine what must remain stable for consumers.
3. Define the smallest contract that captures that stable behavior.
4. Move implementation-specific construction behind a boundary.
5. Ensure consumers interact only through the stable contract.
6. Verify replacement is actually possible without leaking type-specific assumptions.
7. Remove unnecessary flexibility if the expected replacement is too speculative to justify the abstraction.

# Decision rules

- Design for replaceability when the cost of future change is significant or the implementation is already volatile.
- A replaceable design still needs a clear default implementation and simple wiring.
- Replaceability should not become an excuse for abstracting every dependency.
- The stable contract must be based on client needs, not on exposing every implementation capability.

# Anti-patterns

- Over-generalized interfaces created only "for testing."
- Multiple abstraction layers around a single stable implementation with no change pressure.
- Contracts that leak concrete framework types.
- Designing for imagined provider changes while known business requirements remain unresolved.

# Verification

Test the design mentally with a realistic replacement:

- Can the implementation be swapped at the composition boundary?
- Do consumers remain unchanged?
- Does the contract still represent the same conceptual capability?
- Is the replacement simpler than rewriting every consumer?

# Source basis

GoF's interface-oriented design reduces implementation dependencies and supports substitution. Head First treats independent variation and composition as central design concerns. Clean Architecture uses dependency inversion and boundaries to keep volatile details replaceable. Refactoring supplies the evolutionary perspective: introduce and strengthen such boundaries as real change pressure appears.
