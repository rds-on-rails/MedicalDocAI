"""Unit tests for health endpoint."""
import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_200():
    """Test that GET /health returns 200 status code."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_returns_ok_status():
    """Test that response body contains status field with value 'ok'."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"


def test_health_endpoint_accessible_at_health_path():
    """Test that endpoint is accessible at /health path."""
    response = client.get("/health")
    assert response.status_code == 200
    # Verify it's not a 404
    assert response.status_code != 404
