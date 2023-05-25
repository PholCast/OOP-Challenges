
import random
from persona import Persona
class Gestor_Archivo:
  def generar_archivo(self,nombre_archivo):

    with open(nombre_archivo, "w") as f:
        for j,k in list(zip(self.generar_nombres(),self.generar_edades())):
          var = str(j)+"~~"+str(k)
          f.write(var+"\n")

  def leer_archivo(self,nombre_archivo):
    
    with open(nombre_archivo,"r") as f:
      info_personas = f.readlines()

    for i in range(len(info_personas)):
        info_personas[i] = info_personas[i].replace("\n","").split("~~")

    return info_personas

  def generar_nombres(self):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nombres = []
    
    for i in range(1000):
      tam = random.randint(4,10)
      nombre = ""
      for j in range(tam):
        nombre += random.choice(letters)
      nombres.append(nombre)
    return nombres

  def generar_edades(self):
    edades = []
    for i in range(1000):
      num = random.randint(1,99)
      edades.append(num)
    return edades
  def crear_personas(self,nombre_archivo):
    
    datos_personas = self.leer_archivo(nombre_archivo)
    personas = []
    for i in datos_personas:
        person = Persona(i[0],i[1])

        personas.append(person)
    
    return personas
