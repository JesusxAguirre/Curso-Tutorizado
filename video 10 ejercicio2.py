#imprimiendo todos los numeros primos comprendidos entre dos numeros

print("Bienvenido al programa de imprimir numeros primos")

print("\n")

primer_numero=int(input("Digite un primer numero del rango de numeros: "))

print("\n")
segundo_numero=int(input("Digite un segundo numero del rango de numeros: "))

def numeros_primos(numero):
  for n in range(2,numero):
    if numero % n == 0:
      return False
  print(str(numero) + "es primo")
  return True    



for i in range(primer_numero,segundo_numero):
  numeros_primos(i)