from tkinter import *

from modulos_CRUD.clase_conexion import *
from modulos_CRUD.clase_validaciones import *

class Interfaz(Frame):
    def __init__(self,raiz) -> None:
        #------------variables-----------#
        self.Nombre = StringVar()
        self.Password = StringVar()
        self.Apellido = StringVar()
        self.Direccion = StringVar()
        self.ID = StringVar()

        super().__init__(raiz,width=300,height=300)
        self.master = raiz
        self.master.title("Aplicacion con CRUD")
        self.pack()
        
        self.iframe_botones = Frame(raiz)
        self.iframe_botones.pack()
        
        self.crear_widgets()
        
        self.crear_barra_menu()
        
        self.botones_crud()
       
        

    def crear_barra_menu(self):
        menu_bar = Menu(self)
        self.master.config(menu=menu_bar)
         # BDD Menu
        self.bd_menu = Menu(menu_bar, tearoff=0)
        self.bd_menu.add_command(
            label="Conectar", command=lambda: objeto_conexion.conectar_bd()
        )
        self.bd_menu.add_command(label="Salir", command=lambda: objeto_conexion.salir())

        # Delete menu
        self.delete_menu = Menu(menu_bar, tearoff=0)
        self.delete_menu.add_command(
            label="Borrar campos", command=lambda: self.borrar_campos()
        )

        # crud menu
        self.crud_menu = Menu(menu_bar, tearoff=0)
        self.crud_menu.add_command(
            label="Crear",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "CREATE",
            ),
        )
        self.crud_menu.add_command(
            label="Leer",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "READ",
            ),
        )
        self.crud_menu.add_command(
            label="Actualizar",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "UPDATE",
            ),
        )
        self.crud_menu.add_command(
            label="Eliminar",
            command=lambda: objeto_validaciones.validando_formulario(
                App, objeto_conexion, self.ID.get(), "DELETE"
            ),
        )

        # help menu

        self.help_menu = Menu(menu_bar, tearoff=0)
        self.help_menu.add_command(label="Licencia")
        self.help_menu.add_command(label="Acerca de")

        menu_bar.add_cascade(label="BBDD", menu=self.bd_menu)
        menu_bar.add_cascade(label="Borrar", menu=self.delete_menu)
        menu_bar.add_cascade(label="CRUD", menu=self.crud_menu)
        menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

    def crear_widgets(self):
        # contruyendo los widgets
        
        # id

        self.label_id = Label(self, text="ID:")
        self.label_id.grid(row=0, column=0, sticky="e",padx=10, pady=10)

        self.input_id = Entry(self, textvariable=self.ID)
        self.input_id.grid(row=0, column=1)

        # Nombre
        self.label_nombre = Label(
            self,
            text="Nombre: ",
            pady=10,
        )
        self.label_nombre.grid(row=1, column=0, sticky="e",padx=10, pady=10)

        self.input_nombre = Entry(
            self, textvariable=self.Nombre, fg="Red", justify=["right"]
        )
        self.input_nombre.grid(row=1, column=1)

        # password
        self.label_password = Label(self, text="Password: ", pady=10)
        self.label_password.grid(row=2, column=0, sticky="e",padx=10, pady=10)

        self.input_password = Entry(
            self, textvariable=self.Password, show="*", justify=["left"]
        )
        self.input_password.grid(row=2, column=1)

        # apellido
        self.label_apellido = Label(self, text="Apellido: ", pady=10)
        self.label_apellido.grid(row=3, column=0, sticky="e",padx=10, pady=10)

        self.input_apellido = Entry(self, textvariable=self.Apellido)
        self.input_apellido.grid(row=3, column=1)

        # direccion
        self.label_direccion = Label(self, text="Direccion: ", pady=10)
        self.label_direccion.grid(row=4, column=0, sticky="e",padx=10, pady=10)

        self.input_direccion = Entry(self, textvariable=self.Direccion)
        self.input_direccion.grid(row=4, column=1)

        # comentario
        self.label_comentario = Label(self, text="Comentario: ", pady=10)
        self.label_comentario.grid(row=5, column=0, sticky="e",padx=10, pady=10)

        self.input_comentario = Text(self, width=15, height=4)
        self.input_comentario.grid(row=5, column=1)

        # Scroollbar

        self.scrolbar = Scrollbar(self, command=self.input_comentario.yview)
        self.scrolbar.grid(row=5, column=2, sticky="nsew")

    def botones_crud(self):

        #botones

        # create

        self.btn_create = Button(
            self.iframe_botones,
            text="Create",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "CREATE",
            ),
        )
        self.btn_create.grid(row=7, column=0, sticky="e",padx=10, pady=10)

        # read

        self.btn_read = Button(
            self.iframe_botones,
            text="Read",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "READ",
            ),
        )
        self.btn_read.grid(row=7, column=1, sticky="e",padx=10, pady=10)

        # update

        self.btn_update = Button(
            self.iframe_botones,
            text="Update",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "UPDATE",
            ),
        )
        self.btn_update.grid(row=7, column=2, sticky="e",padx=10, pady=10)

        # delete

        self.btn_delete = Button(
            self.iframe_botones,
            text="Delete",
            command=lambda: objeto_validaciones.validando_formulario(
                App,
                objeto_conexion,
                self.ID.get(),
                self.Nombre.get(),
                self.Password.get(),
                self.Apellido.get(),
                self.Direccion.get(),
                self.input_comentario.get("1.0", "end-1c"),
                "DELETE",
            ),
        )
        self.btn_delete.grid(row=7, column=3, sticky="e",padx=10, pady=10)

    def borrar_campos(self):
        self.ID.set("")
        self.Nombre.set("")
        self.Password.set("")
        self.Apellido.set("")
        self.Direccion.set("")
        self.input_comentario.delete("1.0", "end-1c")

    def licencia(self):
        msg.showinfo(
            message="Aplicacion creada por Jesus Aguirre, GITHUB:JesusxAguirre @2023"
        )

    def mostrar_datos(self, datos):
        pass

root = Tk()

App = Interfaz(root)

App.mainloop()
