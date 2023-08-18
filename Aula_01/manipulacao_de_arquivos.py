'''
- Manipulação de Arquivos
  - Ações basicas de manipulação de arquivo
    - Abrir
    - Fechar
    - Ler
    - Escrever
  - Modo de acesso
    - r : Abrir
    - w : Escrever
    - x :  Escrita (falha caso a escrita já exista)
    - r+: Leitura + escrita
    - w+: Lê e escreve (write and read)
    - a : acrescenta no fim (append)
    '''
#--------------------------------------------------------------
def abrir():
  
# - Abrir

#arquivo1 = open(caminho) # Abre o conteúdo do documento carregado para a memória (abre o arquivo)
# open('arquivo.txt')
# open('C:\Downloads\arquivo.txt')

    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Frameworks/manipulacao_de_arquivos.txt', 'r')
#print(arquivo.readable())

# Lê arquivo inteiro
#print(arquivo.read())

# Lê linha a linha
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())

# Lê linha a linha em listas
    lista = arquivo.readlines()
    for linha in lista:
        print(linha)
    print(lista)

    arquivo.close()


def escrever():
      # - Escrever
    #arquivo2 = open(caminho, W) # Abre o arquivo em modo de escrita!

    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Frameworks/manipulacao_de_arquivos.txt','w+')

    #arquivo.write('Conteúdo da primeira linha')
    #arquivo.write('\nConteúdo da segunda linha')

    linha = ['Olá,\nMundo!','\n\nConteudo 1a linha','\nConteudo 2a linha']
    arquivo.writelines(linha)
    arquivo.close()
    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Frameworks/manipulacao_de_arquivos.txt','r')
    #print(arquivo.read())

    arquivo.close()
    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Frameworks/manipulacao_de_arquivos.txt','a')

    linha = ['\nConteudo 3a linha','\nConteudo 4a linha']
    arquivo.writelines(linha)
    arquivo.close()
    arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Frameworks/manipulacao_de_arquivos.txt','r')
    print(arquivo.read())

      # - Fechar
    arquivo.close()

      # - Lê
    #read(caminho) # Lê o arquivo inteiro e printa o arquivo inteiro
    #readline(caminho) # Lê linha por linha
    #readlines(caminho) # Lê o conteudo como uma lista (e não como uma string)

abrir()

escrever()