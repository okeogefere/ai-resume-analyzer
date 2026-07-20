from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.file_service import save_uploaded_file
from app.services.resume_parser import extract_resume_text
from app.services.resume_analyzer import analyze_resume
from app.services.ai_service import generate_resume_feedback
from app.core.logging_config import logger

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload and validate a resume file.
    """

    try:
        file_path = save_uploaded_file(file)

        return {
            "message": "Resume uploaded successfully",
            "filename": Path(file_path).name
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/analyze")
async def analyze_resume_endpoint(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Analyze a resume against a job description.
    """

    logger.info("Analyze endpoint called")

    file_path = None

    try:
        file_path = save_uploaded_file(file)

        resume_text = extract_resume_text(file_path)

        result = analyze_resume(
            resume_text,
            job_description
        )

        ai_feedback = generate_resume_feedback(
            resume_text,
            job_description,
            result
        )

        logger.info("Resume analyzed successfully")

        return {
            **result,
            "ai_feedback": ai_feedback
        }

    except ValueError as e:
        logger.warning(f"Validation error: {e}")

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        logger.exception("Unexpected error during resume analysis")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

    finally:
        if file_path and Path(file_path).exists():
            Path(file_path).unlink()

        logger.info("Temporary file deleted")

