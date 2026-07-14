"""
Professional Video Merger
"""

from pathlib import Path

from utils import (
    ensure_dir,
    get_logger,
    run_command
)

logger = get_logger()


class VideoMerger:

    def __init__(self,
                 output_dir="outputs/video"):

        self.output_dir = Path(output_dir)

        ensure_dir(self.output_dir)

    def merge(self,
              video_path,
              audio_path,
              output_name="translated_video.mp4"):

        output = self.output_dir / output_name

        logger.info("Merging video and translated audio...")

        command = [

            "ffmpeg",

            "-y",

            "-i", str(video_path),

            "-i", str(audio_path),

            "-map", "0:v:0",

            "-map", "1:a:0",

            "-c:v", "copy",

            "-c:a", "aac",

            "-shortest",

            str(output)

        ]

        run_command(command)

        logger.info(f"Saved : {output}")

        return str(output)