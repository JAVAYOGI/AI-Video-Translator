from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent

HOST = os.getenv("HOST", "127.0.0.1")

PORT = int(os.getenv("PORT", "7860"))

DEBUG = os.getenv("DEBUG", "True") == "True"

DEVICE = os.getenv("DEVICE", "auto")

DEFAULT_LANGUAGE = "ta"

DEFAULT_MODEL = "base"

LOG_LEVEL = "INFO"