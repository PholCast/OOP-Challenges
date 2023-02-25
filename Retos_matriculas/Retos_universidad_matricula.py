"""Reto 2 - E5
Implementar el siguiente escenario:

Desarrollaremos una aplicación para gestionar el proceso de matrícula y cancelación de materias. En este problema tenemos varios roles: los estudiantes tienen id, nombre, y una lista de cursos matriculados; los profesores tienen id, nombre y una lista de cursos que dictan; los cursos tienen un id, nombre, una lista de los estudiantes matriculados y el profesor que lo dicta.

En esta aplicación se podrán crear cursos, estudiantes y profesores. Adicionalmente, los estudiantes podrán matricular y cancelar cursos. Cuando se crea un curso, se debe definir el profesor que lo dicta.

--> qué clases deben implementar? cuáles son sus atributos? de qué tipo de datos?

--> instancien varios objetos de cada clase para que puedan probar"""

import random
import matplotlib.pyplot as plt

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

    def rendimiento_estudiante(self):
        cursos_aprobados=0
        cursos_reprobados=0
        for i in range(len(self.student_courses)):
            sumanotas=sum(self.student_courses[i].notas[self.name_student].values())
            promedio=sumanotas/len(self.student_courses[i].parciales)
            if promedio>=3:
                cursos_aprobados+=1
            else:cursos_reprobados+=1

        print(f"cursos aprobados de {self.name_student}:{cursos_aprobados}\ncursos_reprobados de {self.name_student}:{cursos_reprobados}" )

        grafica=[cursos_aprobados,cursos_reprobados]
        
        etiquetas=[f"Cursos aprobados de {self.name_student}",f"Cursos perdidos de {self.name_student}"]
        plt.title(f"Rendimiento de {self.name_student}")
        plt.pie(grafica, labels=etiquetas,autopct='%2.2f%%')
        plt.show()
       



class Professor:
    def __init__(self,name_p,ID_p):
        self.name_p=name_p  #str
        self.ID_p=ID_p  #str
        self.professor_courses=[] #array

    def crear_parciales(self,curso, nombre_parcial,porc_parcial,preguntas):
        if self==curso.professor and porc_parcial>0 and porc_parcial<=100:
            examen=Parcial(nombre_parcial,porc_parcial,preguntas)
            print(f"El parcial {examen.nombre} ha sido creado")
            curso.ingresar_curso(examen)
        elif(self!=curso.professor and porc_parcial>0 or porc_parcial<=100):
            print("ERROR:El parcial no ha sido creado.\nEl profesor no esta en este curso, por lo que no puede crear el parcial")
        else:print("ERROR:El parcial no ha sido creado.\nDebes ingresar un porcentaje mayor que cero y menor o igual a 100")
        
    def evaluar_parcial(self,curso,parcial):
      verificar_parcial=False
      for k in range(len(curso.parciales)):
        if parcial==curso.parciales[k].nombre:
          verificar_parcial=True
      if self == curso.professor and verificar_parcial:
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
        else:print(f"En el curso de {self.name} no hay estudiantes matriculados")

    def ingresar_curso(self,examen):

        self.parciales.append(examen)
    
    def definir_estudiantes(self):
        ganadores=[]
        perdedores=[]
        for y in range(len(self.students)):
            sumaNotas=sum(self.notas[self.students[y].name_student].values())
            promedio=sumaNotas/len(self.parciales)
            if promedio>=3:
                ganadores.append(self.students[y].name_student)
            else:perdedores.append(self.students[y].name_student)


        print("\nEstudiantes que ganaron el curso:",ganadores,"\n\n","Estudiantes que perdieron el curso: ",perdedores)

        ganadores_perdedores=[len(ganadores),len(perdedores)]
        etiquetas=[f"Ganadores del curso {self.name}",f"perdedores del curso {self.name}"]
        plt.title(f"Aprobados y reprobados de {self.name}")
        plt.pie(ganadores_perdedores, labels=etiquetas,autopct='%2.2f%%')
        plt.show()
       
    
        
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

esteban=Student("Esteban gallego","5489")
daniela=Student("Daniela","420")
print("------------------------------------------------------------------------------------------------------\n")

#-------------------------------------------------------------------------------------------

