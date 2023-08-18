'''
 - Faça um programa que escreve uma frase digitada pelo usuario em um arquivo. 
Em seguida o programa de ler e imprimir o conteúdo desse arquivo
'''

print('Escreva uma frase: ')
frase = input()

arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_01/exercicio_01.txt','r+')

arquivo.writelines(frase)
arquivo.close()

arquivo = open('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_01/exercicio_01.txt','r+')
print()
print('=--= LENDO ARQUIVO =--=')
print(arquivo.read())
arquivo.close()