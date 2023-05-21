import pandas as pd
import numpy as np

# Definindo as opções de resposta para cada pergunta
idades = np.random.randint(18, 65, size=200)  # Idades entre 18 e 64 anos
generos = np.random.choice(['Masculino', 'Feminino'], size=200)
regioes = np.random.choice(['Centro', 'Zona Sul', 'Zona Norte', 'Zona Oeste'], size=200)
escolaridade = np.random.choice(['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior'], size=200)
faixas_salariais = np.random.choice(['Até R$ 2.000', 'R$ 2.000 - R$ 5.000', 'Acima de R$ 5.000'], size=200)
profissoes = np.random.choice(['Administrador', 'Professor', 'Engenheiro', 'Médico', 'Advogado','Entregador','MotoristaDeApp', 'DonaDeCasa', 'Vendedor', 'Enfermeiro', 'Tecnicos'], size=200)
situacoes_trabalho = np.random.choice(['Empregado', 'Desempregado', 'Autônomo'], size=200)
qtd_abastecimentos = np.random.randint(0, 8, size=200)  # Quantidade de 0 a 7
dias_abastecimento = np.random.choice(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta','Sábado','Domingo'], size=200)

# Criando o dataframe
data = {
    'Idade': idades,
    'Gênero': generos,
    'Região': regioes,
    'Nível de Escolaridade': escolaridade,
    'Faixa Salarial': faixas_salariais,
    'Profissão': profissoes,
    'Situação do Trabalho': situacoes_trabalho,
    'Qtd. Abastecimentos Semanais': qtd_abastecimentos,
    'Dia de Abastecimento': dias_abastecimento
}

df = pd.DataFrame(data)
df.to_csv('dados_ficticios.csv', index=False)
# Exibindo o dataframe
display(df)
