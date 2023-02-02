import os

#os.makedirs("PruebaDirectorio2")

#os.chdir("PruebaDirectorio2")


lista_archivos = os.listdir('./')

print(lista_archivos)

for archivo in lista_archivos:
  if archivo == "tirar.py":
    os.remove(archivo)

