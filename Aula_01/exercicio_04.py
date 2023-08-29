'''
  - Faça um programa que leia as linhas de 3 a 5 de um arquivo de texto (considere que tem mais do que 5 linhas)
    - Copie as linhas selecionadas em um novo arquivo
'''

from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_04 = caminho_arquivo.parent / 'exercicio_04.txt'
exercicio_04.touch()

def cria_lista(arquivo):
    arquivo.writelines('Ana, Matheus, Sebastião, Jośe, Maria, João')

arquivo_saida = open(exercicio_04,'w')
cria_lista(arquivo_saida)
arquivo_saida.close()

arquivo_entrada = open(exercicio_04,'r')
lista = []
for i in arquivo_entrada:
    linha = i.replace('\n','').split(', ')
    print(linha)
    lista = lista + linha
  
print(lista[3:5])