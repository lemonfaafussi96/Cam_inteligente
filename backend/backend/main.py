from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai import sum as summarize, rap as text_to_rap, tts as tts_generate

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class TextInput(BaseModel):
    text: str
    matiere: str
    profil: dict

@app.post("/transform")
def transform_text(input: TextInput):
    summarized_text = summarize.summarize(input.text)
    rap_text = text_to_rap.text_to_rap(summarized_text, input.profil)
    audio_url = tts_generate.generate_audio(rap_text, input.profil, input.matiere)
    return {"rapText": rap_text, "audioUrl": audio_url}