"Usando el metodo para matricular"
phol.enroll_course(coursePoo)
phol.enroll_course(coursePoo) #ya matriculado
phol.enroll_course(calc)
phol.enroll_course(algebra)
phol.enroll_course(mythology)
phol.enroll_course(introduction)
print("\n")
neithan.enroll_course(coursePoo)
neithan.enroll_course(mythology)
neithan.enroll_course(calc)
neithan.enroll_course(algebra)
neithan.enroll_course(introduction)
neithan.enroll_course(mythology)#ya matriculado
print("\n")
leonardo.enroll_course(introduction)
leonardo.enroll_course(algebra)
leonardo.enroll_course(calc)
leonardo.enroll_course(coursePoo)
leonardo.enroll_course(mythology)
print("\n")
daniela.enroll_course(coursePoo)
daniela.enroll_course(calc)
daniela.enroll_course(algebra)
daniela.enroll_course(mythology)
daniela.enroll_course(introduction)


print("\n")
esteban.enroll_course(coursePoo)
esteban.enroll_course(calc)
esteban.enroll_course(algebra)
esteban.enroll_course(mythology)
esteban.enroll_course(introduction)
print("------------------------------------------------------------------------------------------------------\n")

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




print("------------------------------------------------------------------------------------------------------\n")

"""Implemente la lógica necesaria para que un profesor pueda crear parciales a 
cursos especificos. Las caracteristicas que tendrán esos parciales 
incluyen nombre, porcentaje y preguntas. Defina las clases y metodos que considere necesarios."""

p1.crear_parciales(coursePoo,"Estructuras basicas",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p1.crear_parciales(coursePoo,"Conceptos basicos POO",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})


p2.crear_parciales(calc,"Limites",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p2.crear_parciales(calc,"Derivadas",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})


p2.crear_parciales(algebra,"Matrices",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p2.crear_parciales(algebra,"Gauss",12.5,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})


p3.crear_parciales(mythology,"Mitologia griega",50,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p3.crear_parciales(mythology,"Mayas",10,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})


p3.crear_parciales(introduction,"Sistemas numericos",30,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})
p3.crear_parciales(introduction,"App inventor",20,{"Pregunta 1":"Respuestas 1","Pregunta 2":"Respuestas 2","Pregunta 3":"Respuestas 3"})

"""RETO 5 - E8 Cree la lógica para evaluar un parcial. En esta funcionalidad el profesor 
evaluará un curso con uno de los parciales previamente definido y se le asignará 
una nota de manera aleatoria a cada uno de los estudiantes 
del curso. Cada curso tendrá un registro de notas con base en los parciales 
que se le hayan definido."""

print("------------------------------------------------------------------------------------------------------\n")
#Evaluando parciales
p1.evaluar_parcial(coursePoo,"Estructuras basicas")
p1.evaluar_parcial(coursePoo,"Conceptos basicos POO")


p2.evaluar_parcial(calc,"Limites")
p2.evaluar_parcial(calc,"Derivadas")

p2.evaluar_parcial(algebra,"Matrices")
p2.evaluar_parcial(algebra,"Gauss")

p3.evaluar_parcial(mythology,"Mitologia griega")
p3.evaluar_parcial(mythology,"Mayas")

p3.evaluar_parcial(introduction,"Sistemas numericos")
p3.evaluar_parcial(introduction,"App inventor")


"""PARA MOSTRAR LOS PARCIALES DEL CURSO

for mn in range(len(coursePoo.parciales)):
  print(coursePoo.parciales[mn].nombre)"""



#Imprimiendo las notas de cada curso
print(coursePoo.notas)
print("\n\n")
print(calc.notas)
print("\n\n")
print(algebra.notas)
print("\n\n")
print(mythology.notas)
print("\n\n")
print(introduction.notas)


print("------------------------------------------------------------------------------------------------------\n")

#Graficas de cada curso con sus aprobados y reprobados
coursePoo.definir_estudiantes()
print("\n\n")
calc.definir_estudiantes()
print("\n\n")
algebra.definir_estudiantes()
print("\n\n")
mythology.definir_estudiantes()
print("\n\n")
introduction.definir_estudiantes()
print("\n\n")
print("------------------------------------------------------------------------------------------------------\n")

#Graficas para ver el rendimiento de cada estudiante
phol.rendimiento_estudiante()
print("\n\n")
neithan.rendimiento_estudiante()
print("\n\n")
leonardo.rendimiento_estudiante()
print("\n\n")
esteban.rendimiento_estudiante()
print("\n\n")
daniela.rendimiento_estudiante()


