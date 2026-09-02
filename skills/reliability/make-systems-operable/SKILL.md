---
name: make-systems-operable
description: "Exposes the information and controls an operator needs to understand, diagnose, change, and recover a running system. Use when a new service has no health or readiness endpoint, no structured logs, and no metrics separating working from broken; when disabling a feature or changing a limit requires a full deploy; or when a postmortem timeline shows time lost because responders could not tell what state the system was in. Not for the detection, containment, and recovery design of failures themselves (see design-for-failure), or what to serve while degraded (see degrade-gracefully)."
license: MIT
---

# Make Systems Operable

## Intent
Expose the information and controls operators need to understand, diagnose, change, and recover a running system, so an incident responder isn't limited to reading source code and redeploying.

## Procedure
1. For each significant component, define what "healthy" and "unhealthy" look like concretely, and expose that as a health/readiness check and as metrics — not just as an absence of crashes.
2. Emit structured logs and metrics that let an operator answer, without reading source: what's the current error rate, latency, and throughput; what request caused this specific failure; which version/config is currently live.
3. Add operator controls for the interventions that are foreseeably needed under time pressure — feature flags/kill switches for risky new code, adjustable rate limits or timeouts, the ability to drain or fail over a specific instance — so intervention doesn't require a code change and deploy cycle.
4. Make destructive or high-impact controls safe to use in a hurry: confirm-before-execute, scoped blast radius, and an audit trail of who changed what and when.
5. Document how to reach and use each control (which dashboard, which flag, which command) in the runbook, and verify a responder unfamiliar with the code can actually find and use it.

## Decision rules
- If diagnosing a production issue currently requires reading source code or attaching a debugger, that's an operability gap — prefer exposing the needed signal as a metric/log/trace instead.
- Any behavior likely to need fast disabling (a new algorithm, a risky third-party integration, an experimental code path) should ship behind a flag/kill switch from day one, not added reactively after it causes an incident.
- Prefer exposing a small number of high-signal health indicators (the ones that predict user-visible impact) over a wall of low-level metrics that bury the signal an operator actually needs during an incident.
- Controls that change production behavior should be scoped as narrowly as possible (single tenant, single region, single feature) rather than only offering an all-or-nothing switch.

## Anti-patterns
- A service with no health endpoint, so load balancers and operators alike can only infer health from whether requests are timing out.
- Logs that are unstructured free text with no correlation ID, making it impossible to trace one request's path across services during an incident.
- A "kill switch" that exists in code as a config flag, but changing it requires a full deploy — defeating the purpose of having a fast, low-risk lever.
- Metrics dashboards built for building the feature (internal implementation counters) rather than for diagnosing it in production (user-facing error rate, latency percentiles, saturation).

## Exceptions and trade-offs
- Every flag/control is also a code path that must be tested and kept working, and every additional metric has a cost (cardinality, storage, cognitive load); prioritize operability investment on components with real incident/change history over speculative coverage everywhere.
- Runtime controls (flags, dynamic config) add a layer of state that can drift from what's in source control — mitigate with an audit log and periodic reconciliation, but recognize the trade-off exists.
- For low-risk, rarely-changing internal tools, the cost of building rich operability may exceed the benefit; match investment to blast radius and change frequency, not apply uniformly.

## Verification
- Confirm each production service has a health/readiness endpoint and dashboards that show the key user-facing health signals (error rate, latency, saturation) without needing to read logs.
- Confirm requests are traceable across service boundaries via a correlation/trace ID present in logs.
- Confirm at least one operator-usable control (flag, limit, kill switch) exists for each foreseeably-necessary fast intervention, and that using it does not require a deploy.
- Confirm someone other than the author can find and operate the relevant dashboard/control from the runbook alone, without reading the implementation.
