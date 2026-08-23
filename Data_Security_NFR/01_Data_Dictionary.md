# Data Dictionary

## Core Fields

| Entity | Field | Type | Required | Definition / Rule |
|---|---|---|---|---|
| Patient | patient_id | string(20) | Yes | Enterprise patient identifier |
| Patient | preferred_channel | enum | Yes | SMS, EMAIL, BOTH, NONE |
| Appointment | appointment_id | string(30) | Yes | Unique immutable appointment identifier |
| Appointment | start_at | timestamp | Yes | UTC appointment start |
| Appointment | status | enum | Yes | HELD, CONFIRMED, CANCELLED, COMPLETED, NO_SHOW |
| Appointment | booking_channel | enum | Yes | PATIENT_WEB, STAFF, WAITLIST |
| Appointment | version_no | integer | Yes | Optimistic-concurrency version |
| Notification | delivery_status | enum | Yes | QUEUED, SENT, DELIVERED, FAILED |
| Payment | payment_token_ref | string | Conditional | Gateway token reference; never full card number |
| AuditEvent | event_id | UUID | Yes | Unique event identifier |
| AuditEvent | actor_id | string | Yes | User/service that performed action |
| AuditEvent | outcome | enum | Yes | SUCCESS, DENIED, FAILED |

---

