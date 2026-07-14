"""
Professional Audio Extractor
"""

from pathlib import Path

from utils import (
    ensure_dir,
    get_logger,
    extract_audio,
)

logger = get_logger()


class AudioExtractor:

    def __init__(self, output_dir="temp/audio"):
        self.output_dir = Path(output_dir)
        ensure_dir(self.output_dir)

    def extract(self, video_path):
        """
        Extract WAV audio from a video.
        """

        video_path = Path(video_path)

        output_audio = self.output_dir / f"{video_path.stem}.wav"

        logger.info(f"Extracting audio from: {video_path.name}")

        extract_audio(
            str(video_path),
            str(output_audio)
        )

        logger.info(f"Saved audio: {output_audio}")

        return str(output_audio)