#funciones Decoradoras
def funcion_decoradora(funcion_parametro):

    def funcion_interna():
      print("A continuacion voy a realizar un calculo")
      
      funcion_parametro()
      
      print("He terminado mi trabajo como funcion decoradora")
    
    return funcion_interna


@funcion_decoradora
def suma():
  
  print(25 +30) 


def resta():
  
  print(80 - 25) 
  
  
suma()