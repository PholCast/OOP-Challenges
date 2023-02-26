
"""Crear una clase Person con un atributo age.

Los valores de age deben estar entre 20 y 60.

Cree properties para este atributo.

Cree una lista de 100 objetos de tipo Person 
con edades aleatorias 

Cree una función que reciba una lista de tipo Person y la devuelva 
ordenada ascendentemente. Antes de retornar, imprima las edades de las personas en la lista."""
import random
class Person:
    def __init__(self, age):
        self._age=age
      

    @property
    def person_age(self):
      return self._age

    @person_age.setter
    def person_age(self,edadIngresada):
      if(type(edadIngresada)==int and edadIngresada>=20 and edadIngresada<=60):
        print("Se ha asignado la edad de: ",edadIngresada,"años")
        self._age=edadIngresada
      else:print("Debes asignar un numero entero entre 20 y 60")
    


def mostrar_edades(l):
  for j in range(len(l)):
    print(l[j].person_age, end="\t ")
  return
 # print(listaPersonas)

def ordenarLista(lista):
  lista.sort(key=lambda x: x.person_age)
  return



listaPersonas=[]

for i in range(100):
  x=random.randint(20,60)
  nueva_persona=Person(x)
  listaPersonas.append(nueva_persona)

print("Edades desordenadas:")
mostrar_edades(listaPersonas)


ordenarLista(listaPersonas)
print("\nEdades Ordenadas")
mostrar_edades(listaPersonas)


