# System Event Catalog

## Events

| Event | Producer | Consumers | Required Fields | Purpose |
|---|---|---|---|---|
| AppointmentBooked | Scheduling Service | Notifications, Audit, Reporting | appointmentId, patientId, startAt, channel, eventId | Confirmation and KPI |
| AppointmentRescheduled | Scheduling Service | Notifications, Audit, Reporting | appointmentId, oldStart, newStart, eventId | Updated reminder and traceability |
| AppointmentCancelled | Scheduling Service | Notifications, Audit, Waitlist, Reporting | appointmentId, reason, eventId | Release slot and notify |
| WaitlistOfferCreated | Waitlist Service | Notifications, Audit | waitlistId, appointmentSlotId, expiresAt | Offer earlier slot |
| PaymentAuthorized | Payment Adapter | Audit, Reporting | appointmentId, amount, tokenRef, result | Financial traceability |
| NotificationDelivered | Notification Worker | Audit, Reporting | appointmentId, channel, deliveredAt | Reminder KPI |
| NotificationFailed | Notification Worker | Operations, Audit | appointmentId, channel, errorCode | Support workflow |
| AccessDenied | API/Auth | Security Monitoring, Audit | userId, resource, action, reason | Security visibility |

---

