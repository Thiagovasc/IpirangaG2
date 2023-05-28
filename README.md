# Grupo 2 - Data Storm

## Projeto Inclusão Tech Ipiranga

- [Descrição](#descrição)
- [Instalação](#instalação)
- [API](#api)
- [Endpoints](#endpoints)
- [Configuração](#configuração)
- [Modelo Usuario]()

## Descrição

Projeto desenvolvido no curso de Inclusão Tech Ipiranga para a captação de dados via formulário e fornecer os mesmo para um dashboard Power BI

## Instalação

Clone o repositório ou faça o download dos arquivos.
Certifique-se de ter o Python instalado em sua máquina.

Instale as dependências necessárias executando:

    pip install -r requirements.txt.

## API

Apos a instalação das bibliotecas necessárias
Inicie a API FastAPI executando o comando:
    uvicorn main:app --reload.


## Endpoints

Schema:


    {
        "nome": "string",
        "sobrenome": "string",
        "genero": "Masculino",
        "idade": 0,
        "estado": "string",
        "faixa_salarial": "ate-1-salario",
        "escolaridade": "superior-completo",
        "profissao": "string",
        "situacao_trabalho": "Empregado",
        "frequencia_abastecimento": 0,
        "dia_abastecimento": "Domingo",
        "locais_abastecimento": "proximo-de-casa",
        "tipo_combustivel": "string",
        "manutencao_preventiva": "sim",
        "preocupacao_ambiental": "sim",
        "valorizacao_economia_combustivel": "sim",
        "preferencia_marca_combustivel": "string",
        "pagamento_combustivel_qualidade": "sim",
        "utilizacao_aplicativos": "sim",
        "utilizacao_cartoes_fidelidade": "sim",
        "interesse_tecnologias_propulsao": "sim"
    }


| Command | End Point               | Description                |
|---------|-------------------------|----------------------------|
| GET     | /                       | Retorna a lista de usuários cadastrados. Caso não haja cadastros, retorna um objeto indicando que a lista está vazia.              |
| POST     | /novo                  |  Adiciona um novo cadastro de usuário.        |
| Delete  | /gerar-cadastros        | Gera uma quantidade específica de cadastros de usuários. O número de cadastros desejado deve ser fornecido como um parâmetro de consulta chamado cadastros_request.               |


## Configuração

Verifique o arquivo config.py para configurar as opções da API, como URL de destino e parâmetros de autenticação, se aplicável.
Certifique-se de que a API esteja em execução e acessível.


## Modelo Usuario Cadastrado

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