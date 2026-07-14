"""
Professional Speech To Text Engine
"""

from models.whisper_loader import get_whisper_model
from utils import get_logger

logger = get_logger()


class Transcriber:

    def __init__(
        self,
        model_size="base",
        device="auto",
        compute_type="int8",
    ):
        self.model = get_whisper_model(
            model_size=model_size,
            device=device,
            compute_type=compute_type,
        )

    def transcribe(self, audio_path):

        logger.info("Loading Faster-Whisper Model...")

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5,
            vad_filter=True,
            word_timestamps=True,
        )

        results = []

        logger.info(f"Detected Language : {info.language}")
        logger.info(f"Language Probability : {info.language_probability:.3f}")

        for index, segment in enumerate(segments, start=1):

            words = []

            if segment.words:

                for word in segment.words:

                    words.append(
                        {
                            "word": word.word.strip(),
                            "start": round(word.start, 2),
                            "end": round(word.end, 2),
                            "probability": round(word.probability, 3),
                        }
                    )

            results.append(
                {
                    "id": index,
                    "start": round(segment.start, 2),
                    "end": round(segment.end, 2),
                    "duration": round(segment.end - segment.start, 2),
                    "text": segment.text.strip(),
                    "words": words,
                }
            )

        logger.info(f"Total Segments : {len(results)}")

        return {
            "language": info.language,
            "probability": round(info.language_probability, 3),
            "segments": results,
        }