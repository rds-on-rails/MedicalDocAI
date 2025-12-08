"""Medical Document AI Assistant Backend - Main Application

Usage:
    Development:
        uvicorn app.main:app --reload
    
    Production:
        uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

Environment Variables:
    See .env.example for required configuration
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import router


# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Medical Document AI Assistant Backend Service",
    version="1.0.0"
)

# Parse CORS origins
cors_origins = []
if settings.CORS_ORIGINS:
    if settings.CORS_ORIGINS == "*":
        cors_origins = ["*"]
    else:
        # Handle comma-separated list
        cors_origins = [origin.strip() for origin in settings.CORS_ORIGINS.split(",")]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router with prefix
app.include_router(router, prefix=settings.API_PREFIX)


@app.get("/health")
async def health_check():
    """Health check endpoint.
    
    Returns:
        dict: Status indicating the service is operational
    """
    return {"status": "ok"}
