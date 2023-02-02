from io import open

archivo_externo = open("archivo-externo.txt","r",encoding="utf-8")

#archivo_externo.write("\n Guardamos informacion con el metodo de append")

info= archivo_externo.readlines()

archivo_externo.close()

for i in info:
  if  "narrativo" in i:
    print(i)
    break