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


class CuentaJoven(CuentaCorriente):
    def __init__(self, titular, NumeroCuenta, bonus_promocion):
        super().__init__(titular, NumeroCuenta)
        self.bonus_promocion = bonus_promocion
        self.saldo = self.saldo + bonus_promocion

    def getBonus(self):

        return "El bonus es: " + str(self.bonus_promocion)

    def getDatos(self):
        return super().getDatos() + " bonus promocion: " + str(self.bonus_promocion)


print("Bienvenido al banco de gemas! ")

titular = input("introduce tu nombre de titular: ")
NumeroCuenta = input("indica tu numero de cuenta: ")
BonusPromocion = int(input("introduce el bonus de promocion : "))
cliente = CuentaJoven(titular, NumeroCuenta, BonusPromocion)


def funciones():
    print("Que operacion deseas hacer. ")
    print("1.-Consultar datos de cuenta.")
    print("2.- Consultar bonus")
    print("3.- Depositar Gemas")
    print("4.- Retirar Gemas")
    print("5.- Salir del programa")

    opciones = {1: "Consultar datos de cuenta", 2: "Consultar bonus",
                3: "Depositar Gemas", 4: "Retirar Gemas", 5: "Salir del programa"}

    opcion = int(input("Digite la opcion: "))
    while opcion not in opciones:
        opcion = int(input("Digite la opcion: "))

    print("\n")

    print("Escogiste la opcion de: " + opciones[opcion])

    if opcion == 1:
        print(cliente.getDatos())
        funciones()
    elif opcion == 2:
        print(cliente.getBonus())
        funciones()
    elif opcion == 3:
        deposito = int(
            input("Introduce el numero de gemas que deseas depositar: "))
        cliente.depositar(deposito)
        funciones()
    elif opcion == 4:
        retiro = int(input("Introduce el numero de gemas que deseas retirar"))
        cliente.retirar(retiro)
        funciones()
    else:
        print("Gracias por usar el banco de gemas!")
        sys.exit()


funciones()
