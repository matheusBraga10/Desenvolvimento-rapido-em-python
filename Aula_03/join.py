#string_final = “conector”.join(iteravel)

minha_lista = ["Arroz", "Feijão", "Macarrão"]
texto1 = ", ".join(minha_lista)
with open('texto1.txt', 'w') as arquivo: #usando esta sintaxe para abrir o arquivo, o python fecha o mesmo para você
    arquivo.write(texto1)
texto2 = "\n".join(minha_lista)
with open('texto2.txt', 'w') as arquivo:
    arquivo.write(texto2)

