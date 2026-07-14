"""
FFmpeg Utility Functions
"""

import subprocess
import shutil
from pathlib import Path


class FFmpegError(Exception):
    pass


def ffmpeg_exists():
    """Check whether FFmpeg is installed."""
    return shutil.which("ffmpeg") is not None


def ffprobe_exists():
    """Check whether FFprobe is installed."""
    return shutil.which("ffprobe") is not None


def run_command(command):
    """
    Execute an FFmpeg command.
    """

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise FFmpegError(result.stderr)

    return result.stdout


def get_video_info(video_path):
    """
    Return video metadata using ffprobe.
    """

    command = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        str(video_path)
    ]

    return run_command(command)


def convert_video(input_file, output_file):
    """
    Convert video format.
    """

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_file),
        str(output_file)
    ]

    run_command(command)


def extract_audio(input_video, output_audio):
    """
    Extract audio from video.
    """

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_video),
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        str(output_audio)
    ]

    run_command(command)