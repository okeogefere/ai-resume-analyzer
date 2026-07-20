from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = "AI Resume Analyzer"
    APP_VERSION = "1.0.0"

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    UPLOAD_DIR = BASE_DIR / "uploads"

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".docx",
    }

    GEMINI_MODEL = "models/gemini-flash-latest"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()