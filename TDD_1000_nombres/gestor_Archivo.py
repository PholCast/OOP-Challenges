import random

class Gestor_Archivo:
  def generar_archivo(self):

    with open("Archivo.txt", "w") as f:
        for j,k in list(zip(self.generar_nombres(),self.generar_edades())):
          var = str(j)+","+str(k)
          f.write(f"{var}\n")

  def leer_archivo(self):
    pass
  
  def escribir_archivo(self):
    pass

  def generar_nombres(self):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nombres = []
    for i in range(1000):
      tam = random.randint(1,10)
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
  def crear_personas(self):
    pass

ga = Gestor_Archivo()

ga.generar_archivo()