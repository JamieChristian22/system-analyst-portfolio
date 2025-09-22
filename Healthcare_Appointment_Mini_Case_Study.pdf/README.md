## 📄 Mini Case Study — Healthcare Appointment System

[![Case Study PDF](https://img.shields.io/badge/Case_Study-PDF-9b59b6)](Healthcare_Appointment_Mini_Case_Study.pdf)
[![Domain: Healthcare](https://img.shields.io/badge/Domain-Healthcare-0ea5e9)](#)
[![Method: BPMN](https://img.shields.io/badge/Method-BPMN-10b981)](_Process_Models_Diagrams/BPMN_AsIs_Swimlane_v2.png)
[![Method: UML](https://img.shields.io/badge/Method-UML-14b8a6)](_Process_Models_Diagrams/UML_UseCase_Updated.png)
[![Method: DFD](https://img.shields.io/badge/Method-DFD-22c55e)](_Process_Models_Diagrams/DFD_Level1_Updated.png)
[![Method: ERD](https://img.shields.io/badge/Method-ERD-84cc16)](_Process_Models_Diagrams/ERD_Updated.png)

**Download / Preview:**  
[**Healthcare_Appointment_Mini_Case_Study.pdf**](Healthcare_Appointment_Mini_Case_Study.pdf)

**Context**  
Manual, phone-based scheduling led to long wait times, data entry errors, and missed revenue from no-shows. I designed and delivered an online appointment solution with end-to-end flows for search, booking, reminders, and payments.

**My Role (Systems Analyst / BA)**  
- Elicited & documented requirements (**BRD, FRS, NFR**)  
- Modeled processes & data (**BPMN As-Is/To-Be, DFD L0/L1, UML Use Case, ERD**)  
- Drove integration design (**Auth, Notifications, Payments**) and RTM mapping  
- Led **UAT** planning, test cases, and sign-off evidence

**Scope & Integrations**  
- Patient portal (web/mobile) with provider search & availability  
- Notifications (email/SMS) for confirmations and reminders  
- Payment gateway for deposits/co-pays, with secure webhooks  
- Admin console for schedules, overrides, and reporting exports

**Approach**  
1. **Discovery** → stakeholder interviews, pain-point analysis, KPI baseline  
2. **Design** → process maps, data model, integration contracts, NFRs  
3. **Traceability** → RTM tying requirements → test cases → reports  
4. **UAT** → end-to-end scenarios, defect triage, sign-off  
5. **Reporting** → KPI dashboard aligned to business outcomes

**Outcomes (pilot / mock data)**

| KPI                         | Baseline | Target | Outcome | Status    |
|----------------------------|:--------:|:------:|:-------:|-----------|
| Average Booking Time (min) |   3.5    | ≤ 2.0  | **1.8** | On Track  |
| No-Show Rate (%)           |   12%    | < 10%  | **8%**  | On Track  |
| Billing Accuracy (%)       |   88%    | ≥ 98%  | **95%** | Improving |
| Staff Utilization (%)      |   75%    | ≥ 85%  | **88%** | On Track  |

**Supporting Artifacts (linked in this repo)**  
- Requirements: `Requirements Documentation/BRD_Healthcare_Appointment_System.docx`, `FRS_…`, `NFR_…`  
- Models & Diagrams: `_Process_Models_Diagrams/` (BPMN, DFD, ERD, Use Case)  
- Integration: `System_Analysis_Integration/System_Architecture_Diagram.png`, `_Process_Models_Diagrams/Payment_Integration_Flow_v2.png`  
- Testing & Quality: `Testing_UAT/` (UAT Plan, Test Cases, Feedback incl. Filled)  
- Traceability & Stakeholders: `Traceability_Stakeholders/` (RTM, RACI, Map)  
- Analytics: `Reports_Dashboards/KPI_Dashboard_Formatted.png`

> If the PDF preview doesn’t load in GitHub’s viewer, use the raw link:  
> `https://raw.githubusercontent.com/JamieChristian22/system-analyst-portfolio/main/Healthcare_Appointment_Mini_Case_Study.pdf`

<p align="right"><a href="#top">↑ Back to top</a></p>
