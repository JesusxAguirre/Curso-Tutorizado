edad = input("Introduce tu edad: ")

while edad.isdigit() == False:

  print("El valor introducido es incorrecto")

  edad = input("Introduce tu edad de nuevo: ")



if int(edad) <18:

  print( "No puedes pasar")

else:
  print("Puedas pasar")
