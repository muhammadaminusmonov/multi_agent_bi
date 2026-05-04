markdown
# 🤖 Multi-Agent Business Intelligence (BI) System

A powerful backend system for **multi-agent business intelligence analytics**, leveraging AI agents to process and analyze business data through natural language interactions. Built with **FastAPI**, **LangChain**, and **PostgreSQL** for scalable, intelligent data insights.

---

## ✨ Features

- 🧠 **Multi-Agent Architecture**: Leverages LangChain to coordinate specialized AI agents for data analysis, query planning, and insight generation
- 💬 **Natural Language Queries**: Ask business questions in plain English and receive structured analytical responses
- 📊 **Dashboard Endpoints**: RESTful API endpoints for retrieving analytics, metrics, and visualizations
- 🔗 **Domain Management**: Organize and manage multiple data sources, domains, and business contexts
- 🗄️ **PostgreSQL Integration**: Robust relational database with auto-seeding for quick setup and testing
- 🔐 **CORS-Enabled API**: Ready for frontend integration with React, Vue, or any modern SPA framework
- ⚙️ **Environment-Based Configuration**: Secure management of API keys and credentials via `.env`
- 🐳 **Docker-Ready**: Containerized deployment support for consistent environments

---

## 🏗️ Architecture

```
multi_agent_bi/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── dashboard.py    # Analytics & visualization endpoints
│   │   │   │   ├── domain.py       # Domain/data source management
│   │   │   │   └── chat.py         # Natural language query interface
│   │   │   └── api.py              # API router aggregation
│   │   └── deps.py                 # Dependency injection utilities
│   ├── core/
│   │   ├── config.py               # Settings & environment management
│   │   ├── security.py             # Auth & security utilities (if added)
│   │   └── database.py             # DB session & connection handling
│   ├── models/
│   │   ├── base.py                 # SQLAlchemy base & common models
│   │   ├── domain.py               # Domain/entity data models
│   │   └── dashboard.py            # Analytics result models
│   ├── services/
│   │   ├── agent_orchestrator.py   # LangChain agent coordination logic
│   │   ├── query_processor.py      # NLP-to-SQL/query translation
│   │   └── data_connector.py       # External data source integrations
│   ├── utils/
│   │   ├── logger.py               # Centralized logging configuration
│   │   └── helpers.py              # Shared utility functions
│   ├── main.py                     # FastAPI application entry point
│   └── __init__.py
├── alembic/                        # Database migration scripts
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── tests/                          # Unit & integration tests
│   ├── api/
│   ├── services/
│   └── conftest.py
├── .env.example                    # Environment variables template
├── .gitignore
├── alembic.ini                     # Alembic configuration
├── docker-compose.yml              # Multi-container orchestration
├── Dockerfile                      # Container build instructions
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🛠️ Tech Stack
```
| Category | Technology |
|----------|-----------|
| **Backend Framework** | FastAPI 0.109+ |
| **AI/LLM Framework** | LangChain + OpenAI API |
| **Data Processing** | Pandas, NumPy |
| **Database** | PostgreSQL 14+ |
| **ORM** | SQLAlchemy 2.0 (Async) |
| **Migrations** | Alembic |
| **API Documentation** | OpenAPI 3.0 (Auto-generated Swagger UI) |
| **Configuration** | python-dotenv, Pydantic Settings |
| **Testing** | pytest, httpx |
| **Containerization** | Docker, Docker Compose |
```
---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Docker & Docker Compose (optional, for containerized setup)
- OpenAI API key (for agent functionality)

### 1. Clone the Repository

```bash
git clone https://github.com/muhammadaminusmonov/multi_agent_bi.git
cd multi_agent_bi
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/multi_agent_bi

# OpenAI
OPENAI_API_KEY=sk-your-openai-key-here

# App Settings
ENVIRONMENT=development
API_V1_STR=/api/v1
PROJECT_NAME=Multi-Agent BI
```

### 3. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Initialize Database

```bash
# Run migrations
alembic upgrade head

