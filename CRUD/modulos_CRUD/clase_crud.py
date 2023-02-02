from tkinter import *
from tkinter import messagebox as msg


class CRUD:
    def create_user(self, objeto_conexion, datos):
        try:
            objeto_conexion.cursor.execute(
                """INSERT INTO USUARIOS(NOMBRE_USUARIO,PASSWORD,APELLIDO,DIRECCION,COMENTARIOS) 
                                     VALUES(?,?,?,?,?)""",
                datos,
            )
            objeto_conexion.conexion.commit()

            msg.showinfo(message="Datos insertados correctamente")
        except Exception as ex:
            msg.showerror(message=ex)

    def read_user(self, objeto_app, objeto_conexion, datos):
        try:
            if datos[0] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE ID = ?",
                    datos[0],
                )
            elif datos[1] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE NOMBRE_USUARIO = :nombre_usuario ",
                    {"nombre_usuario": datos[1]},
                )
            elif datos[2] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE PASSWORD = :password",
                    {"password": datos[2]},
                )
            elif datos[3] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE  APELLIDO = :apellido",
                    {"apellido": datos[3]},
                )
            elif datos[4] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE  DIRECCION = :direccion",
                    {"direccion": datos[4]},
                )
            elif datos[5] != "":
                objeto_conexion.cursor.execute(
                    "SELECT NOMBRE_USUARIO,APELLIDO,PASSWORD,DIRECCION,COMENTARIOS FROM USUARIOS WHERE  COMENTARIOS = :comentarios",
                    {"comentarios": datos[5]},
                )

            stmt = objeto_conexion.cursor.fetchall()
            stmt = stmt[0]
            msg.showinfo(
                message="""
                   Nombre : {} , 
                   Apellido: {} , 
                   contraseña: {}
                   Direccion: {}
                   Comentario: {}""".format(
                    *stmt
                )
            )

            objeto_app.Nombre.set(stmt[0])
            objeto_app.Password.set(stmt[1])
            objeto_app.Apellido.set(stmt[2])
            objeto_app.Direccion.set(stmt[3])
            objeto_app.input_comentario.insert(INSERT, [stmt[4]])
        except Exception as ex:
            msg.showerror(message=ex)

    def update_user(self, objeto_conexion, datos):
        try:
            objeto_conexion.cursor.execute(
                """UPDATE USUARIOS SET NOMBRE_USUARIO =:nombre,PASSWORD = :password, APELLIDO = :apellido
                              , DIRECCION = :direccion, COMENTARIOS = :comentarios WHERE ID = :id""",
                {
                    "id": datos[0],
                    "nombre": datos[1],
                    "password": datos[2],
                    "apellido": datos[3],
                    "direccion": datos[4],
                    "comentarios": datos[5],
                },
            )
            objeto_conexion.conexion.commit()

            msg.showinfo(message="Datos actualizados correctamente")
        except Exception as ex:
            msg.showerror(message=ex)

    def delete_user(self, objeto_conexion, id):
        try:
            objeto_conexion.cursor.execute("DELETE FROM USUARIOS WHERE ID = ?", id)

            objeto_conexion.conexion.commit()

            msg.showinfo(message="El usuario ha sido eliminado correctamente")

        except Exception as ex:
            msg.showerror(message=ex)


objeto_crud = CRUD()
