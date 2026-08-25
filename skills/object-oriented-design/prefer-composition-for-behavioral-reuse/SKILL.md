---
name: prefer-composition-for-behavioral-reuse
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Use composition to build behavior from smaller collaborators instead of inheriting implementation by default.

# When to apply

Prefer composition when:

- behavior needs to vary independently;
- multiple behaviors need to be combined;
- runtime substitution is useful;
- inheritance exposes implementation details;
- subclass hierarchies are growing or becoming rigid.

# Procedure

1. Identify the behavior being reused.
2. Determine whether it can be expressed as a collaborator with a clear contract.
3. Give the owning object a reference to the collaborator.
4. Delegate only the responsibility that belongs to that collaborator.
5. Keep collaborator contracts narrow and coherent.
6. Evaluate whether the added object relationships improve the design enough to justify their cognitive cost.

# Decision rules

- Favor composition when behavior should vary independently or be assembled dynamically.
- Do not use composition mechanically when inheritance is a genuine, stable subtype relationship and is simpler.
- Keep delegation explicit and purposeful.
- Avoid chains of trivial forwarding objects that increase indirection without reducing change or complexity.

# Anti-patterns

- Deep inheritance trees used solely for code reuse.
- Subclasses that inherit behavior they cannot safely use.
- Composition graphs so complex that understanding runtime behavior becomes harder than the inheritance they replaced.
- Delegation merely to obey a slogan without a concrete design benefit.

# Verification

Check whether:

- behavior can be replaced without changing the host object;
- collaborators have clear interfaces;
- classes remain focused;
- runtime collaboration is still understandable;
- the composition reduces implementation dependency or isolates variation.

# Source basis

GoF explicitly contrasts white-box inheritance with black-box composition and warns that inheritance can expose implementation details. It recommends favoring object composition over class inheritance, while also noting that composition increases runtime interrelationships and should simplify more than it complicates. Head First reinforces composition as a practical way to vary behavior at runtime.
