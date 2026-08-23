# Source-to-Target Data Mapping

## Mapping

| Source | Source Field | Transformation | Target | Target Field | Validation |
|---|---|---|---|---|---|
| MPI | enterprisePatientId | Direct | Patient | patient_id | Non-null, unique |
| MPI | dateOfBirth | ISO date normalization | Patient | date_of_birth | Valid past date |
| Provider API | providerId | Direct | Provider | provider_id | Active provider |
| Provider API | slotStart | Convert to UTC | AppointmentSlot | start_at | Future timestamp |
| Booking UI | bookingChannel | Map controlled value | Appointment | booking_channel | Allowed enum |
| Payment Gateway | token | Store reference only | Payment | payment_token_ref | Must not match PAN pattern |
| Payment Gateway | authCode | Direct | Payment | authorization_code | Required when approved |
| Notification API | providerMessageId | Direct | Notification | provider_message_id | Unique when sent |
| Notification API | deliveredAt | Convert to UTC | Notification | delivered_at | >= sent_at |
| Application | correlationId | Direct | AuditEvent | correlation_id | Required on material events |

---

