"""
Pipeline Service
"""

from services import (
    AudioService,
    TranslationService,
    SubtitleService,
)

from services.tts_service import TTSService
from services.video_service import VideoService


class PipelineService:

    def __init__(self):

        self.audio = AudioService()

        self.translation = TranslationService()

        self.subtitle = SubtitleService()

        self.tts = TTSService()

        self.video = VideoService()

    def run(
        self,
        video_path,
        target_language="ta",
    ):

        audio = self.audio.process(
            video_path
        )

        translated = self.translation.process(
            audio,
            target_language,
        )

        subtitle = self.subtitle.create(
            translated
        )

        dubbed = self.tts.generate(
            translated
        )

        final_video = self.video.merge(
            video_path,
            dubbed,
        )

        return {

            "video": final_video,

            "audio": dubbed,

            "subtitle": subtitle,

        }