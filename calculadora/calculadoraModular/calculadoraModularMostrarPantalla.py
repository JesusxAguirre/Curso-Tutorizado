from tkinter import * 
def mostrar_pantalla(self,arg):
    self.display.insert(END,arg)
    
def borrar_pantalla(self):
  self.display.delete(first=0,last=END)