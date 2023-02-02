#actualizando registros
import sqlite3

mi_conexion = sqlite3.connect("BBDD/GestionPedidos")

cursor = mi_conexion.cursor()

#cursor.execute("UPDATE PRODUCTOS SET PRECIO=25 WHERE ID = 2")

cursor.execute("DELETE FROM PRODUCTOS WHERE ID= 4")

mi_conexion.commit()

cursor.close()

mi_conexion.close()



