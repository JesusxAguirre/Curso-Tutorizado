#programa de crear un acronimo
#creando lista donde guardar acronimo
acronimo = []
entrada = input("introduce un texto por favor: ")

#haciendo una lista con los datos de entrada
lista = entrada.split()

#recorriendo la lista de datos de entrada
for var in lista:
  
  #creando una sublista por cada palabra de los datos de entrada ex: ['h','o','l','a'  ]
  nueva_lista = list(var)
  #agregando en una nueva lista la primera posicion de la sublista
  acronimo.append(nueva_lista[0])

#uniendo la lista en una cadena
print("".join(acronimo).upper())  