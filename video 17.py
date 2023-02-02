#manejo de execpciones

import math

def calcular_raiz(numero):
  if numero < 0:
    
    raise ValueError ("El numero no puede ser negativo")
  else:
    return math.sqrt(numero)


numero = int(input("Introduce un numero: "))

try:

  print(calcular_raiz(numero))
except:
  print("Ha ocurrido un error")
  
print("Sigue el flujo de ejecucion")