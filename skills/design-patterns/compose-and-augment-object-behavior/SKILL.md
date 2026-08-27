---
name: compose-and-augment-object-behavior
description: "Builds richer or optional behavior by composing objects - Decorator, Composite - instead of a subclass per combination. Use for middleware or stream wrappers adding logging, compression, or encryption in any order, or a part-whole tree (menus and submenus, directories and files) that clients should treat uniformly. Not for swapping one interchangeable algorithm for another (see encapsulate-algorithmic-variation), a single simplified entry point (see control-object-access-and-indirection), or the general composition-over-inheritance preference (see prefer-composition-for-behavioral-reuse)."
license: MIT
---

# Compose and Augment Object Behavior

## Intent
Build richer behavior by composing objects rather than creating increasingly large inheritance hierarchies, especially when optional responsibilities should be combined dynamically.

## Procedure
1. Identify behavior that can be layered (added incrementally around a core) or combined (assembled from independent parts).
2. Define a stable component contract that both the core object and every wrapper/composite will implement.
3. Compose behavior through objects that hold a reference to the thing they augment, rather than through subclassing.
4. Keep each wrapper/decorator focused on one added responsibility so wrappers can be combined in different orders and combinations.
5. For tree-like structures, distinguish leaf and composite behavior through a coherent common contract, deciding deliberately how leaf-only operations (like "add child") are handled.
6. Validate that the resulting object graph — a chain of decorators or a composite tree — remains something a developer can inspect and reason about.

## Decision rules
- Prefer composition over subclassing when responsibilities combine independently and a subclass-per-combination would explode combinatorially.
- Decorator is useful for dynamically adding responsibilities to an individual object while preserving its interface to callers.
- Composite is useful when clients should treat individual objects and compositions of them uniformly, especially for recursive, tree-shaped domains.
- Do not introduce a wrapper if it merely forwards to a single underlying call with no added behavior.

## Anti-patterns
- Deep decorator chains so long that debugging requires stepping through a dozen pass-through layers to find where behavior actually changes.
- Composite interfaces that define operations meaningless for leaves (like `addChild` on a `File`), forcing awkward no-op or exception implementations.
- Wrappers that accidentally change the underlying contract's behavior (e.g., altering error semantics) without documenting it.
- Composition used without documenting which decorators are required, optional, or order-dependent.

## Exceptions and trade-offs
- If there is only one variant of the behavior and no near-term need for combinations, a single class is simpler than a decorator/component split.
- Decorator chains trade a flatter call stack for combinatorial flexibility; when performance-sensitive code needs to avoid extra indirection per call, a monolithic implementation may be preferable.
- Composite's uniform interface can leak type-safety — operations valid only for composites or only for leaves may need runtime checks; accept that cost only when the uniformity genuinely simplifies client code.

## Verification
- Can each composed responsibility be understood and tested independently of the others it's stacked with?
- Does the composed object still satisfy the contract callers expect (same interface, and documented rather than silent changes to behavior)?
- Is the runtime object graph — the decorator stack or composite tree — still something a developer can inspect and debug?
