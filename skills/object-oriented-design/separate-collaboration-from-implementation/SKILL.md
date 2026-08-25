---
name: separate-collaboration-from-implementation
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Make collaboration understandable and stable while allowing implementations to evolve behind the contract.

# When to apply

Use when:

- objects communicate through concrete types;
- callers know construction details they should not need;
- implementation knowledge leaks through parameters or return values;
- collaboration is difficult to test or replace;
- changing one implementation forces unrelated callers to change.

# Procedure

1. Identify the participating responsibilities.
2. Identify the messages/contracts exchanged between them.
3. Remove unnecessary knowledge of construction and representation from callers.
4. Define contracts around required behavior.
5. Choose concrete implementations at a composition boundary.
6. Ensure collaboration remains explicit and easy to trace.

# Decision rules

- Contracts should describe collaboration, not internal storage or framework mechanics.
- Keep object creation separate from object use when that separation reduces coupling.
- Do not hide all collaboration behind dependency injection abstractions; simple direct composition is often enough.
- A boundary is justified when it reduces meaningful implementation dependency or supports independent change/testing.

# Anti-patterns

- Business objects constructing their infrastructure dependencies directly throughout the domain.
- Passing giant framework objects between layers.
- Concrete type checks inside otherwise generic clients.
- Service locators that hide rather than remove dependencies.

# Verification

A reviewer should be able to identify:

- what the collaborator promises;
- why the consumer needs it;
- where the implementation is selected;
- how a different implementation would satisfy the same collaboration.

# Source basis

GoF's abstract coupling and programming-to-interface principles reduce implementation dependencies. Clean Architecture shows how interfaces can change source-code dependency direction while runtime control flow remains unchanged. Head First uses composition and interfaces to make collaborators replaceable.
