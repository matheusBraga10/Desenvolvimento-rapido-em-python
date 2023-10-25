from tkinter import *

janela = Tk()

class aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.botoes()
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

    def botoes(self):
        # Criação botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar')
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar')
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão novo
        self.bt_novo = Button(self.frame_1, text='Novo')
        self.bt_novo.place(relx= 0.4, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar')
        self.bt_alterar.place(relx= 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        # Criação botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar')
        self.bt_apagar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        



aplicacao()
