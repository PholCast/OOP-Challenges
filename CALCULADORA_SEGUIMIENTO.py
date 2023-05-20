from dataclasses import dataclass

#exceptions
#es un 
#guardar un str en una lista 

#exception de terminos 
#que falten los operandos
#que falte el operador 
#faltan llos espacios


#




class DivisionPorCero(Exception):
  pass

class ErrorOperadores(Exception):
  pass

class ErrorNumeros(Exception):
  pass

class ErrorTamano(Exception):
  pass

@dataclass
class Calculadora:
  operadores=["+","-","*","/"]

  def calcular(self,operacion):
        expresion=operacion.split()
        print(expresion)
        print(operacion)
        
        if len(expresion)== 3:
             
            if expresion[0].isdigit() and expresion[2].isdigit():
              left = float(expresion[0])
              right= float(expresion[2])
              operador= expresion[1]
                
              if operador in self.operadores:
                if operador == "+":
                    result= left + right
                    print(result)

                elif operador == "-":
                    result= left - right
                    print(result)

                elif operador == "*":
                    result= left * right
                    print(result)
                    
                elif operador == "/":
                    if(right==0):
                      raise DivisionPorCero("No se permite division por cero")
                    else:
                      result= left / right #Division por cero, espacios, que no sean numeros, que el operador no sea un operador
                      print(result)  
              else:
                raise ErrorOperadores(f"La operación ingresada no es valida: {expresion[1]} no es un operador")                  
            else:
              
              raise ErrorNumeros("Los valores ingresados no son numeros, ingresalos correctamente")
              
        else:
          lista = list(operacion)
          print(lista)
          if len(lista) == 3:
            if lista[0].isdigit() and lista[2].isdigit() and lista[1] in self.operadores:
              raise ErrorTamano("Deja un espacio entre los caracteres")
            
            elif (not lista[0].isdigit()) and lista[2].isdigit() and lista[1] in self.operadores:
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[0]}' no es un numero")
            
            elif lista[0].isdigit() and (not lista[2].isdigit()) and lista[1] in self.operadores:
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[2]}' no es un numero")
            
            elif lista[0].isdigit() and lista[2].isdigit() and (not lista[1] in self.operadores):
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[1]}' no es un operador")

            elif (not lista[0].isdigit()) and (not lista[2].isdigit()) and lista[1] in self.operadores:
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[0]}' y '{lista[2]}' no son numeros")

            elif (not lista[0].isdigit()) and lista[2].isdigit() and (not lista[1] in self.operadores):
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[0]}' no es un numero y '{lista[1]}' no es un operador")
            
            elif lista[0].isdigit() and (not lista[2].isdigit()) and (not lista[1] in self.operadores):
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas,'{lista[2]}' no es un numero y '{lista[1]}' no es un operador")
            
            else:
              raise ErrorTamano(f"Deja un espacio entre los caracteres, Ademas, '{lista[0]}' y '{lista[2]}' no son numeros y '{lista[1]}' no es un operador")
          
          else:
            raise ErrorTamano(f"Deja un espacio entre los numeros y el operador")
            


        



        


while (True):
  try:
    x = Calculadora()
    s=input("Ingresa una operacion: ")
    if s!="terminar":
      x.calcular(s)
      
    else:
      print("El programa ha finalizado")
      break
  except (ErrorTamano,ErrorNumeros,DivisionPorCero,ErrorOperadores) as e:
    print("ERROR:",str(e),"\n")

