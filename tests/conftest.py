import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    """
    return TestClient(app)

@pytest.fixture
def sample_add_request():
    """Sample request for addition."""
    return {"a": 10, "b": 5}

@pytest.fixture
def sample_subtract_request():
    """Sample request for subtraction."""
    return {"a": 10, "b": 5}

@pytest.fixture
def sample_multiply_request():
    """Sample request for multiplication."""
    return {"a": 10, "b": 5}

@pytest.fixture
def sample_divide_request():
    """Sample request for division."""
    return {"a": 10, "b": 5}

@pytest.fixture
def sample_power_request():
    """Sample request for power."""
    return {"base": 2, "exponent": 8}

@pytest.fixture
def sample_sqrt_request():
    """Sample request for square root."""
    return {"number": 16}

@pytest.fixture
def sample_sin_request():
    """Sample request for sine."""
    return {"number": 0}

@pytest.fixture
def sample_cos_request():
    """Sample request for cosine."""
    return {"number": 0}

@pytest.fixture
def sample_tan_request():
    """Sample request for tangent."""
    return {"number": 0}
