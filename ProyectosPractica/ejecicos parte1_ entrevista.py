def max(num1,num2):
  
  return num1 if num1 > num2 else num2

#print(max(10,5))


def max_3(num1,num2,num3):
  
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  else:
    return num3
  
#print(max_3(19,12,39))

def len(cadena):
  
  return sum(1 for x in cadena)

#print(len("Hemos venido en son de paz"))


def vowel(letter):
  
  return True if letter in ("aeiouAEIOU") else False


#print(vowel("A"))

def suma(lista):
  number =0
  for i in lista:
    number += i
  return number

#print(suma([1,2,3,4]))

def multiplicar(lista):
  number =1
  
  for i in lista:
   number = number * i
  
  return number

#print(multiplicar([1,2,3,4]))


def inversa(cadena):
  return cadena[::-1]


#print(inversa("Estoy probando"))

def es_palindromo(cadena):
  
  if cadena == cadena[::-1]: print("Es palindromo") 
  
  else: print("No es palindromo")
  
#es_palindromo("radar")

def superposicion(lista1,lista2):
  
  for i in lista1:
    
    if i in lista2:
      return True
    else:
      return False
  
#print(superposicion(["Mundo","jesus"],["Hola","Mundo"]))

def generar_n_caracteres(n,caracter):
  
  return n * caracter

#print(generar_n_caracteres(5,"*"))

def generar_histograma(lista):
  histo ="*"
  for i in lista:
    
    print(histo * i)
    
generar_histograma([4, 9, 7])