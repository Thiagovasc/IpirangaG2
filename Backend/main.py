from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import UsuarioCadastrado

app = FastAPI()

cadastrados: List[UsuarioCadastrado] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

from endpoints import router

app.include_router(router)
