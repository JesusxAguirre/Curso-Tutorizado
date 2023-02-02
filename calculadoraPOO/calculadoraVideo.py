from tkinter import *
from moduloMatematico.calculosBasicos.funciones_matematica import *


#variables globales
contador =0
root =Tk()

root.geometry("310x475")
root.title("Calculadora")

iframe= Frame(root,width=1000,height=550)

iframe.pack()

#variables globales
operacion = ""
resultado = 0
coma = False
digitos_numerico= StringVar()
digitos_numerico.set("0")



#declarando display
display = Entry(iframe,justify="right",textvariable=digitos_numerico,background="black",fg="#42C920",width=22,font="Aril 22")
display.grid(row=1,column=1,columnspan=4,pady=10)


#------------- funcion alternativa para la coma ----------#

def pulsacion_coma():
  
  contador = 0
  
  for i in digitos_numerico.get():
    if i == ".":
      contador+=1
  
  if contador == 0 :
    digitos_numerico.set(digitos_numerico.get() + ".")
  
#------------ pulsaciones numerios -----------------#

def pulsaciones_teclas(arg):
  
  global operacion
  global coma
  if operacion != "":
    
    digitos_numerico.set(arg)
    
    operacion = ""
  
  else:
    #impidiendo ceros a la izquierda
    if arg == "0" and digitos_numerico.get() == "0":
      digitos_numerico.set("0")
    #concatenando cero con punto , es decir creando un numero decimal
    elif arg == "." and digitos_numerico.get() == "0":
      digitos_numerico.set(digitos_numerico.get() + arg)
      coma = True
    #eliminando cero inicial cuando se intenta colocar una cifra que no sea decimal
    elif arg != "0" and digitos_numerico.get() == "0":
      digitos_numerico.set(arg)
    else:

        digitos_numerico.set(digitos_numerico.get() + arg)
  
  
#----------- funcion de operaciones ---------------#
def suma(num):
  global operacion
  global resultado
  operacion = "suma"
  
  resultado += float(num)
  
  if resultado.is_integer():
    digitos_numerico.set(int(resultado))
  else:
    digitos_numerico.set(resultado)
  
  #definiendo una variable global para crear una lista y usarla en dos funciones

#------------ funcion de operaciones matematicas -----#
def obtener_resultado():
  global resultado
  
  if (resultado + float(digitos_numerico.get())).is_integer():
    digitos_numerico.set(int(resultado + float(digitos_numerico.get())))
  else:
    digitos_numerico.set(resultado + float(digitos_numerico.get()))
    
  resultado = 0
  
 
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

boton_decimal = Button(iframe,text=",",activebackground="grey",width=11,command= lambda: pulsacion_coma())
boton_decimal.grid(row=5,column=1)

boton_division= Button(iframe,text="/",activebackground="grey",width=11)
boton_division.grid(row=2,column=4)


boton_multiplicacion= Button(iframe,text="X",activebackground="grey",width=11)
boton_multiplicacion.grid(row=3,column=4)


boton_resta= Button(iframe,text="-",activebackground="grey",width=11)
boton_resta.grid(row=4,column=4)

boton_suma= Button(iframe,text="+",activebackground="grey",width=11,command= lambda: suma(digitos_numerico.get()))
boton_suma.grid(row=5,column=4)





boton_resultado= Button(iframe,text="=",activebackground="grey",width=11,command= lambda: obtener_resultado())
boton_resultado.grid(row=5,column=3)

#fin del programa
root.mainloop()