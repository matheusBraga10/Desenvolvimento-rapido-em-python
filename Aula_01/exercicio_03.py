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

# opcao = -1
# while opcao != 0:
#   opcao = int(input('Digite \n1 - Novo usuário\n2 - Imprime arquivo\n'))
#   if opcao == 1:
#     arquivo = open(exercicio_03, 'a')
#     nome = input('Digite seu nome: ')
#     arquivo.writelines(nome)
#   else:
#     arquivo = open(exercicio_03,'r')
#     print(arquivo.read())
#     break
# arquivo.close()
