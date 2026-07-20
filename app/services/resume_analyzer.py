from app.services.text_cleaner import clean_text
from app.services.keyword_analyzer import (
    extract_keywords,
    compare_keywords,
    calculate_match_score
)
from app.core.logging_config import logger



def analyze_resume(resume_text, job_description):
    logger.info("Starting resume analysis")


    cleaned_resume = clean_text(resume_text)
    cleaned_job = clean_text(job_description)

    resume_skills = extract_keywords(cleaned_resume)
    job_skills = extract_keywords(cleaned_job)

    comparison = compare_keywords(
        resume_skills,
        job_skills
    )

    score = calculate_match_score(
        comparison["matched"],
        len(job_skills)
    )
    logger.info("Resume analysis completed")


    return generate_analysis_report(
        resume_skills,
        job_skills,
        comparison,
        score
    )

def generate_analysis_report(
    resume_skills,
    job_skills,
    comparison,
    score
):

    return {
        "resume_skills": list(resume_skills),
        "job_skills": list(job_skills),
        "matched_skills": list(comparison["matched"]),
        "missing_skills": list(comparison["missing"]),
        "extra_skills": list(comparison["extra"]),
        "match_score": score
    }

