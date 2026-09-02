---
name: centralize-or-encapsulate-request-handling
description: "Gives a request or coordination step first-class representation - Command, Chain of Responsibility, or Mediator - so it can be queued, undone, logged, or routed through variable handlers. Use for a UI action needing undo, a background job that must be serialized and retried, a request passing through validation, auth, and rate-limiting handlers, or peers wiring a tangled web of direct references for coordination. Not for plain synchronous calls needing none of that, and not for broadcasting a change to many interested consumers (see decouple-publishers-and-subscribers)."
license: MIT
---

# Centralize or Encapsulate Request Handling

## Intent
Represent requests, coordination, or responsibility transfers explicitly when they need to be queued, logged, composed, undone, routed, or mediated, instead of leaving that logic implicit in direct method calls.

## Procedure
1. Identify request handling that is becoming coupled to the caller or receiver, or that peers are coordinating through a growing mesh of direct references.
2. Determine whether the request itself needs a stable representation (to be queued, logged, undone, or replayed) versus needing a routing path through multiple potential handlers, versus needing many peers reduced to one coordination point.
3. Encapsulate the request as an object (Command), route it through a focused chain (Chain of Responsibility), or introduce a mediator, matching the force actually present.
4. Keep receivers focused on executing their responsibility; the request/chain/mediator layer should not absorb that logic.
5. Add composition, queuing, undo, logging, or routing only when a concrete requirement calls for it — not speculatively.
6. Verify that control flow remains traceable: a reader should be able to find where a request is created and where it is ultimately handled.

## Decision rules
- Command is appropriate when requests need to be represented independently of invocation — queued, logged, undone, or scheduled.
- Chain of Responsibility is useful when handlers should process or pass along a request without a fixed caller-to-handler binding, and the set of handlers may vary.
- Mediator is useful when many peers would otherwise become tightly interconnected and a single coordination point reduces that coupling.
- These patterns should simplify coordination, not hide it — if tracing a request becomes harder after applying them, reconsider.

## Anti-patterns
- Command objects created solely to rename a direct method call, with no queuing, undo, or logging need.
- Mediators that absorb so much coordination logic they become god objects.
- Chains with ambiguous handler ownership, where it's unclear which handler is responsible for terminating the chain.
- Hidden queues or asynchronous execution introduced under the guise of a Command that silently change call semantics from synchronous to deferred.

## Exceptions and trade-offs
- If there is exactly one handler and it will stay that way, Chain of Responsibility adds indirection with no payoff — a direct call is clearer.
- Command objects for undo support add memory and bookkeeping cost (storing enough state to reverse an action); skip it for actions that are naturally idempotent or trivially re-derivable.
- A Mediator can become a single point of failure and a hotspot for merge conflicts as a team grows; for a small, stable set of peers, direct references may remain the simpler choice.

## Verification
- Can the request's flow — creation, any queuing, and final handling — be traced by reading the code?
- Does the abstraction solve a real coordination pressure (undo, queuing, variable routing, peer coupling) rather than an imagined one?
- Are responsibilities still localized, with receivers, handlers, and the mediator each owning a distinct concern?
