---
name: encapsulate-what-varies
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Design around change by separating independently varying behavior from the parts of the system that should remain stable.

# When to apply

Use when:

- a conditional changes for multiple implementations;
- requirements explicitly identify alternatives;
- new variants are expected to arrive independently;
- a class repeatedly changes for unrelated algorithmic reasons;
- a volatile dependency is leaking into stable policy.

# Procedure

1. Identify the behavior that varies.
2. Confirm that it varies for a reason different from the surrounding behavior.
3. Identify the stable contract around that variation.
4. Extract the variable behavior behind that contract.
5. Compose or inject the selected implementation.
6. Keep the stable caller independent of the concrete variants.
7. Re-check that the abstraction does not introduce more concepts than the variation justifies.

# Decision rules

- Encapsulate variation that is real, recurring, or explicitly required.
- Do not infer variation solely from imagination.
- Prefer a small stable boundary over a conditional spread through many clients.
- Reuse the same variation boundary when multiple consumers need the same independent behavior.

# Anti-patterns

- "Future-proofing" every branch with speculative interfaces.
- A giant interface containing unrelated variants.
- One class with many flags that select unrelated algorithms.
- Encapsulating something that has no credible independent change pressure.

# Verification

- Can one variant be introduced or replaced without editing every consumer?
- Is the stable contract understandable without knowing the variants?
- Does each variant implement one coherent behavior?
- Did the abstraction reduce change propagation rather than merely move conditionals?

# Source basis

Head First emphasizes that patterns primarily address change and allow parts of a system to vary independently. GoF describes patterns as arrangements of objects that isolate recurring design forces. Clean Architecture connects the same idea to boundaries and separation of things that change for different reasons.
