print("bienvenido al programa de retribucion impositiva ")

print("\n")

renta= float(input("Introduce tu numero de renta para calcular el  valor impositvo: "))

print("\n")
def calcula_impositivo(renta):
  if renta<12000:
    return "tu renta de " +str(renta) + " corresponde el impositivo de 7%"
  elif renta >= 12000 and renta <18000: 
    return "tu renta de " +str(renta) + " corresponde el impositivo de 15%"
  elif renta >= 18000 and renta <35000:
     return "tu renta de " +str(renta) + " corresponde el impositivo de 21%"
  elif renta >=35000 and renta < 70000:
     return "tu renta de " +str(renta) + " corresponde el impositivo de 35%"
  else:
     return "tu renta de " +str(renta) + " corresponde el impositivo de 45%"


print(calcula_impositivo(renta))

print("\n")


print("fin del programa")
