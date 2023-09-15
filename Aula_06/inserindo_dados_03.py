import sqlite3 as conector

class Marca:
  def __init__(self, Nome_marca, sigla):
    self.id = None
    self.Nome_marca = Nome_marca
    self.sigla = sigla

class Veiculo:
  def __init__(self, CPF, placa, ano, cor, proprietario, marca):
    self.placa = placa
    self.ano = ano
    self.cor = cor
    self.proprietario = proprietario
    self.marca = marca
    self.CPF = CPF

try:
  # abertura da conexão
  conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_05/teste.db')

#funçao PRAGMA
  conexao.execute('PRAGMA foreign_keys=on')

# aquisição de um cursor
  cursor = conexao.cursor()

  Marca = Marca('Fiat', 'FCA')
  Veiculo = Veiculo( 12345678911, 'abc-1234', 1998, 'Azul', 'José', 1)

  comando_01 = '''
  INSERT or IGNORE INTO Marca VALUES(:id, :Nome_marca, :sigla);
  '''
  comando_02 = '''
  INSERT or IGNORE INTO Veiculo VALUES(:CPF, :id, :placa, :ano, :cor, :proprietario, :marca);
  '''
  # execução do comando: SELECT, INSERT, CREATE...
  cursor.execute(comando_01, vars(Marca))
  cursor.execute(comando_02, vars(Veiculo))

# Efetivação do comando
  conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()