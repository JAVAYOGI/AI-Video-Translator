"""
Professional Noise Reduction
"""

from pathlib import Path

from utils import (
    ensure_dir,
    get_logger,
    run_command,
)

logger = get_logger()


class NoiseReducer:

    def __init__(self, output_dir="temp/denoised"):
        self.output_dir = Path(output_dir)
        ensure_dir(self.output_dir)

    def reduce(self, input_audio):
        input_audio = Path(input_audio)

        output_audio = self.output_dir / f"{input_audio.stem}_denoised.wav"

        logger.info(f"Reducing noise: {input_audio.name}")

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(input_audio),
            "-af",
            "highpass=f=80,lowpass=f=8000",
            str(output_audio),
        ]

        run_command(command)

        logger.info(f"Denoised audio saved: {output_audio}")

        return str(output_audio)