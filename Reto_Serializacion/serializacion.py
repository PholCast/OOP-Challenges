import pickle
from dataclasses import dataclass




def function(archivo):
    with open(archivo,"rb") as pf:
        new_personas = pickle.load(pf)

    new_personas.sort(key = lambda x: x.id)
    
    print("Nombre\t\tId\t\tEmail\t\t\tEdad")
    for i in new_personas:
       print(f"{i.nombre}\t\t{i.id}\t{i.email}\t\t{i.edad}")
@dataclass
class Persona:
  nombre:str
  id:int
  email:str
  edad:int

file = open("Taller_herencia.txt","r",encoding="latin1")

data = file.readlines()
data.pop(0)

personas= []


for i in range(len(data)):
  aux = data[i].split("\t")
  aux[3] = aux[3].replace("\n","")

  objeto = Persona(aux[0],aux[1],aux[2],int(aux[3]))
  personas.append(objeto)



with open("personas.pickle","wb") as pf:
  pickle.dump(personas,pf)


function("personas.pickle")



