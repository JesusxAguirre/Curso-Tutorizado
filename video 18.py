#comenzando Programacion orientada a objetos

class Coche():
  ruedas=4
  largoChasis=260
  anchoChasis=130 
  arrancado=False

  def arrancar(self):
    self.arrancado = True

  def estadoCoche(self):
    if self.arrancado:
      return "El choce esta funcionando"
    else:
      return "El coche no esta funcionando"    


mazda = Coche() #instacia de clase
ford = Coche()

print(mazda.ruedas)

mazda.arrancar()

print(mazda.estadoCoche())