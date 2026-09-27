# Evidence checklist

Existing Phase 1–3 screenshots are copied to the repository-root `docs/screenshots/` without altering their bytes. The older nested copies remain in Git history.

Capture the following from actual execution; do not use generated/mock screenshots as deployment evidence:

- [ ] Dashboard in demo mode showing its DEMO DATA label.
- [ ] Dashboard in live mode after configuring access and confirming a workspace query.
- [ ] Azure Logs running `01-failed-azure-operations.kql`.
- [ ] Azure Logs running the RBAC-change query.
- [ ] Microsoft Sentinel saved scheduled analytics rule (if deployed).
- [ ] GitHub Actions successful tests and scans.
- [ ] A real Sentinel alert/incident (only if generated).

Redact subscription IDs, tenants, user identifiers, access tokens, and secrets. The `examples/` sample data is synthetic and is not proof of any Azure deployment.
