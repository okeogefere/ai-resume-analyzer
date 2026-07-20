import os
import json

import google.generativeai as genai
from dotenv import load_dotenv
from app.core.config import settings
from app.core.logging_config import logger



load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)



model = genai.GenerativeModel(
    settings.GEMINI_MODEL
)


def generate_resume_feedback(
    resume_text: str,
    job_description: str,
    analysis: dict
):
    logger.info("Sending request to Gemini")

    prompt = f"""
You are an expert technical recruiter and ATS resume reviewer.

Analyze the following resume.

Resume:
{resume_text}

Job Description:
{job_description}

Current Analysis:
{analysis}

Respond ONLY with valid JSON.

Use this exact structure:

{{
    "summary": "...",
    "strengths": [
        "...",
        "..."
    ],
    "missing_skills": [
        "...",
        "..."
    ],
    "suggestions": [
        "...",
        "...",
        "..."
    ]
}}

Do not include markdown.
Do not wrap the JSON in triple backticks.
Do not include any explanation outside the JSON.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()
    
    logger.info("AI feedback received")

    return json.loads(text)


