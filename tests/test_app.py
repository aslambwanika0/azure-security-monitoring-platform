import pytest
from backend.app import app

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("APP_MODE", "demo")
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health(client):
    assert client.get("/health").json["status"] == "healthy"

def test_demo_summary_is_labeled(client):
    result = client.get("/api/summary")
    assert result.status_code == 200
    assert result.json["mode"] == "demo"
    assert result.json["event_count"] == 3
    assert result.json["alert_count"] == 2

def test_dashboard_identifies_demo_data(client):
    result = client.get("/")
    assert result.status_code == 200
    assert b"DEMO DATA" in result.data
