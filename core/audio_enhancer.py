"""
Professional Audio Enhancer
"""

from pathlib import Path

from utils import (
    ensure_dir,
    get_logger,
    run_command,
)

logger = get_logger()


class AudioEnhancer:

    def __init__(self, output_dir="temp/enhanced"):
        self.output_dir = Path(output_dir)
        ensure_dir(self.output_dir)

    def enhance(self, input_audio):
        input_audio = Path(input_audio)

        output_audio = self.output_dir / f"{input_audio.stem}_enhanced.wav"

        logger.info(f"Enhancing audio: {input_audio.name}")

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(input_audio),
            "-af",
            "loudnorm",
            "-ar",
            "16000",
            "-ac",
            "1",
            str(output_audio),
        ]

        run_command(command)

        logger.info(f"Enhanced audio saved: {output_audio}")

        return str(output_audio)