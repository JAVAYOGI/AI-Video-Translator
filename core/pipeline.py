"""
Complete AI Video Translation Pipeline
"""

from core import (
    AudioExtractor,
    AudioEnhancer,
    NoiseReducer,
    Transcriber,
    Translator,
    SubtitleGenerator,
    TextToSpeech,
    VideoMerger,
)

from utils import get_logger

logger = get_logger()


class VideoTranslatorPipeline:

    def __init__(self):

        self.extractor = AudioExtractor()
        self.enhancer = AudioEnhancer()
        self.reducer = NoiseReducer()

        self.transcriber = Transcriber()

        self.translator = Translator(
            source="auto",
            target="ta"
        )

        self.subtitle = SubtitleGenerator()

        self.tts = TextToSpeech()

        self.merger = VideoMerger()

    def run(
        self,
        video_path,
        target_language="ta",
    ):

        logger.info("=" * 60)
        logger.info("AI VIDEO TRANSLATOR STARTED")
        logger.info("=" * 60)

        self.translator = Translator(
            source="auto",
            target=target_language
        )

        audio = self.extractor.extract(video_path)

        enhanced = self.enhancer.enhance(audio)

        denoised = self.reducer.reduce(enhanced)

        transcript = self.transcriber.transcribe(denoised)

        translated = self.translator.translate(transcript)

        subtitle = self.subtitle.create(
            translated,
            "translated.srt"
        )

        text = " ".join(
            item["translated"]
            for item in translated
        )

        dubbed_audio = self.tts.speak(
            text,
            "dubbed.mp3"
        )

        final_video = self.merger.merge(
            video_path,
            dubbed_audio
        )

        logger.info("=" * 60)
        logger.info("PIPELINE COMPLETED")
        logger.info("=" * 60)

        return {
            "video": final_video,
            "audio": dubbed_audio,
            "subtitle": subtitle,
            "language": target_language,
        }