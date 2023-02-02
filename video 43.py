#funciones decoradoras video II

def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args,**kwargs):
      print("A continuacion voy a realizar un calculo")
      
      funcion_parametro(*args, **kwargs)
      
      print("He terminado mi trabajo como funcion decoradora")
      print("\n")
    return funcion_interna


@funcion_decoradora
def suma(a,b):
  
  print(a+b) 

@funcion_decoradora
def resta(a,b):
  
  print(a - b) 
  
@funcion_decoradora
def potencia(base,exponente):
  print(pow(base,exponente))
  
  
  
suma(5,7)


resta(26,6)

#pasando parametros clave:valor
potencia(base=5,exponente=3)