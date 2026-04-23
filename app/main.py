from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import dashboard, domain, chat
from app.db.database import engine
from sqlalchemy import inspect

app = FastAPI(title="Multi-Agent BI Backend", version="0.1.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(dashboard.router)
app.include_router(domain.router)
app.include_router(chat.router)


@app.on_event("startup")
async def startup_event():
    """Check if database is seeded; if not, seed it."""
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if "sales" not in tables:
        print("Database not seeded. Running seed script...")
        from app.db.seed import seed_database
        seed_database()
    else:
        print("Database already seeded.")


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}