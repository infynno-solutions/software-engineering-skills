---
name: separate-collaboration-from-implementation
description: "Keeps the messages objects exchange free of construction details and internal representation, including by relocating construction to a factory or composition root. Use when a caller must construct its own collaborator, a concrete framework or domain object is threaded through several layers just to reach where it is needed, or implementation knowledge leaks through parameters and return values. Not when the fix is naming an explicit contract type (see program-to-abstractions), hiding one object's own fields (see encapsulate-representation), or deciding whether a dependency is worth a swap boundary (see design-for-replaceability)."
license: MIT
---

# Separate Collaboration from Implementation

## Intent

Make collaboration understandable and stable while allowing implementations to evolve behind the contract.

## Procedure

1. Identify the participating responsibilities.
2. Identify the messages/contracts exchanged between them.
3. Remove unnecessary knowledge of construction and representation from callers.
4. Define contracts around required behavior.
5. Choose concrete implementations at a composition boundary.
6. Ensure collaboration remains explicit and easy to trace.

## Decision rules

- Contracts should describe collaboration, not internal storage or framework mechanics.
- Keep object creation separate from object use when that separation reduces coupling.
- Do not hide all collaboration behind dependency injection abstractions; simple direct composition is often enough.
- A boundary is justified when it reduces meaningful implementation dependency or supports independent change/testing.

## Anti-patterns

- Business objects constructing their infrastructure dependencies directly throughout the domain.
- Passing giant framework objects between layers.
- Concrete type checks inside otherwise generic clients.
- Service locators that hide rather than remove dependencies.

## Exceptions and trade-offs

- Introducing a composition root or factory for every collaboration is overkill in a small script or single-use tool with exactly one wiring path that will never change; direct construction is simpler and clearer there.
- Passing a framework object one layer deep — an HTTP request into a thin controller method, say — is often fine. The anti-pattern is threading it through several layers of otherwise-generic business logic, not any framework object touching the code at all.
- Service locators are flagged as an anti-pattern because they hide the dependency graph, but a well-scoped, explicit DI container configured at the composition root is a legitimate, different mechanism aimed at the same goal — don't conflate the two.

## Verification

A reviewer should be able to identify:

- what the collaborator promises;
- why the consumer needs it;
- where the implementation is selected;
- how a different implementation would satisfy the same collaboration.
