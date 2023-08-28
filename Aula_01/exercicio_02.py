
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

    arquivo.writelines(identidade + ' ' + nome + '\n')


def le_arquivo_dicionario():
    dicionario = {}
    for linha in arquivo_entrada:
        string = linha.replace('\n','').split(' ')
        dicionario[string[0]] = string[1]
    return dicionario

arquivo_saida = open(exercicio_02, 'w')
opcao = 1
while opcao == 1:
    opcao = int(input('Digite \n"1" para criar o dicionario\n"2 para ler e imprimir o dicionario\n'))
    if opcao == 1:
        cria_arquivo_dicionario(arquivo_saida)
arquivo_saida.close()
arquivo_entrada = open(exercicio_02 ,'r')
dicionario_final = le_arquivo_dicionario()
    
print(dicionario_final)

