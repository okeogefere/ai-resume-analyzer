from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.file_service import save_uploaded_file
from app.services.resume_parser import extract_resume_text
from app.services.resume_analyzer import analyze_resume

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

    file_path = None

    try:
        # Save uploaded file
        file_path = save_uploaded_file(file)

        # Extract text from resume
        resume_text = extract_resume_text(file_path)

        # Analyze resume
        result = analyze_resume(
            resume_text,
            job_description
        )

        return result

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

    finally:
        # Delete uploaded file after analysis
        if file_path and Path(file_path).exists():
            Path(file_path).unlink()