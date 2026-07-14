"""
Voice Activity Detection (Basic VAD)

Future:
Replace this implementation with Silero VAD.
"""

from pathlib import Path

from pydub import AudioSegment
from pydub.silence import split_on_silence

from utils import ensure_dir, get_logger

logger = get_logger()


class VoiceActivityDetector:

    def __init__(
        self,
        output_dir="temp/chunks",
        silence_thresh=-40,
        min_silence_len=700,
        keep_silence=300,
    ):
        self.output_dir = Path(output_dir)
        ensure_dir(self.output_dir)

        self.silence_thresh = silence_thresh
        self.min_silence_len = min_silence_len
        self.keep_silence = keep_silence

    def split(self, audio_path):

        audio = AudioSegment.from_file(audio_path)

        chunks = split_on_silence(
            audio,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_thresh,
            keep_silence=self.keep_silence,
        )

        output_files = []

        for index, chunk in enumerate(chunks):

            output = self.output_dir / f"chunk_{index+1}.wav"

            chunk.export(output, format="wav")

            output_files.append(str(output))

        logger.info(f"Detected {len(output_files)} speech segments.")

        return output_files