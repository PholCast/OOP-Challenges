"""Ejercicio 2: dadas dos listas l,k donde l es una lista 
con elementos y k es una lista vacía, escriba una 
 que pase todos los elementos de l a k y las devuelva 
 (l estará vacía y k llena con todos los elementos de l 
 manteniendo el orden original). Restricción: sólo puede 
 usar la función pop()."""

l = [1,"a",True,"c",36]


k=[l.pop(0) for i in range(len(l))]
print(f"El array k es: {k}")
print(f"El array l es: {l}")