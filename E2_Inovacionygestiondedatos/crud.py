# crud.py
import pickle
import os
from clases import Usuario

archivo_usuarios = 'usuarios.ispc'
def cargar_usuarios():
    # Verificar si el archivo existe y devolver un diccionario vacío si no
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'rb') as archivo:
            usuarios = pickle.load(archivo)
            if isinstance(usuarios, dict):  # Verificamos que sea un diccionario
                return usuarios
            else:
                return {}  # Si por algún motivo no es un diccionario, se devuelve vacío
    return {}  # Devolver un diccionario vacío si el archivo no existe

def guardar_usuarios(usuarios):
    # Guardar los usuarios en el archivo binario
    with open(archivo_usuarios, 'wb') as archivo:
        pickle.dump(usuarios, archivo)
def agregar_usuario(usuario):
    usuarios = cargar_usuarios() # Cargar los usuarios como diccionario
    usuarios[usuario.username] = usuario # Usar el 'username' como clave en el diccionario
    guardar_usuarios(usuarios) # Guardar los usuarios de nuevo en el archivo

def modificar_usuario(username, nuevo_email=None, nueva_password=None):
    usuarios = cargar_usuarios()
    if username in usuarios:
        if nuevo_email:
            usuarios[username].email = nuevo_email
        if nueva_password:
            usuarios[username].password = nueva_password
        guardar_usuarios(usuarios)
    else:
        print("Usuario no encontrado.")
def eliminar_usuario(username):
    usuarios = cargar_usuarios()
    if username in usuarios:
        del usuarios[username]
        guardar_usuarios(usuarios)
    else:
        print("Usuario no encontrado.")
def buscar_usuario(username=None, email=None):
    usuarios = cargar_usuarios()
    for usuario in usuarios.values():
        if usuario.username == username or usuario.email == email:
            return usuario
    return None
def mostrar_usuarios():
    usuarios = cargar_usuarios()
    for usuario in usuarios.values():
        print(usuario)
