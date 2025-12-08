"""Unit tests for configuration management."""
import os
import pytest
from app.core.config import Settings


def test_settings_default_values():
    """Test that Settings provides default values."""
    settings = Settings()
    assert settings.APP_NAME == "MedicalDocAI"
    assert settings.ENV == "local"
    assert settings.API_PREFIX == "/api"
    assert settings.CORS_ORIGINS == "*"


def test_settings_loads_from_environment(monkeypatch):
    """Test that Settings loads values from environment variables."""
    monkeypatch.setenv("APP_NAME", "TestApp")
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("API_PREFIX", "/v1")
    monkeypatch.setenv("CORS_ORIGINS", "https://example.com")
    
    settings = Settings()
    assert settings.APP_NAME == "TestApp"
    assert settings.ENV == "production"
    assert settings.API_PREFIX == "/v1"
    assert settings.CORS_ORIGINS == "https://example.com"


def test_settings_has_all_required_fields():
    """Test that all required configuration fields are accessible."""
    settings = Settings()
    
    # Application settings
    assert hasattr(settings, "APP_NAME")
    assert hasattr(settings, "ENV")
    assert hasattr(settings, "API_PREFIX")
    
    # CORS settings
    assert hasattr(settings, "CORS_ORIGINS")
    
    # External service credentials
    assert hasattr(settings, "CLAUDE_API_KEY")
    assert hasattr(settings, "RAINDROP_API_KEY")
    assert hasattr(settings, "DATABASE_URL")
    assert hasattr(settings, "VULTR_OBJECT_STORAGE_ACCESS_KEY")
    assert hasattr(settings, "VULTR_OBJECT_STORAGE_SECRET_KEY")
    assert hasattr(settings, "VULTR_OBJECT_STORAGE_BUCKET")


def test_settings_empty_credentials_default():
    """Test that credential fields default to empty strings."""
    settings = Settings()
    assert settings.CLAUDE_API_KEY == ""
    assert settings.RAINDROP_API_KEY == ""
    assert settings.DATABASE_URL == ""
    assert settings.VULTR_OBJECT_STORAGE_ACCESS_KEY == ""
    assert settings.VULTR_OBJECT_STORAGE_SECRET_KEY == ""
    assert settings.VULTR_OBJECT_STORAGE_BUCKET == ""


def test_settings_can_override_credentials(monkeypatch):
    """Test that credential fields can be overridden via environment."""
    monkeypatch.setenv("CLAUDE_API_KEY", "test_claude_key")
    monkeypatch.setenv("RAINDROP_API_KEY", "test_raindrop_key")
    monkeypatch.setenv("DATABASE_URL", "postgresql://test:test@localhost/test")
    
    settings = Settings()
    assert settings.CLAUDE_API_KEY == "test_claude_key"
    assert settings.RAINDROP_API_KEY == "test_raindrop_key"
    assert settings.DATABASE_URL == "postgresql://test:test@localhost/test"
