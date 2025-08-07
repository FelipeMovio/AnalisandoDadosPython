# Passo 1 : Importar a base de dados
# Passo 2 : Visualizar e tratar a base de dados
# Passo 3 : Dar uma olhada na sua base de dados
# Passo 4 : Construir uma analise para identificar o motivo de cancelamento
# - Identificar qual o motivo ou os principáis motivos de cancelamento

import pandas as pd

tabela = pd.read_csv('C:\\Users\\felip\\Desktop\\repositorio\\AnalisandoDadosPython\\Dados\\ClientesBanco.csv', encoding='latin1')
tabela = tabela.drop('CLIENTNUM', axis=1)
print(tabela)

