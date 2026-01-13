from pydantic import BaseModel, Field, field_validator
from typing import Annotated
import math

class BinaryOperationRequest(BaseModel):
    """Request schema for binary operations (add, subtract, multiply, divide)."""
    a: Annotated[float, Field(description="First operand", examples=[10.0])]
    b: Annotated[float, Field(description="Second operand", examples=[5.0])]

class BinaryOperationResponse(BaseModel):
    """Response schema for binary operations."""
    operation: str
    a: float
    b: float
    result: float

class PowerOperationRequest(BaseModel):
    """Request schema for power operation."""
    base: Annotated[float, Field(description="Base number", examples=[2.0])]
    exponent: Annotated[float, Field(description="Exponent", examples=[8.0])]

class PowerOperationResponse(BaseModel):
    """Response schema for power operation."""
    operation: str
    base: float
    exponent: float
    result: float

class UnaryOperationRequest(BaseModel):
    """Request schema for unary operations (sqrt, sin, cos, tan)."""
    number: Annotated[float, Field(description="Input number", examples=[16.0])]
    
    @field_validator('number')
    def validate_number(cls, v):
        return v

class UnaryOperationResponse(BaseModel):
    """Response schema for unary operations."""
    operation: str
    input: float
    result: float

class ErrorResponse(BaseModel):
    """Error response schema."""
    error: str
    message: str