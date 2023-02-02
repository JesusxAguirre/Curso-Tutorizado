from tkinter import *

raiz = Tk()

raiz.title("Primer Programa Tkinter")

raiz.iconbitmap("prueba.ico")

raiz.geometry("700x400")

raiz.config(bg="Green")

iframe = Frame()

#iframe.pack(side="right",anchor="n")

iframe.pack(fill="x")


iframe.config(bg="red")

iframe.config(width="650",height="350")
       
#ultima instruccion
raiz.mainloop()

