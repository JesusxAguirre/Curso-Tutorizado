from io import open
string= "GWYN EL SEÑOR DE LA LUZ quien descubrio la llama primigenia dando asi la era de la luz y oscuridad \n"

archivo_externo = open("archivo-externo.txt",'r+',encoding="utf-8")

lista_archivo = archivo_externo.readlines()

lista_archivo[1] = string


archivo_externo.seek(0)
#archivo_externo.seek(len(archivo_externo.read())/2)

archivo_externo.writelines(lista_archivo)

archivo_externo.close()