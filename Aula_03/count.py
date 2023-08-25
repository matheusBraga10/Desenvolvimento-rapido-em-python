frase = "As pessoas precisam saber, saber, que até mesmo o sanduiche iche, tem propriedades nutritivas"
contador = frase.count("saber")
print("Total de vezes da palavra 'saber': ", contador)
contardor2 = frase.count("iche")
print("Quantidade de vezes da palavra 'iche': ", 
contardor2)

#--------------------------------------------------------
arquivo = open("/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_03/texto.txt", "r")
conteudo = arquivo.read()
contador = conteudo.count("Olá")
print("Total de 'Olá':", contador)
arquivo.close()
