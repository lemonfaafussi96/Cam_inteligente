from gtts import gTTS
import os

def generate_audio(text, profil, matiere):
    folder = f"audio/{matiere.lower()}/"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}rap_{profil['name']}.mp3"
    tts = gTTS(text=text, lang='fr')
    tts.save(filename)
    return filename
