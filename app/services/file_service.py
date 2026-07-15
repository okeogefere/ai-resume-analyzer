import os
import uuid


UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx"
}

os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(file):
    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
        "Only PDF and DOCX files are supported"
    )

    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path