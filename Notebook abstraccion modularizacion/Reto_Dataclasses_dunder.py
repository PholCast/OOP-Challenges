# Modele e implemente el siguiente escenario usando Dataclasses y Dunder methods:

# Un banco le ofrece la posibilidad a clientes de tener una cuenta.

# Cuando un cliente crea una cuenta debe proveer su id y nombre.

# No podrán haber clientes con id repetido.

# Los clientes pueden depositar o retirar dinero de sus cuentas una vez creadas.

# Un cliente le puede transferir dinero a otro cliente.

# El contador del banco puede ver el listado de clientes y lo puede organizar ascendente
# o descendentemente de acuerdo al saldo de cada cliente.

from dataclasses import dataclass


@dataclass
class Bank:
    __customers=[]


    def __repr__(self):
        order=input("Ingresa ascending para ver el listado en orden ascendente. Sino, pulsa cualquier tecla para verlo en orden descendente:  ")
        if order=="ascending":
            self.__customers.sort(key=lambda x: x.get_balance())
            cont=1
            for e in self.__customers:
                print("CLIENTE #",cont)
                print(e)
                cont+=1
                print(20*"-")
                
        
        else:
            self.__customers.sort(key=lambda x: x.get_balance(), reverse=True)
            cont=1
            for e in self.__customers:
                print("CLIENTE #",cont)
                print(e)
                cont+=1
                print(20*"-")
            
        return f"El banco tiene {len(self.__customers)} clientes"




    def get_customers(self):
        return self.__customers

    def add_customer(self,id:int, name:str):
        if(self.verify(id)):

            create_customer = Customer(id,name)

            print(f"El cliente {create_customer.get_name()}, con id {create_customer.get_id()} ha sido creado")

            self.__customers.append(create_customer)
        else:
            print("Error, el id proporcionado ya existe")
    
    def verify(self,id):
        #list comprehension, crea una lista con los id de los clientes que ya existen
        # para luego comparar si ya existe el id
        #Servirá en otros ejercicios para comprobar si en una lista de objetos, ya existe un atributo
        aux=[element.get_id() for element in self.__customers]
        
        if id in aux:
            return False
        else:
            return True
    def deposit_customer(self,id,money):
        index= self.search_customer(id)
        if index!=-1:
            self.__customers[index].deposit(money)
        else:
            print("No existe un cliente con el id proporcionado")

    def withDraw_customer(self,id,money):
        index=self.search_customer(id)
        if index!=-1:
            self.__customers[index].withDraw(money)
        else:
            print("No existe un cliente con el id proporcionado")

    def transfer(self,sender_id,receiver_id,money):
        index_sender_Id=self.search_customer(sender_id)
        index_receiver_Id=self.search_customer(receiver_id)
        
        if (index_receiver_Id != -1 and index_sender_Id!=-1 and self.__customers[index_sender_Id].get_balance()>=money):
            self.__customers[index_sender_Id].withDraw(money)

            print(f"{self.__customers[index_sender_Id].get_name()} has transferido ${money} a {self.__customers[index_receiver_Id].get_name()} ")
            self.__customers[index_receiver_Id].deposit(money)
        else:
            print("Proporciona los id correctamente")

            

    def search_customer(self,id):
        index=-1
        aux=[element.get_id() for element in self.__customers]

        index= aux.index(id)

        return index


        


@dataclass
class Customer:
    __id : int
    __name : str
    __balance:float =0.0


    def __repr__(self):
        return f"Nombre: {self.__name}\nid: {self.__id}\nSaldo: ${self.__balance}"
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self,money):
        if type(money)==float or type(money)==int:
            self.__balance+=money
            print(f"{self.__name }, Se han depositado ${money} a su cuenta")
            print(f"Su saldo actual es: ${self.get_balance()}")
            
        else:
            print("¡ALERTA!, Ingresa un valor numerico a depositar")

    def withDraw(self,money):
        if type(money)==float or type(money)==int and money<=self.__balance:
            self.__balance-=money
            print(f"{self.__name }, Se han retirado ${money} de su cuenta")
            print(f"Su saldo actual es: ${self.get_balance()}")
            
            
        elif type(money)==float or type(money)==int and money>self.__balance:
            print(f"¡ALERTA!, tienes ${self.__balance} no puedes retirar ${money}")
            
        else:
            print("¡ALERTA!, Ingresa un valor numerico a depositar")
            

#Creando el banco
bank= Bank()

#Probando el metodo para añadir clientes al banco
bank.add_customer(125,"Phol")
bank.add_customer(127,"Neithan")


#Probando el metodo para depositar dinero
bank.deposit_customer(125,50000)
bank.deposit_customer(125,70000)

#Metodo retirar dinero
bank.withDraw_customer(125,30000)

print("\n\n\n")
#Metodo de transferir dinero
bank.transfer(125,127,20000)

#Ver el listado de clientes
print(bank)