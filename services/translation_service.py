"""
Translation Service
"""

from core import (
    Transcriber,
    Translator,
)


class TranslationService:

    def __init__(self):

        self.transcriber = Transcriber()

    def process(
        self,
        audio_path,
        target_language,
    ):

        transcript = self.transcriber.transcribe(audio_path)

        translator = Translator(
            source="auto",
            target=target_language,
        )

        translated = translator.translate(transcript)

        return translated