from tkinter import *

from calculadoraModular.calculadoraModularMostrarPantalla import *

def pulsaciones_teclas(self,arg,mostrar):
  
  #impiendo spam de punto decimal
  if arg =="." and arg in self.display.get(): 
    return False
  if mostrar:
    self.operacion += str(arg)
    mostrar_pantalla(self,arg)
  elif  not mostrar and arg == "=":
    borrar_pantalla(self)
    mostrar_pantalla(self,str(eval(self.operacion)))
  else:
      pass

  

def condiciones_reglas(self,arg):
  global contador
  if str(arg) == "0":
    contador = contador + 1
    if contador > 1:
      borrar_pantalla(self)
      self.display.insert(0,0)
      return False

  
   #comprobando si se intentan un numero luego de poner un 0 
  if str(arg) != "0":
      if contador >0 :
        borrar_pantalla(self)
        self.display.insert(0,arg)
        contador = 0
        return False