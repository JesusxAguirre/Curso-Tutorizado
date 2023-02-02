#funciones lambda primer video

"""def calcular_area_triangulo(base,altura):
  
  return (base*altura)/2

triangulo1 = calcular_area_triangulo(3,6)

triangulo2 = calcular_area_triangulo(15,25)"""

area_triangulo =  lambda base,altura:(base*altura)/2


print(area_triangulo(3,6))
print(area_triangulo(15,25))