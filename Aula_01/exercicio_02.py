
'''  - Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte fortmato:
    - 5384423 Manoel
    - 4345566 Albrto
    - 3235574 Mariana
    ...
  O programa deve gerar um dicionario onde as chaves sao as identidades e os valores os nomes. Ao final o programadeve exibir o dicionario.

  Utilize a estrutura dict:
  (https://w3schools.com/python/python_dictionaries.asp)
'''


from pathlib import Path

caminho_projeto = Path()
caminho_arquivo = Path(__file__)
exercicio_02 = caminho_arquivo.parent / 'exercicio_02.txt'
exercicio_02.touch()

def cria_arquivo_dicionario(arquivo):
    print('Entre com seu numero de identidade')
    identidade = input()
    print()
    print('Entre com seu nome')
    nome = input() 

    arquivo.writelines(identidade + ' ' + nome)


def le_arquivo_dicionario():
    for linha in arquivo:
        linha = 
        print(linha)
    

    print()
arquivo_saida = open(exercicio_02, 'w')
opcao = -1
while opcao != 0:
    opcao = int(input('Digite \n"1" para criar o dicionario\n"2 para ler e imprimir o dicionario\n'))
    if opcao == 1:
        cria_arquivo_dicionario(arquivo_saida)
arquivo_saida.close()
else:
    print()


opcao = -1
while opcao != 0:
    opcao = int(input('Digite \n"1" para criar mais dicionarios\n"2 para ler e imprimir o dicionario\n'))
    if opcao == 1:
        arquivo_saida = open(exercicio_02, 'a')
        print('--- Adicionando dados ao dicionário ---')
        print()
        cria_arquivo_dicionario()
    else:
        arquivo_entrada = open(exercicio_02, 'r')
        print('--- Lendo e imprimindo dicionario ---')
        print()
        le_arquivo_dicionario()
        break

arquivo.close()

