from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Settings:

    APP_NAME: str = os.getenv("APP_NAME", "AI Video Translator")

    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")

    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

    HOST: str = os.getenv("HOST", "127.0.0.1")

    PORT: int = int(os.getenv("PORT", 7860))

    TEMP_DIR: str = os.getenv("TEMP_DIR", "temp")

    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "outputs")

    MODEL_SIZE: str = os.getenv("MODEL_SIZE", "medium")

    DEVICE: str = os.getenv("DEVICE", "auto")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    DEFAULT_SOURCE_LANGUAGE: str = os.getenv(
        "DEFAULT_SOURCE_LANGUAGE",
        "auto"
    )

    DEFAULT_TARGET_LANGUAGE: str = os.getenv(
        "DEFAULT_TARGET_LANGUAGE",
        "ta"
    )

    MAX_VIDEO_SIZE_MB: int = int(
        os.getenv("MAX_VIDEO_SIZE_MB", 2048)
    )

    MAX_AUDIO_LENGTH_MINUTES: int = int(
        os.getenv("MAX_AUDIO_LENGTH_MINUTES", 180)
    )


settings = Settings()