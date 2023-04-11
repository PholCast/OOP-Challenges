from tqdm import tqdm
from time import sleep
from dataclasses import dataclass

@dataclass
class Subchef:
    nombre:str
    

    def verificar_orden(self,plato,despensa,ingredientes_plato):
        verificar = True
        
        for i in range(len(plato.ingredientes)):
            if plato.ingredientes[ingredientes_plato[i]]<= despensa[ingredientes_plato[i]]:
                verificar = True
            else:
                verificar = False
                print("No hay suficiente",ingredientes_plato[i])
                break
        
        if(verificar):
            print("Hay suficientes ingredientes en la despensa para realizar el pedido...")
            return True
        else:
            return False


    def cocinar(self,plato,despensa):
        ingredientes_plato=list(plato.ingredientes.keys())
        cocinar_orden = self.verificar_orden(plato,despensa,ingredientes_plato)

        if cocinar_orden == True:
            for p in range(len(plato.ingredientes)):
                print(f"Tomando: {ingredientes_plato[p]}")
                despensa[ingredientes_plato[p]]-= plato.ingredientes[ingredientes_plato[p]]
            progreso = 100
            print("Cocinando...")
            for i in tqdm(range(progreso)): #Para crear la barra de carga mientras cocina
                sleep(0.1)

            self.entregar()


        else:
            print("Lo sentimos, no hay suficientes ingredientes, realiza otro pedido")
            #Luego hay que hacer que el cliente vuelva a hacer el pedido
    
    def entregar(self):
        print(f"El subchef {self.nombre} ha entregado el plato")
