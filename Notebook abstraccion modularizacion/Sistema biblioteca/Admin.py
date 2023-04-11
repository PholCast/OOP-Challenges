from dataclasses import dataclass

@dataclass
class Admin:
    nombre_admin: str
    prestados: int
    reservados: int
    noRegresado: int
    botado: int
    valor_multas: float #Crear metodos para gestionar base de datos, agregar
    #actualizar, etc


#atributos:
#cuantos libros tiene prestados
#cuantos tiene reservados
#cuantos libros no ha regresado
#cuantos libros ha botado
#Valor asociado a las multas

#gestionar la base de datos de la biblioteca
#donde se guarda un registro de cada libro disponible
#en la biblioteca

#Pude agregar, eliminar, actualizar, mostrar informacion
#o hacer busquedas relacionadas a cualquier libro