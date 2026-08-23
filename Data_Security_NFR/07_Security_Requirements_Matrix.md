# Security Requirements Matrix

## Security

| ID | Requirement | Control / Evidence |
|---|---|---|
| SEC-001 | Encrypt data in transit. | TLS configuration evidence |
| SEC-002 | Encrypt production databases and backups at rest. | Platform encryption config |
| SEC-003 | Enforce least-privilege role access. | Role-permission test |
| SEC-004 | Protect secrets outside source code. | Secret-vault configuration |
| SEC-005 | Log privileged and denied actions. | Audit-event test |
| SEC-006 | Mask sensitive values in logs. | Log sample review |
| SEC-007 | Validate input server-side. | Negative test cases |
| SEC-008 | Apply rate limits to public APIs. | Gateway policy |
| SEC-009 | Prevent replay of create/payment requests. | Idempotency-key tests |
| SEC-010 | Perform dependency and application security scanning before release. | Pipeline evidence |
| SEC-011 | Maintain incident escalation for suspected unauthorized access. | Support/runbook evidence |
| SEC-012 | Retain audit data according to approved retention schedule. | Retention policy |

---

