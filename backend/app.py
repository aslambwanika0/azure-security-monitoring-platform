"""Read-only Flask dashboard and API for Azure cloud security monitoring."""
import json
import os
from pathlib import Path
from flask import Flask, jsonify, render_template_string
from dotenv import load_dotenv
from backend.detection import analyze, summarize

load_dotenv()
ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__)

def get_events():
    if os.getenv("APP_MODE", "demo").lower() == "live":
        from backend.azure_logs import collect
        return collect(), "live"
    with (ROOT / "examples" / "sample_azure_activity.json").open(encoding="utf-8") as handle:
        return json.load(handle), "demo"

def snapshot():
    events, mode = get_events()
    alerts = analyze(events)
    return {"mode": mode, "events": events, "alerts": alerts, "summary": summarize(events, alerts)}

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "azure-security-monitoring-platform"})

@app.get("/api/summary")
def summary():
    try:
        state = snapshot()
        return jsonify({"mode": state["mode"], **state["summary"]})
    except Exception:
        app.logger.exception("Failed to retrieve monitoring data")
        return jsonify({"error": "Monitoring data unavailable; verify Azure credentials and workspace configuration."}), 503

@app.get("/api/events")
def events():
    try:
        state = snapshot()
        return jsonify({"mode": state["mode"], "events": state["events"]})
    except Exception:
        app.logger.exception("Failed to retrieve Azure events")
        return jsonify({"error": "Monitoring data unavailable."}), 503

@app.get("/api/alerts")
def alerts():
    try:
        state = snapshot()
        return jsonify({"mode": state["mode"], "alerts": state["alerts"]})
    except Exception:
        app.logger.exception("Failed to analyze Azure events")
        return jsonify({"error": "Monitoring data unavailable."}), 503

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Azure Security Monitoring</title>
<style>
body{font:16px system-ui,sans-serif;background:#0b1220;color:#e7edf6;margin:0;padding:32px;line-height:1.5}
main{max-width:1100px;margin:auto}h1{margin-bottom:4px}.muted{color:#aab7cb}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin:24px 0}
.card{background:#18243a;padding:20px;border:1px solid #304362;border-radius:12px}
.number{font-size:32px;font-weight:bold}table{border-collapse:collapse;width:100%;background:#18243a}
td,th{text-align:left;border-bottom:1px solid #304362;padding:12px;word-break:break-word}
th{color:#bdd1ee}.demo{background:#5a4210;padding:6px 12px;border-radius:8px}
.live{background:#164935;padding:6px 12px;border-radius:8px}
</style></head><body><main><h1>Azure Security Monitoring</h1>
<p class="muted">Read-only event triage • Microsoft Sentinel / Log Analytics</p>
<p><span class="{{ mode }}">{{ mode|upper }} DATA</span>
{% if mode == 'demo' %} Sample events only; no live Azure connection is implied.{% else %} Queried from configured Log Analytics workspace.{% endif %}</p>
<div class="cards"><div class="card">Events<div class="number">{{ summary.event_count }}</div></div>
<div class="card">Alerts<div class="number">{{ summary.alert_count }}</div></div>
<div class="card">High severity<div class="number">{{ summary.by_severity.get('high',0) }}</div></div>
<div class="card">Medium severity<div class="number">{{ summary.by_severity.get('medium',0) }}</div></div></div>
<h2>Detected events</h2><table><thead><tr><th>Time (UTC)</th><th>Rule</th><th>Severity</th><th>Caller</th><th>Operation</th></tr></thead><tbody>
{% for alert in alerts %}<tr><td>{{ alert.time }}</td><td>{{ alert.rule }}</td><td>{{ alert.severity }}</td>
<td>{{ alert.caller }}</td><td>{{ alert.operation }}</td></tr>{% else %}<tr><td colspan="5">No matching alerts in the queried events.</td></tr>{% endfor %}
</tbody></table><p class="muted">API: <a href="/api/summary">Summary</a> · <a href="/api/events">Events</a> · <a href="/api/alerts">Alerts</a></p>
</main></body></html>"""

@app.get("/")
def dashboard():
    try:
        state = snapshot()
        return render_template_string(PAGE, **state)
    except Exception:
        app.logger.exception("Dashboard unavailable")
        return "Monitoring data unavailable. Check server logs and Azure configuration.", 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5001")), debug=False)
