from dataclasses import dataclass, astuple, asdict
from typing import Union

@dataclass
class Vehiculo:
    __marca: str
    __modelo: str
    __año: int
    __velocidadMax: float
    __velocidadActual:float = 0

    def get__velocidadMax(self):
        return self.__velocidadMax

    def set_velocidadMax(self,vel_value: float):
        if(type(vel_value)==float):
            self.__velocidadMax=vel_value
        else: print("Este tipo de dato no es asignable")

    def acelerar(self,seg:Union[float,int]):
        ACELERACION= 9.8
        aux=self.__velocidadActual+(ACELERACION*seg)

        if aux > self.__velocidadMax:
            print(" La velocidad asignada supera el limite, cambiando a la velocidad maxima...")
            self.__velocidadActual=self.__velocidadMax
            print("Velocidad actual= ", self.__velocidadActual)
            
        else: 
            self.__velocidadActual=aux
            print(f"la velocidad ha aumentado a {self.__velocidadActual} km/h")
    

    def frenar(self,seg:float):
        ACELERACION= 9.8
        aux=self.__velocidadActual-(ACELERACION*seg)

        if aux <0:
            print("Error, La velocidad no puede ser negativa, cambiando velocidad a 0...")
            self.__velocidadActual=0
            print("la velocidad actual es 0")
        else: 
            self.__velocidadActual=aux
            print(f"la velocidad ha disminuido a {self.__velocidadActual} km/h")
    
    def mostrar_datos(self):
        
        
        print(f"Marca:{self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}, Velocidad maxima: {self.__velocidadMax} km/h, Velocidad actual {self.__velocidadActual} km/h")