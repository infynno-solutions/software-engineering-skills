---
name: preserve-behavioral-substitutability
description: "Requires a type substituted behind an interface or base class to honor callers' expectations - preconditions, postconditions, invariants, side effects - not just the signature. Use when a subclass overrides a method to throw for a case the base allowed, a new implementation changes whether a method has side effects (a cache-backed repository silently dropping writes), or when judging whether swapping implementations in production is safe. Not when the interface is too broad and forced the throwing override (see keep-interfaces-narrow-and-client-focused), when deciding whether to add a seam at all (see design-for-extension-without-fragile-modification), or when choosing inheritance versus composition (see use-inheritance-only-for-genuine-subtyping)."
license: MIT
---

# Preserve Behavioral Substitutability

## Intent
Require replacements behind an abstraction to honor the behavioral expectations clients rely on, not merely the method signatures.

## Procedure
1. Identify the contract clients actually depend on, not just the declared signature.
2. Check preconditions, postconditions, invariants, error behavior, and side effects for each implementation.
3. Verify each implementation can substitute for another without surprising clients.
4. Move abstraction boundaries when the contract is unstable or contradictory across implementations.

## Decision rules
- A subtype must accept everything its base type accepts (no narrower preconditions) and guarantee at least what its base type guarantees (no weaker postconditions).
- If a "subtype" must reject inputs the base type allows, or throw where the base type doesn't, it isn't a valid subtype of that abstraction — model it as a sibling or separate interface instead.
- Side effects and performance characteristics callers observably depend on (e.g., "always persists synchronously") are part of the contract even when untyped.
- When two implementations can't honor one shared contract, split the abstraction rather than weakening the contract to the lowest common behavior.

## Anti-patterns
- Using inheritance solely because names or shapes look related.
- Treating type compatibility (it compiles) as proof of substitutability.

## Exceptions and trade-offs
- Some languages or platforms enforce parts of the contract statically; behavioral verification is still needed for what the type system can't check.

## Verification
- Run the same behavioral/contract test suite against every implementation through the shared abstraction, not just implementation-specific tests.
- Check every overriding method for narrowed accepted inputs, added thrown exceptions, or removed guarantees relative to the base contract.
- Swap the implementation actually used at a real call site and confirm existing callers' tests still pass unmodified.
