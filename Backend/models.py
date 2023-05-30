from enum import Enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Genero(str, Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"


class NivelEscolaridade(str, Enum):
    SUPERIOR_COMPLETO = "superior-completo"
    SUPERIOR_INCOMPLETO = "superior-incompleto"
    ENSINO_MEDIO_COMPLETO = "medio-completo"
    ENSINO_MEDIO_INCOMPLETO = "medio-incompleto"
    FUNDAMENTAL_COMPLETO = "fundamental-completo"
    FUNDAMENTAL_INCOMPLETO = "fundamental-incompleto"
    ANALFABETO = "analfabeto"




class SituacaoEmpregaticia(str, Enum):
    EMPREGADO = "Empregado"
    DESEMPREGADO = "Desempregado"
    AUTONOMO = "Autonomo"



class DiaDeAbastecimento(str, Enum):
    DOMINGO = "Domingo"
    SEGUNDA = "Segunda"
    TERCA = "Terca"
    QUARTA = "Quarta"
    QUINTA = "Quinta"
    SEXTA = "Sexta"
    SABADO = "Sabado"
    CONFORME_NECESSIDADE = "Conforme-necessidade"




class LocalDeAbastecimento(str, Enum):
    PROXIMO_DE_CASA = "proximo-de-casa"
    PROXIMO_AO_TRABALHO = "proximo-ao-trabalho"
    MAIS_BARATO = "mais-barato"



class RespostaBooleana(str, Enum):
    SIM = "sim"
    NAO = "nao"


class FaixaSalarial(str, Enum):
    ATE_1_SALARIO = "ate-1-salario"
    ENTRE_1_E_2_SALARIOS = "entre-1-e-2"
    ENTRE_2_E_3_SALARIOS = "entre-2-e-3"
    ENTRE_3_E_4_SALARIOS = "entre-3-e-4"
    ACIMA_DE_4_SALARIOS = "acima-de-4"



class UsuarioCadastrado(BaseModel):
    nome: str
    sobrenome: str
    genero: Genero
    idade: int
    estado: str
    faixa_salarial: FaixaSalarial
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


class Response(GenericModel, Generic[T]):
    status: str
    code: int
    mensagem: Optional[T]
    result: Optional[T]  