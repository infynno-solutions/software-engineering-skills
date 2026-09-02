---
name: encapsulate-object-creation
description: "Isolates construction knowledge behind Factory Method, Abstract Factory, Builder, or Prototype. Use when call sites instantiate a concrete class directly and that choice must vary by configuration, platform, or runtime context; when construction assembles several parts in order or has many optional parameters; or when instances come from cloning a configured prototype. Not when a constructor already describes the object simply with no meaningful variation, and not for relocating construction to a composition root without a pattern (see separate-collaboration-from-implementation)."
license: MIT
---

# Encapsulate Object Creation

## Intent
Isolate construction knowledge from clients when object creation varies, is complex, or should not leak concrete implementation choices into stable code.

## Procedure
1. Identify clients that currently instantiate concrete variants directly, and note which decision (platform, config, plugin, user choice) drives which concrete type gets created.
2. Determine whether creation varies independently of the client's other logic, or involves complex multi-step assembly that a single constructor call can't express cleanly.
3. Define the narrow creation contract — just what's needed to obtain a correctly built product, not a general-purpose object bag.
4. Move concrete selection/assembly behind the creation boundary (a factory method, an abstract factory, a builder, or a prototype registry).
5. Keep clients dependent on the product abstraction where appropriate, so they can work with whatever concrete type the factory produces without a type check.
6. Verify that the creation boundary does not become a second business-logic layer — it should build objects, not decide what the application does with them.

## Decision rules
- Use Factory Method when a single method needs to vary which concrete product it returns, typically overridden per subclass or configured per call.
- Use Abstract Factory when families of related products must be created consistently together (e.g., a UI toolkit's matching button, checkbox, and window for one platform).
- Use Builder when construction involves many optional parameters or an ordered sequence of steps that a telescoping constructor would make unreadable.
- Use Prototype when new instances are cheaper or more correct to produce by cloning a preconfigured instance than by re-running full construction logic.
- Keep creation policy close to the architectural boundary that actually owns the choice (e.g., app startup/config, not scattered through business logic).

## Anti-patterns
- Factory wrappers built around a single trivial constructor call, adding a class and an interface for no real variation.
- Factories that absorb unrelated business rules (validation, side effects) instead of staying focused on construction.
- A global factory or registry that becomes an untestable service locator, making dependencies implicit and hard to substitute in tests.
- Abstracting creation for a type that has no meaningful variation today and no credible variation on the horizon.

## Exceptions and trade-offs
- Builder adds real ceremony (a separate builder class, a fluent API) that is only worth it once the parameter list or step ordering is genuinely unwieldy; for two or three required parameters, a plain constructor is clearer.
- Abstract Factory's benefit — consistent product families — comes with the cost that every new product type requires updating every concrete factory; if families rarely change together, per-product factories may be simpler.
- Prototype requires objects to support a correct, efficient clone (deep vs. shallow matters); if cloning correctness is hard to guarantee, plain construction may be safer even if slower.

## Verification
- Can clients avoid unnecessary knowledge of concrete product types, working only against the product abstraction?
- Is the construction complexity or variability that motivated the boundary actually isolated there, rather than partially leaking into callers?
- Does the factory/builder remain focused on construction, without picking up unrelated responsibilities over time?
