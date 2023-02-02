
correo = input("por favor ingrese un correo")


lista_correo = correo.split("@")

nombre = lista_correo[0].split(".")

dominio = lista_correo[1].split(".")

print(nombre)
print(dominio)


if "gmail" in dominio:
  print("hola "+ nombre[0] + "  estoy viendo que tu email esta registrado con google. Eso es genial!")
else:
  print("hola " + nombre[0] + " estoy observando que estas utilizando un dominio personalizado " + dominio[0] + " Impresionante!") 
  # Get user email address
