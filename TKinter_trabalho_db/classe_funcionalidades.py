import sqlite3
from tkinter import *
#from classe_designer import *

class funcionalidades():
    def variaveis(self):
        self.cnpj = self.cnpj_entry.get()
        self.razao_social = self.razao_social_entry.get()
        self.cod_nat_jur = self.cod_nat_jur_entry.get()
        self.qualificacao_responsavel = self.qualificacao_responsavel_entry.get()
        self.capital_social = self.capital_social_entry.get()
        self.Cod_porte = self.Cod_porte_entry.get()
        self.Ente_federativo = self.Ente_federativo_entry.get()

    def limpa_empresa(self):
        self.cnpj = self.cnpj_entry.delete(0, END)
        self.razao_social = self.razao_social_entry.delete(0, END)
        self.cod_nat_jur = self.cod_nat_jur_entry.delete(0, END)
        self.qualificacao_responsavel = self.qualificacao_responsavel_entry.delete(0, END)
        self.capital_social = self.capital_social_entry.delete(0, END)
        self.Cod_porte = self.Cod_porte_entry.delete(0, END)
        self.Ente_federativo = self.Ente_federativo_entry.delete(0, END)

    def conecta_db(self):
        path_empresas_db = '/home/matheus/Empresas0/desafio_tkinter.db'
        self.conn_db = sqlite3.connect(path_empresas_db)
        self.cursor = self.conn_db.cursor(); print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn_db.close(); print('Desconectando ao banco de dados')

    def add_empresa(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''
            INSERT INTO Empresas (CNPJ, razao_social, cod_nat_jur, qualificacao_responsavel, capital_social, Cod_porte, Ente_federativo)
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (self.cnpj, self.razao_social, self.cod_nat_jur, self.qualificacao_responsavel, self.capital_social, self.Cod_porte, self.Ente_federativo))
        self.conn_db.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_empresa()

    def select_lista(self):
        self.lista_empresas.delete(*self.lista_empresas.get_children())
        self.conecta_db()
        lista = self.cursor.execute('''
            SELECT CNPJ, razao_social, cod_nat_jur, qualificacao_responsavel, capital_social, Cod_porte, Ente_federativo  FROM Empresas
            ORDER BY razao_social ASC; ''')
        for i in lista:
            self.lista_empresas.insert('', END, values=i)
        self.desconecta_bd()

    def duplo_clique(self, event):
        self.limpa_empresa()
        self.lista_empresas.selection()

        for n in self.lista_empresas.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.lista_empresas.item(n, 'values')
            self.cnpj_entry.insert(END, col1)
            self.razao_social_entry.insert(END, col2)
            self.cod_nat_jur_entry.insert(END, col3)
            self.qualificacao_responsavel_entry.insert(END, col4)
            self.capital_social_entry(END, col5)
            self.Cod_porte_entry.insert(END, col6)
            self.Ente_federativo_entry.insert(END, col7)
            
    def deleta_empresa(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''DELETE FROM Empresas WHERE CNPJ = ? ''', (self.CNPJ))
        self.conn_db.commit()
        self.desconecta_bd()
        self.limpa_empresa()
        self.select_lista()

    def altera_empresa(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute('''
            UPDATE Empresas SET razao_social = ?, Cod_porte= ?, 
            WHERE CNPJ = ?''', (self.razao_social, self.Cod_porte, self.cnpj))
        self.conn_db.commit()
        self.desconecta_bd()
        self.limpa_empresa()
        self.select_lista()

    def busca_empresa(self):
        self.variaveis()
        self.conecta_db()
        self.lista_empresas.delete(*self.lista_empresas.get_children())
        self.razao_social_entry.insert(END, '%')
        nome = self.razao_social_entry.get()
        self.cursor.execute('''
            SELECT * FROM Empresas
            WHERE  razao_social LIKE '%s' ORDER BY razao_social ASC''' % nome)
        busca_nome_empresa = self.cursor.fetchall()
        for i in busca_nome_empresa:
            self.lista_empresas.insert('', END, values=i)
        self.limpa_empresa()
        self.desconecta_bd()
        