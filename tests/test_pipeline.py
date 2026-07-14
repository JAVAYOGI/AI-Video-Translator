from core.pipeline import VideoTranslatorPipeline

pipeline = VideoTranslatorPipeline()

result = pipeline.run("sample.mp4")

print("\n")

print(result)