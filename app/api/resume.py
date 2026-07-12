from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException
router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


ALLOWED_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed"
        )

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Resume uploaded successfully"
    }