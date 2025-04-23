import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/helloworld")
async def read_root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcao_teste():
    return {"Verdadeiro": True, "numero_aleatório" : random.randint(0, 1000)}

@app.post("/estudante/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudante/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0