#IMPORTANDO LIBRERIAS Y ARCHIVOS
from  abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from iconos import diccionario_iconos
from ExcepcionesChess import ErrorMovimiento,ErrorColor

#CREANDO LA CLASE ABSTRACTA
@dataclass
class Ficha(ABC):
    colorF: str
    nombreF:str
    posicionF:int
    iconoF:str

    def __repr__(self) -> str:
        return self.iconoF   

    @abstractmethod
    def move(self):
        pass

    @property
    def color(self):
        return self.colorF

    @color.setter
    def color(self,color_ingresado):
        self.colorF = color_ingresado
    
    @property
    def nombre(self):
        return self.nombreF

    @nombre.setter
    def nombre(self,nombre_ingresado):
        self.nombreF = nombre_ingresado



    @property
    def posicion(self):
        return self.posicionF
    
    @posicion.setter
    def posicion(self,posicion_ingresada):
        self.posicionF = posicion_ingresada

    @property
    def icono(self):
        return self.iconoF
    
    @icono.setter
    def icono(self,icono_ingresado):
        self.iconoF = icono_ingresado


class Peon(Ficha):
    def __init__(self,color,posicion,iconos):
        self.colorF = color
        self.nombreF = "Peón"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]
    

    def move(self,fila,columna):
        if self.colorF == "Negro":
            if columna-1 == self.posicion["columna"] and fila-1==self.posicion["fila"]+1:
                self.posicionF["fila"] += 1
                return True
            else:
                raise ErrorMovimiento("MOVIMIENTO INVALIDO")
        else:
            if columna-1 == self.posicion["columna"] and fila-1==self.posicion["fila"]-1:
                self.posicionF["fila"] -= 1
                return True
            else:
                raise ErrorMovimiento("MOVIMIENTO INVALIDO")
            

class Torre(Ficha):
    def __init__(self,color,posicion,iconos):
        self.colorF = color
        self.nombreF = "Torre"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]
    

    def move(self,fila,columna):
        self.posicion["vertical"] = fila #configurar
    
class Caballo(Ficha):
     def __init__(self,color,posicion,iconos):
        self.colorF = color
        self.nombreF = "Caballo"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]

     def move(self,mover_posicion):
        self.posicion["vertical"] = mover #configurar

class Alfil(Ficha):
    def __init__(self,color,posicion,iconos):
        self.colorF = color
        self.nombreF = "Alfil"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]

    def move(self,mover_posicion):
        self.posicion["vertical"] = mover #configurar
    
class Reina(Ficha):
    #Error para ver si al dar un color, es diferente de los permitidos
    def __init__(self,color,posicion,iconos):
        if color == "Negro" or color == "Blanco":
            self.colorF = color
        else: 
            raise ErrorColor(f"ERROR, EL COLOR {color} NO ES VALIDO")
        self.nombreF = "Reina"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]

    def move(self,mover_posicion):
        self.posicion["vertical"] = mover #configurar
    
class Rey(Ficha):
    def __init__(self,color,posicion,iconos):
        #Error para ver si al dar un color, es diferente de los permitidos
        if color == "Negro" or color == "Blanco":
            self.colorF = color
        else: 
            raise ErrorColor(f"ERROR, EL COLOR {color} NO ES VALIDO")
        self.nombreF = "Rey"
        self.posicionF = posicion
        self.iconoF = iconos[self.nombreF][self.colorF]

    def move(self,mover_posicion):
        self.posicion["vertical"] = mover #configurar
    



    

    
