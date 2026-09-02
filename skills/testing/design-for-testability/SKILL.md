---
name: design-for-testability
description: "Shapes components with deliberate seams so their important behavior can be exercised in isolation, without invasive setup or heavy mocking. Use when a class reaches for its own dependencies via new, statics, or singletons; when a unit test needs many mocks or reflection just to construct the thing under test; or when designing a new module's constructor and public API. Not for the architecture-level version of keeping business rules runnable with no infrastructure (see design-testable-architecture), choosing a test's scope (see choose-the-right-test-scope), or picking doubles (see use-test-doubles-selectively)."
license: MIT
---

# Design for Testability

## Intent
Shape components so their important behavior can be exercised in isolation, through deliberate seams, instead of invasive setup or mocking.

## Procedure
1. Identify the collaborators a unit needs (DB, clock, network, filesystem, global state) and check whether they're reachable only via concrete construction (`new Foo()`, static/singleton calls) inside the code under test.
2. Introduce a seam at the boundary: pass dependencies in (constructor/parameter injection) rather than reaching out for them, so a test can substitute a controlled implementation.
3. Separate pure decision logic from side-effecting orchestration ("calculate what to do" vs "do it") so the decision logic can be tested without touching I/O at all.
4. Keep constructors/functions honest about what they need — no hidden `this.db = Database.getInstance()` — so a reader, and a test, can see every dependency at the call site.
5. Where a language/framework makes injection awkward (static utility, final class, global config), add a thin wrapper/interface at that one boundary rather than reworking the whole module.

## Decision rules
- If a unit test needs more than 2-3 mocked collaborators or reaching into private state to set up, the design — not the test — is the problem; restructure before adding more test scaffolding.
- Prefer constructor/parameter injection over service locators or global singletons for anything a test will need to control (time, randomness, network, persistence).
- Keep the hard-to-test parts (I/O, external calls) at the edges and the easy-to-test parts (business rules) in the middle, so most logic never needs a double at all.
- A class whose public API can't be exercised without touching a database or network has an untestable boundary that should own an interface.

## Anti-patterns
- Reaching for a heavyweight mocking framework to stub out `static` methods or `final` classes instead of introducing an injectable seam.
- Exposing internal state via test-only getters/setters or reflection instead of designing a real, narrow interface.
- Constructors that silently instantiate their own dependencies, forcing every test of that class to drag in the dependency's full dependency graph.
- Adding a "TestableFoo" subclass that overrides methods just to disable production behavior during tests, instead of injecting the behavior directly.

## Exceptions and trade-offs
- Not every collaborator needs to be injectable — pure, stateless utility calls (math, string formatting) gain nothing from being abstracted behind an interface.
- Over-injecting (passing in a dozen fine-grained dependencies) can make production wiring more complex than the testability gain justifies; group related dependencies into a cohesive collaborator instead.
- Framework-managed lifecycles (DI containers, ORM entities) sometimes limit how far injection can go without fighting the framework — accept a thinner seam there rather than a full rewrite.

## Verification
- Confirm the unit under test can be instantiated and exercised in a test with no real network, filesystem, database, or system clock involved, unless that's the thing being tested.
- Check that dependencies are visible in the constructor/function signature, not discovered through globals or static lookups.
- Re-read the test setup: if it's longer or more complex than the assertions, the seam is probably in the wrong place.
