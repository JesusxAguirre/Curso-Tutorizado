#crear una table con id autoincrementable
import sqlite3

mi_conexion = sqlite3.connect("BBDD/GestionPedidos")

cursor = mi_conexion.cursor()

cursor.execute("""CREATE TABLE PRODUCTOS (
               ID INTEGER PRIMARY KEY AUTOINCREMENT, 
               NARTICULO VARCHAR(50),
               PRECIO INTEGER, 
               SECCION VARCHAR(20)
               )""")


mis_productos = [
  ("Camiseta",35,"Moda"),
  ("Pantalon",45,"Moda"),
  ("Coche",75,"Jugeteria"),
  ("Gorra",35,"Deportes")
] 

cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",mis_productos)


mi_conexion.commit()



cursor.close()

mi_conexion.close()