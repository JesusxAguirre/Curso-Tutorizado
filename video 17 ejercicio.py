nombres=[]
contador= 0

while contador < 10:
  persona=input("introduce el nombre de persona: ")
  if persona in nombres:
    raise ValueError ("Este programa no acepta nombres repetidos")
  else:
    nombres.append(persona)
    contador = contador + 1


print(nombres)

