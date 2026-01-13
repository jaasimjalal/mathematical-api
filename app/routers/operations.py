import math
import logging
from fastapi import APIRouter, status
from app.schemas.operations import (
    BinaryOperationRequest,
    BinaryOperationResponse,
    PowerOperationRequest,
    PowerOperationResponse,
    UnaryOperationRequest,
    UnaryOperationResponse,
    ErrorResponse
)
from app.core.exceptions import (
    DivisionByZeroError,
    NegativeSquareRootError,
    ValidationError
)

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="",
    tags=["Operations"],
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        422: {"model": ErrorResponse, "description": "Unprocessable Entity"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)

# ============ Binary Operations ============

@router.post(
    "/add",
    response_model=BinaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Addition",
    description="Add two numbers: a + b"
)
async def add(request: BinaryOperationRequest):
    """
    Add two numbers.
    
    - **a**: First number
    - **b**: Second number
    """
    result = request.a + request.b
    logger.info(f"Addition: {request.a} + {request.b} = {result}")
    return BinaryOperationResponse(
        operation="add",
        a=request.a,
        b=request.b,
        result=result
    )

@router.post(
    "/subtract",
    response_model=BinaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Subtraction",
    description="Subtract two numbers: a - b"
)
async def subtract(request: BinaryOperationRequest):
    """
    Subtract two numbers.
    
    - **a**: First number
    - **b**: Second number
    """
    result = request.a - request.b
    logger.info(f"Subtraction: {request.a} - {request.b} = {result}")
    return BinaryOperationResponse(
        operation="subtract",
        a=request.a,
        b=request.b,
        result=result
    )

@router.post(
    "/multiply",
    response_model=BinaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Multiplication",
    description="Multiply two numbers: a × b"
)
async def multiply(request: BinaryOperationRequest):
    """
    Multiply two numbers.
    
    - **a**: First number
    - **b**: Second number
    """
    result = request.a * request.b
    logger.info(f"Multiplication: {request.a} * {request.b} = {result}")
    return BinaryOperationResponse(
        operation="multiply",
        a=request.a,
        b=request.b,
        result=result
    )

@router.post(
    "/divide",
    response_model=BinaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Division",
    description="Divide two numbers: a ÷ b"
)
async def divide(request: BinaryOperationRequest):
    """
    Divide two numbers.
    
    - **a**: Numerator
    - **b**: Denominator (cannot be zero)
    """
    if request.b == 0:
        logger.warning(f"Division by zero attempted: {request.a} / {request.b}")
        raise DivisionByZeroError()
    
    result = request.a / request.b
    logger.info(f"Division: {request.a} / {request.b} = {result}")
    return BinaryOperationResponse(
        operation="divide",
        a=request.a,
        b=request.b,
        result=result
    )

# ============ Power Operation ============

@router.post(
    "/power",
    response_model=PowerOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Power",
    description="Calculate base raised to exponent: base^exponent"
)
async def power(request: PowerOperationRequest):
    """
    Calculate power.
    
    - **base**: Base number
    - **exponent**: Exponent
    """
    try:
        result = request.base ** request.exponent
        logger.info(f"Power: {request.base}^{request.exponent} = {result}")
        return PowerOperationResponse(
            operation="power",
            base=request.base,
            exponent=request.exponent,
            result=result
        )
    except Exception as e:
        logger.error(f"Power operation failed: {str(e)}")
        raise ValidationError("Invalid power operation")

# ============ Unary Operations ============

@router.post(
    "/sqrt",
    response_model=UnaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Square Root",
    description="Calculate square root of a number"
)
async def sqrt(request: UnaryOperationRequest):
    """
    Calculate square root.
    
    - **number**: Input number (must be non-negative)
    """
    if request.number < 0:
        logger.warning(f"Negative square root attempted: {request.number}")
        raise NegativeSquareRootError()
    
    result = math.sqrt(request.number)
    logger.info(f"Square root: √{request.number} = {result}")
    return UnaryOperationResponse(
        operation="sqrt",
        input=request.number,
        result=result
    )

@router.post(
    "/sin",
    response_model=UnaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Sine Function",
    description="Calculate sine of angle (radians)"
)
async def sin(request: UnaryOperationRequest):
    """
    Calculate sine.
    
    - **number**: Angle in radians
    """
    result = math.sin(request.number)
    logger.info(f"Sine: sin({request.number}) = {result}")
    return UnaryOperationResponse(
        operation="sin",
        input=request.number,
        result=result
    )

@router.post(
    "/cos",
    response_model=UnaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Cosine Function",
    description="Calculate cosine of angle (radians)"
)
async def cos(request: UnaryOperationRequest):
    """
    Calculate cosine.
    
    - **number**: Angle in radians
    """
    result = math.cos(request.number)
    logger.info(f"Cosine: cos({request.number}) = {result}")
    return UnaryOperationResponse(
        operation="cos",
        input=request.number,
        result=result
    )

@router.post(
    "/tan",
    response_model=UnaryOperationResponse,
    status_code=status.HTTP_200_OK,
    summary="Tangent Function",
    description="Calculate tangent of angle (radians)"
)
async def tan(request: UnaryOperationRequest):
    """
    Calculate tangent.
    
    - **number**: Angle in radians
    """
    try:
        result = math.tan(request.number)
        logger.info(f"Tangent: tan({request.number}) = {result}")
        return UnaryOperationResponse(
            operation="tan",
            input=request.number,
            result=result
        )
    except Exception as e:
        logger.error(f"Tangent operation failed: {str(e)}")
        raise ValidationError("Invalid tangent operation")
