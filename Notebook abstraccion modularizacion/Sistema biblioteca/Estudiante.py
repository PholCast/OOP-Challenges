from dataclasses import dataclass

@dataclass
class Estudiante:
    nombre_estudiante: str
    prestados: int #O será una lista con los libros?
    reservados: int
    noRegresado: int
    botado: int
    valor_multas: float

    #metodos prestar, reservar, regresar, pagar multa.

    #buscar libros por titulo o por autor


#atributos:
#cuantos libros tiene prestados
#cuantos tiene reservados
#cuantos libros no ha regresado
#cuantos libros ha botado
#Valor asociado a las multas


