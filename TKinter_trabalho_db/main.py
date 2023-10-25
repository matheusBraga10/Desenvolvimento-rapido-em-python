from classe_designer import *
from classe_funcionalidades import *
import tkinter as tk

if __name__ == '__main__':

    janela = tk.Tk()
    funcionalidades = classe_funcionalidades()
    designer = classe_designer(janela, classe_funcionalidades) 
    
    
    designer()



    