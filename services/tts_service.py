"""
TTS Service
"""

from core import TextToSpeech


class TTSService:

    def __init__(self):

        self.tts = TextToSpeech()

    def generate(
        self,
        translated,
        filename="dubbed.mp3",
    ):

        text = " ".join(
            segment["translated"]
            for segment in translated
        )

        return self.tts.speak(
            text,
            filename,
        )