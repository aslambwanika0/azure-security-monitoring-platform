"""Read AzureActivity using Azure Identity and Log Analytics query API."""
import os
from datetime import timedelta
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, LogsQueryStatus

QUERY = """
AzureActivity
| where TimeGenerated > ago(7d)
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue, ResourceGroup, ResourceId, CorrelationId
| sort by TimeGenerated desc
| take 500
"""

def collect():
    workspace_id = os.getenv("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "").strip()
    if not workspace_id:
        raise RuntimeError("AZURE_LOG_ANALYTICS_WORKSPACE_ID is missing; use APP_MODE=demo for sample data.")
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=True)
    with LogsQueryClient(credential) as client:
        response = client.query_workspace(workspace_id, QUERY, timespan=timedelta(days=7))
    if response.status == LogsQueryStatus.PARTIAL:
        raise RuntimeError(f"Azure returned partial results: {response.partial_error}")
    if response.status != LogsQueryStatus.SUCCESS:
        raise RuntimeError("Azure Log Analytics query failed.")
    rows = []
    for table in response.tables:
        columns = [column.name for column in table.columns]
        for row in table.rows:
            rows.append({key: value.isoformat() if hasattr(value, "isoformat") else value
                         for key, value in zip(columns, row)})
    return rows
