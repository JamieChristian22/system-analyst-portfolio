# Defect Triage Workflow

## Workflow

```mermaid
flowchart LR
A[Defect Logged] --> B[Validate Reproducibility]
B --> C[Assign Severity/Priority]
C --> D[Owner Assigned]
D --> E[Fix / Configuration]
E --> F[QA Retest]
F --> G{Passed?}
G -- No --> D
G -- Yes --> H[Business Confirmation if UAT]
H --> I[Closed]
```

---

## Severity

| Severity | Definition | Target Response |
|---|---|---|
| Sev 1 | Critical service / patient-safety or major control failure; no workaround | Immediate triage |
| Sev 2 | Major workflow failure; limited workaround | Same business day |
| Sev 3 | Moderate defect; workaround available | Within 2 business days |
| Sev 4 | Cosmetic / minor usability | Planned backlog |

---

