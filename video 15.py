#manejo de exepciones
import sys
contador = 0

def suma(num1,num2):
  return num1+num2

def resta(num1,num2):
  return num1-num2

def multiplicacion(num1,num2):
  return num1*num2

def division(num1,num2):
  try:
    return num1/num2
  except ZeroDivisionError:
    print("No se puede dividir entre 0")
    return "Operacion fallida"


while contador < 3:
  try:
    num1 = int(input("Introduce un primer numero: "))
    num2 = int(input("Introduce un segundo numero numero: "))

    break
  except ValueError:
    contador = contador + 1
    print("No se pueden  colocar datos no numericos") 
    if contador == 3:

      print("Has hecho mas de 3 intentos el programa terminara")
      sys.exit()
  
opcion = input("escribe la operacion matematica que deseas en minisculas ('suma','resta','multiplicacion','division':  ")

if opcion == "suma":
  print(suma(num1,num2))
elif opcion == "resta":
  print(resta(num1,num2))
elif opcion == "multiplicacion":
  print(multiplicacion(num1,num2))
elif opcion == "division":
  print(division(num1,num2))
else:
  print("operacion no contemplada")


print("Operacion ejectuada. flujo de ejecucion continua")