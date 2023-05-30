from models import *
from faker import Faker
from unidecode import unidecode
import requests
from typing import List

fake = Faker("pt_BR")


def gerar_cadastros_randomicos():

    genero = fake.random_element(Genero)
    if genero == Genero.MASCULINO:
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
        faixa_salarial=fake.random_element(FaixaSalarial),
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
        
    return usuario


def adiciona_cadastros(n):
    cadastros_gerados: List[UsuarioCadastrado] = []
    code: int = 0
    reason: str = ''

    for _ in range(n):
        usuario = gerar_cadastros_randomicos()
        cadastros_gerados.append(usuario)

        url = "http://localhost:8000/novo"
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url, headers=headers, json=usuario.dict())
            code = response.status_code
            reason = response.reason


        except requests.exceptions.RequestException as error:
            return Response(
                status = reason,
                code = code,
                mensagem = f"Erro: {error}"
            )

    return Response(
        status = reason,
        code = code,
        mensagem = f"{n} Cadastros gerados com sucesso",
        result = cadastros_gerados
    )
