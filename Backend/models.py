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
    Sim = "sim"
    Nao = "nao"


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
