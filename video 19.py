class Persona():
    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "Sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero

    def setEdad(self, edad):
        if edad < 0 or edad > 100:
            return "Error en la edad"

        else:
            self.__edad = edad
            return self.__edad

    def hablar(self):

        return "La persona que se llama: " + self.__nombre + " esta hablando"

    def caminar(self):

        return "La persona que se llama: " + self.__nombre + " esta caminando"

    def getDatos(self):

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.__edad) + " genero: " + self.genero


p1 = Persona("Jesus", "Aguirre", "Masculino")

boleano = False


def formulario():
    try:
        edad_usuario = int(input("Introduce tu edad: "))
        if edad_usuario < 0 or edad_usuario > 100:
            raise ValueError
        else:
            p1.setEdad(edad_usuario)
            return True
    except ValueError:
        print("Los parametros de edad no son correctos deben ser mayor a 0 y menor a 100 y debe ser un numero")
        return False


while boleano == False:
    boleano = formulario()


print(p1.getDatos())
