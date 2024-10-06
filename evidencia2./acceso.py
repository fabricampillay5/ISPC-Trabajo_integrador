import os.path
import pickle
from datetime import datetime
from clases import Acceso

def cargar_accesos():
    try:
        with open('accesos.ispc', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
def guardar_accesos(accesos):
    with open('accesos.ispc', "wb") as file:
        pickle.dump(accesos, file)

def registrar_acceso(usuario_logueado):
    accesos = cargar_accesos()
    nuevo_acceso = Acceso(len(accesos) + 1, datetime.now(), None, usuario_logueado)
    accesos.append(nuevo_acceso)
    guardar_accesos(accesos)

def iniciar_sesion(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.username == nombre_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("usario no registrado.")
        return

    intentos = 0
    while intentos < 4:
        clave = input("Ingrese su clave: ")
        if clave == usuario_encontrado.password:
            print(f"Acceso concedido. Bienvenido {nombre_usuario}.\n")
            registrar_acceso(usuario_encontrado)  # Registrar el acceso del usuario
            return
        else:
            intentos += 1
            print(f"Clave incorrecta. Intento {intentos}/4.")
            if intentos == 4:
                print("Usuario bloqueado por intentos fallidos.")
                with open("log.txt", "a") as file:
                    file.write(f"Usuario bloqueado: {nombre_usuario}, Intento fallido con clave: {clave}\n")
