
import pytest
import os
from gestor_archivo import Gestor_Archivo
from persona import Persona

#Clase de pruebas

class Test_Gestor_Archivo:
  def test_generar_archivo(self):
    ga = Gestor_Archivo()
    ga.generar_archivo("Texto_prueba.txt")

    assert os.path.isfile("Texto_prueba.txt")

    
    archivo = open("Texto_prueba.txt")
    archivo = archivo.readlines()

    assert len(archivo) == 1000
    
  def test_leer_archivo(self):
    ga = Gestor_Archivo()
    ga.generar_archivo("Texto_prueba.txt")
    archivo_leido = ga.leer_archivo("Texto_prueba.txt")

    assert type(archivo_leido) == list

    for i in archivo_leido:
      assert type(i[0])== str
      assert i[0].isalpha()
      assert i[1].isdigit()

  


  def test_generar_nombres(self):
    #debo corroborar que se cree el nombre
    ga = Gestor_Archivo()
    nombres = ga.generar_nombres() #debería generar 1000 nombres --> una lista con 1000 nombres

    #sí son 1000?
    assert len(nombres) == 1000 

    #todos son alfabéticos
    for nombre in nombres:
      assert nombre.isalpha() == True
      assert len(nombre) >= 4 and len(nombre) <= 10




  def test_generar_edades(self):
    ga = Gestor_Archivo()

    edades = ga.generar_edades()
    #¿son 1000 edades?
    assert len(edades) == 1000

    #Todas son numericas?
    for edad in edades:
      
      assert type(edad) == int
      
      assert edad > 0 and edad <100




  def test_crear_personas(self):
    ga = Gestor_Archivo()
    ga.generar_archivo("Texto_prueba.txt")
    personas_creadas = ga.crear_personas("Texto_prueba.txt")

    assert len(personas_creadas) == 1000
    
    for i in personas_creadas:
      assert isinstance(i, Persona)