# RETO 3
# * Cree un programa con las siguientes funcionalidades:
#   * Generar un archivo txt con 1000 nombres y edades creados de manera aleatoria (no importa si los nombres no tienen sentido). Estos nombres deben ser alfabéticos.
#   * Cargar información desde un archivo txt y crear objetos de tipo persona con estos atributos.
#   * Crear un listado de personas y saludarlos uno a uno con la frase "Hola [nombre de persona]"
# * **Use TDD**


from gestor_archivo import Gestor_Archivo
from persona import Persona
from gestor_saludo import Gestor_saludo

ga = Gestor_Archivo()


ga.generar_archivo("Archivo.txt")
#ga.leer_archivo("Archivo.txt")

lista_personas = ga.crear_personas("Archivo.txt")

saludador = Gestor_saludo()

saludador.saludar(lista_personas)