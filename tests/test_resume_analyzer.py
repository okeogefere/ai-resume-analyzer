from app.services.resume_analyzer import analyze_resume


resume = """
Python Developer
Skills:
Python
FastAPI
Docker
SQL
Git
"""


job = """
Looking for a Python developer.

Requirements:
Python
FastAPI
Docker
AWS
Kubernetes
"""


result = analyze_resume(
    resume,
    job
)

print(result)