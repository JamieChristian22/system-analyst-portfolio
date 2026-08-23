# Rollback Plan

## Triggers

Rollback is considered when confirmed bookings cannot be created reliably, data integrity is at risk, access controls fail materially, critical dependencies cause broad failure without workable degraded mode, or Severity 1 defects cannot be contained within the approved recovery window.

---

## Steps

1. Executive/App Owner declares rollback.
2. Disable new patient web bookings.
3. Place application into controlled maintenance mode.
4. Stop background event consumers.
5. Restore prior application release.
6. Roll back compatible database changes or restore validated snapshot when required.
7. Re-enable prior staff scheduling workflow.
8. Validate patient/provider data control totals.
9. Communicate status to staff and support.
10. Open incident and RCA record.
11. Preserve logs and deployment evidence.

---

## Recovery Objective

Target rollback execution within **60 minutes** of decision for application-only rollback. Database recovery follows the approved RTO/RPO requirements.

---

