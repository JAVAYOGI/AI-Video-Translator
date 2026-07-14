"""
Audio Service
Handles all audio preprocessing.
"""

from core import (
    AudioExtractor,
    AudioEnhancer,
    NoiseReducer,
)


class AudioService:

    def __init__(self):

        self.extractor = AudioExtractor()
        self.enhancer = AudioEnhancer()
        self.reducer = NoiseReducer()

    def process(self, video_path):

        audio = self.extractor.extract(video_path)

        enhanced = self.enhancer.enhance(audio)

        denoised = self.reducer.reduce(enhanced)

        return denoised