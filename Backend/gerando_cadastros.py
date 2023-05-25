from models import *
from faker import Faker
from unidecode import unidecode
import requests 
import json

fake = Faker("pt_BR")


def GerandoCadastro():

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


def AdicionarDados(n):
    if n <= 0:
        return

    usuario = GerandoCadastro()

    url = "http://localhost:8000/novo"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, json=usuario.dict())
        response.raise_for_status()
        response_data = response.json()

        AdicionarDados(n - 1)

    except requests.exceptions.RequestException as error:
        print("Request falhou:", error)
        print(usuario)

AdicionarDados(2)
