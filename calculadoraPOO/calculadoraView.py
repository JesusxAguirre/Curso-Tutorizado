from tkinter import *
from moduloMatematico.calculosBasicos.funciones_matematica import *
root =Tk()

root.geometry("310x475")
root.title("Calculadora")

iframe= Frame(root,width=1000,height=550)

iframe.pack()

digitos_numerico= StringVar()
digitos_numerico.set("0")

#variables globales
operacion = []
resultado = 0
operaciones_continuas =0
variable = 0
#declarando display
display = Entry(iframe,justify="right",textvariable=digitos_numerico,background="black",fg="#42C920",width=22,font="Aril 22")
display.grid(row=1,column=1,columnspan=4,pady=10)

#botones

#------------ verificar resultaddo decimal ------------#

def verificar_decimal():
  global resultado
  
  if resultado.is_integer():
    
    digitos_numerico.set(int(resultado))
  else:
    digitos_numerico.set(resultado)
    



#------------ pulsaciones numerios -----------------#

def pulsaciones_teclas(arg):
  
  global variable
 
  #impidiendo ceros a la izquierda
  if arg == "0" and digitos_numerico.get() == "0":
    digitos_numerico.set("0")
    return False
  
  #impiendo spam de punto decimal
  if arg =="." and arg in digitos_numerico.get():
    return False
  
  #concatenando los numeros digitados
  if variable == 0:
    
    #comprobando si se intenta introducir un numero decimal
    if arg == "." and digitos_numerico.get() == "0":
      digitos_numerico.set(digitos_numerico.get() + arg)
      
    #comprobando si se intentan un numero luego de poner un 0 
    elif arg != "0" and digitos_numerico.get() == "0":
      digitos_numerico.set(arg)
     
    else:
      digitos_numerico.set(digitos_numerico.get() + arg)
    
  else:
    digitos_numerico.set(arg)
    variable = 0
#----------- funcion de operaciones ---------------#
def operaciones(signo):
  #definiendo una variable global para crear una lista y usarla en dos funciones
  global operacion 
  global operaciones_continuas
  global resultado
  

  #sumando las operaciones que se van haciendo
  operaciones_continuas += 1
  
  
  #comprobando el numero de operaciones continuas y se ejecuta una funcion
  if operaciones_continuas == 2:
      obtener_resultado()
      operacion.append(resultado)
      operacion.append(signo)
      operaciones_continuas =1 
      return True
    
  #colocando en una lista los datos ingresados a la calculadora
  operacion.append(digitos_numerico.get())
  operacion.append(signo)
  
    


  digitos_numerico.set("")
  
#------------ funcion de operaciones matematicas -----#
def obtener_resultado():
  global operacion
  global resultado
  global operaciones_continuas
  global variable
  
  
  num1 = float(operacion[0])
  num2 = float(digitos_numerico.get())
  



  if operacion[1] == "+":
    resultado = num1 + num2
    verificar_decimal()
  elif operacion[1] == "X":
    resultado = num1 * num2
    verificar_decimal()
  elif operacion[1] == "-":
    resultado = num1 - num2
    verificar_decimal()
  else:
    resultado = num1 / num2
    verificar_decimal()
  operaciones_continuas =0
  variable =1 
  operacion.clear()

 
#-----------------------primera fila ---------------#

boton_1= Button(iframe,text="1",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("1"))
boton_1.grid(row=2,column=1)


boton_2= Button(iframe,text="2",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("2"))
boton_2.grid(row=2,column=2)

boton_3= Button(iframe,text="3",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("3"))
boton_3.grid(row=2,column=3)

#-----------------------Segunda fila ---------------#
boton_4= Button(iframe,text="4",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("4"))
boton_4.grid(row=3,column=1)

boton_5= Button(iframe,text="5",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("5"))
boton_5.grid(row=3,column=2)

boton_6= Button(iframe,text="6",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("6"))
boton_6.grid(row=3,column=3)


#-----------------------Tercera fila ---------------#
boton_7= Button(iframe,text="7",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("7"))
boton_7.grid(row=4,column=1)

boton_8= Button(iframe,text="8",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("8"))
boton_8.grid(row=4,column=2)

boton_9= Button(iframe,text="9",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("9"))
boton_9.grid(row=4,column=3 )

#---------------------Cuarta fila ---------------#
boton_0= Button(iframe,text="0",activebackground="grey",width=11,command=lambda : pulsaciones_teclas("0"))
boton_0.grid(row=5,column=2)


#-----------------------Botones de operacion ---------------#

boton_decimal = Button(iframe,text=",",activebackground="grey",width=11,command= lambda: pulsaciones_teclas("."))
boton_decimal.grid(row=5,column=1)

boton_division= Button(iframe,text="/",activebackground="grey",width=11,command= lambda: operaciones("/"))
boton_division.grid(row=2,column=4)


boton_multiplicacion= Button(iframe,text="X",activebackground="grey",width=11,command= lambda: operaciones("X"))
boton_multiplicacion.grid(row=3,column=4)


boton_resta= Button(iframe,text="-",activebackground="grey",width=11,command= lambda: operaciones("-"))
boton_resta.grid(row=4,column=4)

boton_suma= Button(iframe,text="+",activebackground="grey",width=11,command= lambda: operaciones("+"))
boton_suma.grid(row=5,column=4)





boton_resultado= Button(iframe,text="=",activebackground="grey",width=11,command=obtener_resultado)
boton_resultado.grid(row=5,column=3)

#fin del programa
root.mainloop()