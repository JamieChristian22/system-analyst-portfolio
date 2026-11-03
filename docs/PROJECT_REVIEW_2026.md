# Healthcare appointment system: integration readiness review

This is a **simulation-based systems analysis artifact**, not a record of a live healthcare deployment.

## Critical integration scenarios

| Scenario | Expected design behavior | Evidence needed |
|---|---|---|
| Two users request the same slot | Exactly one confirmed booking | Concurrency test and data constraint |
| Scheduling API times out | Safe retry without duplicate appointment | Idempotency key design and retry test |
| Invalid patient identifier | Reject and log without exposing private details | Negative contract test |
| Provider availability changes | Recheck availability at confirmation | Sequence diagram and state transition test |
| Notification provider fails | Booking outcome remains explicit; retry/queue notice | Failure injection and operational alert |
| Unauthorized user accesses booking | Deny access with audit event | RBAC negative test |
| Deployment requires rollback | Restore service safely with data reconciliation | Rehearsed rollback evidence |

**Status:** This table defines proposed scenarios; it does not claim execution or passing results.

## Architecture decision record: appointment confirmation

**Context.** Availability may change between a search response and confirmation.

**Recommended design.** Revalidate the slot inside a transaction with a database uniqueness/concurrency control, and make confirmation requests idempotent.

**Alternatives.** Client-side availability checks alone are simpler but cannot reliably prevent concurrent double-booking. Distributed locks add operational complexity.

**Consequences.** The implementation needs a clear appointment state model, conflict response, transaction boundary, and tests for race conditions.

## Reviewer checklist

- [ ] Requirements IDs map to each scenario
- [ ] API contract defines validation and conflict status codes
- [ ] Data model enforces slot integrity
- [ ] Security review covers access, audit, retention and privacy
- [ ] UAT records distinguish planned from executed cases
- [ ] Recovery time and recovery point objectives have owners and measurable targets
- [ ] Production claims are withheld until deployment evidence exists

## Interview demonstration
Walk through business need → functional requirement → sequence diagram → API/data mapping → concurrency failure case → UAT plan → rollout and rollback. Explain where the documented simulation ends and where implementation verification would begin.
