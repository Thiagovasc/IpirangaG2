from unidecode import unidecode
from datetime import date
from enum import Enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar
from faker import Faker
import json
import re

#T = TypeVar['T']

class Genero(str, Enum):
    Masculino = "Masculino"
    Feminino = "Feminino"


class NivelEscolaridade(str, Enum):
    superior_completo = "superior-completo"
    superior_incompleto = "superior-incompleto"
    ensino_medio_completo = "medio-completo"
    ensino_medio_incompleto = "medio-incompleto"
    fundamental_incompleto = "fundamental-completo"
    analfabeto = "analfabeto"


class SituacaoEmpregaticia(str, Enum):
    empregado = "Empregado"
    autonomo = "Autonomo"
    desempregado = "Desempregado"



class DiaDeAbastecimento(str, Enum):
    Domingo = "Domingo"
    Segunda = "Segunda"
    Terca = "Terca"
    Quarta = "Quarta"
    Quinta = "Quinta"
    Sexta = "Sexta"
    Sabado = "Sabado"
    Conforme_necessidade = "Conforme-necessidade"


class LocalDeAbastecimento(str, Enum):
    Proximo_de_casa = "proximo-de-casa"
    Proximo_ao_trabalho = "proximo-ao-trabalho"
    Mais_barato = "mais-barato"


class RespostaBooleana(str, Enum):
    sim = "sim"
    nao = "nao"


class UsuarioCadastrado(BaseModel):
    nome: str
    sobrenome: str
    genero: Genero
    idade: int
    estado: str
    escolaridade: NivelEscolaridade
    profissao: str
    situacao_trabalho: SituacaoEmpregaticia
    frequencia_abastecimento: int
    dia_abastecimento: DiaDeAbastecimento
    locais_abastecimento: LocalDeAbastecimento
    tipo_combustivel: str
    manutencao_preventiva: RespostaBooleana
    preocupacao_ambiental: RespostaBooleana
    valorizacao_economia_combustivel: RespostaBooleana
    preferencia_marca_combustivel: str
    pagamento_combustivel_qualidade: RespostaBooleana
    utilizacao_aplicativos: RespostaBooleana
    utilizacao_cartoes_fidelidade: RespostaBooleana
    interesse_tecnologias_propulsao: RespostaBooleana


fake = Faker("pt_BR")

usuarios = []
for _ in range(10):
    genero = fake.random_element(Genero)
    if genero == Genero.Masculino:
        nome = fake.first_name_male()
    else:
        nome = fake.first_name_female()

    sobrenome=fake.last_name(),
    estado=fake.state()
    profissao=fake.job()
    nome = unidecode(str(nome))
    sobrenome = unidecode(str(sobrenome)).replace("('", "").replace("',)", "")
    profissao = unidecode(str(profissao))
    estado = unidecode(str(estado))
    
    
    usuario = UsuarioCadastrado(
        nome=nome,
        sobrenome=sobrenome,
        genero=genero,  
        idade=fake.random_int(min=18, max=50),
        estado=estado,
        escolaridade=fake.random_element(NivelEscolaridade),
        profissao=profissao,
        situacao_trabalho=fake.random_element(SituacaoEmpregaticia),
        frequencia_abastecimento=fake.random_int(min=1, max=7),
        dia_abastecimento=fake.random_element(DiaDeAbastecimento),
        locais_abastecimento=fake.random_element(LocalDeAbastecimento),
        tipo_combustivel=fake.random_element(["Gasolina", "Etanol", "Diesel"]),
        manutencao_preventiva=fake.random_element(RespostaBooleana),
        preocupacao_ambiental=fake.random_element(RespostaBooleana),
        valorizacao_economia_combustivel=fake.random_element(RespostaBooleana),
        preferencia_marca_combustivel=fake.random_element(["Petrobras", "Shell", "Ipiranga"]),
        pagamento_combustivel_qualidade=fake.random_element(RespostaBooleana),
        utilizacao_aplicativos=fake.random_element(RespostaBooleana),
        utilizacao_cartoes_fidelidade=fake.random_element(RespostaBooleana),
        interesse_tecnologias_propulsao=fake.random_element(RespostaBooleana)
    )
    
    usuarios.append(usuario.__dict__)


# Salvar dados em arquivos JSON
for i, usuario in enumerate(usuarios):
    with open(f"usuario_{i+1}.json", "w") as file:
        json.dump(usuario, file, indent=4)

