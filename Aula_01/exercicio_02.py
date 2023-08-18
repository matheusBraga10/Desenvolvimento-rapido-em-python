
'''  - Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte fortmato:
    - 5384423 Manoel
    - 4345566 Albrto
    - 3235574 Mariana
    ...
  O programa deve gerar um dicionario onde as chaves sao as identidades e os valores os nomes. Ao final o programadeve exibir o dicionario.

  Utilize a estrutura dict:
  (https://w3schools.com/python/python_dictionaries.asp)
'''
def cria_arquivo_dicionario():
    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_01/exercicio_02.txt', 'a')
    print('Entre com seu numero de identidade')
    identidade = input()
    print()
    print('Entre com seu nome')
    nome = input()

    dicionario = {'identidade' : '', 'nome' : ''}
    (dicionario['identidade']) = identidade
    (dicionario['nome']) = nome

    dicionario.update({'identidade': identidade , 'nome' : nome})
    arquivo.writelines(dicionario)
    arquivo.close()


def le_arquivo_dicionario():
    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_01/exercicio_02.txt','r')
    print(arquivo.read())
    arquivo.close()


opcao = -1
while opcao != 0:
    opcao = int(input('Digite \n"1" para criar mais dicionarios\n"2 para ler e imprimir o dicionario\n'))
    if opcao == 1:
        print('--- Adicionando dados ao dicionário ---')
        cria_arquivo_dicionario()
    else:
        print('--- Lendo e imprimindo dicionario ---')
        print()
        le_arquivo_dicionario()
        break