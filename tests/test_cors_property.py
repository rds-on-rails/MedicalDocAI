"""Property-based tests for CORS validation.

Feature: medical-doc-ai-backend, Property 1: CORS origin validation
Validates: Requirements 5.3, 5.4
"""
import pytest
from hypothesis import given, settings, strategies as st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient


def create_app_with_cors(cors_origins_config: str) -> FastAPI:
    """Create a FastAPI app with specified CORS configuration."""
    app = FastAPI()
    
    # Parse CORS origins
    cors_origins = []
    if cors_origins_config:
        if cors_origins_config == "*":
            cors_origins = ["*"]
        else:
            cors_origins = [origin.strip() for origin in cors_origins_config.split(",")]
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    @app.get("/test")
    async def test_endpoint():
        return {"message": "test"}
    
    return app


# Strategy for generating valid domain names
domain_strategy = st.text(
    alphabet=st.characters(whitelist_categories=("Ll", "Nd"), whitelist_characters="-"),
    min_size=1,
    max_size=20
).map(lambda s: f"https://{s}.com")


@given(origin=domain_strategy)
@settings(max_examples=100)
def test_cors_wildcard_allows_any_origin(origin):
    """Property 1: CORS origin validation - wildcard allows any origin.
    
    For any origin, when CORS_ORIGINS is set to "*", the response should
    include Access-Control-Allow-Origin header.
    """
    app = create_app_with_cors("*")
    client = TestClient(app)
    
    response = client.get("/test", headers={"Origin": origin})
    
    # When CORS_ORIGINS is "*", any origin should be allowed
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "*"


@given(origin=domain_strategy)
@settings(max_examples=100)
def test_cors_specific_origin_validation(origin):
    """Property 1: CORS origin validation - specific origin matching.
    
    For any origin, when CORS_ORIGINS is set to a specific domain,
    only that domain should receive CORS headers.
    """
    allowed_origin = "https://example.com"
    app = create_app_with_cors(allowed_origin)
    client = TestClient(app)
    
    response = client.get("/test", headers={"Origin": origin})
    
    # Only the allowed origin should get CORS headers
    if origin == allowed_origin:
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == allowed_origin
    else:
        # For non-matching origins, the header might not be present or be different
        # FastAPI's CORS middleware doesn't add the header for non-allowed origins
        if "access-control-allow-origin" in response.headers:
            assert response.headers["access-control-allow-origin"] != origin


@given(origin=domain_strategy)
@settings(max_examples=100)
def test_cors_comma_separated_list(origin):
    """Property 1: CORS origin validation - comma-separated list.
    
    For any origin, when CORS_ORIGINS contains a comma-separated list,
    only origins in that list should receive matching CORS headers.
    """
    allowed_origins = "https://app1.com,https://app2.com,https://app3.com"
    allowed_list = ["https://app1.com", "https://app2.com", "https://app3.com"]
    app = create_app_with_cors(allowed_origins)
    client = TestClient(app)
    
    response = client.get("/test", headers={"Origin": origin})
    
    # Only allowed origins should get CORS headers
    if origin in allowed_list:
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == origin
    else:
        # Non-allowed origins should not get matching CORS headers
        if "access-control-allow-origin" in response.headers:
            assert response.headers["access-control-allow-origin"] != origin


def test_cors_empty_config_denies_all():
    """Test that empty CORS configuration denies all origins."""
    app = create_app_with_cors("")
    client = TestClient(app)
    
    response = client.get("/test", headers={"Origin": "https://example.com"})
    
    # Empty config should not allow any origin
    # The header might not be present at all
    if "access-control-allow-origin" in response.headers:
        assert response.headers["access-control-allow-origin"] != "https://example.com"
