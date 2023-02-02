#Cueva del gragon
import time
import random

class Juego_Dragon:

  def __init__(self) -> None:
    self.cueva = ""
    self.colores=["rojo","verde","amarillo","azul","negro","plateado","dorado","gris"]
    self.puntos = 0
    self.vivo = "si"
  
  def aumentar_puntos(self):
    self.puntos+=100
  
  def get_puntos(self):
    return "Tu puntuacion total es: {}".format(self.puntos)
  
  def introduccion(self):
    time.sleep(2)
    print ("Estamos en una tierra llena de dragones. Delante de ti,")
    time.sleep(2)
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    time.sleep(2)
    print ("y compartira el tesoro contigo. El otro dragon")
    time.sleep(2)
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    time.sleep(2)
    print("")
    self.decidir_cueva()
    
  def decidir_cueva(self):
    
    print("Debes de escoger una cueva")
    
    while self.cueva != "1" and self.cueva !="2":
      self.cueva = input("A cual cueva quieres entrar? 1 o 2? ->  ")

    self.entrando_cueva()
    
  def entrando_cueva(self):
      print("Te acercas lentamente a la cueva....")
      time.sleep(2)
      print("Hay poco iluminancion, te cuesta dicernir el camino, te vas sobrecogiendo")
      time.sleep(2)
      
      print("Un gran dragon {} sale ante ti, abre su boca y...".format(random.choice(self.colores)))
      print("")

      tesoro = random.randint(1,2)
      
      if str(tesoro) == self.cueva:
        
        print("Te ha entregado el tesoro!")
        time.sleep(4)
        self.aumentar_puntos()
        self.cueva = ""
        print("")
        self.introduccion()
      else:
        print("El dragon te come de un bocado...")
        print(self.get_puntos())
        self.cueva = ""
        print("")
        self.continuar_juego()
        
  def continuar_juego(self):
      self.vivo = input("Deseas continuar el juego? [Si] o [No]")
      
      if self.vivo.lower() == "si":
         self.introduccion()
      else:
        print("Gracias por jugar! Vuelva pronto! :)")
    
objeto_juego = Juego_Dragon()

objeto_juego.introduccion()
