"""
Professional File Utilities
"""

import shutil
import uuid
from pathlib import Path


def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    Path(directory).mkdir(parents=True, exist_ok=True)


def file_exists(path):
    """Check whether a file exists."""
    return Path(path).exists()


def get_extension(path):
    """Return file extension."""
    return Path(path).suffix.lower()


def get_filename(path):
    """Return filename without extension."""
    return Path(path).stem


def get_file_size_mb(path):
    """Return file size in MB."""
    return round(Path(path).stat().st_size / (1024 * 1024), 2)


def generate_filename(extension):
    """Generate unique filename."""
    return f"{uuid.uuid4().hex}{extension}"


def copy_file(src, dst):
    """Copy file."""
    ensure_dir(Path(dst).parent)
    shutil.copy2(src, dst)


def move_file(src, dst):
    """Move file."""
    ensure_dir(Path(dst).parent)
    shutil.move(src, dst)


def delete_file(path):
    """Delete file if it exists."""
    p = Path(path)
    if p.exists():
        p.unlink()


def delete_directory(path):
    """Delete directory recursively."""
    p = Path(path)
    if p.exists():
        shutil.rmtree(p)


def clean_directory(directory):
    """Delete all files in a directory."""
    folder = Path(directory)

    if not folder.exists():
        return

    for item in folder.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)