import os
import uuid
from app.core.config import settings
from app.core.logging_config import logger



settings.UPLOAD_DIR
settings.ALLOWED_EXTENSIONS

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(file):
    logger.info(f"Saving file: {file.filename}")

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in settings.ALLOWED_EXTENSIONS:
        raise ValueError(
        "Only PDF and DOCX files are supported"
    )

    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join(
        settings.UPLOAD_DIR,
        unique_filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read()) 
    
    logger.info("File saved successfully")

    return file_path

