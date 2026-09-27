from backend.detection import analyze, summarize

def test_failed_operation_creates_medium_alert():
    alerts = analyze([{"OperationNameValue": "Microsoft.Compute/virtualMachines/write",
                       "ActivityStatusValue": "Failure", "Caller": "example"}])
    assert len(alerts) == 1
    assert alerts[0]["rule"] == "failed-azure-operation"

def test_role_assignment_success_creates_high_alert():
    alerts = analyze([{"OperationNameValue": "Microsoft.Authorization/roleAssignments/write",
                       "ActivityStatusValue": "Success"}])
    assert alerts[0]["severity"] == "high"

def test_successful_generic_event_generates_no_alert():
    events = [{"OperationNameValue": "Microsoft.Resources/resourceGroups/write",
               "ActivityStatusValue": "Success"}]
    assert analyze(events) == []
    assert summarize(events, [])["event_count"] == 1

def test_failed_rbac_write_does_not_claim_successful_change():
    alerts = analyze([{"OperationNameValue": "Microsoft.Authorization/roleAssignments/write",
                       "ActivityStatusValue": "Failure"}])
    assert [a["rule"] for a in alerts] == ["failed-azure-operation"]
