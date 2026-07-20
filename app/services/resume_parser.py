import fitz
from docx import Document

from app.core.logging_config import logger


def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_text_from_docx(file_path):
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file_path):
    logger.info(f"Extracting resume text from: {file_path}")

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)

    else:
        logger.error(f"Unsupported file format: {file_path}")
        raise ValueError("Unsupported file format")

    logger.info("Resume text extracted successfully")

    return text