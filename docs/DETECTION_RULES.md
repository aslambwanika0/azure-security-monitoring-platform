# Detection engineering

The four `queries/*.kql` files are **proposed queries**, not evidence of deployed Microsoft Sentinel analytic rules. They rely only on the `AzureActivity` table that was previously verified in the workspace.

1. Open Microsoft Sentinel and choose the configured workspace.
2. Open **Logs** and paste a query; choose the documented time range.
3. Validate its output and tune noise. Empty results do not prove that a rule is broken.
4. For a query suitable for scheduled execution, create an analytics rule in Sentinel, set the query, scheduling, alert threshold, entity mapping, and incident grouping according to your tenant and available permissions.
5. Capture the saved rule, a successful execution, and an incident **only if a real incident is generated**. Redact personal information, subscription IDs, and tokens from screenshots.

This repo never creates cloud resources or automatically changes Azure permissions. The Python engine performs read-only triage. Detection matches require analyst investigation; for example, a role assignment write may be an authorized change.

Entra ID sign-in detections require separate `SigninLogs` ingestion and are intentionally not represented as deployed or validated here.
