"""
Video Service
"""

from core import VideoMerger


class VideoService:

    def __init__(self):

        self.merger = VideoMerger()

    def merge(
        self,
        video_path,
        audio_path,
    ):

        return self.merger.merge(
            video_path,
            audio_path,
        )