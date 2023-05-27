from fastapi import FastAPI, Query
from models import UsuarioCadastrado
from fastapi.middleware.cors import CORSMiddleware
from requests import Request
from gerando_cadastros import GerandoCadastro, AdicionarDados

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500/Frontend"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

cadastrados = []

@app.get("/")
def home():
    return cadastrados if len(cadastrados) != 0 else {"Lista vazia"}


@app.post("/novo")
def novo_cadastro(novo: UsuarioCadastrado):
    cadastrados.append(novo)

    return cadastrados


@app.post("/gerar-cadastros")
def gerar_cadastros(cadastros_request: int = Query(..., ge=1)):
    AdicionarDados(cadastros_request)
    return {"message": f"{cadastros_request} cadastros gerados com sucesso."}
