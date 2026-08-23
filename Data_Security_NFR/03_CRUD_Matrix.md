# CRUD Matrix

## Matrix

| Role / Component | Patient | Appointment | Waitlist | Payment | Notification | Audit |
|---|---|---|---|---|---|---|
| Patient User | R limited | C/R/U/Cancel own | C/R/Delete own | C/R own result | R own | None |
| Scheduler | R | C/R/U/Cancel | C/R/U | R result | R | R scoped |
| Operations Manager | R aggregated | R/U override | R/U | R summary | R summary | R |
| Scheduling Service | R | C/R/U | R | R | C event | C |
| Waitlist Service | R | C via offer | C/R/U/Delete | None | C event | C |
| Payment Adapter | R minimum | R | None | C/R/U | None | C |
| Notification Worker | R minimum | R | R | None | C/R/U | C |
| Compliance Analyst | None | R metadata | R metadata | R metadata | R metadata | R |

---

