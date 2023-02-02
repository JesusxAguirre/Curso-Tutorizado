import random

class MasterMind():
  
  def __init__(self,longitud_cadena) -> None:
    self.longitud_cadena = longitud_cadena
    self.secuencia_numeros = []
    for i in range(longitud_cadena):
      self.secuencia_numeros.append(random.randint(1,9))
  
  def compara_secuencia(self):
    contador=0
    posicion_lista= -1
    adivina =input("intenta adivinar la cadena->")
    while adivina != self.secuencia_numeros: 
      print(self.secuencia_numeros)
      adivina =input("con {}  has adivinado {} valores. intenta adivinar la cadena->".format(adivina,contador))
      
      contador=0
      posicion_lista= -1
      adivina = [int(i) for i in adivina]
      
      for i in adivina:
        posicion_lista+=1
        if i == self.secuencia_numeros[posicion_lista]:
          contador+=1
      
    print("con {} has adivinado {}, Felicidades has adivinado todos los valores!".format(adivina,contador))


objeto_juego = MasterMind(int(input("Por favor indica la longitud de la cadena de numeros -> ")))

objeto_juego.compara_secuencia()