# Design Document

## Overview

The Medical Document AI Assistant backend is a FastAPI-based REST API service that provides the foundational infrastructure for AI-powered medical document processing. The service is designed to be hosted on Vultr cloud infrastructure and leverages LiquidMetal's pre-built, enterprise-grade AI infrastructure components to reduce development time. The service follows a layered architecture with clear separation between API routing, business logic, data models, and configuration management. The initial implementation focuses on establishing the core service infrastructure with health monitoring, CORS support, and environment-based configuration, while providing placeholder modules for future medical document processing capabilities that will integrate with LiquidMetal's AI components.

## Architecture

The system follows a modular layered architecture:

```
┌─────────────────────────────────────┐
│         ASGI Server (uvicorn)       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      FastAPI Application            │
│  ┌──────────────────────────────┐   │
│  │   CORS Middleware            │   │
│  └──────────────────────────────┘   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│         API Layer (routes)          │
│  - Health endpoint                  │
│  - Future medical doc endpoints     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Services Layer (business)      │
│  - Placeholder for AI processing    │
│  - Placeholder for doc management   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Models Layer (data)            │
│  - Placeholder for ORM models       │
└─────────────────────────────────────┘
```

**Key Architectural Decisions:**

1. **FastAPI Framework**: Chosen for its async support, automatic OpenAPI documentation, type safety with Pydantic, and high performance
2. **Vultr Cloud Hosting**: Infrastructure hosted on Vultr for reliable, scalable cloud services including compute instances, object storage, and managed databases
3. **LiquidMetal Integration**: Leverages LiquidMetal's pre-built AI infrastructure components to accelerate development of AI-powered features, reducing time-to-market for medical document processing capabilities
4. **Modular Structure**: Separation of concerns with distinct directories for API routes, business logic, models, and configuration
5. **Environment-Based Configuration**: Centralized configuration management using python-dotenv and Pydantic settings
6. **CORS Middleware**: Configurable cross-origin support for frontend integration
7. **Placeholder Modules**: Empty service and model directories to establish structure for future LiquidMetal-powered AI features

## Infrastructure Components

### Vultr Cloud Services

**Compute:**
- Vultr Cloud Compute instances for hosting FastAPI application
- Auto-scaling capabilities for handling variable workloads
- Multiple regions for geographic distribution

**Storage:**
- Vultr Object Storage (S3-compatible) for medical document storage
- High durability and availability for critical medical data
- Integrated with application via boto3 or similar S3 client

**Database:**
- Vultr Managed Database (PostgreSQL) for structured data
- Automated backups and high availability
- Connection pooling for optimal performance

**Networking:**
- Vultr Load Balancers for traffic distribution
- Vultr Firewall for network security
- Private networking between services

### LiquidMetal AI Infrastructure

**Pre-built Components:**
- **AI Orchestration Layer**: Manages AI model invocations and workflow coordination
- **Prompt Management**: Version-controlled prompt templates for medical document analysis
- **Model Connectors**: Pre-built integrations with Claude API and other AI services
- **Caching Layer**: Intelligent caching of AI responses to reduce latency and costs
- **Observability**: Monitoring and logging for AI model performance and costs

**Integration Points:**
- FastAPI service communicates with LiquidMetal via REST APIs or SDK
- LiquidMetal handles AI complexity, allowing FastAPI to focus on business logic
- Shared authentication and authorization between services
- Event-driven architecture for asynchronous AI processing

**Benefits:**
- Reduced development time by 60-80% for AI features
- Enterprise-grade reliability and scalability
- Built-in best practices for AI application development
- Simplified maintenance and updates

## Components and Interfaces

### 1. Main Application (app/main.py)

**Responsibilities:**
- Initialize FastAPI application
- Configure CORS middleware
- Register API routers
- Provide health check endpoint

**Interface:**
```python
# FastAPI application instance
app: FastAPI

# Health endpoint
@app.get("/health")
async def health_check() -> dict
```

### 2. Configuration Module (app/core/config.py)

**Responsibilities:**
- Load environment variables from .env file
- Provide typed configuration settings
- Supply default values for optional settings

**Interface:**
```python
class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    API_PREFIX: str
    CORS_ORIGINS: str
    CLAUDE_API_KEY: str
    RAINDROP_API_KEY: str
    DATABASE_URL: str
    VULTR_OBJECT_STORAGE_ACCESS_KEY: str
    VULTR_OBJECT_STORAGE_SECRET_KEY: str
    VULTR_OBJECT_STORAGE_BUCKET: str
    
    class Config:
        env_file = ".env"

# Global settings instance
settings: Settings
```

### 3. API Router (app/api/routes.py)

**Responsibilities:**
- Define API endpoints
- Group related routes
- Handle request/response processing

