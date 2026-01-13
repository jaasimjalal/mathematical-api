from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """
    Application configuration settings.
    Loaded from environment variables with sensible defaults.
    """
    
    # Application
    APP_NAME: str = "mathematical-api"
    APP_ENV: str = "development"
    VERSION: str = "1.0.0"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 3000
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Singleton settings instance
settings = Settings()
