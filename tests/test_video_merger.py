from pathlib import Path

from core import VideoMerger

video_file = Path("sample.mp4")
audio_file = Path("outputs/audio/dubbed.mp3")

print("Video Exists :", video_file.exists())
print("Audio Exists :", audio_file.exists())

merger = VideoMerger()

output = merger.merge(
    video_file,
    audio_file,
    "translated_video.mp4"
)

print("\nOutput Video:")
print(output)