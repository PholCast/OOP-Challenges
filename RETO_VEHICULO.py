class Vehiculo:
  def __init__(self,marca,modelo,año,color):
    self.marca=marca
    self.modelo=modelo
    self.año=año
    self.color=color


    def arrancar(self):
      print("Arrancando...")

    def detener(self):
      print(f"Deteniéndose...")


class Coche(Vehiculo):
  def __init__(self,marca,modelo,año,color,transmision):
    super().__init__(marca,modelo,año,color)
    self.transmision=transmision

  def arrancar(self):
      print("El coche está Arrancando...")

  def detener(self):
      print("El coche está deteniendose...")
  def estacionando(self):
    print("Estacionando el coche")

class Camioneta(Vehiculo):
  def __init__(self,marca,modelo,año,color,transmision):
    super().__init__(marca,modelo,año,color)
    self.transmision=transmision

  def arrancar(self):
      print("La camioneta está Arrancando...")
  
  def detener(self):
      print("La camioneta está deteniendose...")
  def estacionando(self):
    print("Estacionando la camioneta")



class Motocicleta(Vehiculo):
  def __init__(self,marca,modelo,año,color,transmision):
    super().__init__(marca,modelo,año,color)
    self.transmision=transmision
  def arrancar(self):
      print("La Motocicleta está Arrancando...")
  def detener(self):
      print("La motocicleta está deteniendose...")

  def estacionando(self):
    print("Estacionando la motocicleta")

  

def arrancar_detener(lista):
  for i in lista:
    i.arrancar()
    i.detener()
    



carro=Coche("Mazda","GTX",2004,"blue","Automatica")

moto=Motocicleta("AKT","A500",2006,"red","Manual")

van= Camioneta("Ford","Legend",2015,"purple","Automatica")

arrancar_detener([carro,moto,van])


#GARAGE

class Garage:
  def __init__(self):
    pass

  def abrir(self):
    print("El garage se está abriendo...")

  def cerrar(self):
    print("El garage se está cerrando...")

  def estacionar(self, vehiculo):
    vehiculo.estacionando()
    print("Estacionado con exito")


garage=Garage()
print("\n")
garage.estacionar(moto)

garage.estacionar(carro)
garage.estacionar(van)