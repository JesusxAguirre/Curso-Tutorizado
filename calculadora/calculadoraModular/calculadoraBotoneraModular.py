from tkinter import *

from calculadoraModular.calculadoraModularPulsaciones import *

def construir_botones(self,botones,filas_botones):
  contador = 0
  for fila in range(2, filas_botones+2 ):  
    for columna in range(4):
      botones[contador].grid(row=fila, column=columna)
      contador += 1

def colocar_boton(self,arg,mostrar =True,ancho = 9, alto = 1):
  return Button(self.ventana, text=arg,activebackground="grey", width=ancho, height=alto, command=lambda: pulsaciones_teclas(self,arg,mostrar))