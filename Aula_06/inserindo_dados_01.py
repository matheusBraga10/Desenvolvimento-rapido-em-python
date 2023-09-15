import sqlite3 as conector

try:
  # abertura da conexão
  conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_05/teste.db')

  #funçao PRAGMA
  #conexao.execute('PRAGMA foreign_keys=on')

# aquisição de um cursor
  cursor = conexao.cursor()

  usuario_01 = '''
  INSERT or IGNORE INTO Pessoa (CPF, Nome, Data_nascimento, Usa_oculos)
  VALUES (123456789,'Fulano de Tal','11-11-2011', False);
  '''

  cursor.execute(usuario_01)


  # execução do comando: SELECT, INSERT, CREATE...
  cursor.execute(usuario_01)

# Efetivação do comando
  conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()
