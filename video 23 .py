class Persona():
    almacen_datos = []

    def __init__(self, *datos):
        for dato in datos:
            self.almacen_datos.append(dato)

        self.getDatos(self.almacen_datos)

    def getDatos(self, info):

        for dato in info:
            print(dato)


class Agenda():

    def __init__(self):
        self.miAgenda = {}

    def agregarPersona(self, nombre, telefono):

        self.miAgenda[nombre] = telefono


agendaPersonal = Agenda()

agendaPersonal.agregarPersona("Jesus", "04122679578")
agendaPersonal.agregarPersona("Mario", "12334134123")


print(len(agendaPersonal))