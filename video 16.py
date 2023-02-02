#manejo de execiones

def division():
  try:
    num1=float(input("Introduce un primer valor numerico: "))
    num2=float(input("Introduce un segundo valor numerico:  "))

    print("El resultado es: " + str(num1/num2))
  except:
    print("Ha ocurrido un error")

division()

print("Calculo finalizado ha terminado el programa")