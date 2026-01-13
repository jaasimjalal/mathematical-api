import pytest
from fastapi.testclient import TestClient


def test_add(client: TestClient, sample_add_request):
    """Test addition endpoint."""
    response = client.post("/api/v1/add", json=sample_add_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "add"
    assert data["result"] == 15


def test_subtract(client: TestClient, sample_subtract_request):
    """Test subtraction endpoint."""
    response = client.post("/api/v1/subtract", json=sample_subtract_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "subtract"
    assert data["result"] == 5


def test_multiply(client: TestClient, sample_multiply_request):
    """Test multiplication endpoint."""
    response = client.post("/api/v1/multiply", json=sample_multiply_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "multiply"
    assert data["result"] == 50


def test_divide(client: TestClient, sample_divide_request):
    """Test division endpoint."""
    response = client.post("/api/v1/divide", json=sample_divide_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "divide"
    assert data["result"] == 2


def test_divide_by_zero(client: TestClient):
    """Test division by zero error."""
    response = client.post("/api/v1/divide", json={"a": 10, "b": 0})
    assert response.status_code == 422
    data = response.json()
    assert "error" in data


def test_power(client: TestClient, sample_power_request):
    """Test power endpoint."""
    response = client.post("/api/v1/power", json=sample_power_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "power"
    assert data["result"] == 256


def test_sqrt(client: TestClient, sample_sqrt_request):
    """Test square root endpoint."""
    response = client.post("/api/v1/sqrt", json=sample_sqrt_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "sqrt"
    assert data["result"] == 4


def test_sqrt_negative(client: TestClient):
    """Test square root of negative number error."""
    response = client.post("/api/v1/sqrt", json={"number": -16})
    assert response.status_code == 422
    data = response.json()
    assert "error" in data


def test_sin(client: TestClient, sample_sin_request):
    """Test sine endpoint."""
    response = client.post("/api/v1/sin", json=sample_sin_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "sin"
    assert abs(data["result"]) < 0.001  # sin(0) ≈ 0


def test_cos(client: TestClient, sample_cos_request):
    """Test cosine endpoint."""
    response = client.post("/api/v1/cos", json=sample_cos_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "cos"
    assert abs(data["result"] - 1) < 0.001  # cos(0) ≈ 1


def test_tan(client: TestClient, sample_tan_request):
    """Test tangent endpoint."""
    response = client.post("/api/v1/tan", json=sample_tan_request)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "tan"
    assert abs(data["result"]) < 0.001  # tan(0) ≈ 0
