# estructurade control de while
import math
print("==========Bienveido al progra de de calcular la raiz==========")
intentos = 1
numero = int(input("Introduce un numero positivo: "))

while numero <= 0:
    
    numero = int(input("Introduce un numero positivo: "))

    intentos = intentos + 1
    
    if intentos == 5:
        break


if intentos ==5:
    print("lo siento no tienes acceso al programa")
else:
    print(math.isqrt(numero))
print("Finalizado el programa")
