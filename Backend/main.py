from fastapi import FastAPI, Query
from models import UsuarioCadastrado, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from gerando_cadastros import adiciona_cadastros

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500/Frontend"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

cadastrados: List[UsuarioCadastrado] = []

@app.get("/")
def home():
    return cadastrados if len(cadastrados) != 0 else {"status" : "Lista vazia"}


@app.post("/novo")
def novo_cadastro(novo: UsuarioCadastrado):
    cadastrados.append(novo)

    return Response(
        status = "OK",
        code = 200,
        mensagem = "Cadastro adicionado com sucesso",
        result = novo
    )


@app.post("/gerar-cadastros")
def gerar_cadastros(cadastros_request: int = Query(..., ge=1)):
    return adiciona_cadastros(cadastros_request)


