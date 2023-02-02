class Biografia:
  
  def __init__(self,nombre,apellido,mes_nacimiento,dia_nacimiento,year_born,direccion,meta_personal) -> None:
    self.nombre = nombre
    self.apellido = apellido
    self.mes_nacimiento = mes_nacimiento
    self.dia_nacimiento = dia_nacimiento
    self.year_born = year_born
    self.direccion = direccion
    self.meta_personal = meta_personal
    
  def get_nombre(self):
    return self.nombre.lower().capitalize() + " " + self.apellido.lower().capitalize()
  
  def get_fecha_nacimiento(self):
    return self.mes_nacimiento.lower().capitalize() + " " + self.dia_nacimiento + ", " + self.year_born
  
  def get_direccion(self):
    return self.direccion.lower().capitalize()
  
  def get_meta(self):
    return self.meta_personal.lower().capitalize()
  
print("Bienvenido al programa de tu biografia :)")

#funcion para validar strings
def validar_string(string,validando):
  while True:
    try:  
      if not string.isalpha():
        raise ValueError
      break
    except  ValueError:
      print("El " + validando + " no puede llevar ni numeros ni caracteres especiales: ",string)
      string = input("introduce de nuevo el "+validando+ ":  ")

#funcion para validar numeros      
def validar_number(number,validando):
  while True:
    try:  
      if not number.isnumeric():
        raise ValueError
      break
    except  ValueError:
      print("El " + validando + " solo puede contener numeros: ",number)
      number = input("introduce de nuevo el "+validando+ ":  ")

nombre = input("Introduce tu nombre: ")   
validar_string(nombre,"nombre")
apellido = input("Introduce tu apellido: ")
validar_string(apellido,"apellido")
mes_nacimiento = input("Introduce tu mes de nacimiento: ")
validar_string(mes_nacimiento,"Mes de nacimiento")
dia_nacimiento = input("Introduce tu dia de nacimiento: ")
validar_number(dia_nacimiento,"dia de nacimiento")
year_born = input("introduce el año de tu nacimiento: ")
validar_number(year_born,"Año de nacimiento")
direccion = input("Introduce la direccion de tu hogar: ")
validar_string(direccion,"direccion")
meta_personal = input("Introduce la meta personal de tu hogar: ")
validar_string(meta_personal,"Meta personal")

print("flujo de ejecucion")

objeto =Biografia(nombre,apellido,mes_nacimiento,dia_nacimiento,year_born,direccion,meta_personal)

print(objeto.get_nombre())
print(objeto.get_fecha_nacimiento())
print(objeto.get_direccion())
print(objeto.get_meta())