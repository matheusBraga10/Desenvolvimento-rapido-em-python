''' Carregar o arquivo ".csv" de empresas disponibilizados pela plataforma de dados abertos do governo
federal (https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) em
uma tabela no sqlite através de um programa escrito em Python. Os comandos SQL devem ser escritos neste programa.

O arquivo a ser utilizado será o Empresas0:
'''

import openai
import os
import pandas as pd
import requests
import json

open.api_key = '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'

def generate_ai_ids(user):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", "content": "Você é um especialista em ciência de dados."
            },
            {
                "role": "user", "content": "mostre-me como acessar os dados em .csv o arquivo K3241.K03200Y0.D30812.EMPRECSV dentro de /home/matheus/Empresas0.zip"
            }

        ]
        )
    return completion.choices[0].massage.contenct.strip('\"')

# swd2023_api_url = 'https://sdw-2023-prd.up.app'
# df = pd.read_csv('K3241.K03200Y0.D30812.EMPRECSV')
# users_ids = df['UserID'].tolist()
# print(users_ids)
                                                              
# # def get_user(id):
# #     response = requests.get(f'{swd2023_api_url}/users/{id}')
# #     return response.json() if response.status_code == 200 else None

# users = [user for id in users_ids if (user :=get_user(id)) is not None]
# print((json.drums(users, indent=2)))

# for user in users:
#     metodo = generate_ai_ids(user)
#     print(metodo)