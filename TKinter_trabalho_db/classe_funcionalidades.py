import sqlite3
from tkinter import *
#from classe_designer import *

class funcionalidades():
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

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
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(60) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(60)
            );
        ''')
        self.conn_db.commit(); print('Banco de dados criado')
        self.desconecta_bd()

    def add_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''
            INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)''', (self.nome, self.telefone, self.cidade))
        self.conn_db.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()

    def select_lista(self):
        self.lista_cliente.delete(*self.lista_cliente.get_children())
        self.conecta_db()
        lista = self.cursor.execute('''
            SELECT cod, nome_cliente, telefone, cidade  FROM clientes
            ORDER BY nome_cliente ASC; ''')
        for i in lista:
            self.lista_cliente.insert('', END, values=i)
        self.desconecta_bd()

    def duplo_clique(self, event):
        self.limpa_cliente()
        self.lista_cliente.selection()

        for n in self.lista_cliente.selection():
            col1, col2, col3, col4 = self.lista_cliente.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''DELETE FROM clientes WHERE cod = ? ''', (self.codigo))
        self.conn_db.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''
            UPDATE clientes SET nome_cliente = ?, telefone= ?, cidade = ?
            WHERE cod = ?''', (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn_db.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def busca_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.lista_cliente.delete(*self.lista_cliente.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute('''
            SELECT * FROM clientes
            WHERE  nome_cliente LIKE '%s' ORDER BY nome_cliente ASC''' % nome)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista_cliente.insert('', END, values=i)
        self.limpa_cliente()
        self.desconecta_bd()
        