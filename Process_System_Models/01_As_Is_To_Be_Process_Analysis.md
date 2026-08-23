# As-Is / To-Be Process Analysis

## As-Is

```mermaid
flowchart LR
A[Patient Calls] --> B[Waits in Queue]
B --> C[Staff Verifies Patient]
C --> D[Staff Checks Multiple Calendars]
D --> E{Slot Available?}
E -- No --> F[Offer Callback / Manual Waitlist]
E -- Yes --> G[Enter Appointment]
G --> H[Manual Confirmation]
H --> I[Manual Reminder Process]
I --> J[Appointment]
```

---

## Current-State Issues

- Multiple manual handoffs
- Staff searches calendars sequentially
- No automated hold against concurrent booking
- Limited reminder automation
- Manual waitlist follow-up
- Weak auditability
- High dependency on call-center availability

---

## To-Be

```mermaid
flowchart LR
A[Patient or Staff Starts Search] --> B[Identity / Role Validation]
B --> C[Search Availability Service]
C --> D[Eligible Slots]
D --> E[Temporary Slot Hold]
E --> F[Rules / Payment Validation]
F --> G{Valid?}
G -- No --> H[Release Hold + Error]
G -- Yes --> I[Commit Appointment]
I --> J[Confirmation Event]
J --> K[Notification Service]
I --> L[Reporting / Audit Event]
```

---

## Expected Improvement

The future-state design reduces manual lookup, centralizes business rules, introduces transaction-safe slot holding, automates reminders, strengthens auditability, and provides a consistent workflow across patient and staff channels.

---

