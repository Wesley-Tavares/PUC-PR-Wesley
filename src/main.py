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

@app.get("/reservista/idade/{idade}")
async def validacao_idade_reservista(idade: int):
    if idade >= 18:
        return {"mensagem" : "Aprovado"}
    else:
        return {"mensagem" : "Reprovado"}

@app.get("/reservista/condicionamento")
async def validacao_reservista():
    return {"mensagem" : "Aprovado"}


@app.get("/validacao/{peso}")
async def validacao_peso(peso : int):
    return {"mensagem" : "Avaliação necessária"} if peso > 130 else {"mensagem" : "Peso dentro do limite"}

@app.get("/idade/impar/{numero}")
async def impar(numero : int):
    return {"mensagem" : "impar"} if numero % 2 != 0 else {"mensagem" : "par"}

@app.get ("/prova/nota/{nota}")
async def avaliacao(nota : int):
    return {"mensagem" : "aprovado"} if nota >= 7 else {"mensagem" : "reprovado"}





