---
name: design-idempotent-operations
description: "Makes retried or duplicated invocations converge on the same intended result, so a retry never double-applies an effect. Use for any write endpoint or message consumer a client, gateway, or queue will retry; for costly or irreversible side effects such as charging a card, decrementing inventory, or provisioning a resource; and for at-least-once delivery systems where redelivery is normal rather than an edge case. Not for deciding whether and when to retry (see make-retries-safe-and-bounded), how long to wait before giving up (see use-timeouts-and-deadlines), or failure containment (see isolate-failures-and-limit-blast-radius)."
license: MIT
---

# Design Idempotent Operations

## Intent
Make retried or duplicated invocations of an operation converge on the same intended result, so retries (by clients, message queues, or automation) never double-apply an effect.

## Procedure
1. Identify the operation's effect: is it naturally idempotent already (e.g., `SET status = 'active'`), or does repetition change the outcome (e.g., `balance += amount`, `INSERT` without a uniqueness constraint, "send email")?
2. For non-naturally-idempotent operations, introduce an idempotency key — a client-supplied or deterministically derivable token that uniquely identifies "this logical attempt" — and require it on the request/message.
3. Persist the idempotency key together with the operation's outcome (not just "seen," but the actual result) in the same transaction as the effect, so a retry can return the original result rather than re-executing.
4. On receiving a request/message with a previously-seen key, short-circuit: return the stored result rather than re-running the side effect.
5. For multi-step operations, make each step individually idempotent (or use a saga/state-machine pattern) so a retry that resumes mid-sequence doesn't redo already-completed steps.
6. Set and document the retention window for idempotency keys — how long duplicates are still recognized as duplicates — matched to the realistic redelivery/retry window of the callers.

## Decision rules
- Prefer natural idempotency (absolute-value writes, upserts keyed by a stable identifier, conditional writes) over key-based deduplication when the operation allows it — it needs no extra storage or key management.
- When the effect is external (charge a payment processor, send an SMS) and can't be made naturally idempotent, an idempotency key checked *before* calling out is mandatory, not optional.
- Store the idempotency key and the result atomically with the state change (same transaction/same write) — recording "processed" separately from the effect creates a window where a crash between the two makes the check useless.
- Choose the idempotency key's scope deliberately: per-client-request (client generates a UUID) vs. derived from business identity (e.g., `order_id + line_item`) — client-generated keys need the client's cooperation; derived keys work even against buggy clients but require the derivation to truly be unique per logical operation.

## Anti-patterns
- Treating `INSERT`-only writes as automatically idempotent when there's no unique constraint on the natural key, so a retried insert creates a duplicate row.
- Checking "have I seen this key before" with a read followed by a separate write, allowing two concurrent retries to both pass the check and both execute the effect (a race, not just a rare edge case under load).
- An idempotency key that is accepted but not actually used to guard the side effect — logged for observability but the charge/send happens again anyway.
- Deduplicating at the API layer only, while an internal event/message triggered by that API call is republished on every retry and causes downstream double-processing.

## Exceptions and trade-offs
- Not everything needs idempotency: pure reads, and operations where the caller can tolerate and detect duplicates externally (e.g., a client-side dedupe after the fact) may not be worth the extra bookkeeping.
- Idempotency keys add storage, a retention/cleanup policy, and a bit of latency (the existence check) — weigh this against the cost of the alternative (double-charging a customer) rather than applying it uniformly to low-stakes operations.
- Some operations are inherently hard to make idempotent (rate-limited third-party calls with no dedupe support on their side); in those cases, shift to at-most-once semantics with explicit acknowledgment of possible gaps, and document the trade-off rather than pretending the operation is safe to retry.

## Verification
- Confirm a test exercises "submit the same request/message twice" and asserts the side effect happened exactly once and the same result was returned both times.
- Confirm the idempotency check and the effect are inside the same atomic unit (transaction), not two separate operations that can interleave under concurrency.
- Confirm concurrent duplicate requests (not just sequential retries) are handled correctly — race a second identical request in while the first is still in flight.
- Confirm the idempotency key retention window is documented and covers the actual maximum retry/redelivery window of real callers, including queue redrive and client backoff policies.
