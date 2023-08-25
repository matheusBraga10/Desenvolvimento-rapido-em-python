arquivo = open("/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_03/texto.txt", "r")

for linha in arquivo:
    print(repr(linha)) 
arquivo.seek(0) #reinicia o cursor do arquivo para o inicio
for linha in arquivo:
    print(repr(linha.strip())) 


contador = 0
contador_2 = 0

for linha in arquivo:
    if linha:
        contador = contador +  1
    elif linha.strip(): #testa 'false' com string vazia
        contador_2 = contador_2 + 1

print("Total = ", contador)
print("Total real = ", contador_2)

arquivo.close()
