# Complete the live Azure evidence (operator runbook)

This portion requires access to Aslam's own Azure tenant. The repository's Python code and CI are implemented and tested; live Azure deployment and screenshots have **not** been independently verified.

## 1. Protect your identity and budget
- Keep `.env` out of Git and avoid sharing tenant IDs, subscription IDs, resource identifiers, personal sign-in records, or secrets in screenshots.
- Check the subscription's Azure cost/budget settings before running recurring analytics.
- Verify the existing Central US Log Analytics workspace and Sentinel configuration in the Azure portal.

## 2. Run and verify the dashboard locally
From a **fresh, project-root clone** of this branch (not from the Mac home-directory Git root):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m backend.app
```

Open http://127.0.0.1:5001 and verify the **DEMO DATA** label. Capture `docs/screenshots/dashboard-demo.png` (synthetic demo only).

For live data, authenticate with `az login` and create a local `.env` based on `.env.example`:
```dotenv
APP_MODE=live
AZURE_LOG_ANALYTICS_WORKSPACE_ID=<workspace-guid>
PORT=5001
```
The account must have workspace query permissions. Restart the application and confirm `/api/summary` reports `"mode":"live"`. A 503 response means live data could not be queried and is **not** evidence of a live dashboard. If successful, capture `dashboard-live.png` with sensitive values redacted.

## 3. Query and validate in Sentinel
In Azure Portal → Microsoft Sentinel → the previously configured workspace → Logs, run each file under `queries/` using the corresponding data/time range. Verify that `AzureActivity` is present and that the schema matches. Empty detections can be normal and should not be represented as successful alerts.

For a suitable query, use Microsoft Sentinel → Analytics → Create → Scheduled query rule. Set:
- Rule name, description, appropriate tactics, and severity;
- KQL from the verified query;
- Query schedule/lookback and result threshold tuned to your lab;
- Entity mapping only where supported by the actual table/columns;
- Incident creation and grouping according to your lab goals.

Review the preview/query results and save the rule. The UI and available controls vary by tenant. Capture the rule details and status after successful creation as `sentinel-analytics-rule.png`.

If your Azure workspace actually creates an alert/incident, capture its details with sensitive fields redacted. **Do not invent an incident or use a fabricated screenshot.**

## 4. GitHub proof
Open Actions → Python tests and security checks and save a screenshot showing the result. GitHub run 36345414327 on September 27, 2026 completed successfully with 7 tests, no Bandit findings and no known vulnerabilities in the dependency audit. A subsequent commit upgrades checkout/setup-python actions; use the newest successful run when capturing.

## 5. Safely add authentic screenshots
Place only the reviewed/redacted evidence within this project's `docs/screenshots/` in the **clean clone**, check status for unexpected files, and stage the screenshot filenames explicitly:

```bash
git status --short
git add docs/screenshots/dashboard-demo.png
# Add other screenshot filenames only after they exist and are reviewed.
git diff --cached --name-only
git commit -m "Document validated dashboard and Sentinel evidence"
git push origin feat/complete-security-platform
```

Do not run `git add .` in the older Mac home-directory Git repository. Do not merge PR #1 until you reconcile its code with the untracked Mac-local `backend/` and `tests/` directories.
