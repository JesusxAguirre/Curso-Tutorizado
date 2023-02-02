from io import open
archivo_externo = open("clientes.txt","r",encoding='utf-8')

lista = archivo_externo.readlines()
archivo_externo.close()
lista2 = ["Codigo articulo","Nombre","Direccion","Poblacion","Telf","Responsable"]
clientes=[]
for row in lista:
  variable=row.split(";")
  cliente = {"Codigo":variable[0],"Nombre":variable[1],"Direccion":variable[2],"Poblacion":variable[3],"Telefono":variable[4],"Responsable":variable[5]}
  clientes.append(cliente)

for c in clientes:
  print("Codigo Articulo={} Nombre={} Direccion={} Poblacion={} Tlfn={} Responsable{}"
  .format(c["Codigo"],c["Nombre"],c["Direccion"],c["Poblacion"],c["Telefono"],c["Telefono"],c["Responsable"]))