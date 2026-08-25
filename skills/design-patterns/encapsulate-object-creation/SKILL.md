---
name: encapsulate-object-creation
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Isolate construction knowledge from clients when object creation varies, is complex, or should not leak concrete implementation choices into stable code.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify clients that currently instantiate concrete variants directly.
2. Determine whether creation varies independently or involves complex assembly.
3. Define the narrow creation contract.
4. Move concrete selection/assembly behind a creation boundary.
5. Keep clients dependent on the product abstraction where appropriate.
6. Verify that the creation boundary does not become a second business-logic layer.

# Decision rules

- Use Factory Method, Abstract Factory, Builder, or Prototype when their creation-related forces actually exist.
- Keep creation policy close to the architectural boundary that owns the choice.
- Do not hide simple constructors merely to appear abstract.
- Prefer explicit construction when variation is trivial and stable.

# Anti-patterns

- Factory wrappers around one trivial constructor.
- Factories containing unrelated business rules.
- A global factory becoming an untestable service locator.
- Abstracting creation that has no meaningful variation.

# Verification

- Can clients avoid unnecessary knowledge of concrete products?
- Is construction complexity or variability actually isolated?
- Does the factory remain focused on construction?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
