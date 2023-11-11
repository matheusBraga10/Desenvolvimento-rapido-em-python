nome = "Fulano"
teste_string = "Olá " + nome + "."
teste_fstring1 = f"Olá {nome}."
teste_fstring2 = f"Olá {nome.upper()}."
teste_fstring3 = f"Quantos anos você tem? {pow(2,6)}."
teste_fstring4 = f"O número 2 é maior que 1? {2>1}"
teste_fstring5 = f"O número 5 está na lista [1, 2, 3, 4]? {5 in [1, 2, 3, 4]}"

print(teste_string)
print(teste_fstring1)
print(teste_fstring2)
print(teste_fstring3)
print(teste_fstring4)
print(teste_fstring5)

#-------------------------------------------------------------------
from cmath import pi
from datetime import datetime

frutas = ["Pera", "Uva", "Maçã", "Salada Mista"]

for fruta in frutas:
    fruta_string = f"Nome: {fruta:15} - Número de letras: {len(fruta): 3}"
    print(fruta_string)

print() # apenas para dar uma quebra de linha

pi_string = f"O número pi é: {pi:.1f}"
pi_string2 = f"O número pi deslocado é: {pi:6.1f}"
pi_string3 = f"O número pi com 4 casas decimais: {pi:.4f}"

print(pi_string)
print(pi_string2)
print(pi_string3)

print() # apenas para dar uma quebra de linha

data = datetime.now()
data_string = f"A data de hoje é {data}"
data_string2 = f"A data de hoje formatada: {data: %d/%m/%y}"

print(data_string)
print(data_string2)
