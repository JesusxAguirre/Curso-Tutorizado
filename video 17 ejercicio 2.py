nombres = []
contador = 0
def agregar_lista(nombres,persona):
  try:
    if persona in nombres:
      raise ValueError
    else:
      nombres.append(persona)
  except ValueError:
    print("Este nombre ya esta introducido en la lista:",persona)

while contador <10:
  persona = input("introduce un nombre: ")

  agregar_lista(nombres,persona)

  contador = contador +1



print(nombres)