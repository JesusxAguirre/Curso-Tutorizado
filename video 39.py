#funcion match solo busca al principio

import re

""" codigo1 = "Casdasdasdasdsasd255"

codigo2 = "asdasdasdasdas133dasdasdqwrehrethbffawfre"

codigo3 = "asda255sdfsdfsdfsdfsdfsdfsdf"

if re.search("255",codigo3,re.IGNORECASE):
  print("he encontrado el codigo",codigo1)
else:
  print("No se ha encontrado el codigo")
   """
  
cadena = "example(unwanted thing)example"	
 
print(re.sub("[^/(/)]","",cadena))