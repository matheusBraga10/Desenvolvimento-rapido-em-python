import sqlite3
from tkinter import *
#from classe_designer import *

class funcionalidades():
    def variaveis(self):
        self.cnpj = self.cnpj_entry.get()
        self.razao_social = self.razao_social_entry.get()
        self.cod_nat_jur = self.cod_nat_jur_entry.get()
        self.desc_natureza = self.desc_natureza_entry.get()
        self.qualificacao_responsavel = self.qualificacao_responsavel_entry.get()
        self.capital_social = self.capital_social_entry.get()
        self.Cod_porte = self.Cod_porte_entry.get()
        self.Ente_federativo = self.Ente_federativo_entry.get()

    def limpa_empresa(self):
        self.cnpj = self.cnpj_entry.delete(0, END)
        self.razao_social = self.razao_social_entry.delete(0, END)
        self.cod_nat_jur = self.cod_nat_jur_entry.delete(0, END)
        self.desc_natureza = self.desc_natureza_entry.delete(0, END)
        self.qualificacao_responsavel = self.qualificacao_responsavel_entry.delete(0, END)
        self.capital_social = self.capital_social_entry.delete(0, END)
        self.Cod_porte = self.Cod_porte_entry.delete(0, END)
        self.Ente_federativo = self.Ente_federativo_entry.delete(0, END)

    def conecta_db(self):
        try:
            path_empresas_db = '/home/matheus/Documentos/MeusProjetos/Desenvolvimento-rapido-em-python/Desenvolvimento-rapido-em-python/TKinter_trabalho_db/empresas.db'
            self.conn_db = sqlite3.connect(path_empresas_db)
            self.cursor = self.conn_db.cursor(); print('Conectando ao banco de dados')
            return True
        except sqlite3.DatabaseError as error:
            print('Erro na conexao:', error)
            return False

    def desconecta_bd(self):
        if(self.conn_db):
            self.cursor.close()
            self.conn_db.close(); print('Desconectando ao banco de dados')

    def add_empresa(self):
        if(self.conecta_db()):
            try:
                self.variaveis()
                self.cursor.execute('''
                    INSERT INTO Empresa (cnpj, nome, cod_natureza, desc_natureza, qualificacao, cap_social, cod_porte, desc_porte)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (self.cnpj, self.razao_social, self.cod_nat_jur, self.desc_natureza, self.qualificacao_responsavel, self.capital_social, self.Cod_porte, self.Ente_federativo))
                self.conn_db.commit()
                self.desconecta_bd()
                self.select_lista()
                self.limpa_empresa()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def select_lista(self):
        if(self.conecta_db()):
            try:
                self.lista_empresas.delete(*self.lista_empresas.get_children())
                lista = self.cursor.execute('''
                    SELECT cnpj, nome, cod_natureza, qualificacao, cap_social, cod_porte, desc_porte  FROM Empresa
                    ORDER BY nome ASC; ''')
                for i in lista:
                    self.lista_empresas.insert('', END, values=i)
                self.desconecta_bd()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def duplo_clique(self, event):
        if(self.conecta_db()):
            try:
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
            except sqlite3.DatabaseError as erro:
                print(erro)
                    
    def deleta_empresa(self):
        if(self.conecta_db()):
            try:
                self.variaveis()
                self.conecta_db()
                self.cursor.execute('''DELETE FROM Empresa WHERE cnpj = ? ''', (self.CNPJ,))
                self.conn_db.commit()
                self.desconecta_bd()
                self.limpa_empresa()
                self.select_lista()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def altera_empresa(self):
        if(self.conecta_db()):
            try:
                self.variaveis()        
                self.cursor.execute('''
                    UPDATE Empresa SET nome = ?, cod_porte= ?, 
                    WHERE cnpj = ?''', (self.razao_social, self.Cod_porte, self.cnpj))
                self.conn_db.commit()
                self.desconecta_bd()
                self.limpa_empresa()
                self.select_lista()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def busca_empresa(self):
         if(self.conecta_db()):
            try:
                self.variaveis()
                self.lista_empresas.delete(*self.lista_empresas.get_children())
                self.razao_social_entry.insert(END, '%')
                nome = self.razao_social_entry.get()
                self.cursor.execute('''
                    SELECT * FROM Empresa
                    WHERE  nome LIKE '%s' ORDER BY nome ASC''' % nome)
                busca_nome_empresa = self.cursor.fetchall()
                for i in busca_nome_empresa:
                    self.lista_empresas.insert('', END, values=i)
                self.limpa_empresa()
                self.desconecta_bd()
            except sqlite3.DatabaseError as erro:
                print(erro)        