from tkinter import *

raiz = Tk()

raiz.title("Segundo programa con Tkinter")

raiz.geometry("700x400")

raiz.config(bg="White")

iframe= Frame()

iframe.pack()

label = Label(iframe,text="Estamos en el mes de Noviembre",bg="blue",fg="white",font=("Courier",20))

logo = PhotoImage(file="Examen de modelado.png")

imagen = Label(iframe,image=logo)

imagen.pack()

label.pack()


raiz.mainloop()