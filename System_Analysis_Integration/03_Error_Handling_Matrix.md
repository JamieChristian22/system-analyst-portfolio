# Integration & Application Error Handling Matrix

## Matrix

| Code | Condition | User Response | System Response | Alert? |
|---|---|---|---|---|
| APP-4001 | Invalid search filter | Explain invalid field | Reject request | No |
| APP-4091 | Slot already booked | Ask user to select another slot | Release hold, return fresh search link | No |
| APP-4221 | Duplicate-service rule | Explain policy | Do not create appointment | No |
| INT-5031 | Provider schedule unavailable | Temporary unavailable message | Retry 2x, log dependency failure | Yes after retry |
| INT-5021 | Notification provider error | Appointment remains confirmed | Retry 3x then dead-letter | Yes on terminal failure |
| PAY-4021 | Payment declined | Explain payment not approved | Do not confirm mandatory-payment appointment | No |
| PAY-5031 | Gateway unavailable | Temporary payment error | Release hold after timeout | Yes |
| SEC-4031 | Unauthorized operation | Generic access denied | Log security audit event | Yes if repeated pattern |
| SYS-5001 | Unexpected server error | Generic error with reference ID | Log stack/correlation, rollback transaction | Yes |

---

