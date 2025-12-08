"""Unit tests for API router integration."""
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.api.routes import router
from app.core.config import settings


def test_router_included_in_app():
    """Test that API router is included in the main application."""
    # Check that the router is in the app's routes
    route_paths = [route.path for route in app.routes]
    
    # The router should be included with the API_PREFIX
    # Since the router is empty, we just verify it's been included
    # by checking that the app has the router registered
    assert router in [route.app for route in app.routes if hasattr(route, 'app')]


def test_router_mounted_with_api_prefix():
    """Test that routes are mounted with correct API_PREFIX."""
    # Add a test route to the router
    @router.get("/test")
    async def test_route():
        return {"message": "test"}
    
    client = TestClient(app)
    
    # The route should be accessible at API_PREFIX + route path
    expected_path = f"{settings.API_PREFIX}/test"
    response = client.get(expected_path)
    
    # Should get a successful response (not 404)
    assert response.status_code == 200
    assert response.json() == {"message": "test"}


def test_api_prefix_from_config():
    """Test that API_PREFIX from config affects route paths."""
    # Create a new app with custom config
    from app.core.config import Settings
    
    custom_settings = Settings(API_PREFIX="/v2")
    
    custom_app = FastAPI()
    custom_router = router
    custom_app.include_router(custom_router, prefix=custom_settings.API_PREFIX)
    
    @custom_router.get("/custom")
    async def custom_route():
        return {"message": "custom"}
    
    client = TestClient(custom_app)
    
    # Route should be accessible at custom prefix
    response = client.get("/v2/custom")
    assert response.status_code == 200


def test_router_allows_extension_without_modifying_main():
    """Test that new endpoints can be added through router without modifying main.py."""
    # Add a new route to the router
    @router.get("/new-endpoint")
    async def new_endpoint():
        return {"message": "new"}
    
    client = TestClient(app)
    
    # The new route should be accessible
    response = client.get(f"{settings.API_PREFIX}/new-endpoint")
    assert response.status_code == 200
    assert response.json() == {"message": "new"}
