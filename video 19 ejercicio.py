import sys


class CuentaCorriente:
    NumeroCuenta = ""
    titular = ""
    saldo = 0

    def __init__(self, titular, NumeroCuenta):
        self.titular = titular
        self.NumeroCuenta = NumeroCuenta

    def depositar(self, deposito):
        try:
            self.saldo = self.saldo + deposito
        except:
            print("Ha ocurrido un error vuelve a intentar")

    def retirar(self, retiro):
        try:
            self.saldo = self.saldo - retiro
        except:
            print("Ha ocurrido un error vuelve a intentarlo")

    def getDatos(self):
        return "Tus datos son, titular: " + self.titular + " numero de cuenta: " + self.NumeroCuenta + " saldo: " + str(self.saldo)


print("Bienvenido al banco de gemas! ")

titular = input("introduce tu nombre de titular: ")
NumeroCuenta = input("indica tu numero de cuenta: ")
cliente = CuentaCorriente(titular, NumeroCuenta)


def funciones():
    print("Que operacion deseas hacer. ")
    print("1.-Consultar datos de cuenta.")
    print("2.- Depositar Gemas")
    print("3.- Retirar Gemas")
    print("4.- Salir del programa")

    opciones = {1: "Consultar datos de cuenta",
                2: "Depositar Gemas", 3: "Retirar Gemas", 4: "Salir del programa"}
    
    opcion = int(input("Digite la opcion: "))
    while opcion not in opciones:
        opcion = int(input("Digite la opcion: "))

    print("\n")

    print("Escogiste la opcion de: " + opciones[opcion])

    if opcion == 1:
        print(cliente.getDatos())
        funciones()
    elif opcion == 2:
        deposito = int(
            input("Introduce el numero de gemas que deseas depositar: "))
        cliente.depositar(deposito)
        funciones()
    elif opcion == 3:
        retiro = int(input("Introduce el numero de gemas que deseas retirar"))
        cliente.retirar(retiro)
        funciones()
    else:
        print("Gracias por usar el banco de gemas!")
        sys.exit()


funciones()
