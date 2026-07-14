from core import NoiseReducer

reducer = NoiseReducer()

audio = reducer.reduce("temp/enhanced/sample_enhanced.wav")

print(audio)