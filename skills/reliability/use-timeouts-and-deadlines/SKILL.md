---
name: use-timeouts-and-deadlines
description: "Gives every blocking operation an explicit time budget and propagates an overall deadline through chains of dependent calls. Use for a network call, database query, lock acquisition, or queue read relying on a library default that may wait forever; for a call chain where each service sets its own local timeout with no shared deadline; or for polling an external condition with no upper bound. Not for deciding whether to attempt the call again after it times out (see make-retries-safe-and-bounded), or what to do once you have given up waiting (see degrade-gracefully)."
license: MIT
---

# Use Timeouts and Deadlines

## Intent
Avoid indefinite waiting by giving every blocking operation an explicit time budget, and propagate an overall deadline through chains of dependent calls so a caller that has given up doesn't leave downstream work running pointlessly.

## Procedure
1. Find every blocking call (HTTP/RPC client, DB driver, lock, queue consumer, `Future.get()`/`await` without a timeout) and confirm it has an explicit, finite timeout — not a library default that may be unset or unreasonably large.
2. Set the timeout based on the actual expected latency distribution of the operation (e.g., p99 plus margin), not an arbitrary round number copied from elsewhere.
3. For a chain of calls serving one logical request, establish an overall deadline at the entry point and propagate the *remaining* budget to each downstream call, rather than letting each hop apply its own full timeout independently.
4. When a deadline is exceeded or about to be, stop doing further work for that request — cancel downstream calls where the transport supports cancellation, and don't start new dependent calls once the remaining budget is exhausted or too small to be useful.
5. Make timeout expirations observable (logged/metriced, distinguishable from other error types) so a spike in timeouts is diagnosable separately from a spike in explicit errors.

## Decision rules
- Every blocking call must have a finite timeout; "the library's default" is only acceptable once you've confirmed what that default actually is and that it's intentional, not unset.
- In a multi-hop call chain, downstream timeouts should be derived from the remaining portion of the overall deadline, not each independently set to the same full value — otherwise a request can be "alive" downstream long after the original caller stopped waiting.
- Prefer a timeout tight enough to fail fast on genuine unavailability but loose enough to accommodate normal tail latency — base it on measured p99/p999, not a guess.
- Distinguish a timeout (gave up waiting, outcome unknown) from an explicit failure response (definitely failed) in both handling logic and metrics — they imply different next actions (see `reason-about-partial-failure`).

## Anti-patterns
- An HTTP client, DB connection, or lock acquisition left at its library-default timeout without anyone having verified what that default is — sometimes literally infinite.
- A three-hop call chain where each service independently sets a 30s timeout, so the total possible wait for the original caller is effectively 90s+ even though the caller itself only waits 30s and has already returned an error to its own caller.
- Continuing to do expensive work (calling further downstream services, writing to a database) after the request's deadline has already passed and the original caller has stopped listening.
- Setting an extremely short timeout copied from an unrelated fast endpoint onto a call whose normal latency is much higher, causing constant spurious timeout failures under completely normal conditions.

## Exceptions and trade-offs
- Some operations are legitimately long-running (batch jobs, large exports) and should not use a short synchronous timeout at all — model them as async with polling/callback and a separate, appropriate timeout for that async lifecycle instead of forcing a request/response timeout onto them.
- Very aggressive timeouts reduce tail latency exposure but increase false-positive failures/retries under normal jitter; there's a real trade-off between failing fast and failing unnecessarily — tune from measured latency data, not intuition.
- Deadline propagation across service boundaries requires every hop to cooperate (read and respect the incoming deadline); if some services in the chain don't support it, propagation is only partially effective — treat that as a known gap, not silently assume it works everywhere.

## Verification
- Confirm every blocking call on the request path has an explicit, finite timeout that was chosen from measured latency data, not left at a library default.
- Confirm a multi-hop chain has a single overall deadline that is propagated and derived from remaining budget at each hop, rather than each hop timing out independently at full duration.
- Confirm work is not started or continued downstream after the request's deadline has already elapsed (test by injecting a slow response near the deadline boundary).
- Confirm timeout events are visible in metrics/logs as a distinct category from other failures, so timeout rate can be monitored and alerted on separately.
