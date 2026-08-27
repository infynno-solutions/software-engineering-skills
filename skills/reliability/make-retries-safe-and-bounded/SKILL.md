---
name: make-retries-safe-and-bounded
description: "Retries only operations that are safe to repeat, and bounds every retry loop with backoff and a deadline so retries cannot run forever or amplify an outage. Use when code catches a timeout, connection reset, 5xx, or 429 and calls the same operation again; when a client SDK's default retry behavior has never been reviewed; or when client, gateway, and service each retry independently and multiply load on a struggling downstream. Not for making an operation safe to repeat in the first place (see design-idempotent-operations), or the per-attempt timeout bounding each try (see use-timeouts-and-deadlines)."
license: MIT
---

# Make Retries Safe and Bounded

## Intent
Retry only operations for which repeated execution is safe or explicitly controlled, and bound every retry loop with backoff and a deadline so retries cannot run forever or amplify an outage.

## Procedure
1. Classify the failure before retrying: is it transient (timeout, connection reset, 429/503) or is it a client error, validation failure, or business-logic rejection (400, 403, "insufficient funds")? Only retry the former.
2. Confirm the operation is safe to repeat — naturally idempotent, protected by an idempotency key, or genuinely side-effect-free (a read). If not, do not retry it blindly; make it safe first (see `design-idempotent-operations`) or don't retry.
3. Bound the retry loop with both a maximum attempt count and an overall deadline, whichever is hit first, so a persistent outage cannot cause an unbounded loop.
4. Use exponential backoff with jitter between attempts, not a fixed short interval, to avoid synchronized retry storms across many clients hitting the same recovering dependency.
5. Respect any explicit backpressure signal from the callee (e.g., `Retry-After` header, 429 with a hint) instead of retrying on your own schedule.
6. Check for retry amplification across the call chain: if an upstream caller also retries, a downstream failure can turn into a multiplicative load spike; coordinate budgets or retry at only one layer.

## Decision rules
- Retry idempotent/naturally-safe operations (GETs, operations guarded by an idempotency key) more liberally; treat non-idempotent operations without such protection as not-retryable by default.
- Never retry 4xx-class client errors that indicate the request itself is wrong (bad input, auth failure, not-found) — retrying them wastes budget and cannot succeed.
- Prefer a capped number of attempts plus jittered exponential backoff over a fixed retry interval, especially for anything that could be called by many clients simultaneously (thundering herd risk).
- When a circuit breaker is present, retries should stop entirely while the breaker is open — retrying into an open circuit defeats its purpose.

## Anti-patterns
- `while (true) { try { ...; break } catch { } }` — an unbounded retry loop with no attempt limit, no deadline, and no backoff.
- Retrying a non-idempotent write (e.g., "create order") on timeout, when the original request may have actually succeeded server-side and the timeout was only on the response — this creates duplicates, not resilience.
- Fixed-interval retries with no jitter across many client instances, causing synchronized retry storms that repeatedly re-overload a recovering dependency.
- Retrying at every layer of a call chain independently with no shared budget, so a single downstream failure fans out into an order-of-magnitude larger retry load than intended.

## Exceptions and trade-offs
- For latency-sensitive user-facing paths, a small number of fast retries (or none) may be preferable to a longer backoff sequence that blows the user's patience budget — bound retries by the caller's time budget, not just an abstract attempt count.
- Retrying non-idempotent operations is sometimes accepted as a deliberate risk (e.g., low-value, easily reconciled operations) when making them idempotent is disproportionately expensive — that should be a documented trade-off, not a default.
- Aggressive retrying can turn a partial outage into a total one by adding load exactly when a dependency is least able to absorb it; when in doubt, prefer failing fast and letting `degrade-gracefully` or a human handle it over retrying harder.

## Verification
- Confirm every retry loop has both a maximum attempt count and a wall-clock deadline — not just one of the two.
- Confirm the retried operation is verified idempotent/safe-to-repeat, or the code explicitly restricts retries to read-only/safe cases.
- Confirm backoff uses jitter, and that a load test with many concurrent clients hitting a failing dependency doesn't show synchronized retry spikes.
- Confirm the retry logic distinguishes retryable failure classes (timeouts, 5xx, 429) from non-retryable ones (4xx validation/auth errors) rather than retrying on any exception.
