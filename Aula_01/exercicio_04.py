'''
  - Faça um programa que leia as linhas de 3 a 5 de um arquivo de texto (considere que tem mais do que 5 linhas)
    - Copie as linhas selecionadas em um novo arquivo
'''

from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_02 = caminho_arquivo.parent / 'exercicio_02.txt'
exercicio_02.touch()