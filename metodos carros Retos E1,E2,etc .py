
class Car:
    def __init__(self,color,model, price,km):
        self.color=color
        self.model=model
        self.price=price
        self.km=km
        self.turned_on = False
        
    
    def turn_on(self):
        if self.turned_on==False:
            self.turned_on=True
            print("Carro encendido")
        else:
            print("Accion invalida, El carro ya se encuentra encendido")

    def turn_off(self):
        if self.turned_on==True:
            self.turned_on=False
            print("Carro apagado")
        else:
            print("Accion invalida, El carro ya esta apagado")

    def drive(self,recorrido):
        if self.turned_on==True:
            
            self.km+=recorrido
            print(f"Km recorridos en el carro: {round(recorrido,2)} ")
            print(f"Km totales del carro: {round(self.km,2)}")
        else:
            print("Debes encender el auto antes de conducir")

        


class Garage:
    def __init__(self,cars):
        self.cars=cars

    def garage_price(self):
        total=0
        for j in range(len(self.cars)):
            total+=self.cars[j].price
        print(f"El precio del garage es:{total}")

c1=Car("Blue",2008,30,400)
c2=Car("Green",1999,40,600)
c3=Car("Purple",2015,25,950)

car_list=[c1,c2,c3]
g1=Garage(car_list)

print(c1.color)

c1.color="light blue"

#print("El nuevo color es: ",c1.color)
print("\n\n\n")


#print("El garage es: ",g1.cars)           Así solo muestra metadatos

for i in range(len(g1.cars)):
    print(g1.cars[i].color)

g1.garage_price()



c1.turn_off()
print("------------------------------------------------------\n")
c1.turn_on()
print("------------------------------------------------------\n")
c1.turn_on()
print("------------------------------------------------------\n")
c1.turn_off()

print("------------------------------------------------------\n")
c1.drive(50)
print("------------------------------------------------------\n")
c1.turn_on()
print("------------------------------------------------------\n")

c1.drive(426)




"""
    Cantidad de dinero en un garage
garage_money=0
for j in range(len(g1.cars)):
    garage_money+=g1.cars[i].price

print(f"Valor total del garage es:{garage_money}"""

