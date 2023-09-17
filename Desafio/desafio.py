''' Carregar o arquivo ".csv" de empresas disponibilizados pela plataforma de dados abertos do governo
federal (https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) em
uma tabela no sqlite através de um programa escrito em Python. Os comandos SQL devem ser escritos neste programa.

O arquivo a ser utilizado será o Empresas0:
'''


import pandas as pd

arquivo = '/home/matheus/Empresas0/empresas.csv'
df = pd.read_csv(arquivo, sep=';', encoding='ISO-8859-1')

print(df.count())
