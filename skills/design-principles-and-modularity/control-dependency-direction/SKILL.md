---
name: control-dependency-direction
description: "Decides which way dependency arrows point between modules, packages, and whole architectural components, so volatile details (UI, database, framework) depend on stable business-rule policy and never the reverse. Use when defining which components may import which, choosing which package owns an interface shared by two others, reviewing an import from domain code into a framework or adapter, or tracing a change that rippled upward from infrastructure into business logic. Not for deciding where the boundary itself sits (see identify-and-place-architectural-boundaries), existing cycles (see prevent-dependency-cycles), the technique of placing the interface on the policy side and injecting the concrete (see invert-dependencies-around-stable-policy), or one class depending on a concrete collaborator (see program-to-abstractions)."
license: MIT
---

# Control Dependency Direction

## Intent
Treat dependency arrows as a design tool at every scale — between classes, packages, and whole components — and ensure they point from volatile, detail-heavy code toward stable, abstract policy, so that changing a detail never forces a change to the business rules that use it.

## Procedure
1. Draw (or find) the current dependency graph for the area under review. Mark each component as either policy (business rules, use cases) or detail (I/O, framework, persistence, UI, external service), and mark which are volatile (change often) versus stable (change rarely).
2. For each edge in the graph, check its direction: it should point from detail toward policy, or between details, never from policy toward a specific detail implementation.
3. Where policy needs something a detail provides (e.g., use-case code needs to persist data), define an interface owned by the policy side, expressed in the policy's own vocabulary (`OrderRepository.save(order)`, not `SqlConnection.execute(sql)`). The detail component implements that interface.
4. Wire the concrete implementation to the interface at the outermost layer (composition root / entry point / dependency-injection configuration), not inside the policy code.
5. Verify the fix by checking that the policy component's source no longer imports anything from the detail component's package/namespace — only the reverse, or a shared abstraction package that both depend on.
6. Re-run or trace a build/compile-dependency check (language-appropriate: import graph, module graph, architecture-fitness test) to confirm no accidental backward edge was left behind.

## Decision rules
- A dependency should point from the component more likely to change toward the component less likely to change, not the reverse.
- If component A's source imports concrete types from component B, and B is a volatile detail while A expresses business policy, the dependency is backwards — invert it with an interface owned by A.
- An interface used to invert a dependency belongs in the same component as the client that calls it (the policy side), not in the component that implements it.
- Two components that are both details (e.g., two different infrastructure adapters) may depend on each other directly; inversion is specifically about policy-to-detail edges.
- Prefer one inversion point per genuinely volatile dependency, not one per class — inverting every internal collaborator turns useful abstraction into needless indirection (see Anti-patterns).
- The direction of the dependency arrow, not the direction of the runtime control flow, is what this skill governs — control can still flow from policy into the detail's implementation at runtime through the interface.
- Treat a dependency edge as a commitment to shield the dependent from the depended-on's changes, not as a fact you merely accept because the code compiles that way.

## Anti-patterns
- A use-case or domain class that directly constructs or calls a concrete database client, HTTP client, or framework class instead of depending on an interface it owns.
- An interface defined in the detail component ("the database module's interface") that the policy component must import and conform to — this keeps the policy dependent on the detail's vocabulary even though it looks abstract.
- Wrapping every single class, including other policy classes, behind an interface "for consistency," producing a maze of one-implementation interfaces that add indirection without inverting anything meaningful.
- Doing the inversion only in method signatures while the constructor still `new`s up the concrete detail directly, so the compile-time dependency is unchanged even though it looks abstracted.
- Placing the wiring/composition code inside a component that is itself supposed to be stable policy, making that component depend on every detail it wires.
- Optimizing the diagram (arrow direction on paper) instead of actual change propagation behavior.
- Creating interface-only dependencies that still leak implementation details through parameter or return types.

## Exceptions and trade-offs
- Language/runtime data structures and standard-library types are not "details" in this sense — depending on the language's own collections or primitives is fine.
- A dependency direction is useful only insofar as it supports real lifecycle and change goals; don't invert a direction with no observed volatility difference. For a small script or a component with a genuinely single, unchanging implementation of a dependency, introducing an interface purely for inversion can be premature abstraction.
- Within a single volatile component, its internal parts can depend on each other freely — the discipline matters at component boundaries, not every internal call.
- Some frameworks require policy classes to extend a base class or carry an annotation to function at all; where that's unavoidable, isolate it to the thinnest possible adapter layer rather than treating it as acceptable throughout — see `keep-frameworks-as-details`.

## Verification
- The policy component's import/dependency list contains no concrete detail types; only interfaces it owns, plus other policy code.
- Every interface used for inversion is defined in (or owned by) the policy side, not the detail side.
- Redraw the dependency graph after the change and confirm arrows now flow from volatile toward stable, not the reverse.
- Swapping the concrete detail implementation (e.g., replacing the database or an external client) requires touching only the detail component and the wiring code, not the policy code.
- Confirm no new edge exists only to satisfy a compiler/import mechanism rather than a real architectural relationship.
- An automated dependency-direction check (import-linter, architecture test, module boundary tool) passes, if the project has one; if not, note this as a gap.
