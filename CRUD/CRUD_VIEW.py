from tkinter import *

from modulos_CRUD.clase_conexion import *
from modulos_CRUD.clase_validaciones import *
root = Tk()
menu_bar = Menu(root)
root.config(menu=menu_bar)


class Interfaz:

    def __init__(self, view) -> None:

        iframe = Frame(root, height=500, width=500)

        iframe.pack()

        iframe_botones = Frame(root)
        iframe_botones.pack()

        self.view = view
        self.view.title("Aplicacion con CRUD")

        self.Nombre = StringVar()
        self.Password = StringVar()
        self.Apellido = StringVar()
        self.Direccion = StringVar()
        self.ID = StringVar()
        # contruyendo los widgets

        # BDD Menu
        self.bd_menu = Menu(menu_bar, tearoff=0)
        self.bd_menu.add_command(
            label="Conectar", command=lambda: objeto_conexion.conectar_bd())
        self.bd_menu.add_command(
            label="Salir", command=lambda: objeto_conexion.salir())

        # Delete menu
        self.delete_menu = Menu(menu_bar, tearoff=0)
        self.delete_menu.add_command(
            label="Borrar campos", command=lambda: self.borrar_campos())

        # crud menu
        self.crud_menu = Menu(menu_bar, tearoff=0)
        self.crud_menu.add_command(label="Crear", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                           self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "CREATE"))
        self.crud_menu.add_command(label="Leer", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                          self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "READ"))
        self.crud_menu.add_command(label="Actualizar", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                                self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "UPDATE"))
        self.crud_menu.add_command(label="Eliminar", command=lambda: objeto_validaciones.validando_formulario(
            App, objeto_conexion, self.ID.get(), "DELETE"))

        # help menu

        self.help_menu = Menu(menu_bar, tearoff=0)
        self.help_menu.add_command(label="Licencia")
        self.help_menu.add_command(label="Acerca de")

        menu_bar.add_cascade(label="BBDD", menu=self.bd_menu)
        menu_bar.add_cascade(label="Borrar", menu=self.delete_menu)
        menu_bar.add_cascade(label="CRUD", menu=self.crud_menu)
        menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

        # labels
        # id
        self.label_id = Label(iframe, text="ID: ", pady=10)
        self.label_id.grid(row=0, column=0, padx=20)

        self.input_id = Entry(iframe, textvariable=self.ID)
        self.input_id.grid(row=0, column=1)
        # Nombre
        self.label_nombre = Label(iframe, text="Nombre: ", pady=10, )
        self.label_nombre.grid(row=1, column=0, padx=20)

        self.input_nombre = Entry(
            iframe, textvariable=self.Nombre, fg="Red", justify=['right'])
        self.input_nombre.grid(row=1, column=1)

        # password
        self.label_password = Label(iframe, text="Password: ", pady=10)
        self.label_password.grid(row=2, column=0)

        self.input_password = Entry(
            iframe, textvariable=self.Password, show="*", justify=['left'])
        self.input_password.grid(row=2, column=1)

        # apellido
        self.label_apellido = Label(iframe, text="Apellido: ", pady=10)
        self.label_apellido.grid(row=3, column=0)

        self.input_apellido = Entry(iframe, textvariable=self.Apellido)
        self.input_apellido.grid(row=3, column=1)

        # direccion
        self.label_direccion = Label(iframe, text="Direccion: ", pady=10)
        self.label_direccion.grid(row=4, column=0)

        self.input_direccion = Entry(iframe, textvariable=self.Direccion)
        self.input_direccion.grid(row=4, column=1)

        # comentario
        self.label_comentario = Label(iframe, text="Comentario: ", pady=10)
        self.label_comentario.grid(row=5, column=0)

        self.input_comentario = Text(iframe, width=15, height=4)
        self.input_comentario.grid(row=5, column=1)

        # Scroollbar

        self.scrolbar = Scrollbar(iframe, command=self.input_comentario.yview)
        self.scrolbar.grid(row=5, column=2, sticky="nsew")

        # botones

        # create

        self.btn_create = Button(iframe_botones, text="Create", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                                         self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "CREATE"))
        self.btn_create.grid(row=7, column=0, padx=10, pady=10)

        # read

        self.btn_read = Button(iframe_botones, text="Read", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                                     self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "READ"))
        self.btn_read.grid(row=7, column=1, padx=10, pady=10)

        # update

        self.btn_update = Button(iframe_botones, text="Update", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                                         self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "UPDATE"))
        self.btn_update.grid(row=7, column=2, padx=10, pady=10)

        # delete

        self.btn_delete = Button(iframe_botones, text="Delete", command=lambda: objeto_validaciones.validando_formulario(App, objeto_conexion, self.ID.get(),
                                                                                                                         self.Nombre.get(), self.Password.get(), self.Apellido.get(), self.Direccion.get(), self.input_comentario.get("1.0", "end-1c"), "DELETE"))
        self.btn_delete.grid(row=7, column=3, padx=10, pady=10)

    def borrar_campos(self):
        self.ID.set("")
        self.Nombre.set("")
        self.Password.set("")
        self.Apellido.set("")
        self.Direccion.set("")
        self.input_comentario.delete("1.0", "end-1c")

    def licencia(self):

        msg.showinfo(
            message="Aplicacion creada por Jesus Aguirre, GITHUB:JesusxAguirre @2023")

    def mostrar_datos(self, datos):
        pass


App = Interfaz(root)

root.mainloop()
