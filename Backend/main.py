from fastapi import FastAPI
from models import UsuarioCadastrado
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

cadastrados = []

@app.get("/")
def home():
    return cadastrados if len(cadastrados) != 0 else {"hello world"}


@app.post("/novo")
def novo_cadastro(novo: UsuarioCadastrado):
    cadastrados.append(novo)

    return cadastrados
