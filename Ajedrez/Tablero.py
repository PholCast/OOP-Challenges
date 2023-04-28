from dataclasses import dataclass

@dataclass
class Tablero:
    fichas = ""
    tablero = []
    

    def crear_tablero(self):
        self.tablero = [[" " for i in range(8)] for i in range(8)]

    def mostrar_tablero(self):
        for row in self.tablero:
            print(row)
    
    def llenar_tablero(self,lista_negra,lista_blanca):
        for i in range(16):
            self.tablero[lista_negra[i].posicion["fila"]][lista_negra[i].posicion["columna"]] = lista_negra[i]
        for j in range(16):
            self.tablero[lista_blanca[j].posicion["fila"]][lista_negra[j].posicion["columna"]] = lista_blanca[j]




tablero = Tablero()

