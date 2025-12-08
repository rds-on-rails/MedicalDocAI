"""Configuration management using Pydantic settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    
    # Application settings
    APP_NAME: str = "MedicalDocAI"
    ENV: str = "local"
    API_PREFIX: str = "/api"
    
    # CORS settings
    CORS_ORIGINS: str = "*"
    
    # External service credentials
    CLAUDE_API_KEY: str = ""
    RAINDROP_API_KEY: str = ""
    DATABASE_URL: str = ""
    VULTR_OBJECT_STORAGE_ACCESS_KEY: str = ""
    VULTR_OBJECT_STORAGE_SECRET_KEY: str = ""
    VULTR_OBJECT_STORAGE_BUCKET: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
