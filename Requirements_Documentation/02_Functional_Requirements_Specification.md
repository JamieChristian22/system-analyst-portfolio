# Functional Requirements Specification

## Functional Scope

The appointment platform is decomposed into six functional domains: Identity & Access, Search & Availability, Appointment Management, Notifications, Payments, and Reporting/Audit.

---

## Functional Requirements

| ID | Function | Requirement | Validation |
|---|---|---|---|
| FR-001 | Identity | Validate patient identity using patient ID plus configured verification factor. | UAT-01 |
| FR-002 | Search | Filter slots by service, provider, location, date, and eligibility. | UAT-02 |
| FR-003 | Availability | Display only active, unreserved, policy-eligible slots. | UAT-03 |
| FR-004 | Booking | Temporarily hold selected slot for 5 minutes during confirmation. | UAT-04 |
| FR-005 | Booking | Commit appointment transaction atomically and release hold on failure. | UAT-05 |
| FR-006 | Reschedule | Create replacement slot reservation before cancelling original appointment. | UAT-06 |
| FR-007 | Cancellation | Apply cancellation-reason code and policy validation. | UAT-07 |
| FR-008 | Waitlist | Add eligible patient to ranked waitlist by requested service/location/date window. | UAT-08 |
| FR-009 | Notification | Send confirmation immediately after successful booking. | UAT-09 |
| FR-010 | Notification | Schedule reminders 48 and 24 hours before eligible appointment. | UAT-10 |
| FR-011 | Payment | Request tokenized payment authorization from external payment gateway. | UAT-11 |
| FR-012 | Staff Console | Allow authorized staff to search patients and manage appointments. | UAT-12 |
| FR-013 | Reporting | Produce daily scheduling metrics by channel, location, service, and provider. | UAT-13 |
| FR-014 | Audit | Record create/update/cancel/login/access-denied/payment-result events. | UAT-14 |
| FR-015 | Integration | Retry transient notification failures up to 3 times using backoff. | UAT-15 |
| FR-016 | Integration | Route unrecoverable interface failures to an operations exception queue. | UAT-16 |

---

## Business Logic

- A provider slot cannot have more than one confirmed appointment.
- A held slot expires after 5 minutes if booking is not committed.
- Cancellation inside a configured restricted window requires staff intervention.
- A patient cannot hold more than one active appointment for the same service within the duplicate-service window unless overridden by authorized staff.
- Waitlist offers expire after 30 minutes.
- Payment failure does not create a confirmed appointment when payment is mandatory.
- Notification failure does not cancel an already confirmed appointment.

---