# (Optional) Seed initial data
python -m app.core.seed_data
```

### 5. Run the Application

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### 6. Access the API

- 🌐 **Base URL**: `http://localhost:8000`
- 📚 **Interactive Docs**: `http://localhost:8000/docs` (Swagger UI)
- 🔍 **Alternative Docs**: `http://localhost:8000/redoc` (ReDoc)

---

## 📡 API Endpoints Overview

### 🔗 Domain Management
```
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/domains/` | List all configured domains | Optional |
| `POST` | `/api/v1/domains/` | Create a new data domain | ✅ |
| `GET` | `/api/v1/domains/{id}` | Get domain details | Optional |
| `PUT` | `/api/v1/domains/{id}` | Update domain configuration | ✅ |
| `DELETE` | `/api/v1/domains/{id}` | Delete a domain | ✅ |
```
### 📊 Dashboard & Analytics
```
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/v1/dashboard/metrics` | Retrieve key business metrics | Optional |
| `POST` | `/api/v1/dashboard/query` | Execute custom analytical query | ✅ |
| `GET` | `/api/v1/dashboard/visualizations` | List available chart configs | Optional |
| `POST` | `/api/v1/dashboard/export` | Export report as CSV/PDF | ✅ |
```
### 💬 Natural Language Chat Interface
```
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/v1/chat/ask` | Submit natural language question | ✅ |
| `GET` | `/api/v1/chat/history` | Retrieve conversation history | ✅ |
| `DELETE` | `/api/v1/chat/history` | Clear chat history | ✅ |
```
### 🔐 Authentication (If Enabled)
```
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/auth/login` | Obtain JWT access token |
| `POST` | `/api/v1/auth/register` | Register new user account |
| `GET` | `/api/v1/users/me` | Get current user profile |
```
---

## 🧠 How Multi-Agent Analysis Works

```mermaid
graph LR
    A[User Query] --> B[Query Parser Agent]
    B --> C{Intent Classification}
    C -->|Analytical| D[Data Retrieval Agent]
    C -->|Comparative| E[Comparison Agent]
    C -->|Predictive| F[Forecasting Agent]
    D --> G[Query Executor]
    E --> G
    F --> G
    G --> H[Results Aggregator]
    H --> I[Response Formatter]
    I --> J[JSON/NL Response]
```

### Agent Roles

1. **Query Parser Agent**: Interprets natural language, extracts entities, identifies intent
2. **Data Retrieval Agent**: Generates optimized SQL/queries, fetches relevant data
3. **Analysis Agent**: Applies statistical methods, identifies trends & patterns
4. **Insight Generator**: Synthesizes findings into actionable business insights
5. **Response Formatter**: Structures output for API consumption or natural language reply

---

## 🗄️ Database Schema (Key Models)

### Domain Model
```python
class Domain(Base):
    __tablename__ = "domains"
    
    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(255), nullable=False, unique=True)
    description: Optional[str] = Column(Text)
    data_source_config: dict = Column(JSONB)  # Connection params, credentials
    schema_metadata: dict = Column(JSONB)     # Table/column descriptions
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, onupdate=datetime.utcnow)
```

### Dashboard Metric Model
```python
class DashboardMetric(Base):
    __tablename__ = "dashboard_metrics"
    
    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    domain_id: UUID = Column(UUID(as_uuid=True), ForeignKey("domains.id"))
    name: str = Column(String(255), nullable=False)
    query_template: str = Column(Text)  # Parameterized SQL/DSL
    visualization_type: str = Column(String(50))  # line, bar, pie, table
    refresh_interval: int = Column(Integer, default=3600)  # seconds
    is_active: bool = Column(Boolean, default=True)
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/api/test_chat.py

# Run async tests
pytest -o asyncio_mode=auto
```

### Test Structure
```
tests/
├── conftest.py              # Shared fixtures (DB, client, auth)
├── api/
│   ├── test_domains.py      # Domain endpoint tests
│   ├── test_dashboard.py    # Analytics endpoint tests
│   └── test_chat.py         # NLP interface tests
├── services/
│   ├── test_agent_orchestrator.py
│   └── test_query_processor.py
└── utils/
    └── test_helpers.py
```
---

## 🐳 Docker Deployment

### Build & Run with Docker Compose

