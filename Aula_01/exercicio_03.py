'''
 - Escreva um programa que leia um arquivo com um conjunto de nomes (1 por linha). O programa deve ordenar os nomes e gerar um novo arquivo com os nomes ordenados.

  Utilize a função sort:
  (https:/w3schools.com/python/ref_list_sort.asp)

'''
from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_03 = caminho_arquivo.parent / 'exercicio_03.txt'
exercicio_03.touch()


def cria_arquivo(arquivo):
  arquivo.writelines('''Ana\nMatheus\nSebastião\nJosé\nMaria\nJoão''')
  
    

arquivo_saida = open(exercicio_03,'w')
cria_arquivo(arquivo_saida)
arquivo_saida.close()

arquivo_entrada = open(exercicio_03,'r')
arquivo_entrada.sort()
print(arquivo_entrada.read())
arquivo_entrada.close()
