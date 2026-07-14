from core import (
    Transcriber,
    Translator,
    SubtitleGenerator
)

transcriber = Transcriber()

result = transcriber.transcribe(
    "temp/denoised/sample_enhanced_denoised.wav"
)

translator = Translator(
    target="ta"
)

translated = translator.translate(result)

subtitle = SubtitleGenerator()

path = subtitle.create(
    translated
)

print(path)