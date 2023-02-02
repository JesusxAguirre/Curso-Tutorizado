# condicional elif

a = "10"
b = "10"

print(int(a)+int(b))



print("/n")

print("Programa de comprobacion de numero positivo negativo o neutro")


A = int(input("Introduce un numero para comprobar si es un numero real"))


def numero_real(A):
    if A < 0:
        return str(A) + " Es negativo"
    elif A == 0:
        return str(A) + " Es numero neutro"
    else:
        return str(A) + " Es positivio"

print(numero_real(A))