# LinkedIn post package — text and existing project screenshots

## Post text (copy into LinkedIn)

I'm excited to share a cybersecurity portfolio project I've been developing: **Azure Cloud Security Monitoring & Detection Platform!**

I built this project to strengthen my hands-on experience in cloud security, SIEM monitoring, Python automation, and detection engineering.

The platform brings together:

• Microsoft Sentinel, Azure Monitor, and Log Analytics for centralized security monitoring.
• Kusto Query Language (KQL) queries to investigate failed operations, RBAC changes, and security-sensitive Azure activity.
• A Python/Flask security dashboard with an event detection engine, a clearly labeled demo mode, and optional read-only Azure Log Analytics integration.
• Automated testing and security scanning using GitHub Actions, Bandit, and pip-audit.

The initial successful CI run passed all **7 automated tests**, with no Bandit findings or known dependency vulnerabilities.

A key takeaway has been learning how cloud telemetry moves from data ingestion to investigation—and the importance of distinguishing tested application code from live cloud deployment. I'm continuing to validate the Sentinel analytics rules and live dashboard in my Azure environment.

Explore the code, screenshots, and progress:
https://github.com/aslambwanika0/azure-security-monitoring-platform/pull/1

#Cybersecurity #CloudSecurity #MicrosoftAzure #MicrosoftSentinel #Python #KQL #DetectionEngineering #DevSecOps

---

## Existing project images for the LinkedIn carousel

These are actual existing GitHub screenshots, showing Phase 1–3 milestones. Review and redact personal information, account details, subscription/tenant/resource identifiers, and secrets **before** uploading to LinkedIn. Markdown embeds render here and on GitHub, but do not automatically attach to a LinkedIn post; save each image and upload as a multi-image post.

### 1. Microsoft Sentinel enabled
![Microsoft Sentinel enabled](screenshots/sentinel-enabled.png)

### 2. Azure Activity Logs
![Azure Activity Logs ingestion setup](screenshots/azure-activity-logs.png)

### 3. First KQL query
![First AzureActivity KQL query](screenshots/first-kql-query.png)

### 4. Log Analytics workspace
![Azure Log Analytics workspace](screenshots/log-analytics-workspace.png)

### 5. Original Flask backend
![Original local Flask backend](screenshots/flask-running.png)

### Optional CI screenshot
[Successful initial GitHub Actions test/security run](https://github.com/aslambwanika0/azure-security-monitoring-platform/actions/runs/36345414327) — capture a fresh screenshot in GitHub if desired.

These images do not prove newer analytics rules were deployed or that the new dashboard was authenticated against live Azure. See [live validation runbook](LIVE_VALIDATION_RUNBOOK.md).
