import sqlite3

mi_conexion = sqlite3.connect("BBDD/miBBDD")

cursor = mi_conexion.cursor()

#muchos_productos = [("Patin",100,"Deportes"),("Cenicero",20,"Ceramica"),("Pantalon",80,"Moda")]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",muchos_productos)


cursor.execute("SELECT * FROM PRODUCTOS")

stmt = cursor.fetchall()

for p in stmt:
  print("Nombre: ",p[0], "Precio: ",p[1])
cursor.close()

mi_conexion.close()