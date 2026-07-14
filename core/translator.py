from models.translator_loader import get_translator
from utils import get_logger

logger = get_logger()


class Translator:

    def __init__(self,
                 source="auto",
                 target="ta"):

        self.translator = get_translator(
            source,
            target
        )

    def translate(self, transcript):

        logger.info("Translating...")

        translated = []

        for segment in transcript["segments"]:

            text = self.translator.translate(
                segment["text"]
            )

            translated.append({

                "id": segment["id"],

                "start": segment["start"],

                "end": segment["end"],

                "duration": segment["duration"],

                "original": segment["text"],

                "translated": text

            })

        logger.info(
            f"Translated {len(translated)} segments."
        )

        return translated