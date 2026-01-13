# Mathematical API

FastAPI-based microservice for mathematical operations.

## Overview

A production-ready REST API providing mathematical operations with validation, error handling, and logging.

## Features

- RESTful endpoints for mathematical operations
- Input validation with Pydantic
- Structured logging
- Error handling
- Health check endpoint
- OpenAPI/Swagger documentation
- Docker containerization
- CI/CD pipeline with Jenkins

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/v1/add` | POST | Addition |
| `/api/v1/subtract` | POST | Subtraction |
| `/api/v1/multiply` | POST | Multiplication |
| `/api/v1/divide` | POST | Division |
| `/api/v1/power` | POST | Power operation |
| `/api/v1/sqrt` | POST | Square root |
| `/api/v1/sin` | POST | Sine function |
| `/api/v1/cos` | POST | Cosine function |
| `/api/v1/tan` | POST | Tangent function |

## Environment Variables

```bash
APP_NAME=mathematical-api
APP_ENV=production
PORT=3000
LOG_LEVEL=INFO
```

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
# Clone repository
git clone https://github.com/jaasimjalal/mathematical-api.git
cd mathematical-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

### Access API Documentation
- Swagger UI: http://localhost:3000/docs
- ReDoc: http://localhost:3000/redoc

## Docker

### Build and Run
```bash
# Build image
docker build -t mathematical-api:latest .

# Run container
docker run -p 3000:3000 mathematical-api:latest
```

## Jenkins CI/CD

The repository includes a Jenkinsfile for automated builds and testing.

### Jenkins Pipeline Stages
1. **Checkout** - Clone repository
2. **Dependencies** - Install Python packages
3. **Test** - Run automated tests
4. **Build** - Build Docker image
5. **Deploy** - Run container locally

## API Examples

### Addition
```bash
curl -X POST http://localhost:3000/api/v1/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
```

### Square Root
```bash
curl -X POST http://localhost:3000/api/v1/sqrt \
  -H "Content-Type: application/json" \
  -d '{"number": 16}'
```

### Power
```bash
curl -X POST http://localhost:3000/api/v1/power \
  -H "Content-Type: application/json" \
  -d '{"base": 2, "exponent": 8}'
```