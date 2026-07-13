from app.services.keyword_analyzer import compare_keywords


resume_skills = {
    "python",
    "sql",
    "docker",
    "git"
}

job_skills = {
    "python",
    "docker",
    "aws",
    "kubernetes"
}


result = compare_keywords(
    resume_skills,
    job_skills
)

print(result)