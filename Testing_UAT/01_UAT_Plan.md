# User Acceptance Testing Plan

## Purpose

Validate that the system supports agreed patient, scheduler, manager, compliance, payment, notification, and exception workflows before production approval.

---

## Entry Criteria

- Approved BRD/FRS/NFR baseline
- Test environment stable
- Required interfaces available or approved stubs
- Test users/roles provisioned
- Severity 1/2 system-test defects closed
- UAT data loaded
- Traceability matrix updated

---

## Exit Criteria

- 100% Critical and High UAT scenarios executed
- >=95% total UAT scenarios passed
- Zero open Severity 1 defects
- No open Severity 2 defect without approved workaround and owner
- Business owner signs acceptance
- Production-readiness actions assigned

---

## Test Cycles

| Cycle | Focus | Planned Cases | Result |
|---|---|---:|---|
| UAT-1 | Core booking/search/identity | 18 | 17 pass, 1 defect |
| UAT-2 | Reschedule/cancel/waitlist | 14 | 14 pass |
| UAT-3 | Payments/notifications | 12 | 11 pass, 1 defect |
| UAT-4 | Staff roles/reporting/audit | 16 | 16 pass |
| Regression | Resolved defect confirmation | 8 | 8 pass |

---

