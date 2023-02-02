def max_in_list(lista):
  inicio = 0 
  for i in lista:
    
    if i > inicio:
      
      inicio = i
    
  return inicio
    
#print(max_in_list([8,10,15,4]))

def mas_larga(cadena):
  return max(cadena.split(" "), key=len)
      

print(mas_larga("El señor Gwyn de la luz fue aquel que descubrio la llama original"))

def count_mayuscula(cadena):
  contador = 0
  
  for i in cadena:
    
    if i.isupper():
      contador+=1
  
  return contador 

#print(count_mayuscula("El señor Gwyn de la luz fue aquel que descubrio la llama original"))



def edad_personas():
  contador=0
  annio_actual = int(input("Digite el año actual -> "))
  
  personas = []
  
  while len(personas) <= 4:
    nombre = input("Introduce un nombre de una persona ->")
    annio_nacimiento = int(input("Introduce el annio de nacimiento de esa persona ->"))
    
    personas.append(nombre)
    personas.append(annio_nacimiento)

  while len(personas) > 0:
    for i in range(personas.pop(),annio_actual):
      contador+=1
    
    print(personas.pop() + " tienen o tendran la edad de " + str(contador))
    contador = 0
    
#edad_personas() 
 
 
 
def edad_mayor_20():   
  lista_edades = []
  while len(lista_edades) < 10: 
    edad_persona = int(input("Introduce la edad de una persona -> "))
    lista_edades.append(edad_persona)
  
  tupla_edades = tuple(lista_edades)
  contador = 0
  
  for i in tupla_edades:
    if i >= 20:
      contador+=1
  
  return contador 

#print(edad_mayor_20())

def buscar_letra():
  lista_nombres = []
  contador = 0
  while len(lista_nombres) <10:
    
    lista_nombres.append(input("Introduce un nombre por favor -> "))

  busqueda = input("Introduce la letra que quieres buscar -> ")
  
  for i in lista_nombres:
    if busqueda.lower() == i[0] or busqueda.upper() == i[0] :
      contador+=1
  
  return contador


#print(buscar_letra())

def contar_vocales():
  frase = input("Introduce una frase por favor -> ")
  
  return sum(1 for i in frase if i in "aeiouAEIOU")

#print(contar_vocales())

def es_bisiesto():
  
  aniio_busqueda = int(input("Introduce el año que quieres saber si es bisiesto -> "))
  
  return "Es bisiesto" if aniio_busqueda % 4 == 0 else "No es bisiesto"

print(es_bisiesto())
