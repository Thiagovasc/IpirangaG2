from enum import Enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Genero(str, Enum):
    MASCULINO = "MASCULINO"
    FEMININO = "FEMININO"



class NivelEscolaridade(str, Enum):
    SUPERIOR_COMPLETO = "SUPERIOR_COMPLETO"
    SUPERIOR_INCOMPLETO = "SUPERIOR_INCOMPLETO"
    ENSINO_MEDIO_COMPLETO = "ENSINO_MEDIO_COMPLETO"
    ENSINO_MEDIO_INCOMPLETO = "ENSINO_MÉDIO_INCOMPLETO"
    FUNDAMENTAL_COMPLETO = "FUNDAMENTAL_COMPLETO"
    FUNDAMENTAL_INCOMPLETO = "FUNDAMENTAL_INCOMPLETO"
    ANALFABETO = "ANALFABETO"



class LocalizacaoRegional(str, Enum):
    ACRE = 'AC'
    ALAGOAS = 'AL'
    AMAPA = 'AP'
    AMAZONAS = 'AM'
    BAHIA = 'BA'
    CEARA = 'CA'
    DISTRITO_FEDERAL = 'DF'
    ESPIRITO_SANTO = 'ES'
    GOIAS = 'GO'
    MARANHAO = 'MA'
    MATO_GROSSO = 'MT'
    MATO_GROSSO_DO_SUL = 'MS'
    MINAS_GERAIS = 'MG'
    PARA = 'PA'
    PARAIBA = 'PB'
    PARANA = 'PR'
    PERNAMBUCO = 'PE'
    PIAUI = 'PI'
    RIO_DE_JANEIRO = 'RJ'
    RIO_GRANDE_DO_NORTE = 'RN'
    RIO_GRANDE_DO_SUL = 'RS'
    RONDONIA = 'RO'
    RORAIMA = 'RR'
    SANTA_CATARINA = 'SC'
    SAO_PAULO = 'SP'
    SERGIPE = 'SE'
    TOCANTINS = 'TO'



class SituacaoEmpregaticia(str, Enum):
    EMPREGADO = "EMPREGADO"
    DESEMPREGADO = "DESEMPREGADO"
    AUTONOMO = "AUTÔNOMO"



class DiaDeAbastecimento(str, Enum):
    DOMINGO = "DOMINGO"
    SEGUNDA = "SEGUNDA"
    TERCA = "TERCA"
    QUARTA = "QUARTA"
    QUINTA = "QUINTA"
    SEXTA = "SEXTA"
    SABADO = "SABADO"
    CONFORME_NECESSIDADE = "CONFORME_NECESSIDADE"




class LocalDeAbastecimento(str, Enum):
    PROXIMO_DE_CASA = "PROXIMO_DE_CASA"
    PROXIMO_AO_TRABALHO = "PROXIMO_AO_TRABALHO"
    LOCAL_MAIS_BARATO = "LOCAL_MAIS_BARATO"



class RespostaBooleana(str, Enum):
    SIM = "SIM"
    NAO = "NÃO"


class FaixaSalarial(str, Enum):
    ATE_1_SALARIO = "ATE_1_SALARIO"
    ENTRE_1_E_2_SALARIOS = "ENTRE_1_E_2_SALARIOS"
    ENTRE_2_E_3_SALARIOS = "ENTRE_2_E_3_SALARIOS"
    ENTRE_3_E_4_SALARIOS = "ENTRE_3_E_4_SALARIOS"
    ACIMA_DE_4_SALARIOS = "ACIMA_DE_4_SALARIOS"



class UsuarioCadastrado(BaseModel):
    nome: str
    sobrenome: str
    genero: Genero
    idade: int
    estado: LocalizacaoRegional
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