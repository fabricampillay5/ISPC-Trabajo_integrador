# database.py
import mysql.connector
from mysql.connector import Error
import bcrypt

def conectar():
    try:
        conexion = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="fabriciocampillay5",
        database="gestion_usuarios"
        )
        if conexion.is_connected():
            print("Conexion exitosa a la base de datos.")
            return conexion
    except Error as e:
        print(f"Error: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexcion cerrada.")

def insertar_usuario(username, password, email):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Usuario (username, password, email) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (username, password, email))
    conexion.commit()
    cerrar_conexion(conexion)
    print("Usuario insertado con exito.")

def obtener_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuario")
    resultados = cursor.fetchall()
    cerrar_conexion(conexion)
    return resultados

# cifrado de contraseña
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verificar_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
