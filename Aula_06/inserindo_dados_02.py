import sqlite3 as conector

class Pessoa:
  def __init__(self, id, Nome, Data_nascimento, Usa_oculos):
    self.id = id
    self.Nome = Nome
    self.Data_nascimento = Data_nascimento
    self.Usa_oculos = Usa_oculos

try:
  # abertura da conexão
  conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_05/teste.db')

  #funçao PRAGMA
  conexao.execute('PRAGMA foreign_keys=on')

# aquisição de um cursor
  cursor = conexao.cursor()

  Pessoa = Pessoa(12345678911, 'José', '1990-12-01', False)

  comando = '''
  INSERT INTO Pessoa (CPF, Nome, Data_nascimento, Usa_oculos)
  VALUES (?,?,?,?);
  '''

  # execução do comando: SELECT, INSERT, CREATE...
  cursor.execute(comando, (Pessoa.id, Pessoa.Nome, Pessoa.Data_nascimento, Pessoa.Usa_oculos))

# Efetivação do comando
  conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()
