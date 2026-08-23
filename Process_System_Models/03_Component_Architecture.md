# Application Component Architecture

## Architecture

```mermaid
flowchart LR
WEB[Patient Web UI] --> API[API Gateway]
STAFF[Staff Console] --> API
API --> AUTH[Auth Adapter]
API --> SCHED[Scheduling Service]
API --> WAIT[Waitlist Service]
API --> PAY[Payment Adapter]
SCHED --> RULES[Rules Engine]
SCHED --> DB[(Appointment DB)]
WAIT --> DB
SCHED --> EVENTS[Event Publisher]
EVENTS --> NOTIF[Notification Worker]
EVENTS --> AUDIT[Audit Worker]
NOTIF --> NPROV[SMS/Email Provider]
PAY --> PGW[Payment Gateway]
AUDIT --> LOG[(Audit Store)]
DB --> ETL[Reporting Extract]
ETL --> BI[Operations Dashboard]
```

---

## Responsibilities

| Component | Responsibility |
|---|---|
| API Gateway | Request routing, throttling, correlation ID |
| Auth Adapter | Identity token validation and role claims |
| Scheduling Service | Search orchestration, slot holds, booking state |
| Rules Engine | Eligibility, cancellation, duplicate-service, override rules |
| Waitlist Service | Enrollment, ranking, offer lifecycle |
| Payment Adapter | Tokenized authorization requests and result handling |
| Event Publisher | Durable business-event publication |
| Notification Worker | Confirmation/reminder delivery and retry |
| Audit Worker | Immutable audit-event persistence |
| Reporting Extract | Curated operational KPI feed |

---

