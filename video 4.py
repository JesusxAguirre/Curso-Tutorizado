# video de tuplas las tuplas es lo mismo que una lista pero mas optimizada


datos = ("Jesus", 4, 6, 1999)


print(datos)

# las tuplas se pueden convertir en listas

lista = list(datos)

print(lista)

armas = ["Alabarda", "Katana", "Pica", "Espadon","Espadon","Espadon"]

# convitiendo lista en tupla

tupla = tuple(armas)

print(tupla)

# buscando datos en una tupla devuelve un dato boleano
verdadero ="Alabarda" in tupla

if verdadero:
    print("El elemento en la tupla si se encuentra")
else:
    print("El elemento en la tupla no se encuentra")

print(tupla.count("Espadon"))

print(len(tupla))