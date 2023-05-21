from Chef import Chef
from Subchef import Subchef
from Cliente import Cliente
from Menu import Menu, menu_restaurante
from Despensa import despensa

def mostrar_menu(m):
    for i  in range(len(m)):
        print(f"{i+1} - {m[i].nombre}: ${m[i].precio}")


while(True): 

    daniela=Cliente("Daniela",8000)
    print(f"Daniela, tienes {daniela.dinero} pesos")

    mostrar_menu(menu_restaurante.get_platos())



    mario = Subchef("Mario")

    orden1=daniela.pedido(menu_restaurante)
    continuar = mario.cocinar(orden1,despensa)

    if continuar == False:
        pass
    else:
        break
    


    