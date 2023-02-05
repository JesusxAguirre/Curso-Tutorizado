from tkinter import messagebox as msg
from modulos_CRUD.clase_crud import *


class Validaciones:
    def __init__(self) -> None:
        pass

    def validando_formulario(
        self,
        objeto_app,
        objeto_conexion,
        *args
    ):
        argumentos = [*args]
        if "CREATE" in argumentos:
            argumentos.remove("CREATE")
            self.llamando_create(
                objeto_conexion, argumentos
            )
        elif "READ" in argumentos:
            argumentos.remove("READ")
            self.llamando_read(
                objeto_app,
                objeto_conexion,
                argumentos
            )
        elif "UPDATE" in argumentos:
            argumentos.remove("UPDATE")
            self.llamando_update(
                objeto_conexion, argumentos
            )
        elif "DELETE" in argumentos:
            argumentos.remove("DELETE")
            self.llamando_delete(objeto_conexion, id)

    # funcion para llamar a la funcion de CREATE
    def llamando_create(
        self, objeto_conexion, argumentos
    ):
        if (
            "" not in argumentos
            and objeto_conexion.conexion
        ):
         
            objeto_crud.create_user(objeto_conexion, argumentos)
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
        argumentos
    ):
        if objeto_conexion.conexion and len(argumentos) != 0:
        
            objeto_crud.read_user(objeto_app, objeto_conexion, argumentos)
        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            else:
                msg.showerror(
                    message="Debes enviar al menos un campo para consultar")

    def llamando_update(
        self, objeto_conexion, argumentos
    ) -> None:
        elementos_len = (1 for x in argumentos if x != "")
        if (
            objeto_conexion.conexion and
             any(valor.isnumeric() for valor in argumentos) and 
             elementos_len >1
        ):

            objeto_crud.update_user(objeto_conexion, argumentos)

        else:
            if not objeto_conexion.conexion:
                msg.showerror(
                    message="Debes de conectar con la base de datos antes de realizar cualquier operacion"
                )
            elif any(valor.isnumeric() for valor in argumentos):
                print( any(valor.isnumeric() for valor in argumentos))
                print(argumentos)
                msg.showerror(
                    message="Debes de indicar el id para poder actualizar el registro"
                )
            else:
                msg.showerror(
                    message="Debes enviar al menos un campo para actualizar")

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
                msg.showerror(
                    message="Debes enviar al menos un campo para consultar")


objeto_validaciones = Validaciones()
