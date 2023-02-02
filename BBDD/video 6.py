#conectando con MySQL

import mysql.connector

datos = {"host":"localhost","dbname":"casa_sobre_la_roca","user":"root","password":""}


mi_conexion = mysql.connector.connect(host= datos["host"], database =datos["dbname"],user = datos["user"], password = datos["password"])

cursor = mi_conexion.cursor()

cursor.execute("SELECT * FROM USUARIOS WHERE nombre = Jesus")

stmt = cursor.fetchall()

for i in stmt:
  print(i)
    
cursor.close()

mi_conexion.close()