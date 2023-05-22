def remove_punt(letra):
  punt = ",.!?¿¡;()'"
  for i in punt:
    letra = letra.replace(i,"")
  return letra

file = open("canciones.txt","r",encoding="utf-8")

data = file.read()

canciones = data.split("-----")

#Separando canciones
cancion1 = canciones[0]
cancion2 = canciones[1]
cancion3 = canciones[2]


#Reemplazando saltos de linea y dobles espacios
cancion1 = cancion1.replace("\n"," ")
cancion1 = cancion1.replace("  "," ")

cancion2 = cancion2.replace("\n"," ")
cancion2 = cancion2.replace("  "," ")

cancion3 = cancion3.replace("\n"," ")
cancion3 = cancion3.replace("  "," ")

#Removiendo signos de puntuación
cancion1 = remove_punt(cancion1)
cancion2 = remove_punt(cancion2)
cancion3 = remove_punt(cancion3)


#Aplicando minusculas
cancion1 = cancion1.lower()
cancion2 = cancion2.lower()
cancion3 = cancion3.lower()


#Seperando palabras de cada canción
palabrasCancion1 = cancion1.split()
palabrasCancion2 = cancion2.split()
palabrasCancion3 = cancion3.split()

lista_palabras_canciones = [palabrasCancion1,palabrasCancion2,palabrasCancion3]

#diccionario de las palabras de cada canción
diccionario_palabrasCancion1 = {}
diccionario_palabrasCancion2 = {}
diccionario_palabrasCancion3 = {}
lista_diccionarios_canciones = [diccionario_palabrasCancion1,diccionario_palabrasCancion2,diccionario_palabrasCancion3]


#Llenando diccionario por cada cancion
for j in range(3):
    for word in lista_palabras_canciones[j]:
        if(word in lista_diccionarios_canciones[j] ):
            lista_diccionarios_canciones[j][word] += 1 #modificación --> palabras[palabra] = palabras[palabra]+1
        else:
            lista_diccionarios_canciones[j][word] = 1 #creación

    #lista_diccionarios_canciones[j] = dict(sorted(lista_diccionarios_canciones[j].items(), key=lambda x: x[1], reverse=True))

diccionario_palabrasCancion1 = dict(sorted(diccionario_palabrasCancion1.items(), key = lambda x: x[1], reverse=True))  
diccionario_palabrasCancion2 = dict(sorted(diccionario_palabrasCancion2.items(), key = lambda x: x[1], reverse=True))  
diccionario_palabrasCancion3 = dict(sorted(diccionario_palabrasCancion3.items(), key = lambda x: x[1], reverse=True)) 


# #TODAS LAS CANCIONES
palabras = {}

for i in range(3):
  for palabra in lista_palabras_canciones[i]:
    if(palabra in palabras):
        palabras[palabra] += 1 #modificación --> palabras[palabra] = palabras[palabra]+1
    else:
        palabras[palabra] = 1 #creación
  
#print(palabras)
palabras= dict(sorted(palabras.items(), key=lambda x: x[1], reverse=True))
#print(palabras)


print(f"La primera canción usa {len(diccionario_palabrasCancion1)} palabras diferentes")
print(f"La segunda canción usa {len(diccionario_palabrasCancion2)} palabras diferentes")
print(f"La tercera canción usa {len(diccionario_palabrasCancion3)} palabras diferentes")
print(f"Teniendo en cuenta todas las canciones se usan {len(palabras)} palabras diferentes")


print("\n")
print("Las 5 palabras más usadas son: ")

def CincoMasUsadas(diccionario):
    cont = 0
    for clave in palabras.keys():
        if cont < 5:
            print(clave)
            cont+=1
        else:
            break
    return
   
CincoMasUsadas(palabras)
print("\n")
#SPANISH.TXT
castellano = open("spanish.txt","r",encoding="utf-8")

castellano = castellano.read()

castellano = castellano.replace("\n"," ")

#print(castellano)
castellano = castellano.split(" ")

castellano.remove("")

for m in castellano:
   if m in palabras:
      del palabras[m]

print("Borrando las que están en spanish.txt, las 5 palabras más usadas son: ")

CincoMasUsadas(palabras)


