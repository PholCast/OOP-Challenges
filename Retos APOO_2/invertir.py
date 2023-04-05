#Ejercicio:

#Cree una función para invertir una lista --> la solución debe usar el operador insert, del o pop.

#usando sólo insert
def invertir(l):
  l_aux = []
  for i in l:
    l_aux.insert(0,i)
  return l_aux

invertir([1,2,3])


#usando sólo pop
def invertir_pop(l):
  l_aux = [l.pop() for i in range(len(l))]
  print(l_aux)
  return l_aux
invertir_pop([1,2,3])
