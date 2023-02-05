import sqlite3
from tkinter import messagebox as msg
from tkinter import simpledialog
import sys

class Conexion:
    def __init__(self) -> None:
        self.conexion = None
        self.cursor = None
        self.BBDD = None

    def conectar_bd(self):
        self.BBDD = simpledialog.askstring("BBDD","Introduce el nombre de la base de datos")
        self.conexion = sqlite3.connect(self.BBDD)
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute(
                """CREATE TABLE USUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100))"""
            )

            self.conexion.commit()

            msg.showinfo(message="Base de datos creada con exito")

        except:
            msg.showinfo(message="Conectado correctamente a la base de datos")

    def salir(self):
        try:
            valor_salir =msg.askquestion("Salir", "¿Desea salir de la aplicacion?")
            
            if valor_salir:
              self.cursor.close()
              self.conexion.close()
              sys.exit()
        except:
            msg.showerror(
                message="No puedes cerrar la conexion sin que esta este inicializada"
            )


objeto_conexion = Conexion()
