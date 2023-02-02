from tkinter import messagebox as msg
from modulos_CRUD.clase_crud import *


class Validaciones:
    def __init__(self) -> None:
        pass

    def validando_formulario(
        self,
        objeto_app,
        objeto_conexion,
        id,
        nombre,
        password,
        apellido,
        direccion,
        comentario,
        consulta,
    ):
        if consulta == "CREATE":
            self.llamando_create(
                objeto_conexion, nombre, password, apellido, direccion, comentario
            )
        elif consulta == "READ":
            self.llamando_read(
                objeto_app,
                objeto_conexion,
                id,
                nombre,
                password,
                apellido,
                direccion,
                comentario,
            )
        elif consulta == "UPDATE":
            self.llamando_update(
                objeto_conexion, id, nombre, password, apellido, direccion, comentario
            )
        else:
            self.llamando_delete(objeto_conexion, id)

    # funcion para llamar a la funcion de CREATE
    def llamando_create(
        self, objeto_conexion, nombre, password, apellido, direccion, comentario
    ):
        # creando lista para pasarlelo a la clase crud
        if (
            nombre
            and password
            and apellido
            and direccion
            and comentario
            and objeto_conexion.conexion
        ):
            datos = [nombre, password, apellido, direccion, comentario]
            objeto_crud.create_user(objeto_conexion, datos)
        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            else:
                msg.showerror(
                    message="Rellena todos los campos para enviar el formulario!"
                )

    # funcion para buscar un dato
    def llamando_read(
        self,
        objeto_app,
        objeto_conexion,
        id,
        nombre,
        password,
        apellido,
        direccion,
        comentario,
    ):
        if objeto_conexion.conexion and (
            id or nombre or password or apellido or direccion or comentario
        ):
            datos = [id, nombre, password, apellido, direccion, comentario]

            objeto_crud.read_user(objeto_app, objeto_conexion, datos)
        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            else:
                msg.showerror(message="Debes enviar al menos un campo para consultar")

    def llamando_update(
        self, objeto_conexion, id, nombre, password, apellido, direccion, comentario
    ) -> None:
        if (
            objeto_conexion.conexion
            and id
            and (nombre or password or apellido or direccion or comentario)
        ):
            datos = [id, nombre, password, apellido, direccion, comentario]

            objeto_crud.update_user(objeto_conexion, datos)

        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            elif not id:
                msg.showerror(
                    message="Debes de indicar el id para poder actualizar el registro"
                )
            else:
                msg.showerror(message="Debes enviar al menos un campo para consultar")

    def llamando_delete(self, objeto_conexion, Id):
        if objeto_conexion.conexion and Id:
            objeto_crud.delete_user(objeto_conexion, Id)

        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            elif not id:
                msg.showerror(
                    message="Debes de indicar el id para poder actualizar el registro"
                )
            else:
                msg.showerror(message="Debes enviar al menos un campo para consultar")


objeto_validaciones = Validaciones()
