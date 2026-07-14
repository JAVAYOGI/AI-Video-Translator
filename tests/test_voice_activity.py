from core import VoiceActivityDetector

vad = VoiceActivityDetector()

chunks = vad.split(
    "temp/denoised/sample_enhanced_denoised.wav"
)

print()

print("Speech Chunks")

for chunk in chunks:
    print(chunk)