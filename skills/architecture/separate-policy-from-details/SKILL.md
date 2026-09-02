---
name: separate-policy-from-details
description: "Separates what should happen (a business decision) from how it is currently carried out (I/O, formatting, a tool call) within one function or class. Use when a function both decides a discount and formats currency, or the same rule is duplicated across mechanism-specific call sites. Not when the detail is the database or a framework (see keep-databases-as-details, keep-frameworks-as-details), for component-level dependency direction (see control-dependency-direction), or when the goal is fast tests (see design-testable-architecture)."
license: MIT
---

# Separate Policy From Details

## Intent
Within any given piece of code, separate what it decides (the business rule, the policy) from how that decision is carried out or communicated (UI, formatting, specific I/O calls, specific tools) — so the policy reads clearly on its own and the mechanism can change without touching the decision.

## Procedure
1. Read the code under review and, line by line, label each part as either policy (a decision that reflects a business rule — "is this order eligible," "what is the discount," "should this alert fire") or detail (mechanism — how a value gets formatted, which specific API is called, which log format is used, which serialization is chosen).
2. Look for a policy statement that is entangled with a detail statement in the same expression or the same few lines — e.g., a condition that checks business eligibility inline with a call that sends an HTTP request.
3. Extract the policy into its own function/method with a name describing the decision, taking plain inputs and returning a plain decision/value — no I/O, no formatting, no specific external call inside it.
4. Move the detail (the I/O call, the formatting, the specific tool invocation) to a caller or a separate function whose name describes the mechanism, which invokes the policy function and acts on its result.
5. Re-read the extracted policy function in isolation: it should be understandable and checkable by someone who knows the business rule but nothing about how the system delivers output or talks to external systems.
6. Where the same decision is duplicated across multiple mechanism-specific call sites (e.g., the same eligibility check written slightly differently in three different handlers), consolidate it into the one extracted policy function so mechanism changes at any call site can't accidentally also change the rule.

## Decision rules
- A block of code is "policy" if changing it changes what the system decides; it's "detail" if changing it changes only how a decision already made gets carried out or communicated.
- If explaining a function's business rule to a non-technical stakeholder requires narrating format strings, specific API calls, or logging statements, policy and detail are still tangled.
- Two implementations of "the same decision" that differ because they're embedded in two different mechanisms (one embedded in an email handler, one embedded in a push-notification handler) is a sign the decision needs extracting to one shared policy function that both mechanisms call.
- Prefer the detail depending on the policy (calling it, using its result) over the policy depending on the detail (formatting, calling out, or branching on delivery mechanism) — this is the same directional principle as `control-dependency-direction`, applied inside a single function or class rather than across components.

## Anti-patterns
- A function that both computes a business value and formats it for a specific display context (e.g., computes a discount and also builds the HTML string showing it) in one undifferentiated block.
- Business eligibility or authorization logic written inline inside a specific I/O call's arguments or callback, rather than as a named, separately readable condition.
- The same business rule re-implemented slightly differently in multiple mechanism-specific places (a REST handler, a batch job, a CLI command) because it was never extracted to one shared policy function.
- A policy function that takes "the request object" or "the response writer" as a parameter just to reach into it for one value, coupling the decision's signature to a specific delivery mechanism it doesn't need.
- Log messages, metrics calls, or formatting logic sprinkled directly inside a decision's conditional branches, making the actual rule hard to see among the surrounding mechanism.

## Exceptions and trade-offs
- Trivial one-line decisions (a simple threshold check used exactly once) don't need to be extracted into their own named function purely for policy/detail separation — apply this where the entanglement actually makes the code harder to read or reuse, not as a mechanical rule for every conditional.
- Performance-critical hot paths occasionally justify inlining a decision with its mechanism to avoid extra calls/allocations; if so, that trade-off should be a deliberate, commented choice, not a default.
- Where a "detail" is actually stable and unlikely to ever vary (e.g., a fixed internal format used nowhere else), the cost of separating it out may not be worth it — judge by whether the mixing currently makes the code hard to read or change, not by an absolute rule that all detail must always be separated.

## Verification
- The extracted policy function can be read and its correctness judged by someone with business knowledge but no knowledge of the specific I/O/formatting/tooling used elsewhere in the code.
- The policy function's signature and body contain no direct I/O calls, formatting/serialization code, or specific external tool/library calls.
- If the same business rule was previously duplicated across mechanism-specific call sites, there is now one function those sites call, not several near-duplicate implementations.
- Changing the mechanism (a different output format, a different notification channel) requires touching only the detail code, not the policy function.
