# Authentication & Authorization Matrix

## Roles

| Role | Authentication | Key Permissions | Restrictions |
|---|---|---|---|
| Patient | OIDC identity + configured verification | Manage own eligible appointments; own waitlist; own payment result | Cannot view other patients or override policy |
| Scheduler | Enterprise SSO + MFA | Search patients; create/reschedule/cancel; view limited audit | Cannot manage access roles |
| Operations Manager | Enterprise SSO + MFA | Reporting, overrides, operational audit | Override reason required |
| Compliance Analyst | Enterprise SSO + MFA | Read audit metadata and compliance reports | No appointment modification |
| Support Analyst | Enterprise SSO + MFA | View operational status, retry failed notifications where allowed | PHI limited to minimum necessary |
| Platform Administrator | Privileged identity + MFA | Configuration and platform operations | No business-policy override unless separately assigned |

---

## Authorization Requirements

- Authorization is evaluated server-side.
- Patient access is object-scoped to the authenticated patient identity.
- Staff permissions derive from enterprise groups/claims.
- Privileged roles require MFA.
- Administrative actions generate audit events.
- Access-denied patterns are forwarded to security monitoring.
- Temporary elevated access uses approved time-limited process.

---

