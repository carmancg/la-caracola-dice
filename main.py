from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PalabrasInput(BaseModel):
    palabras: list[str]

@app.post("/elegir")
def elegir_palabra(data: PalabrasInput):
    return {"palabra_elegida": random.choice(data.palabras)}
