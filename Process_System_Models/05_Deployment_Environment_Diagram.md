# Deployment & Environment Model

## Deployment

```mermaid
flowchart TB
subgraph Internet
U[Patient Browser]
end
subgraph DMZ
WAF[WAF / Load Balancer]
end
subgraph Application
WEB[Web Tier]
API[API Tier]
WORK[Background Workers]
end
subgraph Data
DB[(Relational DB)]
CACHE[(Cache)]
AUD[(Audit Store)]
end
subgraph Enterprise
IDP[Identity Provider]
MON[Monitoring / Logging]
end
U --> WAF --> WEB --> API
API --> DB
API --> CACHE
WORK --> DB
WORK --> AUD
API --> IDP
WEB --> MON
API --> MON
WORK --> MON
```

---

## Environments

| Environment | Purpose | Data | Deployment |
|---|---|---|---|
| Development | Developer integration | Synthetic | On demand |
| Test | System/integration testing | Synthetic | CI/CD |
| UAT | Business validation | Masked/synthetic | Controlled release candidate |
| Staging | Production-like readiness | Masked | Release pipeline |
| Production | Live operations | Production PHI | Approved pipeline with change record |

---

