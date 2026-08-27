---
name: avoid-premature-distribution
description: "Decides whether a module boundary should also become a network/process boundary. Use when a doc or PR proposes a new microservice, split-out API, or queue between in-process components, or when consolidating an over-distributed system. Not for where the source boundary goes (see choose-boundaries-by-change-and-coupling), the deployable/pipeline decision (see design-for-independent-deployment), or fault tolerance (see design-for-partial-failure-in-distributed-systems)."
license: MIT
---

# Avoid Premature Distribution

## Intent
Keep the deployment topology as simple as the requirements allow: prefer a well-bounded module inside one deployable over a separate service until independent deployment, scaling, or fault isolation is an actual, demonstrated need.

## Procedure
1. Identify the specific driver being cited for distribution: independent deploy cadence, independent scaling, fault isolation, a genuinely separate runtime/language requirement, or organizational autonomy.
2. For each driver, check whether it is real today (measured load, actual conflicting release schedules, an actual incident where a shared failure domain caused an outage) or anticipated ("we might need to scale this later").
3. If the driver is anticipated rather than measured, implement the boundary as an in-process module with an explicit interface (a source-level seam) instead of a service. Keep the interface designed so it *could* be extracted later without touching callers.
4. If the driver is real and current, confirm the interface is already clean (single entry point, no shared mutable state, no reach-through into the other side's internals) before extracting it — extraction should be a deployment change, not also a design change.
5. When extracting, budget for the recurring cost: network failure handling, versioning across the boundary, distributed testing/debugging, and operational surface (deploy pipeline, monitoring, on-call). Confirm the team accepts this cost, not just the developer proposing the split.
6. Record the decision and the specific trigger that would justify revisiting it (e.g., "extract when p99 write latency from module X blocks module Y's release train").

## Decision rules
- A module that changes for reasons unrelated to another module's release schedule does not need its own service merely because it is conceptually distinct.
- Network boundaries are justified by independent scaling, independent fault domains, independent deploy cadence with conflicting release trains, or a hard runtime/language split — not by "microservices are the standard" or by org chart alone.
- If the team cannot name the operational owner, on-call path, and monitoring for a proposed new service, it is not ready to be a service.
- A source-level boundary (module, package, well-defined interface) gets almost all the coupling and testability benefits of a service boundary at a fraction of the operational cost.

## Anti-patterns
- Splitting a service because "it might need to scale independently someday" with no load data.
- Distributing along org-chart lines when the modules involved have no independent release requirement.
- Adding a message queue or REST call between two components that always deploy together and share a database transaction.
- Treating "microservices" as the default starting topology for a new system instead of the topology earned by demonstrated need.
- Extracting a service before the source-level interface is clean, so the network call just ships the existing spaghetti coupling over the wire.

## Exceptions and trade-offs
- Regulatory or data-residency requirements (e.g., a subsystem must run in a different jurisdiction) can justify distribution with no prior measured need.
- A genuinely different runtime requirement (GPU workload, different language ecosystem, third-party vendor requiring isolation) is a legitimate immediate driver.
- Very large teams (dozens of engineers on one codebase) may accept the extra operational cost of a service boundary earlier, purely to get deploy independence, even before scaling pressure exists — but this should be a deliberate trade-off, not a default.
- Starting distributed because the target production environment already mandates a service-mesh/container-per-component model is a legitimate constraint, not a violation of this skill.

## Verification
- For each proposed or existing service boundary, there is a written driver (scaling, fault isolation, deploy independence, runtime split) with supporting evidence, not just a design preference.
- The source-level interface at the boundary is already clean and minimal before or independent of the extraction.
- The team can name who owns deployment, monitoring, and incident response for the new service.
- Reverting the boundary back to in-process (if the driver turns out to be wrong) is possible without a full rewrite, because the interface was designed as a seam from the start.
