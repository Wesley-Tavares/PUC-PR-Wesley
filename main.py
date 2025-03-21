from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste1")
def funcao_teste():
    return {"Verdadeiro": True, "numero_aleatório" : random.randint(0, 1000)}