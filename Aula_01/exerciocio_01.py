'''
 - Faça um programa que escreve uma frase digitada pelo usuario em um arquivo. 
Em seguida o programa de ler e imprimir o conteúdo desse arquivo
'''

from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_01 = caminho_arquivo.parent / 'exercicio_01.txt'
exercicio_01.touch()

print('Escreva uma frase: ')
frase = input()

arquivo = open(exercicio_01,'r+')

arquivo.writelines(frase)
arquivo.close()

arquivo = open(exercicio_01,'r+')
print()
print('=--= LENDO ARQUIVO =--=')
print(arquivo.read())
arquivo.close()