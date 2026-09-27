# LinkedIn post draft — Azure security engineering portfolio

I’ve been developing an Azure Cloud Security Monitoring & Detection Platform to strengthen my hands-on experience in cloud security, SIEM monitoring, Python, and detection engineering.

The project brings together:
- Microsoft Sentinel, Azure Monitor, Log Analytics, and Azure Activity Logs to centralize security-relevant cloud activity.
- Kusto Query Language (KQL) investigations for failed Azure operations, RBAC changes, and sensitive resource modifications.
- A read-only Python/Flask dashboard and detection engine, with a clearly labeled demonstration mode and an optional authenticated Log Analytics collector.
- GitHub Actions for automated tests and security checks with Bandit and pip-audit.

The latest validated CI run passed 7 tests, reported no Bandit findings, and found no known dependency vulnerabilities.

A key lesson from this build has been separating a working prototype from a fully deployed detection: the code and queries are in GitHub, and live Sentinel rule validation and further Azure screenshots remain on my checklist.

Project and progress: https://github.com/aslambwanika0/azure-security-monitoring-platform/pull/1

#Cybersecurity #CloudSecurity #MicrosoftAzure #MicrosoftSentinel #Python #KQL #DetectionEngineering #DevSecOps

## Suggested LinkedIn image carousel

Use the following **real existing screenshots**, in this order. Open each link, review and redact account/tenant/subscription/personal information, save the image, then upload it as an image attachment to LinkedIn. GitHub images embedded in a Markdown document do **not** automatically attach to a LinkedIn post.

1. [Microsoft Sentinel enabled](screenshots/sentinel-enabled.png)
2. [Azure Activity Logs ingestion](screenshots/azure-activity-logs.png)
3. [First AzureActivity KQL investigation](screenshots/first-kql-query.png)
4. [Log Analytics workspace](screenshots/log-analytics-workspace.png)
5. [Original Flask backend screenshot](screenshots/flask-running.png)

Optional: [Successful automated test/security workflow](https://github.com/aslambwanika0/azure-security-monitoring-platform/actions/runs/36345414327). Capture this directly from GitHub after verifying the display.

Caption idea for first image: **Azure Cloud Security Monitoring & Detection Platform | Portfolio Project**

These original screenshots show Phase 1–3 evidence. Do not represent them as screenshots of the newer live dashboard or deployed analytics rules.
