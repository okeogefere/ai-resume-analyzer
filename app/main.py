from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.resume import router as resume_router

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the AI Resume Analyzer API"
    }

app.include_router(health_router)
app.include_router(resume_router)