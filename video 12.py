#recorriendo un diccioranio con bucle for

diccionario={"Nombre":"Jesus","Apellido":"Aguirre","Edad":23}

for clave,valor in diccionario.items():
  print(clave + "->" + str(valor))