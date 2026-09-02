---
name: control-object-access-and-indirection
description: "Interposes controlled indirection - Proxy or Facade - between a caller and a target without changing the target's interface. Use for lazily loading an expensive resource, checking authorization before forwarding a call, caching in front of a slow lookup, standing in for an object across a network boundary, or offering one simplified entry point over a subsystem. Not for translating between two genuinely different interfaces (see adapt-incompatible-interfaces) or layering optional, combinable behaviors onto an object (see compose-and-augment-object-behavior)."
license: MIT
---

# Control Object Access and Indirection

## Intent
Introduce controlled indirection when direct access to an object needs isolation, lazy behavior, protection, remote access, caching, or another stable access policy — or when a complex subsystem needs a simpler entry point.

## Procedure
1. Identify the access concern that should be separated from the target object: lazy loading, authorization, remoteness, caching, or similar.
2. Preserve the target's interface where transparency is useful, so callers can't tell (except for the policy's effects) whether they're talking to the real object or its proxy.
3. Place the access policy in a proxy or facade-like boundary, not scattered across callers.
4. Keep the target unaware of caller-side concerns like caching or authorization — those belong in the boundary, not the domain object.
5. Make latency, caching, authorization, or remote semantics explicit where they change observable behavior (e.g., document that a proxy method can now throw a network error the real object never could).
6. Avoid indirection that provides no concrete value — a proxy that forwards every call unchanged with no added policy isn't earning its place.

## Decision rules
- Proxy is useful when access control, deferred loading, remote access, caching, or similar concerns vary independently of the target's core behavior.
- Facade is useful when the goal is a simpler interface over a subsystem rather than transparent substitution for one specific object.
- Keep the indirection observable where behavior such as latency, partial failure, or staleness changes semantics that callers need to reason about.

## Anti-patterns
- Proxy used as a generic wrapper habit for every object, regardless of whether any access concern actually applies.
- Facades that absorb business logic instead of just simplifying a subsystem's entry point.
- Hiding remote calls behind apparently local method-call semantics without documenting the new failure modes (timeouts, partial failure, retries).
- Multiple layers of indirection (a facade over a proxy over another proxy) with no distinct responsibility assigned to each layer.

## Exceptions and trade-offs
- Transparent proxies that hide remoteness or caching can make performance and failure characteristics harder to reason about; when that risk outweighs the convenience, an explicit, differently-named method (e.g., `fetchRemote()` instead of a same-named proxy method) may be the more honest design.
- A facade narrows what most callers see, but callers with legitimate advanced needs still need a path to the subsystem's full interface — don't let the facade become the only way in if that blocks real use cases.
- For a subsystem with only one or two classes, a facade adds a layer with little payoff; reserve it for subsystems complex enough that a simplified surface meaningfully helps callers.

## Verification
- Is the access concern (lazy loading, authorization, caching, remoteness) isolated in the boundary rather than duplicated at call sites?
- Is the additional indirection worth its complexity given what it actually buys callers?
- Are changed semantics — latency, new failure modes, staleness — visible to callers rather than silently hidden behind a familiar-looking interface?