```bash
# Start all services (app + postgres)
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down

# Stop + remove volumes (resets DB)
docker-compose down -v
```
### docker-compose.yml Overview
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql+asyncpg://user:pass@db:5432/multi_agent_bi
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - db
    volumes:
      - ./app:/app/app  # Hot-reload for development

  db:
    image: postgres:14-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: multi_agent_bi
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```
---

## 🔐 Security Best Practices

- ✅ **Environment Variables**: Never commit `.env`; use `.env.example` as template
- ✅ **Secrets Management**: Use vault/secret manager for production API keys
- ✅ **Input Validation**: Pydantic models enforce strict request schemas
- ✅ **CORS Configuration**: Restrict origins in production via `settings.py`
- ✅ **Rate Limiting**: Implement via middleware for public endpoints
- ✅ **SQL Injection Protection**: SQLAlchemy ORM + parameterized queries
- ✅ **Audit Logging**: Log sensitive operations with user context

---

## 🔄 CI/CD Integration (GitHub Actions Example)

`.github/workflows/ci.yml`:
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        env:
          DATABASE_URL: postgresql+asyncpg://postgres:test@localhost:5432/postgres
          OPENAI_API_KEY: test-key
        run: pytest --cov=app --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```
---

## 🛠️ Development Guidelines

### Code Style
- Follow [PEP 8](https://pep8.org/) with 4-space indentation
- Use type hints for all function signatures
- Docstrings: Google style for public APIs
- Max line length: 88 characters (Black formatter compatible)

### Commit Convention
feat(api): add natural language query endpoint
fix(db): resolve connection timeout in async session
docs(readme): update deployment instructions
test(chat): add integration tests for agent orchestration
refactor(agent): extract query parsing logic into service


### Branch Strategy
- `main`: Production-ready code (protected)
- `develop`: Integration branch for features
- `feature/*`: New functionality (e.g., `feature/forecasting-agent`)
- `hotfix/*`: Critical production fixes

---

## 📦 Production Deployment Checklist

- [ ] Set `ENVIRONMENT=production` in `.env`
- [ ] Configure proper `CORS_ALLOW_ORIGINS`
- [ ] Use managed PostgreSQL (AWS RDS, Cloud SQL, etc.)
- [ ] Set up reverse proxy (Nginx, Traefik) with SSL/TLS
- [ ] Enable Gunicorn/Uvicorn workers for concurrency
- [ ] Implement health check endpoint (`/health`)
- [ ] Configure structured logging (JSON format for ELK/Splunk)
- [ ] Set up monitoring (Prometheus metrics endpoint)
- [ ] Rotate API keys and database credentials regularly
- [ ] Enable database backups & point-in-time recovery

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** your feature branch:  
   ```bash
   git checkout -b feat/your-amazing-feature
   ```
3. **Commit** your changes with clear messages:  
   ```bash
   git commit -m "feat: add predictive forecasting agent"
   ```
4. **Push** to your branch:  
   ```bash
   git push origin feat/your-amazing-feature
   ```
5. **Open** a Pull Request with:
   - Clear description of changes
   - Screenshots/logs for UI/behavior changes
   - Updated tests & documentation

### Contribution Areas Needed
- 🧪 Additional unit/integration tests
- 📊 New visualization types (heatmap, funnel, cohort)
- 🔌 Connectors for Snowflake, BigQuery, Redshift
- 🌍 Multi-language support for queries
- 📱 WebSocket endpoint for real-time analytics streaming

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- 🦜⛓️ [LangChain](https://langchain.com) for powerful agent orchestration
- ⚡ [FastAPI](https://fastapi.tiangolo.com) for high-performance async APIs
- 🐘 [PostgreSQL](https://postgresql.org) for robust relational data management
- 🐍 [SQLAlchemy](https://sqlalchemy.org) for elegant database abstraction
- 🧪 [pytest](https://pytest.org) for reliable testing framework

---

> 💡 **Pro Tip**: Start with simple analytical queries like _"Show me monthly revenue trends for Q1 2024"_ to test the agent pipeline. Gradually increase complexity with comparative and predictive questions as you configure your data domains.

**🚀 Ready to transform your business data into intelligent insights?**
```
