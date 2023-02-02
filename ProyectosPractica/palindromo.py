#programa para averiguar si una cadena es un palindromo
def es_palindromo():
  string = input("introduce un palindromo por favor: ")

  var=list(string)

  var.reverse()

  palindromo = "".join(var)


  if(string == palindromo):
    print("Es un palindromo")
  else:
    print("No es un palindromo")
    
def es_palindromo2():
  string = input("introduce un palindromo por favor: ")
  if(string == string[::-1]):
    print("Es un palindromo")
  else:
    print("No es un palindromo")
  
es_palindromo2()