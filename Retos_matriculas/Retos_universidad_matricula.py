"""Reto 2 - E5
Implementar el siguiente escenario:

Desarrollaremos una aplicación para gestionar el proceso de matrícula y cancelación de materias. En este problema tenemos varios roles: los estudiantes tienen id, nombre, y una lista de cursos matriculados; los profesores tienen id, nombre y una lista de cursos que dictan; los cursos tienen un id, nombre, una lista de los estudiantes matriculados y el profesor que lo dicta.

En esta aplicación se podrán crear cursos, estudiantes y profesores. Adicionalmente, los estudiantes podrán matricular y cancelar cursos. Cuando se crea un curso, se debe definir el profesor que lo dicta.

--> qué clases deben implementar? cuáles son sus atributos? de qué tipo de datos?

--> instancien varios objetos de cada clase para que puedan probar"""

import random
class Student:
    def __init__(self,name_student,ID_student):
        self.name_student=name_student #str
        self.ID_student=ID_student  #str
        self.student_courses=[]  #array


    """RETO 3 - E6 (0.2 para los 5 primeros de cada literal): enroll_course, cancel_course,
      remove_student, get_student_list"""
    
    def enroll_course(self,course):
        if not (course in self.student_courses): 
            self.student_courses.append(course)
            #course.students.append(self)
            course.enroll_student(self)
            print(f"ESTUDIANTE {self.name_student}, SU CURSO {course.name} FUE MATRICULADO CON EXITO")
        else:
            print(f"ACCION INVALIDA: El estudiante {self.name_student} ya esta matriculado en el curso {course.name} ")
    
    def cancel_course(self,course):
        verifica=False
        for i in range(len(self.student_courses)):
            if self.student_courses[i]==course:
                verifica=True
        if verifica==True:
            self.student_courses.remove(course)
            course.remove_student(self)
            print("CURSO CANCELADO CON EXITO")
        else:
            print("No puedes cancelar un curso que no esta matriculado")




class Professor:
    def __init__(self,name_p,ID_p):
        self.name_p=name_p  #str
        self.ID_p=ID_p  #str
        self.professor_courses=[] #array

    def crear_parciales(self,curso, nombre_parcial,porc_parcial,preguntas):
        if self==curso.professor:
            examen=Parcial(nombre_parcial,porc_parcial,preguntas)
            print(f"El parcial {examen.nombre} ha sido creado")
            curso.ingresar_curso(examen)
        else: print("El profesor no esta en este curso, por lo que no puede crear el parcial")
        
    def evaluar_parcial(self,curso,parcial):
      verificar_parcial=False
      for k in range(len(curso.parciales)):
        if parcial==curso.parciales[k].nombre:
          verificar_parcial=True
      if self == curso.professor and verificar_parcial:
        print("VERDADERO")
        for j in range(len(curso.students)):
          
          curso.notas[curso.students[j].name_student][parcial]=round(random.uniform(0,5),2)
          
      elif(self == curso.professor and verificar_parcial==False):
        print(f"ERROR: El parcial {parcial} no se encuentra en el curso {curso.name}")
      else:print(f"ERROR: {self.name_p} no es el profesor del curso {curso.name} ")




class Course:
    def __init__(self,name,ID,professor ): 
        self.name=name #str
        self.ID=ID #str
        self.students=[] #array
        self.professor=professor    #array
        professor.professor_courses.append(self)

        self.parciales=[]
        self.notas={}

    

    def enroll_student(self,student):
        self.students.append(student)
        self.notas[student.name_student]={}

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{self.name}: El estudiante {student.name_student} ha sido removido del curso")
            del self.notas[student.name_student]
        else:
            print(f"El estudiante {student.name_student} no esta matriculado")

        if self in student.student_courses:
            student.student_courses.remove(self)
            


    def get_student_list(self):
        if len(self.students)>0:
            print(f"Los estudiantes del curso {self.name} son:")
            for i in range(len(self.students)):
                print("Estudiante #",i+1,": ",self.students[i].name_student)
        else:print(f"En el curso {self.name} no hay estudiantes matriculados")

    def ingresar_curso(self,examen):

        self.parciales.append(examen)
    
    
        
"""RETO 4 - E7

Implemente la lógica necesaria para que un profesor pueda crear parciales a
 cursos especificos. Las caracteristicas que tendrán esos parciales incluyen 
 nombre, porcentaje y preguntas. Defina las clases y metodos que considere necesarios."""

class Parcial: 
  def __init__(self, nombre, porcentaje, preguntas):
    self.nombre = nombre
    self.porcentaje = porcentaje
    self.preguntas = preguntas
    
"""Creacion profesores"""
p1=Professor("Jonathan","320")

p2=Professor("Ofelia","023")

p3=Professor("Mary","6352")


#------------------------------------------------------------------------------------------
"""Creacion cursos"""

coursePoo=Course("Programacion","145",p1)

calc=Course("Calculo","547",p2)

algebra=Course("Algebra lineal","472",p2)

mythology=Course("Mitologia","396",p3)

introduction=Course("Introduccion","44102",p3)




#------------------------------------------------------------------------------------------
"""Creacion estudiantes"""
phol=Student("Phol Castañeda","789")
neithan=Student("Neithan Gomez","014")
leonardo=Student("Leonardo Guevara", "658")
#-------------------------------------------------------------------------------------------

"Usando el metodo para matricular"
phol.enroll_course(coursePoo)
phol.enroll_course(coursePoo) #ya matriculado
phol.enroll_course(calc)
phol.enroll_course(algebra)
print("\n")
neithan.enroll_course(coursePoo)
neithan.enroll_course(mythology)
neithan.enroll_course(introduction)
neithan.enroll_course(mythology)#ya matriculado
print("\n")
leonardo.enroll_course(introduction)
leonardo.enroll_course(algebra)
leonardo.enroll_course(calc)
#-------------------------------------------------------------------------------------------

print("\n")
"Usando el metodo get student list"
coursePoo.get_student_list()

#-------------------------------------------------------------------------------------------

"""Usando el metodo cancelar y remover estudiante"""
"""print("\n")
phol.cancel_course(coursePoo)

phol.cancel_course(coursePoo)
print("\n")
coursePoo.remove_student(neithan)"""



"""for p in range(len(neithan.student_courses)):
    print(f"Curso #{p+1} de {neithan.name_student}: ",neithan.student_courses[p].name)
"""

print("\n")
lenguaje=Course("Lenguaje","5820",p1)
lenguaje.get_student_list()





#Implemente la lógica necesaria para que un profesor pueda crear parciales a cursos especificos. Las caracteristicas que tendrán esos parciales incluyen nombre, porcentaje y preguntas. Defina las clases y metodos que considere necesarios.

p1.crear_parciales(coursePoo,"Estructuras basicas",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p1.crear_parciales(coursePoo,"Conceptos basicos POO",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})


p1.evaluar_parcial(coursePoo,"Estructuras basicas")
p1.evaluar_parcial(coursePoo,"Conceptos basicos POO")
"""PARA MOSTRAR LOS PARCIALES DEL CURSO

for mn in range(len(coursePoo.parciales)):
  print(coursePoo.parciales[mn].nombre)"""
print(coursePoo.notas)
