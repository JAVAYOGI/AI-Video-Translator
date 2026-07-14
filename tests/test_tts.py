from core import TextToSpeech

tts = TextToSpeech()

audio = tts.speak(

    "வணக்கம். இது AI வீடியோ மொழிபெயர்ப்பாளர்.",

    "dubbed.mp3"

)

print(audio)