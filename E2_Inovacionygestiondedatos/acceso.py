# accesos.py
import os.path
import pickle
from datetime import datetime
from clases import Acceso
import os
from crud import cargar_usuarios

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

def registrar_intento_fallido(username, password):
    with open (archivo_logs, 'a') as  archivo:
        archivo.write(f"Intento fallido: Usuario: {username}, Password: {password}, Fecha: {datetime.now()}\n")

def ingresar_sistema(username, password):
    usuarios = cargar_usuarios()
    if username in usuarios and usuarios[username].password == password:
        acceso = Acceso(id=len(cargar_accesos()) + 1, fechaIngreso=datetime.now(), fechaSalida=None, usuarioLogueado=username)
        registrar_acceso(acceso)
        print(f"Bienvenido {username}. Has ingresado al sistema.")
    else:
        print("Datos incorrectos.")
        registrar_intento_fallido(username, password)
