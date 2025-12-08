"""Unit tests for documentation."""
import os


def test_readme_exists():
    """Test that README.md exists."""
    assert os.path.isfile("README.md"), "README.md should exist"


def test_readme_contains_venv_instructions():
    """Test that README contains virtual environment instructions."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "python -m venv venv" in content.lower(), \
        "README should contain virtual environment creation instructions"
    assert "virtual environment" in content.lower(), \
        "README should mention virtual environment"


def test_readme_contains_pip_install():
    """Test that README contains pip install command."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "pip install -r requirements.txt" in content.lower(), \
        "README should contain pip install command"


def test_readme_contains_uvicorn_reload():
    """Test that README contains uvicorn command with --reload flag."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "uvicorn" in content.lower(), \
        "README should contain uvicorn command"
    assert "--reload" in content, \
        "README should contain --reload flag for development"
    assert "uvicorn app.main:app --reload" in content, \
        "README should contain complete uvicorn command"


def test_readme_contains_setup_section():
    """Test that README contains setup instructions section."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "setup" in content.lower() or "installation" in content.lower(), \
        "README should contain setup or installation section"


def test_readme_contains_environment_config():
    """Test that README references environment configuration."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert ".env" in content.lower(), \
        "README should reference .env file"
    assert "environment" in content.lower(), \
        "README should mention environment configuration"


def test_readme_contains_vultr_info():
    """Test that README contains Vultr hosting information."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "vultr" in content.lower(), \
        "README should contain Vultr hosting information"


def test_readme_contains_liquidmetal_info():
    """Test that README contains LiquidMetal AI components information."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "liquidmetal" in content.lower(), \
        "README should contain LiquidMetal AI components information"
