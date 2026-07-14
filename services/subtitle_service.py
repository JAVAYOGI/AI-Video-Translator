"""
Subtitle Service
"""

from core import SubtitleGenerator


class SubtitleService:

    def __init__(self):

        self.generator = SubtitleGenerator()

    def create(
        self,
        translated,
    ):

        return self.generator.create(
            translated,
            "translated.srt",
        )