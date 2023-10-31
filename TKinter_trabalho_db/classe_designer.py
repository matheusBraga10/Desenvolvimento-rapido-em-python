from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

from classe_funcionalidades import *


janela = Tk()


class designer(funcionalidades):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.select_lista()
        self.indice()
        janela.mainloop()
    
    def tela(self):
        self.janela.title('Sistema de cadastro de Empresas')
        self.janela.configure(background='#44474a')
        self.janela.geometry('900x600')
        self.janela.resizable(True, True)
        self.janela.minsize(width=900, height=600)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd= 3, bg= '#d9dbde', highlightthickness=5, highlightbackground= '#496487')
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.janela, bd= 3, bg= '#d9dbde', highlightthickness=5, highlightbackground= '#496487')
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets_frame_1(self):
        # Criação botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'), command= self.limpa_empresa)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.10)
        # Criação botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'), command=self.busca_empresa)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.10)
        # Criação botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'), command=self.add_empresa)
        self.bt_novo.place(relx= 0.4, rely= 0.1, relwidth= 0.1, relheight= 0.10)
        # Criação botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'), command=self.altera_empresa)
        self.bt_alterar.place(relx= 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.1)
        # Criação botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'), command=self.deleta_empresa)
        self.bt_apagar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.1)

        # Criação label entrada do CNPJ
        self.lb_cnpj = Label(self.frame_1, text= 'CNPJ',bg= '#d9dbde',fg='#496487')
        self.lb_cnpj.place(relx= 0.05, rely= 0.03)

        self.cnpj_entry = Entry(self.frame_1)
        self.cnpj_entry.place(relx= 0.05, rely= 0.12, relwidth= 0.08)

        # Criação label entrada do Razão social
        self.lb_razao_social = Label(self.frame_1, text= 'Razão Social',bg= '#d9dbde',fg='#496487')
        self.lb_razao_social.place(relx= 0.05, rely= 0.2)

        self.razao_social_entry = Entry(self.frame_1)
        self.razao_social_entry.place(relx= 0.05, rely= 0.28, relwidth= 0.9)

        # Criação label entrada do Codigo natureza
        self.lb_cod_nat_jur = Label(self.frame_1, text= 'Código Natureza Juridica',bg= '#d9dbde',fg='#496487')
        self.lb_cod_nat_jur.place(relx= 0.05, rely= 0.38)

        self.cod_nat_jur_entry = Entry(self.frame_1)
        self.cod_nat_jur_entry.place(relx= 0.05, rely= 0.48, relwidth= 0.4)

        # Crianção label entrada da Descrição Natureza
        self.lb_desc_natureza = Label(self.frame_1, text= 'Descrição Natureza Juridica',bg= '#d9dbde',fg='#496487')
        self.lb_desc_natureza.place(relx= 0.55, rely= 0.38)

        self.desc_natureza_entry = Entry(self.frame_1)
        self.desc_natureza_entry.place(relx= 0.55, rely= 0.48, relwidth= 0.4)

        # Criação label entrada do Qualificacao do responsavel
        self.lb_qualificacao_responsavel = Label(self.frame_1, text= 'Qualificação do Responsável',bg= '#d9dbde',fg='#496487')
        self.lb_qualificacao_responsavel.place(relx= 0.05, rely= 0.58)

        self.qualificacao_responsavel_entry = Entry(self.frame_1)
        self.qualificacao_responsavel_entry.place(relx= 0.05, rely= 0.68, relwidth= 0.4)

        # Criação label entrada do Capital Social
        self.lb_capital_social = Label(self.frame_1, text= 'Capital Social',bg= '#d9dbde',fg='#496487')
        self.lb_capital_social.place(relx= 0.55, rely= 0.58)

        self.capital_social_entry = Entry(self.frame_1)
        self.capital_social_entry.place(relx= 0.55, rely= 0.68, relwidth= 0.4)

        # Criação label entrada do Codigo Porte
        self.lb_Cod_porte = Label(self.frame_1, text= 'Código Porte',bg= '#d9dbde',fg='#496487')
        self.lb_Cod_porte.place(relx= 0.05, rely= 0.78)

        self.Cod_porte_entry = Entry(self.frame_1)
        self.Cod_porte_entry.place(relx= 0.05, rely= 0.88, relwidth= 0.4)
        
        # Criação label entrada do Ente federativo
        self.lb_Ente_federativo = Label(self.frame_1, text= 'Ente Federativo',bg= '#d9dbde',fg='#496487')
        self.lb_Ente_federativo.place(relx= 0.55, rely= 0.78)

        self.Ente_federativo_entry = Entry(self.frame_1)
        self.Ente_federativo_entry.place(relx= 0.55, rely= 0.88, relwidth= 0.4)

    def lista_frame_2(self):
        self.lista_empresas = ttk.Treeview(self.frame_2, height= 3, column= ('col1','col2','col3','col4', 'col5','col6','col7', 'col8'))
        self.lista_empresas.heading('#0', text='')
        self.lista_empresas.heading('#1', text='CNPJ')
        self.lista_empresas.heading('#2', text='Razão Social')
        self.lista_empresas.heading('#3', text='Código Natureza Jurídica')
        self.lista_empresas.heading('#4', text='Descrição Natureza Jurídica')
        self.lista_empresas.heading('#5', text='Qualificação do Responsavel')
        self.lista_empresas.heading('#6', text='Capital Social')
        self.lista_empresas.heading('#7', text='Codigo Porte')
        self.lista_empresas.heading('#8', text='Ente Federativo')

        self.lista_empresas.column('#0', width=1)
        self.lista_empresas.column('#1', width=25)
        self.lista_empresas.column('#2', width=80)
        self.lista_empresas.column('#3', width=75)
        self.lista_empresas.column('#4', width=75)
        self.lista_empresas.column('#5', width=75)
        self.lista_empresas.column('#6', width=75)
        self.lista_empresas.column('#7', width=75)
        self.lista_empresas.column('#8', width=20)

        self.lista_empresas.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.barra_de_rolagem_lista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_empresas.configure(yscroll=self.barra_de_rolagem_lista.set)
        self.barra_de_rolagem_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.lista_empresas.bind('<Double-1>', self.duplo_clique)
        
    def indice(self):
        barra_de_menu = Menu(self.janela)
        self.janela.config(menu = barra_de_menu)
        file_menu_1 = Menu(barra_de_menu)
        file_menu_2 = Menu(barra_de_menu)

        def quit():
            self.janela.destroy()
        
        #barra_de_menu.add_cascade(label= 'Opções', menu = limpa_empresa)
        barra_de_menu.add_cascade(label= 'Sobre', menu = file_menu_2)

        file_menu_1.add_command(label= 'Limpar', command = self.limpa_empresa)
        file_menu_1.add_command(label= 'Buscar', command = self.busca_empresa)
        file_menu_1.add_command(label= 'Novo', command = self.add_empresa)
        file_menu_1.add_command(label= 'Alterar', command = self.altera_empresa)
        file_menu_1.add_command(label= 'Apagar', command = self.add_empresa)
        file_menu_1.add_command(label= 'Sair', command = quit)

        #file_menu_2.add_command(label= 'Informações', command= mb.showinfo('deleta_empresaformação', 'É necessário informar código e nome'))

