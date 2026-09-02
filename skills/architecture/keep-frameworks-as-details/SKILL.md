---
name: keep-frameworks-as-details
description: "Confines a web, app, or UI framework to the outer edge so business rules never extend framework base classes or need its runtime to execute. Use when a domain class extends a controller or entity base class, or a framework upgrade is expected to touch business-rule files. Not for persistence coupling (see keep-databases-as-details), the general policy/detail split (see separate-policy-from-details), or top-level folder layout (see let-architecture-scream-the-domain)."
license: MIT
---

# Keep Frameworks as Details

## Intent
Treat the web framework, UI toolkit, or application framework as a replaceable tool plugged in at the system's outer edge, so business rules and use cases never marry themselves to that framework's base classes, lifecycle, or conventions.

## Procedure
1. Identify where business/domain logic currently touches the framework directly: extends a framework base class, uses framework-injected parameters as its primary inputs, relies on framework lifecycle callbacks (`onCreate`, `beforeSave`, request-scoped context) to trigger business behavior, or is annotated in a way that changes its runtime behavior.
2. Extract the actual decision/business behavior into a plain class or function with no framework base class and no framework-specific types in its signature — inputs and outputs should be plain data or domain objects.
3. Keep the framework-touching code (controllers, handlers, framework entity classes, UI components) as a thin adapter: it receives the framework's request/event, translates it into the plain inputs the business logic needs, calls the business logic, and translates the result back into whatever the framework expects.
4. Where the framework requires a base class or annotation for its own mechanics (e.g., a controller must extend a base controller to be routable), confine that requirement to the adapter layer only — never let it apply to the class holding the actual business rule.
5. Check whether framework conventions are shaping business vocabulary (e.g., calling a use case a "Controller," organizing code by the framework's MVC folders instead of by business capability) — if so, that's the framework dictating architecture rather than being a detail plugged into one; see `let-architecture-scream-the-domain` for the structural fix.
6. Verify by asking: could the business logic under review run in a plain test, or in a different framework entirely, without modification? If not, trace what's blocking that and extract it.

## Decision rules
- A business rule or use-case class should be instantiable and callable with no framework runtime present — no servlet container, no dependency-injection container, no UI event loop required just to construct or invoke it.
- If a framework annotation or base class encodes a business decision (e.g., an authorization rule expressed only as a framework security annotation with no equivalent plain check the business logic could enforce itself), that decision has leaked into the framework layer and should be pulled back into policy code that the adapter merely invokes.
- Framework lifecycle hooks (request start/end, component mount/unmount, ORM entity lifecycle events) are acceptable places to *call* business logic from, but not acceptable places to *contain* business logic.
- Prefer the framework's own recommended extension points (middleware, filters, plugins) for cross-cutting framework concerns (auth token parsing, request logging) precisely because those are framework details — don't build a custom system to avoid the framework there. This skill is about protecting business rules, not about avoiding the framework everywhere.

## Anti-patterns
- A "service" or "use case" class that extends a framework base class purely out of habit (copy-pasted from a framework-generated controller template) even though it contains business logic that has nothing to do with HTTP or the framework's request cycle.
- Business validation rules expressed only as framework-specific annotations (e.g., a validation attribute) with no plain function a test could call directly — the rule only exists as framework configuration.
- Organizing the whole codebase's top-level structure around the framework's conventions (`controllers/`, `models/`, `views/` mirroring the framework's generator output) so that finding "what does this system actually do" requires understanding the framework rather than the domain.
- Business logic that reads framework-managed request-scoped state (thread-local, request context) directly instead of receiving its inputs as explicit parameters, making it impossible to call outside a live request.
- Upgrading the framework and discovering business-rule files needed changes because they depended on framework internals that changed, not just adapter code.

## Exceptions and trade-offs
- Some frameworks are pervasive by design (e.g., a UI framework's component model) and fighting every use of a base class is not worth it for pure rendering/presentation code that has no business logic in it — apply this skill to where actual business rules live, not to every framework-touching line.
- Very small applications or scripts where the framework essentially *is* the whole application (a single-purpose CLI tool wrapping one library) may not have enough independent business logic to justify the extraction — judge by whether there's a decision worth testing independently.
- Where the team has explicitly decided to commit long-term to one framework and accepts the coupling risk as a trade-off for development speed, that's a legitimate call — but it should be a stated decision, not an unnoticed default, and revisit it using `design-around-the-system-lifecycle` if the system's expected life grows.

## Verification
- Business-rule/use-case classes have no framework base class and can be constructed and invoked from a plain unit test with no framework runtime started.
- Framework annotations present on business logic (if any) are non-behavioral (documentation-only) rather than ones that change runtime behavior in a way not mirrored by explicit code.
- The adapter/controller layer contains translation logic only, not business decisions.
- A hypothetical framework swap for the adapter layer is traceable to touching only adapters, not the business-rule files underneath.
