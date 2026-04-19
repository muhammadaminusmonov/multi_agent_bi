from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import dashboard, domain, chat

app = FastAPI(title="Multi-Agent BI Backend", version="0.1.0")

# CORS for Streamlit frontend (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)
app.include_router(domain.router)
# chat router will be added next
app.include_router(chat.router)

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# ... your app code ...
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)