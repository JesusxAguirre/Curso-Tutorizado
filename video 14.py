#generadores video 2

def capitales_mundo(*ciudades):
  for capital in ciudades:
    yield from capital


capitales_devueltas =capitales_mundo("Berlin","Roma","Bogota","Madrid","Pekin","Caracas")

for i in capitales_devueltas:
  print(i)