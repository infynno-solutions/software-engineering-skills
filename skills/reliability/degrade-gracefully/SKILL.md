---
name: degrade-gracefully
description: "Keeps serving the parts of a request or system that can still be served correctly when full functionality is unavailable. Use when optional enrichment - recommendations, reviews, personalization, facets - currently fails the whole checkout or auth response; when load shedding requires deciding which requests or features to drop first; or when a cached or precomputed value could stand in for a live call that is down. Not for reasoning about which components failed and what state that leaves (see reason-about-partial-failure), the broader detection and containment design (see design-for-failure), or the path back to full functionality (see design-for-recovery)."
license: MIT
---

# Degrade Gracefully

## Intent
When full functionality is unavailable, keep serving the parts of a request or system that can still be served correctly instead of failing the whole thing.

## Procedure
1. Classify each piece of functionality in the flow as essential (request is meaningless without it) or enhancing (nice to have, safe to omit or approximate).
2. For each enhancing piece, define an explicit fallback: cached/stale value, default value, feature turned off, or a simpler algorithm — not "let the exception propagate."
3. Make the fallback trigger on the actual failure signal (timeout, error, circuit open), not on ambient conditions, and make it observable (metric/log) so degraded mode is visible, not silent.
4. Decide and document how degraded output is presented to the caller — omitted section, stale-labeled data, reduced precision — so it's a deliberate contract, not an accident.
5. Verify the essential path has no hidden dependency on the enhancing path (e.g., logging a "personalization applied" event must not block checkout).

## Decision rules
- If losing a component means the response would be misleading or unsafe (wrong price, wrong permissions), that component is essential — do not degrade it, fail the request instead.
- If losing a component only removes richness (recommended items, avatar image), it's a degrade candidate — never let it take down the essential response.
- Prefer serving stale/cached data with a clear signal over serving nothing, when staleness is safe for that data (catalog metadata, non-financial content) — never for data where staleness is unsafe (inventory counts at checkout, account balance).
- Under load shedding, drop the cheapest-to-lose, most-optional traffic first, and make the shedding policy explicit rather than whatever happens to time out first.

## Anti-patterns
- Wrapping an optional call in try/catch that swallows the error and returns an empty/null result with no fallback content and no log/metric — the failure becomes invisible.
- A single unhandled exception from an enrichment service taking down the entire page or API response.
- "Graceful" degradation that silently serves stale or wrong data with no indication to the caller or downstream systems that it's degraded.
- Building elaborate fallback logic for a component that is actually essential, masking a correctness bug instead of accepting the request should fail.

## Exceptions and trade-offs
- Some domains (financial transactions, safety-critical control) should not degrade at all — failing loudly and stopping is safer than serving an approximate result; know which parts of your system fall here before applying this skill uniformly.
- Serving stale data trades correctness-of-recency for availability; only acceptable when the business tolerates that staleness window.
- Degraded mode adds a code path that is exercised rarely, which itself needs testing (chaos/fault injection) or it will rot and fail when actually needed.

## Verification
- Confirm each optional dependency has a defined fallback and that a fault-injection test (kill/timeout that dependency) proves the essential path still succeeds.
- Confirm degraded responses are observable — a metric, log line, or response flag indicates degraded mode occurred.
- Confirm no essential behavior secretly depends on an "optional" component (audit call graph, not just intent).
- Confirm the fallback content itself cannot violate correctness/safety constraints (e.g., a cached price is never served as authoritative).
