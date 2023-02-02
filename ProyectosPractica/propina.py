class Propina:
  
  OPCIONES_PROPINA = {"1":18,"2":20,"3":25}
  
  def __init__(self,numero_personas,factura) -> None:
    self.numero_personas = numero_personas
    self.factura = factura
  
  def calcular_propina(self,monto_propina):
    total_monto = (self.factura * monto_propina)/100
    total_monto = total_monto+ self.factura
    monto_persona = total_monto/self.numero_personas
    return monto_persona,total_monto
  
  
  
#programa para calcular propinas
while True:
  try:
    numero_personas = int(input("Introduce el numero de personas en que se dividar la factura: "))
    break
  except ValueError:
    print("el numero de personas tiene que ser un numero")
    
while True:
  try:
    factura =float(input("which is the invoice at today?: "))
    break
  except ValueError:
    print("la factura debe ser numerica")


objeto = Propina(numero_personas,factura)
   


print("Que propina deseas dar. ")
print("1.-18%.")
print("2.- 20%")
print("3.- 25%")


opcion_escogida = input("escoge una opcion con un numero del 1 al 3: ")

while opcion_escogida not in objeto.OPCIONES_PROPINA:
  opcion_escogida = input("no escogiste correctamente intenta de nuevo")


resultado =objeto.calcular_propina(objeto.OPCIONES_PROPINA[opcion_escogida])

print("a todos les toca abonar: ",resultado)