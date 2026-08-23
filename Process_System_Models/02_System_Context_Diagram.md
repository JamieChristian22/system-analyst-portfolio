# System Context Diagram

## Context

```mermaid
flowchart TB
P[Patient] --> AMS[Appointment Management System]
S[Scheduling Staff] --> AMS
M[Operations Manager] --> AMS
AMS --> MPI[Patient Identity / Master Patient Index]
AMS --> CAL[Provider Scheduling Source]
AMS --> NOTIF[SMS / Email Provider]
AMS --> PAY[Payment Gateway]
AMS --> BI[Reporting Platform]
AMS --> IAM[Identity Provider]
AMS --> LOG[Central Logging / Monitoring]
```

---

## System Boundary

The Appointment Management System owns appointment search orchestration, temporary holds, booking state, waitlist state, rule enforcement, staff workflow, audit generation, and operational reporting extracts. Patient identity, provider-source data, outbound messaging transport, payment processing, and enterprise identity are external dependencies.

---

