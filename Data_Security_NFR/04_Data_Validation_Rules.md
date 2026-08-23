# Data Validation Rules

## Validation

| ID | Field / Object | Rule | Error |
|---|---|---|---|
| DV-001 | patient_id | Must exist and be active in patient identity source. | PATIENT_NOT_FOUND |
| DV-002 | start_at | Must be future and within published scheduling horizon. | INVALID_SLOT_DATE |
| DV-003 | appointment status | Must follow allowed state transitions. | INVALID_STATE_TRANSITION |
| DV-004 | provider/service | Provider must be authorized for service type. | PROVIDER_SERVICE_MISMATCH |
| DV-005 | payment amount | Must equal configured copay amount for transaction context. | PAYMENT_AMOUNT_MISMATCH |
| DV-006 | phone | E.164-compatible normalization before notification. | INVALID_PHONE |
| DV-007 | email | Valid email format and length <=254. | INVALID_EMAIL |
| DV-008 | cancellation reason | Required for same-day cancellation. | REASON_REQUIRED |
| DV-009 | override | Requires permitted role and non-empty reason. | OVERRIDE_NOT_AUTHORIZED |
| DV-010 | event_id | Must be unique for event consumer idempotency. | DUPLICATE_EVENT |

---