**Interface:**
```python
# APIRouter instance
router: APIRouter

# Future endpoints will be added here
# Example: @router.post("/documents")
```

### 4. Services Module (app/services/)

**Responsibilities:**
- Placeholder for business logic
- Future AI document processing
- Future integration with external services

**Interface:**
```python
# Placeholder - will contain service classes for:
# - Document processing
# - AI integration (Claude)
# - Storage management (Vultr)
# - Bookmark management (Raindrop)
```

### 5. Models Module (app/models/)

**Responsibilities:**
- Placeholder for ORM models
- Future database schema definitions
- Future Pydantic request/response models

**Interface:**
```python
# Placeholder - will contain:
# - SQLAlchemy ORM models
# - Pydantic schemas for API validation
```

## Data Models

### Configuration Model

```python
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
```

### Health Check Response Model

```python
class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str
```

### Future Models

The models directory will eventually contain:
- **Document**: Medical document metadata and content
- **User**: User authentication and profile information
- **ProcessingJob**: AI processing job status and results
- **Annotation**: Document annotations and highlights

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*


### Property 1: CORS origin validation

*For any* origin header value, when a request is made with that origin, the system should only include CORS allow headers in the response if the origin matches the configured CORS_ORIGINS pattern (including wildcard "*" matching any origin).

**Validates: Requirements 5.3, 5.4**

### Property 2: Module import integrity

*For any* Python module in the application (app, app.api, app.core, app.models, app.services), importing that module should complete without raising an ImportError.

**Validates: Requirements 8.1, 8.2**

## Error Handling

### Configuration Errors

**Missing Required Configuration:**
- When critical environment variables are missing (e.g., API keys for production), the application should fail fast at startup with a clear error message
- The Settings class should validate required fields based on the ENV setting

**Invalid Configuration Values:**
- When configuration values are malformed (e.g., invalid URLs), Pydantic validation should raise ValidationError with descriptive messages
- CORS_ORIGINS should be parsed correctly whether it's a single value, comma-separated list, or wildcard

### HTTP Errors

**404 Not Found:**
- When a client requests a non-existent endpoint, FastAPI should return a 404 with a JSON error response
- The error response should include a detail message

**405 Method Not Allowed:**
- When a client uses an incorrect HTTP method on an endpoint, FastAPI should return a 405 response

**500 Internal Server Error:**
- When an unhandled exception occurs, FastAPI should return a 500 response
- In development (ENV=local), the response should include a stack trace
- In production, the response should hide implementation details

### CORS Errors

**Origin Rejection:**
- When a request comes from a non-allowed origin, the CORS middleware should not include Access-Control-Allow-Origin headers
- The browser will block the response, but the server should still process the request

### Import Errors

**Module Not Found:**
- When a required module cannot be imported at startup, Python should raise ImportError with the module name
- The error should be logged and the application should fail to start

## Testing Strategy

The testing strategy employs both unit testing and property-based testing to ensure comprehensive coverage of the application's behavior.

### Unit Testing

Unit tests will verify specific examples and integration points:

**Configuration Tests:**
- Test that Settings loads values from .env file correctly
- Test that default values are applied when environment variables are not set
- Test that all required configuration fields are present

**Health Endpoint Tests:**
- Test that GET /health returns 200 status code
- Test that response body contains {"status": "ok"}
- Test that the endpoint is accessible at the root path

**Application Structure Tests:**
- Test that all required directories exist (app/, app/api/, app/core/, app/models/, app/services/)
- Test that all required files exist (__init__.py files, main.py, routes.py, config.py)
- Test that requirements.txt contains required dependencies

**Router Integration Tests:**
- Test that API router is included in the main application
- Test that routes are mounted with the correct API_PREFIX
- Test that CORS middleware is added to the application

### Property-Based Testing

Property-based tests will verify universal properties across many inputs using the **Hypothesis** library for Python:

**Property Test Configuration:**
- Each property-based test will run a minimum of 100 iterations
- Tests will use Hypothesis strategies to generate random test data
- Each test will be tagged with a comment referencing the design document property

**CORS Property Tests:**
- **Property 1: CORS origin validation**
  - Generate random origin strings (valid domains, invalid formats, wildcards)
  - Set CORS_ORIGINS to various patterns (specific domains, comma-separated lists, "*")
  - Verify that Access-Control-Allow-Origin header is only present when origin matches configuration
  - Tag: `# Feature: medical-doc-ai-backend, Property 1: CORS origin validation`

**Import Property Tests:**
- **Property 2: Module import integrity**
  - Iterate through all application modules (app, app.api, app.core, app.models, app.services)
  - Attempt to import each module dynamically
  - Verify that no ImportError is raised for any module
  - Tag: `# Feature: medical-doc-ai-backend, Property 2: Module import integrity`

