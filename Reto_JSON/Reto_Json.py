import csv

import json
x = open("Taller_herencia.csv",encoding="latin-1")

reader = csv.reader(x)
# lista = []
# for row in reader:
 
#   lista.append(row)


#print(lista)

reader=list(reader)


#print(reader)
lista= []
for i in reader[1:]:
  lista.append(i)

#print(lista)

diccionario = {}

  


for i in range(len(lista)):
  aux={"Nombre":"","Id":"","Email":"","Edad":""}
  claves=list(aux.keys())
  for j in range(4):
    aux[claves[j]] = lista[i][j]
  diccionario["Persona"+str(i)]=aux


#VARIABLE IMPORTANTE
#print(diccionario)

json_string = json.dumps(diccionario)
json_cargado = json.loads(json_string)

for t in json_cargado:
  json_cargado[t]["Edad"] = len(json_cargado[t]["Email"])
  del(json_cargado[t]["Email"])
print("\n\n")

#VARIABLE IMPORTANTE
#print(json_cargado)


json_cargado_final = json.dumps(json_cargado)

with open("CreartxtConInfoJSON.txt","w") as f:
  f.write(json_cargado_final)

print(json_cargado)

with open("createJsonFile.json","w")as p:
  json.dump(json_cargado_final,p,indent = 2)