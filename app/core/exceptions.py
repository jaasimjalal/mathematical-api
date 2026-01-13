from fastapi import HTTPException, status

class BaseAPIException(HTTPException):
    """Base exception for API errors."""
    def __init__(self, status_code: int, detail: str, headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class ValidationError(BaseAPIException):
    """Input validation error."""
    def __init__(self, detail: str = "Invalid input"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

class DivisionByZeroError(BaseAPIException):
    """Division by zero error."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Division by zero is not allowed"
        )

class NegativeSquareRootError(BaseAPIException):
    """Square root of negative number error."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Square root of negative number is not allowed"
        )