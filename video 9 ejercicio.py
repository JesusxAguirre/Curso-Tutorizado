# importando libreria de numero aleatorio
import random

# creando numero aleatorio
numero_aleatorio = random.randint(1, 100)

# inicializando contador para guardar el numero de intentos
contador = 1

# variable booleana para el bucle while
verdadero = False

while verdadero == False:
    usuario_numero = int(input("Introduce el numero que deseas intentar adivinar, recuerda que es del 1 al 100:  "))
    print("\n")
    if usuario_numero > numero_aleatorio:
        print("el numero es mayor siguie intentando!")
        print("\n")
        contador = contador + 1
    elif usuario_numero < numero_aleatorio:
        print("El numero es menor que el numero aleatorio, sigue intentando")
        print("\n")
        contador = contador + 1
    else:
        verdadero = True

print("Bien hecho has adivinado el numero. utilizaste : " +str(contador)+ " intentos")
