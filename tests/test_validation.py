import pytest
from fastapi.testclient import TestClient


def test_invalid_add_missing_field(client: TestClient):
    """Test addition with missing field."""
    response = client.post("/api/v1/add", json={"a": 10})
    assert response.status_code == 422


def test_invalid_add_extra_field(client: TestClient):
    """Test addition with extra field."""
    response = client.post("/api/v1/add", json={"a": 10, "b": 5, "c": 15})
    assert response.status_code == 200  # Extra fields allowed by Pydantic


def test_invalid_sqrt_negative(client: TestClient):
    """Test square root with negative number."""
    response = client.post("/api/v1/sqrt", json={"number": -16})
    assert response.status_code == 422
    data = response.json()
    assert "negative number" in data["error"].lower()
