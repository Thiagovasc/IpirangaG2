from datetime import date
from enum import Enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar


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
    idade: date
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


"""class Response(GenericModel, Generic[T]):
    status: str
    code: str
    message: Optional[T]
    result: Optional[T]"""