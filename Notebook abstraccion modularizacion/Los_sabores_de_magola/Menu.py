from Plato import Plato
from dataclasses import dataclass
@dataclass
class Menu:
    __platos = []

    def crear_plato(self,nombre,ingredientes,precio):
        plato = Plato(nombre,ingredientes,precio)
        self.__platos.append(plato)

    def get_platos(self):
        return self.__platos


menu_restaurante=Menu()

menu_restaurante.crear_plato("Pure de papas",{"Papa":4,"Mantequilla":0.5,"Leche":0.3,"Sal":4},15000)
menu_restaurante.crear_plato("Espaguetis",{"Pasta":4,"Queso":1,"Carne": 4,"Salsa": 2,"Sal":2},10000)

menu_restaurante.crear_plato("Quesadilla",{"Tortilla":2,"Queso":2,"Pollo":5,"Salsa":1,"Sal":3},12000)

menu_restaurante.crear_plato("Salchipapa",{"Papa":3,"Salchicha":3,"Queso":1,"Salsa":1,"Sal":1},6000)

menu_restaurante.crear_plato("Perro",{"Pan":1,"Salchicha":1,"Salsa":1,"Queso":1},7000)

#print(menu_restaurante.get_platos())
        



