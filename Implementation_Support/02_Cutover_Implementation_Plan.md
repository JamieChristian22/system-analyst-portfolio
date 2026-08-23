# Cutover & Implementation Plan

## Strategy

Phased production launch begins with staff-assisted use, then enables patient self-service for two pilot locations before broader rollout. This reduces operational risk and creates measurable checkpoints.

---

## Cutover Schedule

| Time | Activity | Owner | Success Check |
|---|---|---|---|
| T-7 days | Freeze production configuration changes | App Owner | Change freeze active |
| T-2 days | Final reference-data reconciliation | Data Lead | 100% control totals |
| T-1 day | Production endpoint smoke tests | Integration Lead | All critical dependencies pass |
| T-4 hrs | Deploy release | DevOps | Pipeline successful |
| T-3 hrs | Database migrations | DBA | Migration checks pass |
| T-2 hrs | Application smoke test | QA | Critical paths pass |
| T-90 min | Staff role validation | Security / Ops | Required users authenticated |
| T-60 min | Monitoring and alert check | Support | Alerts visible |
| T-30 min | Go/No-Go review | Sponsor/App Owner | Go decision |
| T0 | Enable staff workflow | Operations | First test booking successful |
| T+4 hrs | Enable pilot patient web booking | Product/Ops | Booking and notification success |
| T+24 hrs | Hypercare checkpoint | Program Team | No critical incidents |

---

## Go / No-Go Thresholds

No-go if a Severity 1 defect is open, a critical dependency is unavailable, database reconciliation fails, production authentication fails for required roles, or rollback cannot be executed.

---