### Test Organization

```
tests/
├── __init__.py
├── test_config.py          # Unit tests for configuration
├── test_health.py          # Unit tests for health endpoint
├── test_structure.py       # Unit tests for project structure
├── test_cors_property.py   # Property test for CORS validation
└── test_imports_property.py # Property test for module imports
```

### Testing Tools

- **pytest**: Test framework and runner
- **pytest-asyncio**: Support for testing async FastAPI endpoints
- **httpx**: Async HTTP client for testing FastAPI applications
- **hypothesis**: Property-based testing library
- **pytest-cov**: Code coverage reporting

### Continuous Testing

- Tests should run automatically on every commit via CI/CD
- Minimum code coverage target: 80%
- All tests must pass before merging to main branch
- Property-based tests should be run with increased iterations (1000+) in CI

## Deployment Considerations

### Local Development

- Use uvicorn with --reload flag for hot reloading
- Load configuration from .env file
- Enable debug mode and detailed error messages
- CORS_ORIGINS can be set to "*" for convenience

### Production Deployment on Vultr

**Compute Infrastructure:**
- Deploy on Vultr Cloud Compute instances (optimized for Python/FastAPI workloads)
- Use uvicorn with multiple workers for concurrency (workers = 2 * CPU cores + 1)
- Consider Vultr Kubernetes Engine (VKE) for container orchestration at scale
- Load configuration from environment variables (not .env file)

**Storage:**
- Use Vultr Object Storage for medical document storage (S3-compatible API)
- Configure VULTR_OBJECT_STORAGE_* environment variables for bucket access
- Enable versioning and lifecycle policies for document retention

**Database:**
- Use Vultr Managed Databases for PostgreSQL (future requirement)
- Configure DATABASE_URL with connection pooling
- Enable automated backups and point-in-time recovery

**Security:**
- Disable debug mode and hide error details in production
- Set specific CORS_ORIGINS for security (frontend domain only)
- Enable HTTPS/TLS termination at Vultr Load Balancer
- Use Vultr Firewall to restrict access to backend services
- Store API keys in Vultr's secure environment variable management

**LiquidMetal Integration:**
- Deploy LiquidMetal AI infrastructure components alongside FastAPI service
- Configure LiquidMetal endpoints for AI processing pipelines
- Use LiquidMetal's pre-built connectors for Claude API integration
- Leverage LiquidMetal's monitoring and observability tools

**Monitoring:**
- Use Vultr monitoring for CPU, memory, and network metrics
- Integrate with LiquidMetal's AI-specific monitoring dashboards
- Set up alerts for service health and performance degradation

### Environment Variables

All sensitive configuration should be provided via environment variables:
- API keys should never be committed to version control
- .env file should be in .gitignore
- .env.example should contain all keys with placeholder values

### Health Monitoring

- The /health endpoint can be used by load balancers and monitoring systems
- Future enhancements could include:
  - Database connectivity checks
  - External service availability checks
  - Memory and CPU usage metrics

## Future Enhancements

This initial implementation establishes the foundation. Future iterations will add:

1. **Authentication & Authorization:**
   - JWT-based authentication
   - Role-based access control for medical professionals
   - API key authentication for service-to-service calls
   - Integration with LiquidMetal's authentication components

2. **Document Management:**
   - Upload medical documents (PDF, DOCX, images)
   - Store documents in Vultr Object Storage with S3-compatible API
   - Retrieve and list documents with metadata
   - Use LiquidMetal's document processing pipelines

3. **AI Processing with LiquidMetal:**
   - Integration with Claude API via LiquidMetal's pre-built connectors
   - Extract medical entities (diagnoses, medications, procedures) using LiquidMetal's NLP components
   - Generate summaries and insights with LiquidMetal's AI orchestration layer
   - Leverage LiquidMetal's prompt management and versioning
   - Use LiquidMetal's caching layer for improved performance

4. **Database Integration:**
   - SQLAlchemy ORM models for documents, users, and processing jobs
   - Deploy on Vultr Managed Database (PostgreSQL)
   - Database migrations with Alembic
   - Connection pooling and query optimization
   - Use LiquidMetal's data layer abstractions

5. **Raindrop Integration:**
   - Sync medical research bookmarks
   - Categorize and tag documents
   - Search across bookmarks and documents
   - Integrate with LiquidMetal's knowledge graph

6. **Advanced Features:**
   - Real-time processing status via WebSockets
   - Batch document processing with LiquidMetal's job queue
   - Document versioning and audit trails
   - Export processed data in various formats
   - Multi-region deployment on Vultr for global availability
   - Use LiquidMetal's observability stack for AI model monitoring
