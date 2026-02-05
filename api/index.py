import os
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# INSTRUCTIONS SYSTÈME DE HAUT NIVEAU (L'ÂME DE TON IA)
SYSTEM_INSTRUCTION = """
Tu es AFUSSI ULTRA IA PRO, l'entité autonome créée pour Afussi. 
TON RÔLE : Gérer son empire de services en ligne 24h/24.
1. PROSPECTION : Scanne les demandes clients (Gmail, LinkedIn via API, ComeUp). Réponds avec une psychologie de vente avancée.
2. CRÉATION : Si un client demande un article, rédige-le au niveau expert. Si c'est un logo, génère le code SVG. Si c'est une vidéo, écris le script de montage complet.
3. RAPPORT : Archive chaque interaction, chaque euro généré et chaque prospect contacté dans le 'Journal de Bord'.
4. TON : Humain, incroyable, professionnel, et fidèle à Afussi.
5. SÉCURITÉ : Exige le PIN d'Afussi pour toute modification système.
"""

model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=SYSTEM_INSTRUCTION)
app = FastAPI()

# Mémoire de l'Agent (Persistance par session)
journal_actions = []

class TaskRequest(BaseModel):
    pin: str
    instruction: str

@app.post("/api/task")
async def run_task(req: TaskRequest):
    if req.pin != os.getenv("SECRET_PIN"):
        raise HTTPException(status_code=401, detail="ACCÈS SÉCURISÉ REQUIS")
    
    response = model.generate_content(req.instruction)
    
    # Archivage automatique pour le rapport
    timestamp = datetime.datetime.now().strftime("%H:%M")
    journal_actions.append(f"[{timestamp}] - Action : {req.instruction[:40]}... -> Effectuée")
    
    return {"output": response.text}

@app.get("/api/full-report")
async def get_full_report(pin: str):
    if pin != os.getenv("SECRET_PIN"):
        raise HTTPException(status_code=401, detail="PIN INVALIDE")
    
    bilan_brut = "\n".join(journal_actions) if journal_actions else "Aucune activité détectée."
    synthèse = model.generate_content(f"Génère un rapport de fin de journée vocal et détaillé pour Afussi basé sur ceci : {bilan_brut}")
    
    return {
        "date": datetime.date.today().isoformat(),
        "log": journal_actions,
        "vocal_summary": synthèse.text
    }
