from dataclasses import dataclass

@dataclass
class Alumno:
    __nombre:str
    __edad: int
    __notas: list[float]


    def __repr__(self ):
        prom:float=self.promedio()
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Promedio: {prom}"
    

    def promedio(self):
        suma:float=0.0
        for i in range(len(self.__notas)):
            suma+=self.__notas[i]
        
        promedio:float=suma/len(self.__notas)
        return promedio


    

    def nota_mayor(self):
        aux:list=self.__notas
        aux.sort(reverse=True)
        
        print(f"la nota mayor de {self.__nombre} es: {aux[0]}")
        


    def nota_menor(self):
        aux:list=self.__notas
        aux.sort()
        
        print(f"la nota menor de {self.__nombre} es: {aux[0]}")



def mejor_alumno(alumnos:list[Alumno]):
    alumnos.sort(key=lambda x: x.promedio())
    cantidad:int=len(alumnos)
    
    print("El mejor alumno fue: \n",alumnos[cantidad-1])
  