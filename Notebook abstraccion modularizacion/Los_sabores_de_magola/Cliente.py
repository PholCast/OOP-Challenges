from dataclasses import dataclass

@dataclass
class Cliente:
    nombre:str
    dinero:int

    def pedir(self,menu):
        lista_platos=menu.get_platos()
        booleano=True
        while(booleano):
            while(True):
                pedido=int(input("Ingresa el numero del plato que deseas pedir: "))
                if pedido>=1 and pedido<=len(lista_platos):
                    break
                else:
                    print("Ingresa un numero valido")
            if lista_platos[pedido-1].precio > self.dinero:
                print("NO TIENES FONDOS SUFICIENTES,pide otro plato")
            else:
                print("Haz hecho la orden ")
                self.pagar(lista_platos[pedido-1].precio)
                return lista_platos[pedido-1]
            
    def pedido(self,menu):
        
        return self.pedir(menu)

        
    
    def pagar(self,precio):
        self.dinero-=precio
        print(f"Haz pagado, ahora tienes ${self.dinero} pesos")


        

