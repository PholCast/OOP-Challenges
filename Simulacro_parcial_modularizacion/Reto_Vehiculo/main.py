from Vehiculo import Vehiculo
def main():
    vehiculo1 = Vehiculo("Ford", "Mustang", 2022, 250.0)
    vehiculo1.acelerar(10)
    vehiculo1.mostrar_datos()  # salida esperada: "Marca: Ford, Modelo: Mustang, Año: 2022, Velocidad máxima: 250.0 km/h, Velocidad actual: 98.0 km/h"
    vehiculo1.frenar(5)
    vehiculo1.mostrar_datos()  # salida esperada: "Marca: Ford, Modelo: Mustang, Año: 2022, Velocidad máxima: 250.0 km/h, Velocidad actual: 48.5 km/h"
if __name__=="__main__":
    main()