from tkinter import *

root = Tk()

class Calculadora:
  
  def __init__(self,ventana) -> None:
    self.ventana = ventana
    self.ventana.title("Calculadora POO")
    
    self.operacion = ""
    
    #agregar display
    self.display = Entry(ventana,justify="right",background="black",fg="#42C920",width=25,font=("Arial 15"))
  
    #ubicar display
    self.display.grid(row=1,column=0,columnspan=4,pady=10)

    #creacion de botones
    
    boton_7 = self.colocar_boton(7)  
    boton_8 = self.colocar_boton(8)  
    boton_9 = self.colocar_boton(9)  
    boton_div = self.colocar_boton("/")  
    
    #----------------------------------------------------
    
    boton_4 = self.colocar_boton(4)  
    boton_5 = self.colocar_boton(5)  
    boton_6 = self.colocar_boton(6)  
    boton_x = self.colocar_boton("*")
    boton_x.config(text="X")  
    
    #----------------------------------------------------
    
    boton_1 = self.colocar_boton(1)  
    boton_2 = self.colocar_boton(2)  
    boton_3 = self.colocar_boton(3)  
    
    #---------------------------------------------------
    boton_0 = self.colocar_boton(0)
    boton_resta = self.colocar_boton("-")  
    boton_suma = self.colocar_boton("+")  
    boton_igual = self.colocar_boton("=", mostrar = False)  
    boton_coma = self.colocar_boton(".") 
    
    #------------------------------------------------------
    
    botones = [boton_7,boton_8,boton_9,boton_div,boton_4,boton_5,boton_6,boton_x,boton_1,boton_2,boton_3,boton_0
    ,boton_resta,boton_suma,boton_igual,boton_coma]
    contador =0
    
    for fila in range(2,6):
      for columna in range(4):
        
       
  
        botones[contador].grid(row=fila,column = columna)
        contador +=1
        
  def colocar_boton(self,arg,mostrar =True,ancho = 9, alto = 1):
      return Button(self.ventana, text=arg,activebackground="grey", width=ancho, height=alto, command=lambda: self.pulsaciones_teclas(arg,mostrar))
  
  def pulsaciones_teclas(self,arg,mostrar):
      if mostrar:
        self.operacion += str(arg)
        self.mostrar_pantalla(arg)
      elif  not mostrar and arg == "=":
        self.borrar_pantalla()
        self.mostrar_pantalla(str(eval(self.operacion)))
      else:
        pass
  def mostrar_pantalla(self,arg):
    self.display.insert(END,arg)
    
  def borrar_pantalla(self):
    self.display.delete(first=0,last=END)
mi_calculadora = Calculadora(root)

root.mainloop()