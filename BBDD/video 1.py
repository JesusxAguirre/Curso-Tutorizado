import sqlite3

mi_conexion = sqlite3.connect("BBDD/miBBDD")

cursor = mi_conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (N_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#cursor.execute("INSERT INTO PRODUCTOS  VALUES ('Camiseta',25,'Moda')")

mi_conexion.commit()

cursor.close()

mi_conexion.close()