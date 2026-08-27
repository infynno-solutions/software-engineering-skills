---
name: prefer-composition-for-behavioral-reuse
description: "The default preference for building behavior by holding and delegating to a narrow collaborator rather than subclassing to reuse code. Use when a subclass would exist only to reuse a helper method, behaviors must combine or vary at runtime, or a hierarchy keeps growing to cover new combinations. Not for the substitutability test on a genuine type family (see use-inheritance-only-for-genuine-subtyping), for the named Decorator and Composite structures (see compose-and-augment-object-behavior), or for two independently varying dimensions (see separate-abstraction-from-implementation)."
license: MIT
---

# Prefer Composition for Behavioral Reuse

## Intent

Use composition to build behavior from smaller collaborators instead of inheriting implementation by default.

## Procedure

1. Identify the behavior being reused.
2. Determine whether it can be expressed as a collaborator with a clear contract.
3. Give the owning object a reference to the collaborator.
4. Delegate only the responsibility that belongs to that collaborator.
5. Keep collaborator contracts narrow and coherent.
6. Evaluate whether the added object relationships improve the design enough to justify their cognitive cost.

## Decision rules

- Favor composition when behavior should vary independently or be assembled dynamically.
- Do not use composition mechanically when inheritance is a genuine, stable subtype relationship and is simpler.
- Keep delegation explicit and purposeful.
- Avoid chains of trivial forwarding objects that increase indirection without reducing change or complexity.

## Anti-patterns

- Deep inheritance trees used solely for code reuse.
- Subclasses that inherit behavior they cannot safely use.
- Composition graphs so complex that understanding runtime behavior becomes harder than the inheritance they replaced.
- Delegation merely to obey a slogan without a concrete design benefit.

## Exceptions and trade-offs

- Composition multiplies the number of objects and constructor/wiring parameters; for a truly stable two- or three-level "is-a" hierarchy with no behavioral surprises, plain inheritance is simpler to read and construct.
- Deep delegation chains — an object whose only job is forwarding every call to another — can become harder to trace at runtime than the inheritance tree they replaced. Composition is a means of isolating variation, not an end in itself.
- Language and framework idioms sometimes expect inheritance (extending a base test-case class, framework lifecycle hooks); following the framework's expected extension point is often more pragmatic than composing around it just to avoid `extends`.

## Verification

Check whether:

- behavior can be replaced without changing the host object;
- collaborators have clear interfaces;
- classes remain focused;
- runtime collaboration is still understandable;
- the composition reduces implementation dependency or isolates variation.
