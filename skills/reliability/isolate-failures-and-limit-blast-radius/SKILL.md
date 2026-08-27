---
name: isolate-failures-and-limit-blast-radius
description: "Partitions resources and failure domains so one component, tenant, workload, or dependency failing stays contained and cannot cascade. Use when a shared connection pool, thread pool, queue, or rate-limit budget lets one slow caller starve the others; when tenants share infrastructure with noisy-neighbor risk unaddressed; or when a dependency sits on a request path with no circuit breaker or bulkhead. Not for what happens after the failure to get back to good (see design-for-recovery), or what to serve while something is down (see degrade-gracefully)."
license: MIT
---

# Isolate Failures and Limit Blast Radius

## Intent
Partition resources and failure domains so that one component, tenant, workload, or dependency failing stays contained and cannot cascade through the whole system.

## Procedure
1. Map shared resources on the request/processing path (connection pools, thread pools, queues, caches, rate-limit budgets, database instances) and identify which independent callers/features/tenants contend for each.
2. For each shared resource, decide the isolation mechanism: separate pools per tenant/feature (bulkhead), per-dependency circuit breakers, per-tenant rate limits/quotas, or physical/logical partitioning (separate queues, shards, or clusters).
3. Size isolated resource pools so that one caller exhausting its own allocation cannot exhaust another's — a single global pool shared by all callers is not isolation.
4. Add a circuit breaker (or equivalent) around calls to a dependency that can be slow/down, so that dependency's failure doesn't consume unbounded capacity waiting on it.
5. Define and test the actual blast radius: simulate one tenant/dependency/component failing and confirm unrelated tenants/components keep functioning within their own budgets.

## Decision rules
- If two unrelated features or tenants currently share one thread/connection pool with no per-caller limit, that is not isolated — one slow caller can starve all others regardless of how good its individual error handling is.
- Prefer bulkheads (dedicated pools/quotas per failure domain) over a single global pool with only a total cap — a global cap still allows one caller to consume the whole budget before the cap is hit.
- Choose the failure-domain boundary to match actual business/blast-radius boundaries (tenant, region, criticality tier), not implementation convenience — isolating by an arbitrary technical boundary that doesn't map to who's affected doesn't limit blast radius where it matters.
- When a dependency's failure rate crosses a threshold, prefer failing fast (circuit open) over letting every caller individually time out — a circuit breaker turns N slow failures into one fast one.

## Anti-patterns
- All tenants or features sharing one unbounded thread pool or connection pool, so one tenant's traffic spike or one slow endpoint degrades every other tenant.
- A circuit breaker configured so broadly that one dependency's outage trips a breaker shared by unrelated call sites, taking down features that don't even depend on the failing dependency.
- "Isolating" at the code level (separate service, separate class) while both still share the same underlying database connection pool or the same underlying VM/host resources, so the isolation is illusory under load.
- Sizing bulkheads by guesswork instead of the actual concurrency/throughput each caller needs, so the isolation mechanism itself becomes the bottleneck for legitimate traffic.

## Exceptions and trade-offs
- Full isolation (separate infrastructure per tenant) is the strongest guarantee but the most expensive; for low-stakes or trusted-internal callers, coarser isolation (shared pool with a per-caller quota) may be an acceptable, cheaper trade-off.
- Bulkheading reduces resource utilization efficiency — capacity reserved for tenant A sits idle while tenant B is starved, even though the whole-system total is fine; that inefficiency is the cost of the guarantee and should be sized deliberately, not left unbounded.
- Over-isolating (many tiny pools/circuits for things that never interact) adds operational complexity and monitoring surface for no real blast-radius benefit; isolate at boundaries where correlated failure actually occurs.

## Verification
- Confirm each shared resource pool has a per-caller/per-tenant limit, not only a global limit.
- Confirm a fault-injection or load test shows one component/tenant failing or saturating its resource does not degrade metrics for unrelated components/tenants.
- Confirm circuit breakers exist on calls to dependencies that are not fully within your control, and that breaker state is observable (open/closed/half-open visible in monitoring).
- Confirm the isolation boundary matches the actual business blast-radius concern (which tenants/features must not affect each other), not just a convenient code module boundary.
