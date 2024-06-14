# CONEXION A LA BASE DE DATOS
# ARCHIVO PARA MANEJAR LA BASE DE DATOS ESTO AYUDARA A TENER UN CODIGO LIMPIO

import mysql.connector

def conectar():
    try:
        mybd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="fabriciocampillay5",
            database="AllBreads"
        )
        return mybd
    except mysql.connector.Error as err:
        print(f"Error de conexion a la base de datos: {err}")
        return None
