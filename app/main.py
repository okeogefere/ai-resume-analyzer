from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes against job descriptions using Python and AI.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the AI Resume Analyzer API"
    }

app.include_router(health_router)
app.include_router(resume_router)