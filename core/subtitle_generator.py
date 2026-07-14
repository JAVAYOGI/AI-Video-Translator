from pathlib import Path

from utils import (
    ensure_dir,
    get_logger
)

logger = get_logger()


class SubtitleGenerator:

    def __init__(self,
                 output_dir="outputs/subtitles"):

        self.output_dir = Path(output_dir)

        ensure_dir(self.output_dir)

    def format_time(self, seconds):

        hours = int(seconds // 3600)

        minutes = int(
            (seconds % 3600) // 60
        )

        secs = int(seconds % 60)

        millis = int(
            (seconds - int(seconds)) * 1000
        )

        return (
            f"{hours:02}:{minutes:02}:{secs:02},"
            f"{millis:03}"
        )

    def create(self,
               translated,
               filename="subtitle.srt"):

        output = self.output_dir / filename

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as file:

            for index, segment in enumerate(
                translated,
                start=1
            ):

                file.write(f"{index}\n")

                file.write(
                    f"{self.format_time(segment['start'])}"
                    " --> "
                    f"{self.format_time(segment['end'])}\n"
                )

                file.write(
                    segment["translated"] + "\n\n"
                )

        logger.info(
            f"Subtitle saved : {output}"
        )

        return str(output)