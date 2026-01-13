# Security utilities (placeholder for future auth implementation)
from fastapi import Header, HTTPException, status
from typing import Optional

async def verify_api_key(api_key: Optional[str] = Header(None)):
    """
    Placeholder for API key verification.
    Can be extended with actual authentication logic.
    """
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key required"
        )
    # Add actual verification logic here
    return True
