#generadores

#funcion tradicional primero y luego generador

def generar_pares(limite):
  num = 1

  numeros_pares=[]

  while num < limite:
    numeros_pares.append(num*2)

    num = num + 1 
  
  return numeros_pares

#funcion generador
def generar_pares2(limite):
  num = 1

  while num < limite:
    yield num *2

    num = num + 1



sucesion_pares = generar_pares2(6)

for i in sucesion_pares:
  print(i)