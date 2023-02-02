from tkinter import *

from calculadoraModular.calculadoraBotoneraModular import *
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

    #creacion de botones fila1
    
    boton_7 = colocar_boton(self,7)  
    boton_8 = colocar_boton(self,8)  
    boton_9 = colocar_boton(self,9)  
    boton_div = colocar_boton(self,"/")  
    
    #---------------------------------------------------- fila 2
    
    boton_4 = colocar_boton(self,4)  
    boton_5 = colocar_boton(self,5)  
    boton_6 = colocar_boton(self,6)  
    boton_x = colocar_boton(self,"*")
    boton_x.config(text="X")  
    
    #---------------------------------------------------- fila 3
    
    boton_1 = colocar_boton(self,1)  
    boton_2 = colocar_boton(self,2)  
    boton_3 = colocar_boton(self,3)  
    
    #--------------------------------------------------- fila 4
    boton_0 = colocar_boton(self,0)
    boton_resta = colocar_boton(self,"-")  
    boton_suma = colocar_boton(self,"+")  
    boton_igual = colocar_boton(self,"=", mostrar = False)  
    boton_coma = colocar_boton(self,".") 
    
    #------------------------------------------------------
    
    botones = [boton_7,boton_8,boton_9,boton_div,boton_4,boton_5,boton_6,boton_x,boton_1,boton_2,boton_3,boton_0
    ,boton_resta,boton_suma,boton_igual,boton_coma]
    
    construir_botones(self,botones,4)
    
mi_calculadora = Calculadora(root)

root.mainloop()