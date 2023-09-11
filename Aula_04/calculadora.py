class FormulaError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return self.value


expressao = "1 - 1 "

elementos= expressao.split()

if len(elementos) != 3:
  raise FormulaError("A expressão está com mais de 3 elementos")

try:
  valor1 = float(elementos[0])
  valor2 = float(elementos[2])

except ValueError as error:
  raise FormulaError("Não é possível converter os valores")

else:
  if(elementos[1] != "+" and elementos[1] != "-"):
    raise FormulaError("Operador informado está errado!")
  if(elementos[1] == "+"):
    print("Soma: ", valor1 + valor2)
  elif(elementos[1] == "-"):
    print("Subtração: ", valor1 - valor2)

print("Fim do programa!")