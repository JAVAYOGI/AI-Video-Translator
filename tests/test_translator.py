from core import (
    Transcriber,
    Translator
)

transcriber = Transcriber()

result = transcriber.transcribe(
    "temp/denoised/sample_enhanced_denoised.wav"
)

translator = Translator(
    target="ta"
)

translated = translator.translate(result)

for item in translated[:5]:

    print(item)