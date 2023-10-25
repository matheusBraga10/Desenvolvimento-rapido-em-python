import sqlite3


class funcionalidades():
    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_db(self):
        self.conn_db = sqlite3.connect('clientes.db')
        self.cursor = self.conn_db.cursor(); print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn_db.close(); print('Desconectando ao banco de dados')

    def monta_tabela(self):
        self.conecta_db()
        # Cria tabela
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTERGER PRIMARY KEY,
            nome_cliente CHAR(60) NOT NULL,
            telefone INTERGER(20),
            cidade CHAR(60)
            );
        ''')
        self.conn_db.commit(); print('Banco de dados criado')

    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_db()
        self.cursor.execute('''
            INSERT INT clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)''', self.nome, self.telefone, self.cidade)
        self.conn_db.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()

    def select_lista(self):
        self.lista_cliente.delete(*self.lista_cliente.get_childre())
        self.conecta_db()
        lista = self.cursor.execute('''SELECT cod, nome_cliente, telefone, cidade  FROM clientes
            ORDER BY nome_cliente ASC; ''')
        for i in lista:
            self.lista_cliente.insert('', END, values=1)
        self.desconecta_bd()

    def duplo_clique(self):
        