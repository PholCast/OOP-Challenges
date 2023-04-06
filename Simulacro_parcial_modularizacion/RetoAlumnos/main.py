from alumnos import Alumno, mejor_alumno

phol=Alumno("Phol", 18, [4.8,2.3,2.1])
leo=Alumno("Leo", 21, [5.0,1.2,3.4])
angel=Alumno("Angel", 13, [3.4,4.5,3.8])
daniela=Alumno("Daniela",17,[3.4,4.7,3.9])
neithan=Alumno("Neithan",16,[4.3,3.7,2.4])

lista:list=[phol,leo,angel,daniela,neithan]


leo.nota_mayor()
leo.nota_menor()
print("\n\n\n")

#verificando promedios
print("Promedios:")
print(phol.promedio())
print(leo.promedio())
print(angel.promedio())
print(daniela.promedio())
print(neithan.promedio())

print("\n\n\n")


#Funciona!
mejor_alumno(lista)