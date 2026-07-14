"""
File Validation Utilities
"""

from pathlib import Path
import mimetypes

VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".wmv",
    ".flv",
    ".webm",
    ".m4v",
}

AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".ogg",
    ".m4a",
}

SUBTITLE_EXTENSIONS = {
    ".srt",
    ".vtt",
    ".ass",
}


def file_exists(path):
    return Path(path).exists()


def is_empty(path):
    return Path(path).stat().st_size == 0


def extension(path):
    return Path(path).suffix.lower()


def validate_video(path):
    if not file_exists(path):
        raise FileNotFoundError(path)

    return extension(path) in VIDEO_EXTENSIONS


def validate_audio(path):
    if not file_exists(path):
        raise FileNotFoundError(path)

    return extension(path) in AUDIO_EXTENSIONS


def validate_subtitle(path):
    if not file_exists(path):
        raise FileNotFoundError(path)

    return extension(path) in SUBTITLE_EXTENSIONS


def get_mime_type(path):
    mime, _ = mimetypes.guess_type(path)
    return mime


def file_size_mb(path):
    return round(Path(path).stat().st_size / (1024 * 1024), 2)