# Logging & Monitoring Requirements

## Monitoring

| ID | Signal | Threshold / Objective | Response |
|---|---|---|---|
| MON-001 | API availability | >=99.9% monthly | P1 if broad outage |
| MON-002 | Search latency p95 | <=3 sec | Investigate if >3 sec for 10 min |
| MON-003 | Booking success rate | >=98.5% excluding business-rule rejection | Alert if <97% for 5 min |
| MON-004 | Notification delivery | >=95% | Alert if <90% over 15 min |
| MON-005 | Payment dependency errors | <2% | Alert if >5% for 5 min |
| MON-006 | Dead-letter queue | 0 normal steady state | Alert when >10 |
| MON-007 | Access denied anomaly | Baseline + security rules | Security alert |
| MON-008 | Reporting extract | Complete by 05:00 | Alert if missing by 05:15 |

---

## Logging Standard

Structured logs include timestamp, service, environment, correlation ID, event/result code, duration, dependency name where applicable, and non-sensitive technical context. Logs must not contain full payment card data, authentication secrets, or unnecessary PHI.

---

