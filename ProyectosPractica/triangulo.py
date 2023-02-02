def triangulo(n_veces):
  caracter = "*"
  contador = 1
  for i in range(n_veces):
    print("          "+ caracter * contador + "        ")

    contador+= 2
    
    


triangulo(9)