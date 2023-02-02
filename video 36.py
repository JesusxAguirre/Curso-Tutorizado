from tkinter import *
from tkinter import messagebox as msg
raiz = Tk()

raiz.title("3er video con Tkinter")

iframe = Frame(raiz,width=1000,height=550)

iframe.pack()


Nombre = StringVar()
Apellido = StringVar()
Correo = StringVar()
Direccion = StringVar()

#declarando los widgets
  #labels
labelNombre = Label(iframe,text="Nombre: ",pady=10)
labelApellido = Label(iframe,text="Apellido: ",pady=10)
labelCorreo = Label(iframe,text="Correo: ",pady=10)
labelDireccion = Label(iframe,text="Direccion: ",pady=10)
labelComentario = Label(iframe,text="Comentarios: ")
  #entrys
textoNombre = Entry(iframe,textvariable=Nombre)
textoApellido = Entry(iframe,show="*",textvariable=Apellido)
textoCorreo = Entry(iframe,textvariable=Correo)
textoDireccion = Entry(iframe,textvariable=Direccion)

  #text
texto_opiniones = Text(iframe,width=10,height=4)  
  #boton
def funcionBoton():
  
  msg.showinfo("Saludo", Nombre.get() + " "+ Apellido.get()+ " "  +  Correo.get())
  #miVariable.set("Jesus")
botonEnviar = Button(raiz,text="Enviar",command=(funcionBoton))



#scrollbar
miscrollvertical=Scrollbar(iframe,command=texto_opiniones.yview)

#posicionando widgets
labelNombre.grid(row=0,column=0,sticky="e")
textoNombre.grid(row=0,column=1)
textoCorreo.config(fg="red")
labelApellido.grid(row=1,column=0,sticky="e")
textoApellido.grid(row=1,column=1)
labelCorreo.grid(row=2,column=0,sticky="e")
textoCorreo.grid(row=2,column=1)
labelDireccion.grid(row=3,column=0,sticky="e")
textoDireccion.grid(row=3,column=1)
botonEnviar.pack()
#comentario posicion
labelComentario.grid(row=4,column=0)
texto_opiniones.grid(row=4,column=1, pady=10)
miscrollvertical.grid(row=4,column=2,sticky="nsew")
raiz.mainloop()