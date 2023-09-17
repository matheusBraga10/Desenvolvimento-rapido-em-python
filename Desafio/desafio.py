''' Carregar o arquivo ".csv" de empresas disponibilizados pela plataforma de dados abertos do governo
federal (https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) em
uma tabela no sqlite através de um programa escrito em Python. Os comandos SQL devem ser escritos neste programa.

O arquivo a ser utilizado será o Empresas0:
'''


import pandas as pd

arquivo = '/home/matheus/Empresas0/K3241.K03200Y0.D30812.EMPRECSV'
df = pd.read_csv(arquivo, sep=';', encoding='ISO-8859-1')
# from pyspark.sql import SparkSession



# spark = SparkSession.builder.master('local[*]').appName("Iniciando com Spark").config('spark.ui.port', '4050').getOrCreate()

# empresas = spark.read.csv(arquivo, sep=';', inferSchema=True);
# empresas.printSchema()

# print(empresas.count())
