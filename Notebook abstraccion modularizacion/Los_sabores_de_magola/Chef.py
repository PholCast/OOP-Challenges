from dataclasses import dataclass
from Despensa import despensa
@dataclass
class Chef:
    nombre:str


    def verificar_orden(self,plato,despensa):
        verificar = True
        ingredientes_plato=list(plato.ingredientes.keys())
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

        
        


    def cocinar(self):
