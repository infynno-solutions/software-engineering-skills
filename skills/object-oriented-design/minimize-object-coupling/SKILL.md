---
name: minimize-object-coupling
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Keep object collaborations small, explicit, and stable so each object can be understood and changed with limited knowledge of the rest of the system.

# When to apply

Use when:

- an object directly knows many concrete collaborators;
- internal details of one object are required to use another;
- changes propagate through long call chains;
- tests require constructing large object graphs for a small unit;
- objects communicate through shared mutable state.

# Procedure

1. Inventory important collaborators and dependencies.
2. Determine what knowledge each dependency requires.
3. Remove dependencies that are incidental rather than necessary for the responsibility.
4. Replace concrete or representation-level dependencies with narrow contracts when justified.
5. Reduce shared mutable state and hidden ordering assumptions.
6. Keep each collaboration focused on a coherent request.
7. Check the result for over-indirection and excessive plumbing.

# Decision rules

- Prefer small, explicit collaborations over broad object knowledge.
- Reduce coupling when it creates change propagation, cognitive load, or testing difficulty.
- Do not confuse fewer references with lower conceptual coupling; a single dependency can still expose many assumptions.
- Do not eliminate necessary domain relationships merely to achieve a low dependency count.

# Anti-patterns

- Objects reaching through several collaborators to manipulate internal state.
- Shared mutable globals used as an implicit coordination protocol.
- Concrete implementation dependencies spread across consumers.
- A "facade" that merely hides a huge dependency graph without simplifying the underlying contract.

# Verification

- Can an object use its collaborator without knowing its internals?
- Are dependencies visible in the contract or constructor?
- Does a local implementation change avoid forcing broad changes?
- Can the object be tested without recreating unrelated system state?

# Source basis

Code Complete describes loose coupling as reducing overall complexity and making it possible to focus on one thing at a time. GoF explains abstract coupling and composition as mechanisms for reducing implementation dependencies. Head First emphasizes loose coupling through composition. Clean Architecture generalizes coupling control to source-code dependency direction and architectural boundaries.
