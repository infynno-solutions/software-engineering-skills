---
name: adapt-incompatible-interfaces
description: "Introduces a thin translation layer (Adapter) between a client and a provider whose method names, parameter shapes, error conventions, or data formats do not match. Use when wrapping a third-party SDK behind the interface your code already calls, bridging a legacy XML service into typed objects, swapping vendors invisibly to callers, or letting a test double stand in for a class it cannot implement. Not for varying algorithms behind a contract you control (see encapsulate-algorithmic-variation), a simplified entry point over a whole subsystem (see control-object-access-and-indirection), or whether the seam is warranted at all (see identify-and-place-architectural-boundaries)."
license: MIT
---

# Adapt Incompatible Interfaces

## Intent
Introduce a compatibility boundary when two collaborators have useful behavior but incompatible interfaces, so existing code can work with the new one without invasive changes on either side.

## Procedure
1. Identify the incompatible client and provider contracts precisely: method signatures, data shapes, error/exception conventions, and units.
2. Decide which side's interface should remain stable — usually the caller's, since that is the code you don't want to touch.
3. Introduce an adapter at the boundary that implements the stable interface and holds a reference to the incompatible provider.
4. Translate semantics explicitly rather than blindly mapping names — a `close()` on one side may need to become `flush()` then `disconnect()` on the other, not a single renamed call.
5. Keep the translation localized to the adapter; do not let callers reach around it to the raw provider.
6. Test edge cases where the contracts differ semantically: error codes that don't map one-to-one, null/absent conventions, and units or precision differences.

## Decision rules
- The adapter should isolate incompatibility rather than spread translation code across every call site.
- Prefer semantic translation over mechanical forwarding when the two sides mean different things by similar-sounding operations.
- Keep adapters thin enough that they do not become a second domain model with their own business rules.
- Use adapters at architectural boundaries when integrating external systems, not as a general-purpose wrapper habit.

## Anti-patterns
- Scattered ad hoc conversions repeated throughout callers instead of one adapter.
- Adapters that grow business policy instead of pure translation.
- Assuming a matching method signature means matching semantics (e.g., synchronous vs. asynchronous, inclusive vs. exclusive ranges).
- Adapter chains where no single adapter is responsible for the transformation, so nobody can say where a value's meaning changed.

## Exceptions and trade-offs
- If you own both interfaces and can change either one directly, changing the interface is usually simpler than adding an adapter — reserve adapters for boundaries you don't control.
- An adapter over a very unstable or evolving external API can itself become a maintenance burden; consider whether pinning a version or vendoring a thin client is more honest than repeatedly patching the adapter.
- A one-off, single-call-site mismatch may not be worth a named adapter class — an inline conversion can be clearer than the ceremony of a new type.

## Verification
- Is the incompatibility confined to one boundary rather than leaking into callers?
- Is the semantic translation explicit and covered by tests for the cases where the two contracts disagree?
- Can either side change internally without forcing unrelated callers to change?
