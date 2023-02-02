#herencia 

class Persona():

    def hablar(self):

        return "Hablo como una persona"


class Trabajador(Persona):

    def hablar(self):

        return "Hablo como un trabador"


class Director(Trabajador):

    def hablar(self):

        return "Hablo como un director"

def hazlesHablar(listaPersonas):

  for persona in listaPersonas:

    print(persona.hablar())

Antonio = Persona()

Mario = Trabajador()

Ana = Director()

print(Antonio.hablar())

print(Mario.hablar())

print(Ana.hablar())


print("-----------------------------------------------------------------------")


listaPersonas=[Antonio,Mario,Ana]

hazlesHablar(listaPersonas)