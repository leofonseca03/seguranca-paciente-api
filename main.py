from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

from fastapi.middleware.cors import CORSMiddleware

class Evento(BaseModel):
    descricao: str

app = FastAPI(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)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/classificar")
async def classificar_evento(evento: Evento):
    prompt = f"""
    Aja como um especialista em segurança do paciente. Leia a descrição abaixo e classifique o evento de acordo com as diretrizes da ANVISA e da OMS.

    Descrição: "{evento.descricao}"

    Responda com:
    - Tipo de incidente
    - Local do incidente
    - Consequências
    - Classificação (ex: incidente sem dano, evento adverso grave, etc)
    - Perguntas adicionais se necessário
    - Definições dos termos usados
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em segurança do paciente."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return {"resposta": resposta.choices[0].message["content"]}
