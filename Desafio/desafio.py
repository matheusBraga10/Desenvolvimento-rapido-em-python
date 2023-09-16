''' Carregar o arquivo ".csv" de empresas disponibilizados pela plataforma de dados abertos do governo
federal (https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) em
uma tabela no sqlite através de um programa escrito em Python. Os comandos SQL devem ser escritos neste programa.

O arquivo a ser utilizado será o Empresas0:
'''

import sqlite3 as conector
import os
import pandas as pd


all_files = list(filter(lambda x:'.csv' in x, os.listdir('/home/matheus/Documentos/Empresas0/')))

arquivo = []
for 