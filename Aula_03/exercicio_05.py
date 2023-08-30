'''Abra um arquivo texto, calcule e escreva o numero de
caracteres, o número de linhas e o número de palavras neste
arquivo. Escreva também quantas vezes cada letra ocorre no
arquivo (ignorando letras com acento). Obs.: palavras são
separadas por um ou mais caracteres, espaço, tabulação ou
nova linha.'''

from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_05 = caminho_arquivo.parent / 'exercicio_05_aula_02.txt'
exercicio_05.touch()

arquivo_saida = open(exercicio_05,'w')
arquivo_saida.writelines('As pessoas me perguntam porque eu não tenho nenhuma tatuagem. Eu sempre respondo: Você colocaria um adesivo em uma Ferrari?')
arquivo_saida.close()

arquivo_entrada = open(exercicio_05,'r')
print('Total de letras')
print(len(arquivo_entrada.read()))
arquivo_entrada.close()
print()

arquivo_entrada = open(exercicio_05,'r')
numero_linhas = []
for i in arquivo_entrada:
    linha  = i.replace('\n','').split(', ')
    numero_linhas = numero_linhas + linha
print('Total de linhas')
print(len(numero_linhas))
arquivo_entrada.close()
print()

arquivo_entrada = open(exercicio_05,'r')
numero_palavras = []
for i in arquivo_entrada:
    palavra = i.replace('\n','').split(' ')
    numero_palavras = numero_palavras + palavra
print('Total de palavras')
print(len(numero_palavras))
print()

arquivo_entrada = open(exercicio_05,'r')
numero_caracter = arquivo_entrada.read()
print('Total de letras "a"')
print(numero_caracter.count('a'))