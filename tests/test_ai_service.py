from app.services.ai_service import generate_resume_feedback


resume = """
Python developer with FastAPI, Django, SQL,
PostgreSQL, and AWS experience.
"""


job = """
Looking for Python developer with FastAPI,
Docker, Kubernetes, and AWS.
"""


analysis = {
    "matched_skills": [
        "python",
        "fastapi",
        "aws"
    ],
    "missing_skills": [
        "docker",
        "kubernetes"
    ],
    "match_score": 60
}


result = generate_resume_feedback(
    resume,
    job,
    analysis
)


print(result)