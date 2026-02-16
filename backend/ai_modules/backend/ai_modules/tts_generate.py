from gtts import gTTS
import os

def generate_audio(text, profil, matiere):
    # Crée un nom unique pour chaque élève et matière
    filename = f"audio_pre_generated/{matiere.lower()}/rap_{profil['name']}.mp3"
    tts = gTTS(text=text, lang='fr')
    tts.save(filename)
    return filename
