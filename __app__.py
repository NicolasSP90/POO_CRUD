# Objetos
from interface.interface import Interface

import os

# Limpa a tela
os.system("cls")

# Instancia a interface e adiciona o status True. 
# Enquanto for verdadeiro o programa vai sempre trazer um novo menu da interface.
running = Interface(status=True)

menu = running.selecao_menu()

while running.status == True:
    menu = running.selecao_menu(menu)
        
os.system("cls")
print("Programa Finalizado")