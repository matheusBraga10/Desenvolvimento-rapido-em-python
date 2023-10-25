from tkinter import *

janela = Tk()

class aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        janela.mainloop()
    
    def tela(self):
        self.janela.title('Sistema de cadastro')
        self.janela.configure(background='#44474a')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=500)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd= 3, bg= '#d9dbde', highlightthickness=5, highlightbackground= '#496487')
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.janela, bd= 3, bg= '#d9dbde', highlightthickness=5, highlightbackground= '#496487')
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets_frame_1(self):
        # Criação botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'))
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'))
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'))
        self.bt_novo.place(relx= 0.4, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'))
        self.bt_alterar.place(relx= 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#496487', fg='white', font=('verdana',8,'bold'))
        self.bt_apagar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        # Criação label entrada do codigo
        self.lb_codigo = Label(self.frame_1, text= 'Código')
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        # Criação label entrada do nome
        self.lb_nome = Label(self.frame_1, text= 'Nome')
        self.lb_nome.place(relx= 0.05, rely= 0.3)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely= 0.4, relwidth= 0.8)

        # Criação label entrada do telefone
        self.lb_telefone = Label(self.frame_1, text= 'Telefone')
        self.lb_telefone.place(relx= 0.05, rely= 0.55)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely= 0.65, relwidth= 0.4)

        # Criação label entrada do Cidade
        self.lb_cidade = Label(self.frame_1, text= 'Cidade')
        self.lb_cidade.place(relx= 0.05, rely= 0.55)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.05, rely= 0.65, relwidth= 0.4)
        
        
        

aplicacao()
