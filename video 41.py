#video de funciones lambda
#numero2
"""
calculo_potencia  =lambda numero,exponente: numero**exponente

print(calculo_potencia(3,3))"""

#dando formato numero con una funcion lambda

"""comision_formato = lambda numero : "¡{}!$".format(numero)

print(comision_formato(3700))"""

#ordenando la suma de las tuplas
"""lista_numeros = [(11,5),(15,7),(2,4),(15,19),(8,4)]



lista_numeros.sort(key=lambda t: t[0] + t[1])

print(lista_numeros)"""


musicos = ["Elvis Presley","Bruce Springsteen","Elton Jhon","Tina Turner","Axel Rose"]

def orderar_apellido(m):
  return m.split()[1]

musicos.sort(key=lambda apellido : apellido.split()[1])

print(musicos)
