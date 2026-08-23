# Interface Control Document

## Interface Inventory

| ID | Interface | Direction | Protocol | Authentication | SLA | Failure Handling |
|---|---|---|---|---|---|---|
| INT-001 | Identity Provider | Inbound/Outbound | OIDC/OAuth 2.0 | Signed JWT | 99.95% | Deny access; log correlation ID |
| INT-002 | Patient Identity/MPI | Outbound query | REST/JSON | mTLS + service token | p95 <2s | Retry 2x; exception queue |
| INT-003 | Provider Schedule Source | Bidirectional | REST/JSON | mTLS + OAuth | p95 <2s | Retry transient; do not confirm stale slot |
| INT-004 | Notification Provider | Outbound | REST/JSON | API credential vault | 99.9% | Retry 3x; dead-letter queue |
| INT-005 | Payment Gateway | Outbound | REST/JSON | Tokenized gateway auth | p95 <3s | No appointment commit if mandatory payment fails |
| INT-006 | Reporting Platform | Outbound batch | SFTP/CSV | SSH key | Daily by 05:00 | Alert and rerun once |
| INT-007 | Central Logging | Outbound stream | HTTPS/JSON | Service identity | <60 sec lag | Local buffer and alert |

---

## Interface Principles

- Every request carries a correlation ID.
- No interface stores credentials in application configuration files.
- Transient failures are retried only when the operation is idempotent or protected by an idempotency key.
- Duplicate inbound/outbound events are safely ignored using event IDs.
- PHI is minimized to the fields required by the receiving system.
- Interface failures are observable through structured logs and alerts.

---

