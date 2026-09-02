---
name: design-for-failure
description: "The umbrella discipline of treating hardware, dependency, network, and human failure as normal operating conditions and designing explicit detection, containment, and recovery up front. Use when a new service or integration has only the success path specified, when an architecture doc has no section on a dependency being unreachable, slow, or returning bad data, or when a postmortem shows a failure mode nothing detected until a customer noticed. Once the failure category is known, reach directly for use-timeouts-and-deadlines, make-retries-safe-and-bounded, isolate-failures-and-limit-blast-radius, or design-for-recovery instead."
license: MIT
---

# Design for Failure

## Intent
Assume failure of hardware, dependencies, networks, and humans is a normal operating condition, and design explicit detection, containment, and recovery behavior for it up front rather than bolting it on after an incident.

## Procedure
1. List every external dependency (network call, disk, queue, third-party API, clock, other service) the component touches, and for each, ask: what happens if it is slow, down, or returns wrong/corrupt data?
2. For each identified failure, decide explicitly: detect it (how do we know it happened?), contain it (does it stay local or cascade?), and recover from it (automatic retry, failover, degrade, or surface to a human?).
3. Distinguish failures that are expected and routine (a peer node restarting, a transient network blip) from failures that indicate a deeper problem (data corruption, a bug) — the latter should not be silently retried or masked.
4. Write the failure behavior into the design doc/interface contract alongside the happy path, not as an afterthought section.
5. Validate assumptions with fault injection (kill a dependency, inject latency, corrupt a response) before relying on the design in production.

## Decision rules
- Every dependency call in the design must have an answer to "what if this fails," even if the answer is "the whole request fails fast and returns an error" — an *unconsidered* dependency, not a considered failure, is the defect.
- Prefer failure modes that are detectable (a metric fires, a log appears) over ones that fail silently and are found by a customer or a later data audit.
- Treat "it hasn't failed in production yet" as insufficient evidence that a dependency is reliable enough to go unhandled.
- Distinguish single-point-of-failure components (only one instance, no redundancy) from replicated ones early — SPOFs need an explicit decision about acceptable downtime, not an implicit assumption they won't fail.

## Anti-patterns
- A design or architecture doc with a detailed happy-path sequence diagram and no failure-path diagram or discussion at all.
- Treating "add a try/catch" as equivalent to designing for failure — catching an exception without a defined detection/containment/recovery story just relocates the bug.
- Assuming a managed cloud service or third-party API "basically never fails" and therefore needs no failure handling at the call site.
- Designing failure handling only for the failures that already happened in a past incident, without generalizing to the class of failure they represent.

## Exceptions and trade-offs
- Exhaustively designing for every conceivable failure has diminishing returns; prioritize by (likelihood × blast radius), and explicitly accept low-likelihood/low-impact gaps rather than pretending they're covered.
- Some failure handling (full multi-region failover) is expensive to build and operate — it's legitimate to defer it, but the decision to defer should be explicit and revisited as the system's criticality grows, not silent.
- Over-engineering failure handling for a prototype or internal tool wastes effort better spent elsewhere; match the rigor to the system's actual criticality.

## Verification
- Confirm the design doc or PR has an explicit failure-mode section covering each external dependency, not just the happy path.
- Confirm at least the highest-blast-radius failure modes have been exercised via fault injection, chaos testing, or a game day, not just reasoned about on paper.
- Confirm failures are observable (metrics/logs/alerts) rather than only handled silently in code.
- Confirm SPOFs identified during design have an explicit, documented decision about acceptable impact, not an implicit assumption of reliability.
