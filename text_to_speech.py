import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text):

    if os.path.exists("output.mp3"):
        os.remove("output.mp3")

    tts = gTTS(text=text, lang="ar")
    tts.save("output.mp3")

    print("🔊 Playing response...")
    playsound("output.mp3")