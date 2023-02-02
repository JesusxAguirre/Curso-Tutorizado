class Vehiculo():
    color = ""
    ruedas = ""
    ancho = ""
    alto = ""
    velocidades = ""
    asientos = ""

    def acelerar(self):

        return "Este vehiculo esta acelerando"

    def frenar(self):

        return "Este vehiculo esta Frenando"

    def derrapar(self):

        return "Este vehiculo esta Derrapando"

    def girar(self):

        return "Este vehiculo esta girando"


class Bicicleta(Vehiculo):

    def __init__(self):
        super().__init__()

        self.color = "azul y plateado"
        self.ruedas = 2
        self.ancho = "30 mm"
        self.alto = "170 cm"
        self.velocidades = 7
        self.asientos = 1

class Moto(Bicicleta):

  def __init__(self):
      self.cilindrada = 4


class Coche(Vehiculo):

  def retroceso(self):
    return "Este vehiculo esta dando marcha atras"

  def arrancar(self):
    return "Este vehiculo esta arrancando"