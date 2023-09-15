'''
- SQLite está contido em muitos apps (python, Chrome, contatos do celular...)
- É um SQL menor que funciona igual a um banco de daddos tradicional, porém em menor volume
- Conectores são bobliotecas capazes de se conectar ao banco de dados

- Principais métodos dos conectores
  - connect (Ato de conecção com o banco de dados)
  - connection (conecção estabelecida com funções)
    - commit (confirma todas as operações pendentes)
    - rollback (Desfa todas as operações pendentes)
    - cursor (retorna um objeto tipo cursor)
    - close (encerra a conexão)
  - cursor (funções)
    - execute (Prepara e executa a operação passada como parametro)
    - fetchone (retorna a proxima linha)
    - fetchall (retorna todas as linhas)

- Excessões dos conectores
  - error (É a mais abrangente)

- Tipos de dados
  - SQLite:(null, int, float, str, blob)
  - MySQL e PostgreSQL (mais complexos e completos)
'''

import sqlite3 as conector
try:
  # abertura da conexão
    conexao = conector.connect('/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Aula_05/teste.db')
# aquisição de um cursor
    cursor = conexao.cursor()

    comando_01 = '''
    CREATE TABLE Pessoa
    (
    CPF INT(11) NOT NULL,
    Nome VARCHAR(30) NOT NULL,
    Data_nascimento VARCHAR(12) NOT NULL,
    Usa_oculos BLOB,
    PRIMARY KEY (CPF)
    );
    '''
    comando_02 = '''
    CREATE TABLE Marca
    (
    id INT(5),
    Nome_marca VARCHAR(20) NOT NULL,
    sigla VARCHAR(12) NOT NULL,
    
    PRIMARY KEY (id)
    );
    '''

    comando_03 = '''
    CREATE TABLE Veiculo
    (
    id,
    CPF,
    placa INT(7) NOT NULL,
    ano VARCHAR(4) NOT NULL,
    cor VARCHAR(12) NOT NULL,
    proprietario INTEGRER(20) NOT NULL,
    marca INTEGRER(10) NOT NULL,
    FOREIGN KEY (id) REFERENCES Marca (id),
    FOREIGN KEY (CPF) REFERENCES Pessoa (CPF),
    PRIMARY KEY (placa)
    );
    '''



    
# execução do comando: SELECT, INSERT, CREATE...
    cursor.execute(comando_01)
    cursor.execute(comando_02)
    cursor.execute(comando_03)
# Efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
  print('Erro no banco de dados', erro)
finally:
  # fechamento das conexoes
  cursor.close()
  conexao.close()
