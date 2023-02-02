#ejercicio video 12 

print("Bienvenido al programa de insertar paises y ciudades que pertenecen a ese pais")
print("\n")

pais = input("Introduce un pais: ")
ciudades=[]
paises ={}
while pais != "salir":

  ciudad = input("Introduce una ciudad por favor: ")

  ciudades.append(ciudad)

  paises[pais]=ciudades

  pais = input("Introduce un pais: ")
  if pais not in paises:
    ciudades=[]

print(paises)