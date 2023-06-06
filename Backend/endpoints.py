from fastapi import APIRouter, Query
from gerando_csv import gerando_csv
from main import cadastrados
from models import Response, UsuarioCadastrado
from gerando_cadastros import adiciona_cadastros

router = APIRouter()

@router.get("/")
def home():
    return cadastrados if len(cadastrados) != 0 else {"status" : "Lista vazia"}

@router.post("/novo")
def novo_cadastro(novo: UsuarioCadastrado):
    cadastrados.append(novo)
    gerando_csv(novo)

    return Response(
        status = "OK",
        code = 200,
        mensagem = "Cadastro adicionado com sucesso",
        result = novo
    )

@router.post("/gerar-cadastros")
def gerar_cadastros(cadastros_request: int = Query(..., ge=1)):
    return adiciona_cadastros(cadastros_request)
