"""Deterministic triage of Azure Activity events. No automated remediation."""
from collections import Counter
from datetime import datetime, timezone

FAILED = {"failure", "failed"}
ROLE_ASSIGNMENT = "microsoft.authorization/roleassignments/write"
ROLE_DELETION = "microsoft.authorization/roleassignments/delete"
PUBLIC_ACCESS = (
    "microsoft.storage/storageaccounts/write",
    "microsoft.network/networksecuritygroups/securityrules/write",
)

def _value(event, *keys):
    for key in keys:
        value = event.get(key)
        if value is not None:
            return str(value)
    return ""

def analyze(events):
    """Return stable, explainable alerts from a list of AzureActivity-shaped dicts."""
    alerts = []
    for index, event in enumerate(events):
        operation = _value(event, "OperationNameValue", "operation").lower()
        status = _value(event, "ActivityStatusValue", "status").lower()
        caller = _value(event, "Caller", "caller") or "unknown"
        when = _value(event, "TimeGenerated", "time")
        resource = _value(event, "ResourceId", "resource_id", "ResourceGroup")
        common = {
            "id": f"event-{index + 1}",
            "time": when,
            "caller": caller,
            "operation": operation,
            "resource": resource,
            "source": "AzureActivity",
        }
        if status in FAILED:
            alerts.append({**common, "rule": "failed-azure-operation",
                           "severity": "medium", "reason": "Azure reported an unsuccessful operation."})
        if ROLE_ASSIGNMENT in operation and status not in FAILED:
            alerts.append({**common, "rule": "role-assignment-change",
                           "severity": "high", "reason": "Azure RBAC role assignment was written; review the principal and scope."})
        if ROLE_DELETION in operation and status not in FAILED:
            alerts.append({**common, "rule": "role-assignment-deletion",
                           "severity": "medium", "reason": "Azure RBAC role assignment was deleted; verify authorization."})
        if any(item in operation for item in PUBLIC_ACCESS) and status not in FAILED:
            alerts.append({**common, "rule": "security-sensitive-resource-change",
                           "severity": "medium", "reason": "Sensitive storage or network configuration changed; inspect details before treating it as risky."})
    return alerts

def summarize(events, alerts):
    return {
        "event_count": len(events),
        "alert_count": len(alerts),
        "by_severity": dict(Counter(a["severity"] for a in alerts)),
        "by_rule": dict(Counter(a["rule"] for a in alerts)),
    }
