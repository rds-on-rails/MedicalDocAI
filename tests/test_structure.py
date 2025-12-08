"""Unit tests for project structure validation."""
import os
from pathlib import Path


def test_app_directory_exists():
    """Test that app directory exists."""
    assert os.path.isdir("app"), "app directory should exist"


def test_app_init_exists():
    """Test that app/__init__.py exists."""
    assert os.path.isfile("app/__init__.py"), "app/__init__.py should exist"


def test_app_main_exists():
    """Test that app/main.py exists."""
    assert os.path.isfile("app/main.py"), "app/main.py should exist"


def test_api_directory_exists():
    """Test that app/api directory exists."""
    assert os.path.isdir("app/api"), "app/api directory should exist"


def test_api_init_exists():
    """Test that app/api/__init__.py exists."""
    assert os.path.isfile("app/api/__init__.py"), "app/api/__init__.py should exist"


def test_api_routes_exists():
    """Test that app/api/routes.py exists."""
    assert os.path.isfile("app/api/routes.py"), "app/api/routes.py should exist"


def test_core_directory_exists():
    """Test that app/core directory exists."""
    assert os.path.isdir("app/core"), "app/core directory should exist"


def test_core_init_exists():
    """Test that app/core/__init__.py exists."""
    assert os.path.isfile("app/core/__init__.py"), "app/core/__init__.py should exist"


def test_core_config_exists():
    """Test that app/core/config.py exists."""
    assert os.path.isfile("app/core/config.py"), "app/core/config.py should exist"


def test_models_directory_exists():
    """Test that app/models directory exists."""
    assert os.path.isdir("app/models"), "app/models directory should exist"


def test_models_init_exists():
    """Test that app/models/__init__.py exists."""
    assert os.path.isfile("app/models/__init__.py"), "app/models/__init__.py should exist"


def test_services_directory_exists():
    """Test that app/services directory exists."""
    assert os.path.isdir("app/services"), "app/services directory should exist"


def test_services_init_exists():
    """Test that app/services/__init__.py exists."""
    assert os.path.isfile("app/services/__init__.py"), "app/services/__init__.py should exist"


def test_requirements_txt_exists():
    """Test that requirements.txt exists."""
    assert os.path.isfile("requirements.txt"), "requirements.txt should exist"


def test_requirements_contains_fastapi():
    """Test that requirements.txt contains fastapi."""
    with open("requirements.txt", "r") as f:
        content = f.read()
    assert "fastapi" in content.lower(), "requirements.txt should contain fastapi"


def test_requirements_contains_uvicorn():
    """Test that requirements.txt contains uvicorn."""
    with open("requirements.txt", "r") as f:
        content = f.read()
    assert "uvicorn" in content.lower(), "requirements.txt should contain uvicorn"


def test_requirements_contains_python_dotenv():
    """Test that requirements.txt contains python-dotenv."""
    with open("requirements.txt", "r") as f:
        content = f.read()
    assert "python-dotenv" in content.lower(), "requirements.txt should contain python-dotenv"


def test_requirements_contains_pydantic():
    """Test that requirements.txt contains pydantic."""
    with open("requirements.txt", "r") as f:
        content = f.read()
    assert "pydantic" in content.lower(), "requirements.txt should contain pydantic"
