#empezando con las expresiones regulares

import re

cadena = "Estoy trabajando con python un sabado y en vacaciones. El proximo sabado no pienso programar"

busqueda = "sabado"

if re.search(busqueda,cadena):
  print("se encontro el patron",busqueda)
else:
  print("no se encontro el patron",busqueda)
  
  
texto_encontrado = re.search(busqueda,cadena)

print(texto_encontrado.span())


print(re.findall(busqueda,cadena))