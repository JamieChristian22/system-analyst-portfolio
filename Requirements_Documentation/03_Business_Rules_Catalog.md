# Business Rules Catalog

## Rules

| Rule ID | Rule | Source | System Behavior |
|---|---|---|---|
| BRULE-001 | Provider slots are unique by provider, location, start time, and service. | Scheduling Operations | Reject duplicate confirmed assignment. |
| BRULE-002 | Appointment duration is determined by service type. | Clinical Operations | Calculate end time from configured duration. |
| BRULE-003 | New-patient visits require identity verification before confirmation. | Patient Access | Block confirmation until verified. |
| BRULE-004 | Same-day cancellations require a reason code. | Operations Policy | Require value before submit. |
| BRULE-005 | Waitlist ranking uses urgency class, requested date, and enrollment timestamp. | Patient Access | Sort eligible candidates deterministically. |
| BRULE-006 | Reminder channel follows patient communication preference unless unavailable. | Patient Communications | Use fallback channel when allowed. |
| BRULE-007 | Payment details are tokenized by the gateway; full PAN is never stored. | Security | Store token and result only. |
| BRULE-008 | Staff override requires authorized role and reason. | Compliance | Log override actor and reason. |
| BRULE-009 | Cancelled slots become searchable only after transaction completion. | Scheduling Operations | Prevent transient duplicate exposure. |
| BRULE-010 | Audit events are immutable to application users. | Compliance | Read-only access except platform administrators. |

---

