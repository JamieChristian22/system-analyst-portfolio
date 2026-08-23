# User Stories & Acceptance Criteria

## Stories

| ID | User Story | Acceptance Criteria |
|---|---|---|
| US-001 | As a patient, I want to search available appointments so I can choose a convenient time. | Eligible slots only; filters apply; results in <=3 seconds at p95. |
| US-002 | As a patient, I want to book online so I do not need to call. | Slot held, identity validated, rules pass, appointment ID generated, confirmation sent. |
| US-003 | As a patient, I want reminders so I remember my appointment. | 48h and 24h reminders scheduled where eligible; delivery outcome logged. |
| US-004 | As a scheduler, I want to book for a patient so I can support callers. | Authorized role; patient selected; same validation rules; actor audit captured. |
| US-005 | As a scheduler, I want to override configured restrictions when policy permits. | Override limited to permitted roles; reason required; audit event created. |
| US-006 | As an operations manager, I want appointment KPIs so I can identify access and utilization issues. | Dashboard by location/service/provider/channel with daily refresh. |
| US-007 | As a patient, I want to join a waitlist so I can receive an earlier appointment. | Eligibility checked; preference window stored; rank calculated. |
| US-008 | As a compliance analyst, I want an audit trail so sensitive actions are traceable. | Actor, action, timestamp, target object, result, source channel retained. |

---

