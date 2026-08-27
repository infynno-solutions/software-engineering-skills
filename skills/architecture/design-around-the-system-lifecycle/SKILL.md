---
name: design-around-the-system-lifecycle
description: "Weighs build speed, deployability, operability, and maintainability as competing forces on an architecture decision, not just runtime correctness. Use when a design review has only asked whether it works, or a design that is clean at build time will be costly to operate or change later. Not for whether a component gets its own deployable (see design-for-independent-deployment), policy/mechanism separation (see separate-policy-from-details), or general option-weighing (see evaluate-engineering-trade-offs)."
license: MIT
---

# Design Around the System Lifecycle

## Intent
Treat how a system will be developed, deployed, operated, and maintained as first-class architectural requirements, so the design is optimized for the system's whole lifetime rather than only for getting a first working version to run.

## Procedure
1. Name the lifecycle phases relevant to the decision at hand: development (how hard is it to build and test locally, how fast is the feedback loop), deployment (how does a change get to production, what can go wrong during rollout), operation (how is the running system observed, diagnosed, and kept healthy), and maintenance (how does it change over time, how easy is it to modify safely).
2. For the design option under consideration, estimate its cost or benefit in each phase — even roughly. A design that is fast to build but has no logging/metrics story is optimizing development at operation's expense; note that trade explicitly.
3. Identify which phase matters most for this system's actual context (a short-lived prototype weighs development heavily; a system expected to run for years with an on-call rotation weighs operation and maintenance heavily).
4. Check for phase-specific structural needs: can a developer run and test the relevant piece in isolation (development)? Can this piece be deployed/rolled back without taking down unrelated pieces (deployment)? Does it expose enough telemetry to diagnose a production incident without attaching a debugger (operation)? Can a future engineer change this piece without first fully understanding the rest of the system (maintenance)?
5. Where two phases pull in opposite directions (e.g., a shortcut that speeds initial development but makes production debugging much harder), make the trade-off an explicit, written decision rather than an unexamined default toward whichever phase is happening right now (usually development).
6. Revisit the decision if the system's expected lifetime or usage pattern changes materially (a prototype that became a production system needs its lifecycle trade-offs re-made).

## Decision rules
- Weight the lifecycle phases by the system's actual expected lifetime and criticality, not by which phase the team happens to be in right now.
- A design decision that saves time in development but has no plan for how it will be diagnosed in production should be treated as incomplete, not as done.
- Long-lived, frequently-changed systems should bias toward maintainability and operability even at some cost to initial development speed; short-lived or throwaway systems should bias the other way.
- Deployment friction (manual steps, long build times, unclear rollback) compounds over the system's life — treat it as a real architectural cost, not an ops-team afterthought.
- If nobody can answer "how would we know this broke in production, and how would we fix it," the design is not finished regardless of how clean its code looks.

## Anti-patterns
- Designing and reviewing purely against "does the happy path work in a demo," with no consideration of how a failure will be observed or diagnosed once it's live.
- Treating deployability as something to bolt on after the architecture is otherwise finished, rather than as a constraint the architecture is designed against from the start.
- Optimizing exclusively for the initial build (fastest to code) in a system explicitly expected to run and be maintained for years.
- Choosing a technology or pattern purely because it's fast to prototype with, then shipping it to production unchanged without re-evaluating its operational and maintenance cost.
- Adding extensive operational tooling (dashboards, alerting, elaborate deploy pipelines) to a genuinely short-lived or experimental system where the cost isn't justified.

## Exceptions and trade-offs
- A true throwaway prototype or spike can and should skip most operation/maintenance investment — apply this skill by explicitly deciding that, not by never having considered it.
- Under a hard deadline, it's legitimate to consciously defer a lifecycle concern (e.g., minimal observability at launch, better dashboards after), as long as the deferral is a decision, tracked, and revisited — not silent debt.
- Small internal tools with a single, known maintainer can reasonably accept lower investment in onboarding/discoverability than a system multiple teams will touch.

## Verification
- For the design decision under review, each of development, deployment, operation, and maintenance has been at least briefly considered and the trade-offs stated, even if the conclusion is "not a concern here, because X."
- There is a concrete answer for how a production failure in this component would be detected and diagnosed.
- There is a concrete answer for how this component is deployed and rolled back independently of unrelated changes, or an explicit acceptance that it isn't.
- If the system's expected lifetime is long, the maintenance cost of the chosen option was compared against at least one alternative, not assumed.
