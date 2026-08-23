# API Requirements Specification

## Endpoints

| Method | Endpoint | Purpose | Success | Key Validation |
|---|---|---|---|---|
| GET | /api/v1/availability | Search appointment slots | 200 | Filters, eligibility, active provider/location |
| POST | /api/v1/appointments | Create appointment | 201 | Identity, hold, business rules, idempotency |
| GET | /api/v1/appointments/{id} | Retrieve appointment | 200 | User authorization to target appointment |
| PATCH | /api/v1/appointments/{id} | Reschedule/update | 200 | Allowed fields, policy window, concurrency |
| DELETE | /api/v1/appointments/{id} | Cancel appointment | 200 | Cancellation rule, reason where required |
| POST | /api/v1/waitlist | Create waitlist entry | 201 | Eligibility and duplicate entry prevention |
| POST | /api/v1/payments/authorize | Authorize copay | 200 | Token only; amount; appointment context |
| GET | /api/v1/operations/kpis | Retrieve KPI summary | 200 | Authorized manager role |

---

## Common API Requirements

- JSON UTF-8 request/response.
- ISO 8601 timestamps in UTC.
- Idempotency-Key required for create appointment and payment authorization.
- Correlation-ID returned in response headers.
- 400 for schema/validation errors, 401 unauthenticated, 403 unauthorized, 404 not found, 409 state/concurrency conflict, 422 business-rule rejection, 429 throttling, 500 unexpected error, 503 dependency unavailable.
- Validation errors return code, field, message, and correlation ID.
- API version is explicit in URL.
- Sensitive values are never echoed into error messages or logs.

---

## Sample Create Appointment Request

```json
{
  "patientId": "PAT-10482",
  "providerId": "PRV-208",
  "locationId": "LOC-03",
  "serviceTypeId": "SRV-NEWPAT",
  "slotStart": "2026-09-14T14:00:00Z",
  "bookingChannel": "PATIENT_WEB",
  "paymentToken": "tok_sim_91284"
}
```

---

## Sample Response

```json
{
  "appointmentId": "APT-20260914-88412",
  "status": "CONFIRMED",
  "startAt": "2026-09-14T14:00:00Z",
  "confirmationNumber": "CNF-88412",
  "notificationStatus": "QUEUED"
}
```

---

