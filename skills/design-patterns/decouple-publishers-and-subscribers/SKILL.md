---
name: decouple-publishers-and-subscribers
description: "Decouples a source of change from its consumers via Observer or pub/sub, so consumers can be added or removed without editing the producer. Use when a model, UI control, or domain event has a growing set of interested consumers - logging, analytics, and cache invalidation each subscribing independently. Not for a single fixed consumer, where a direct call is clearer; not for a request routed to exactly one handler out of several (see centralize-or-encapsulate-request-handling); not for an event log used as service integration (see use-logs-events-and-change-data-capture-deliberately)."
license: MIT
---

# Decouple Publishers and Subscribers

## Intent
Decouple producers of events or changes from consumers when consumers should evolve independently and the producer should not know their concrete implementations.

## Procedure
1. Identify a one-to-many dependency or event publication point where the producer currently either hardcodes its consumers or is starting to accumulate more of them.
2. Define the event/notification contract: what data travels with a notification, and what a subscriber's callback signature looks like.
3. Register or compose consumers through an abstraction (an observer list, an event bus, a subscription object) rather than the publisher holding named references to each one.
4. Keep publisher logic independent of concrete subscribers — it should be able to add a new subscriber type without a code change to the publisher.
5. Define ordering, delivery, failure, and lifecycle semantics when they matter: do subscribers run in registration order, synchronously, and what happens if one throws or the publisher is destroyed while subscribers remain registered?
6. Prevent notification mechanics from becoming hidden control flow that a reader can't discover by looking at the publisher alone.

## Decision rules
- Observer/pub-sub is appropriate when consumers vary independently from the publisher and the set of consumers isn't fixed at compile time.
- Keep the notification abstraction focused — one clear kind of event per channel, not an all-purpose bus carrying unrelated payloads.
- Explicitly define synchronous vs. asynchronous delivery if it affects correctness (e.g., whether a subscriber sees a fully-updated object or one mid-mutation).
- Avoid observers when a direct call makes the dependency clearer and the relationship is stable and singular.

## Anti-patterns
- Hidden observer graphs so deep or implicit that a reader can't trace what happens when a value changes without running the program.
- Subscriber side effects that depend on undocumented ordering between subscribers (subscriber B silently assumes subscriber A already ran).
- Using notification as a blanket replacement for every direct dependency, even ones that are simple and 1:1.
- A global event bus used without ownership or lifecycle boundaries, so nobody knows who can publish, who can subscribe, or when subscriptions are cleaned up.

## Exceptions and trade-offs
- Observer trades traceable, explicit call chains for flexibility; in a small codebase with one consumer, that trade isn't worth making yet.
- Synchronous observer notification inside a hot path can create surprising performance costs as subscribers accumulate — consider whether asynchronous delivery or batching is needed, and document the choice.
- Memory leaks from subscribers that are never unregistered are a real, common cost of this pattern; weigh it against the coupling cost of the direct-call alternative, and prefer patterns (weak references, explicit unsubscribe, scoped subscriptions) that make lifecycle management concrete.

## Verification
- Can the publisher remain unchanged as the set or type of consumers varies?
- Are delivery and failure semantics (ordering, sync/async, what happens when a subscriber throws) understandable and documented?
- Can a reviewer trace important control flow — what happens when this event fires — without having to discover hidden subscribers by running the code?
