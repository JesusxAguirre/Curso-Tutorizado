import sqlite3
from tkinter import *
from tkinter import messagebox as msg


class Conexion:
    def __init__(self) -> None:
        self.conexion = None
        self.cursor = None

    def conectar_bd(self):
        self.conexion = sqlite3.connect("CRUD/Usuarios")
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
            self.cursor.close()
            self.conexion.close()

            msg.showinfo(message="Conexion cerrada correctamente")
        except:
            msg.showerror(
                message="No puedes cerrar la conexion sin que esta este inicializada"
            )


objeto_conexion = Conexion()
