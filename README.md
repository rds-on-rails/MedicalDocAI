# MedicalDocAI

Medical Document AI Assistant Backend - A FastAPI-based REST API service for AI-powered medical document processing.

## Overview

The Medical Document AI Assistant backend provides foundational infrastructure for AI-powered medical document processing. Built with FastAPI and Python 3.11+, the service is designed to be hosted on Vultr cloud infrastructure and leverages LiquidMetal's pre-built, enterprise-grade AI infrastructure components to accelerate development.

### Key Features

- **FastAPI Framework**: High-performance async web framework with automatic OpenAPI documentation
- **Vultr Cloud Hosting**: Scalable cloud infrastructure with compute, object storage, and managed databases
- **LiquidMetal Integration**: Pre-built AI components for rapid development of AI-powered features
- **Modular Architecture**: Clean separation of concerns with distinct layers for API, business logic, and data
- **Environment-Based Configuration**: Flexible configuration management for different deployment environments
- **CORS Support**: Configurable cross-origin resource sharing for frontend integration

## Infrastructure

### Vultr Cloud Services

- **Compute**: Vultr Cloud Compute instances for hosting the FastAPI application
- **Storage**: Vultr Object Storage (S3-compatible) for medical document storage
- **Database**: Vultr Managed Database (PostgreSQL) for structured data
- **Networking**: Vultr Load Balancers and Firewall for traffic distribution and security

### LiquidMetal AI Components

- **AI Orchestration Layer**: Manages AI model invocations and workflow coordination
- **Prompt Management**: Version-controlled prompt templates for medical document analysis
- **Model Connectors**: Pre-built integrations with Claude API and other AI services
- **Caching Layer**: Intelligent caching of AI responses to reduce latency and costs
- **Observability**: Monitoring and logging for AI model performance and costs

## Setup Instructions

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd MedicalDocAI
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Configure environment variables**

Copy the example environment file and update with your credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys and configuration. See the Environment Configuration section below for details.

### Running the Development Server

Start the development server with hot reloading:

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc
- **Health check**: http://localhost:8000/health

## Environment Configuration

The application uses environment variables for configuration. All required variables are listed in `.env.example`:

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | MedicalDocAI |
| `ENV` | Environment (local, staging, production) | local |
| `API_PREFIX` | API route prefix | /api |
| `CORS_ORIGINS` | Allowed CORS origins (comma-separated or *) | * |
| `CLAUDE_API_KEY` | Claude API key for AI processing | - |
| `RAINDROP_API_KEY` | Raindrop API key for bookmark management | - |
| `DATABASE_URL` | PostgreSQL database connection URL | - |
| `VULTR_OBJECT_STORAGE_ACCESS_KEY` | Vultr Object Storage access key | - |
| `VULTR_OBJECT_STORAGE_SECRET_KEY` | Vultr Object Storage secret key | - |
| `VULTR_OBJECT_STORAGE_BUCKET` | Vultr Object Storage bucket name | - |

## Project Structure

```
MedicalDocAI/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py           # API route definitions
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py           # Configuration management
│   ├── models/                 # Data models (placeholder)
│   │   └── __init__.py
│   └── services/               # Business logic (placeholder)
│       └── __init__.py
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_health.py
│   ├── test_structure.py
│   ├── test_router.py
│   ├── test_cors_property.py
│   └── test_imports_property.py
├── .env.example                # Example environment variables
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md
```

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=html
```

Run specific test files:

```bash
pytest tests/test_health.py -v
```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Production Deployment

### Vultr Deployment

1. **Provision Vultr Cloud Compute instance**
   - Choose an instance optimized for Python/FastAPI workloads
   - Configure firewall rules to allow HTTP/HTTPS traffic

2. **Set up Vultr Object Storage**
   - Create a bucket for medical document storage
   - Generate access keys and configure environment variables

3. **Configure Vultr Managed Database**
   - Provision a PostgreSQL database
   - Configure connection pooling and backups
   - Update DATABASE_URL environment variable

4. **Deploy the application**

```bash
# Install dependencies
pip install -r requirements.txt

# Run with multiple workers
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

5. **Set up monitoring**
   - Configure Vultr monitoring for CPU, memory, and network metrics
   - Integrate with LiquidMetal's AI-specific monitoring dashboards

### Security Considerations

- Set `ENV=production` in production environments
- Use specific CORS origins (not wildcard `*`)
- Store API keys securely using Vultr's environment variable management
- Enable HTTPS/TLS termination at Vultr Load Balancer
- Use Vultr Firewall to restrict access to backend services

## Future Enhancements

- Authentication & Authorization (JWT, role-based access control)
- Document Management (upload, storage, retrieval)
- AI Processing with LiquidMetal (entity extraction, summarization)
- Database Integration (SQLAlchemy ORM, migrations)
- Raindrop Integration (bookmark syncing, categorization)
- Advanced Features (WebSockets, batch processing, versioning)

## License

See LICENSE file for details.
