# Reviewer guide and asset provenance checklist

**Project:** system-analyst-portfolio · [README](README.md) · [License](LICENSE) · [CI runs](https://github.com/JamieChristian22/system-analyst-portfolio/actions)

## Five-minute review

1. Read the root README for purpose, limitations, and simulated versus measured results.
2. Open the project paths below to inspect tracked deliverables; their presence alone is not proof of correctness.
3. Review GitHub Actions for actual test outcomes. Queued or failed runs are not passing tests.
4. Verify input datasets, calculation methods, and evidence before citing performance outcomes.

### Project entry points

1. [Data_Security_NFR](<Data_Security_NFR>)
2. [Healthcare_Appointment_System_Case_Study](<Healthcare_Appointment_System_Case_Study>)
3. [Implementation_Support](<Implementation_Support>)
4. [Process_System_Models](<Process_System_Models>)
5. [Reports_Dashboards](<Reports_Dashboards>)
6. [Requirements_Documentation](<Requirements_Documentation>)
7. [System_Analysis_Integration](<System_Analysis_Integration>)

## Third-party asset and dataset provenance checklist

The following are **sample tracked candidates** for source and reuse-rights checks. Their inclusion does not imply they are external, unlicensed, or unsafe.

| Tracked asset candidate | Verification status |
| --- | --- |
| `Reports_Dashboards/01_Executive_KPI_and_System_Health_Dashboard.xlsx` | **Not independently verified** — check origin and permissions |
| `Reports_Dashboards/KPI_Dashboard.xlsx` | **Not independently verified** — check origin and permissions |
| `Reports_Dashboards/KPI_Dashboard_Formatted.png` | **Not independently verified** — check origin and permissions |
| `System_Analysis_Integration/05_Integration_Data_Analysis.xlsx` | **Not independently verified** — check origin and permissions |
| `System_Analysis_Integration/CONTEXT DIAGRAM (LEVEL 0).png` | **Not independently verified** — check origin and permissions |
| `System_Analysis_Integration/HIGH-LEVEL ARCHITECTURE.png` | **Not independently verified** — check origin and permissions |
| `System_Analysis_Integration/PAYMENT INTEGRATION FLOW.png` | **Not independently verified** — check origin and permissions |
| `Testing_UAT/04_UAT_Test_Cases_and_Defect_Log.xlsx` | **Not independently verified** — check origin and permissions |

For each external asset, record original source URL, creator/provider, terms, allowed redistribution and commercial use, and any required notices. For original or synthetic work, note how it was produced and ensure any modeled results are plainly labeled. The MIT repository license does not automatically grant rights to externally owned content.

**Security:** Never include API keys, private/customer data, or identifying screenshots in an evidence file. Treat current-branch scanning and historical secret scanning as separate checks.

This document is **navigation and review guidance**, not a security audit pass, ownership certification, or legal clearance. See [GitHub Actions](https://github.com/JamieChristian22/system-analyst-portfolio/actions) for live test results.
