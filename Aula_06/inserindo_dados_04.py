import sqlite3 as conector

class Pessoa:
  def __init__(self, id, Nome, Data_nascimento, Usa_oculos):
    self.id = id
    self.Nome = Nome
    self.Data_nascimento = Data_nascimento
    self.Usa_oculos = Usa_oculos

class Marca:
  def __init__(self, Nome_marca, sigla):
    self.id = None
    self.Nome = Nome_marca
    self.sigla = sigla

class Veiculo:
  def __init__(self, placa, ano, cor, motor, proprietario, marca):
    self.placa = placa
    self.ano = ano
    self.cor = cor
    self.motor = motor
    self.proprietario = proprietario
    self.marca = marca

try:
  # abertura da conexão
  conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_05/teste.db')

#funçao PRAGMA
  conexao.execute('PRAGMA foreign_keys=on')

# aquisição de um cursor
  cursor = conexao.cursor()

  Pessoa = Pessoa(12345678912, 'Silvia', '1990-12-05', True)

  comando = '''
  INSERT INTO Pessoa VALUES(:id, :Nome, :Data_nascimento, :Usa_oculos);
  '''
  # criando veiculos
  comando_02 = 'INSERT INTO  Veiculo VALUES (:placa, :ano, :cor, :proprietario, :marca);'
  veiculo_01 = Veiculo('aaa-0001',2011, 'Prata',  12345678910,'Silvia', 'marca_01.id')
  veiculo_02 = Veiculo('aaa-0002',2012, 'Preto',  12345678911,'José', 'marca_02.id')
  veiculo_03 = Veiculo('aaa-0003',2013, 'Azul', 12345678912,'Matheus', 'marca_01.id')
  veiculo_04 = Veiculo('aaa-0004',2014, 'Vermelho', 12345678913,'Fulano de Tal', 'marca_01.id')

  # execução do comando: SELECT, INSERT, CREATE...
  cursor.execute(comando, vars(Pessoa))
  cursor.execute(comando_02, vars(Veiculo))

# Efetivação do comando
  conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()