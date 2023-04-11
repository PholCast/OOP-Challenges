from Chef import Chef
from Subchef import Subchef
from Cliente import Cliente
from Menu import Menu, menu_restaurante
from Despensa import despensa

def mostrar_menu(m):
    for i  in range(len(m)):
        print(f"{i+1} - {m[i].nombre}: ${m[i].precio}")


daniela=Cliente("Daniela",8000)

mostrar_menu(menu_restaurante.get_platos())



mario = Subchef("Mario")

mario.cocinar(daniela.pedido(menu_restaurante),despensa)