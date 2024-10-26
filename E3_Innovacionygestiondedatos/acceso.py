# accesos.py
import os.path
import pickle
from datetime import datetime
from clases import Acceso
import os
from crud import cargar_usuarios
from database import hash_password, verificar_password, insertar_usuario, obtener_usuario


archivo_accesos = 'accesos.ispc'
archivo_logs = 'logs.txt'

def registrar_acceso(acceso):
    accesos = cargar_accesos()
    accesos.append(acceso)
    guardar_accesos(accesos)

def cargar_accesos():
    if os.path.exists(archivo_accesos):
        with open(archivo_accesos, 'rb') as archivo:
            return pickle.load(archivo)
    return []

def guardar_accesos(accesos):
    with open(archivo_accesos, 'wb') as archivo:
        pickle.dump(accesos, archivo)

# Registro de intentos fallidos
def registrar_intento_fallido(username, password):
    with open(archivo_logs, 'a') as  archivo:
        archivo.write(f"Intento fallido: Usuario: {username}, Password: {password}, Fecha: {datetime.now()}\n")

# Ingreso al sistema con verificación de contraseña cifrada
def ingresar_sistema(username, password):
    usuarios = obtener_usuario()
    for user in usuarios:
        if user[1] == username and verificar_password(password, user[2].encode('utf-8')):
            acceso = Acceso(id=len(cargar_accesos()) + 1, fechaIngreso=datetime.now(), fechaSalida=None, usuarioLogueado=username)
            registrar_acceso(acceso)
            print(f"Bienvenido {username}. Has ingresado al sistema.")
            return
    print("Datos incorrectos.")
    registrar_intento_fallido(username, password)
