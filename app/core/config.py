from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Application settings
    app_name: str = "FastAPI Microservice"
    version: str = "1.0.0"
    debug: bool = False
    
    # Database settings
    database_url: str = "sqlite:///./app.db"
    
    # Security settings
    secret_key: str = "your-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    
    # CORS settings
    allowed_hosts: list = ["*"]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()