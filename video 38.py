import re
""" 
lista_nombres = ["htttp://www.pildorasinformaticas.es","ftp://www.pildorasinformaticas.es","htttp://www.pildorasinformaticas.com"]

for nombre in lista_nombres:
  
  if re.findall("es$",nombre):
    print(nombre) """
    
    
lista_terminos = ["camión","niños","niñas","camion","ejemplo"]

for termino in lista_terminos:
  if re.findall("cami[oó]n",termino):
    print(termino)
    
    
#--------------- viendo si se pueden filtrar las cedulas -------------------#

cedulas = ["V27666555","E223445","R24","E1234","V25523523","v21234567"]

for cedula in cedulas:
  
  if re.findall("V|E([0-9]{5,8})",cedula):
    print(cedula) 
    
    
#-------------------agrupando---------------------------------------#
""" 
lista_productos = ["Ma:1","Se1","Ma2","Va1","Ba2","Se2","Ma.3","Ma4","Se:3","SeA","SeB","Va2","SeC"]

for producto in lista_productos:
  if re.findall("Ma[.:]",producto):
    print(producto) """