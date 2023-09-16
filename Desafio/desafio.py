''' Carregar o arquivo ".csv" de empresas disponibilizados pela plataforma de dados abertos do governo
federal (https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) em
uma tabela no sqlite através de um programa escrito em Python. Os comandos SQL devem ser escritos neste programa.

O arquivo a ser utilizado será o Empresas0:
'''

import pandas as pd
import requests 
import json
import os

ENDERECO = '/home/matheus/Documentos/Empresas0/K3241.K03200Y0.D30812.EMPRECSV'
RETORNO = 'https://sdw-2023-prd.up.railway.app/'

df = pd.read_csv(ENDERECO)

user_ids = df['id'].tolist()
print(user_ids)

def get_user(id):

    response = requests.get(ENDERECO)
    return response.json() if response.status_code == 200 else None

user = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(user, ident=2))


