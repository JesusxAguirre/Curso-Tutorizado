#conectando con postgresql

import psycopg2

datos = {"host":"localhost","dbname":"Personas","user":"postgres","password":"12345678"}


mi_conexion = psycopg2.connect(host= datos["host"], database =datos["dbname"],user = datos["user"], password = datos["password"])

cursor = mi_conexion.cursor()

cursor.execute("SELECT * FROM ALUMNOS")

stmt = cursor.fetchall()

print(stmt)
    
cursor.close()

mi_conexion.close()