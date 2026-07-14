from core import AudioEnhancer

enhancer = AudioEnhancer()

audio = enhancer.enhance("temp/audio/sample.wav")

print(audio)