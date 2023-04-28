from dataclasses import dataclass

#exceptions
#es un 
#guardar un str en una lista 

#exception de terminos 
#que falten los operandos
#que falte el operador 
#faltan llos espacios


#

class ErrorTerminos(Exception):
    pass

class DivisionCero(Exception):
    pass

class ErrorNum(Exception):
    pass


@dataclass
class Calculadora:
    op= input("Ingrese la operación que desea realizar: ")
    operadores=["+","-","*","/"]
    
    def calcular(self):
        expresion= self.op.split()
        print(self.op)

        
        if len(expresion)== 3:
            try:
                if expresion[0].isdigit() and expresion[2].isdigit():
                    operator= expresion[1]
                    opdL= float(expresion[0])
                    opdR= float(expresion[2])
                    
                
                    try:
                        if operator in self.operadores:
                            if operator == "+":
                                result= opdL + opdR
                                print(result)

                            elif operator == "-":
                                result= opdL - opdR
                                print(result)
                            
                            elif operator == "*":
                                result= opdL * opdR
                                print(result)

                            try:
                                if operator == "/":
                                    if opdR== 0:
                                        raise DivisionCero("Eso está malo mona, eso no se puede hacer")
                                    else:
                                        result= opdL/ opdR
                                        print(result) 
                            except DivisionCero:
                                raise DivisionCero("graveeeeee")
                        else:
                            print("m")   
                    except ErrorTerminos:
                        raise ErrorTerminos("Eso así no sirve")
                else:
                    print("SAPA")
            except:
                raise ErrorNum("eso está malooooooooo")
                
    

x= Calculadora()
x.calcular()