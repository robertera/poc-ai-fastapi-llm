# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import openai
import os

from app.utils import find_context

app = FastAPI()

from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
use_fake_llm = os.getenv("USE_FAKE_LLM", "false").lower() == "true"

FAQS_PATH = os.path.join(os.path.dirname(__file__), 'data', 'faqs.csv')
df = pd.read_csv(FAQS_PATH)

class Question(BaseModel):
    question: str

def fake_llm_response(prompt: str) -> str:
    return f"(FAKE LLM) Resposta simulada para o prompt: {prompt[:60]}..."

@app.post("/ask")
def ask(question_data: Question):
    question = question_data.question
    context_row = find_context(df, question)
    contexto = context_row['texto']
    prompt = f"Contexto: {contexto}\nPergunta: {question}\nResponda de forma clara e objetiva."

    if use_fake_llm:
        answer = fake_llm_response(prompt)
    else:
        try:
            client = openai.OpenAI(api_key=openai_api_key)
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente especializado."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = chat_completion.choices[0].message.content.strip()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"answer": answer, "context": contexto}