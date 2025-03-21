from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/teste3")
def funcao_teste():
    return {"Hello": "Terra"}