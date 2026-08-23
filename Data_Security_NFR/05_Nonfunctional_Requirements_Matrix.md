# Nonfunctional Requirements Matrix

## NFRs

| ID | Category | Requirement | Verification |
|---|---|---|---|
| NFR-001 | Performance | Availability search p95 <=3 seconds at 200 concurrent users. | Load test |
| NFR-002 | Performance | Appointment commit p95 <=4 seconds excluding user think time. | Load test |
| NFR-003 | Availability | Monthly service availability >=99.9%, excluding approved maintenance. | Monitoring report |
| NFR-004 | Scalability | Support 2x forecast peak without architecture redesign. | Capacity test |
| NFR-005 | Security | All external traffic uses TLS 1.2+; secrets stored in managed vault. | Security review |
| NFR-006 | Access | Role-based authorization enforced server-side for every protected operation. | Security/UAT |
| NFR-007 | Audit | Material audit events available within 60 seconds. | Integration test |
| NFR-008 | Recovery | RTO <=2 hours; RPO <=15 minutes for appointment data. | DR exercise |
| NFR-009 | Backup | Encrypted backups retained 35 days; restore tested quarterly. | Ops evidence |
| NFR-010 | Observability | 100% of API requests carry correlation IDs and structured result logging. | Log review |
| NFR-011 | Usability | Core patient booking flow meets WCAG 2.1 AA design requirements. | Accessibility test |
| NFR-012 | Data | No full payment card number stored in application data stores or logs. | Data/security scan |

---

