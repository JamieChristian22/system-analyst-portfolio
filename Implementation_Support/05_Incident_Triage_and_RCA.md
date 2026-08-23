# Incident Triage & Root Cause Analysis

## Incident Example

**Incident:** INC-2026-017  
**Severity:** P2  
**Symptom:** A subset of confirmed appointments did not receive SMS confirmation during a 43-minute period.  
**Customer Impact:** 64 appointments affected; bookings remained valid. Email confirmations were delivered for users with email preference.  
**Detection:** Notification failure-rate alert exceeded 5% threshold.

---

## Timeline

| Time | Event |
|---|---|
| 10:12 | Notification error rate alert triggered |
| 10:17 | Tier 2 confirmed SMS provider timeout pattern |
| 10:23 | Incident owner assigned and vendor status checked |
| 10:31 | Retry queue paused to avoid repeated provider load |
| 10:44 | Provider service recovered |
| 10:49 | Retry queue resumed with rate limit |
| 10:55 | Delivery success returned above 98% |
| 11:08 | 64 failed confirmations reprocessed successfully |

---

## Root Cause

The SMS provider experienced elevated timeout rates. The application retry policy retried quickly enough to amplify request pressure during the degraded period. Booking transactions were unaffected because notifications are asynchronous.

---

## Corrective Actions

1. Change retry policy to exponential backoff with jitter.
2. Add circuit-breaker behavior at configured failure threshold.
3. Add provider-status health signal to support dashboard.
4. Add operational runbook for notification-provider degradation.
5. Add regression test for sustained dependency timeouts.
6. Track delivery by channel to identify fallback opportunities.

---

