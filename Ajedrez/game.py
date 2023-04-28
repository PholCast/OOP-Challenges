

from iconos import diccionario_iconos
from Tablero import Tablero
from Ficha import Ficha,Peon,Torre,Caballo,Alfil,Reina,Rey
import unicodedata

#Creamos el tablero
board = Tablero()

board.crear_tablero()
#board.mostrar_tablero()

#Lista de fichas por su color

fichas_negras = []
fichas_blancas = []
def peones(lista_negra, lista_blanca,diccionario):
    
    for i in range(8):
        peon_negro=Peon("Negro",{"fila":1,"columna":i},diccionario)
        lista_negra.append(peon_negro)
    for j in range(8):
       peon_blanco=Peon("Blanco",{"fila":6,"columna":j},diccionario)
       lista_blanca.append(peon_blanco) 
    

def caballos(lista_negra,lista_blanca,diccionario):
    posiciones_caballos=[1,6]
    for i in range(2):
        caballo_negro = Caballo("Negro",{"fila":0,"columna":posiciones_caballos[i]},diccionario)
        lista_negra.append(caballo_negro)
    for j in range(2):
        caballo_blanco = Caballo("Blanco",{"fila":7,"columna":posiciones_caballos[j]},diccionario)
        lista_blanca.append(caballo_blanco)

def torres(lista_negra,lista_blanca,diccionario):
    posiciones_torres=[0,7]
    for i in range(2):
        torre_negra = Torre("Negro",{"fila":0,"columna":posiciones_torres[i]},diccionario)
        lista_negra.append(torre_negra)
    for j in range(2):
        torre_blanca= Torre("Blanco",{"fila":7,"columna":posiciones_torres[j]},diccionario)
        lista_blanca.append(torre_blanca)

def alfiles(lista_negra,lista_blanca,diccionario):
    posiciones_alfiles = [2,5]
    for i in range(2):
        alfil_negro = Alfil("Negro",{"fila":0,"columna":posiciones_alfiles[i]},diccionario)
        lista_negra.append(alfil_negro)
    for j in range(2):
        alfil_blanco = Alfil("Blanco",{"fila":7,"columna":posiciones_alfiles[j]},diccionario)
        lista_blanca.append(alfil_blanco)



peones(fichas_negras,fichas_blancas,diccionario_iconos)
caballos(fichas_negras,fichas_blancas,diccionario_iconos)
torres(fichas_negras,fichas_blancas,diccionario_iconos)
alfiles(fichas_negras,fichas_blancas,diccionario_iconos)

reina_negra = Reina("Negro",{"fila":0,"columna":3},diccionario_iconos)
reina_blanca = Reina("Blanco",{"fila":7,"columna":3},diccionario_iconos)

rey_negro = Rey("Negro",{"fila":0,"columna":4},diccionario_iconos)
rey_blanco = Rey("Blanco",{"fila":7,"columna":4},diccionario_iconos)

fichas_blancas.append(reina_blanca)
fichas_blancas.append(rey_blanco)

fichas_negras.append(reina_negra)
fichas_negras.append(rey_negro)

#print(fichas_negras,"\n\n",fichas_blancas)


board.llenar_tablero(fichas_negras,fichas_blancas)
board.mostrar_tablero()