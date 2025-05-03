from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes poner ["https://tu-usuario.github.io"] para más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PalabrasInput(BaseModel):
    palabras: list[str]

@app.post("/elegir")
def elegir_palabra(data: PalabrasInput):
    return {"palabra_elegida": random.choice(data.palabras)}
