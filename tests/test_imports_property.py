"""Property-based tests for module import integrity.

Feature: medical-doc-ai-backend, Property 2: Module import integrity
Validates: Requirements 8.1, 8.2
"""
import importlib
import pytest
from hypothesis import given, settings, strategies as st


# List of all application modules that should be importable
APPLICATION_MODULES = [
    "app",
    "app.api",
    "app.api.routes",
    "app.core",
    "app.core.config",
    "app.models",
    "app.services",
    "app.main",
]


@given(module_name=st.sampled_from(APPLICATION_MODULES))
@settings(max_examples=len(APPLICATION_MODULES))
def test_module_import_integrity(module_name):
    """Property 2: Module import integrity.
    
    For any application module, importing that module should complete
    without raising an ImportError.
    """
    try:
        # Attempt to import the module
        module = importlib.import_module(module_name)
        
        # Verify the module was imported successfully
        assert module is not None
        assert hasattr(module, "__name__")
        assert module.__name__ == module_name
        
    except ImportError as e:
        pytest.fail(f"Failed to import module {module_name}: {e}")


def test_all_modules_importable():
    """Test that all application modules can be imported without errors."""
    for module_name in APPLICATION_MODULES:
        try:
            module = importlib.import_module(module_name)
            assert module is not None
        except ImportError as e:
            pytest.fail(f"Failed to import module {module_name}: {e}")


def test_fastapi_imports():
    """Test that FastAPI and related imports work correctly."""
    try:
        import fastapi
        import uvicorn
        from app.main import app
        
        assert fastapi is not None
        assert uvicorn is not None
        assert app is not None
        
    except ImportError as e:
        pytest.fail(f"Failed to import FastAPI dependencies: {e}")


def test_custom_modules_import():
    """Test that all custom modules import successfully."""
    try:
        from app.core.config import settings
        from app.api.routes import router
        
        assert settings is not None
        assert router is not None
        
    except ImportError as e:
        pytest.fail(f"Failed to import custom modules: {e}")


def test_no_circular_imports():
    """Test that there are no circular import issues."""
    # Import all modules in sequence
    for module_name in APPLICATION_MODULES:
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            if "circular import" in str(e).lower():
                pytest.fail(f"Circular import detected in {module_name}: {e}")
            raise
