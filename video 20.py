

class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):

        return "Estoy hablando"

    def piensa(self):

        return "Estoy pensando"

    def camina(self):

        return "Estoy caminando"

    def come(self):

        return "Estoy comiendo"


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):
        Persona.__init__(self,nombre, apellido, edad)
        self.escuela = escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"


class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        Persona.__init__(self,nombre, apellido, edad)
        self.empresa = empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Empresa: " + self.empresa

    def trabaja(self):

        return "Estoy trabajando"


class Director(Trabajador, Estudiante):
    
    def __init__(self, nombre, apellido, edad, empresa,escuela,bonus):
        Trabajador.__init__(self,nombre, apellido, edad, empresa)
        Estudiante.__init__(self,nombre, apellido, edad, escuela)


        self.bonus = bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)
    
    def dirige(self):
        
        return "Estoy dirigiendo"


persona1 = Persona("Jesus", "Aguirre", 23)

estudiante1 = Estudiante("Ana", "Martinez", 18, "19 de abril")

print(persona1.getDatosPersonales())

print(estudiante1.getDatosPersonales())

print("---------------------------------------------------------------------")

trabajador1 = Trabajador("Mario","Vergolini",45,"Ferrari")

print(trabajador1.getDatosPersonales())

director1 = Director("Lario","PrimRose",60,"FORD","NASA",2000)

print(director1.getDatosPersonales())