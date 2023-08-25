#lista_termos = variavel_string.split(separador)

frase = "uma frase de teste para vermos o método"
lista_frase = frase.split(' ')
print(lista_frase)
frase1 = "Eu amo comer café da manhã"
lista_termos1 = frase1.split() #usar sem argumentos ele quebra nos espaços em branco
print(lista_termos1)
frase2 = "Amora abacaxi abacate banana"
lista_termos2 = frase2.split() #usar sem argumentos ele quebra nos espaços em branco
print(lista_termos2)
frase3 = "Carro,moto,avião"
lista_termos3 = frase3.split(',')
print(lista_termos3)

frase = "Eu amo comer amoras no café da manhã"
#Resultado obtido utilizando o método countdiretamente
print("Contagem direta:", frase.count("amo"))
#Resultado obtido utilizando a quebra de frase em palavras
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == "amo":
        contador += 1
print("Contagem correta: ", contador)
frase = "Eu amo comer amoras no café da manhã."
lista_termos = frase.split()
contagem = lista_termos.count("amo")
print("Contagem = ", contagem)
