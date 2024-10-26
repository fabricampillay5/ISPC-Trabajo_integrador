# crud.py
import pickle
import os
from clases import Usuario
from database import insertar_usuario, hash_password

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

    # guardar en la base de datos
    insertar_usuario(usuario.username, hash_password(usuario.password), usuario.email)
    print("Usuario agregado correctamente a la base de datos")

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

# funciones agregadas en la evidencia 3

def ordenar_usuarios_burbuja(usuarios):
    n = len(usuarios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if usuarios[j].username > usuarios[j + 1].username:
                usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
    return usuarios

def ordenar_usuarios_python(usuarios):
    return sorted(usuarios, key=lambda usuario: usuario.username)

def guardar_usuarios_ordenados(usuarios, metodo='burbuja'):
    if metodo == 'burbuja':
        usuarios_ordenados = ordenar_usuarios_burbuja(usuarios)
    elif metodo == 'python':
        usuarios_ordenados = ordenar_usuarios_python(usuarios)
    else:
        print("metodo de ordenamiento no reconocido.")
        return
    with open("usuarios.ispc", "wb") as file:
        pickle.dump(usuarios_ordenados, file)
    print(f"Usuarios ordenados guardados usando el metodo: {metodo}")

def buscar_usuario_secuencial(usuarios, username):
    for usuario in usuarios:
        if usuario.username == username:
            print("Busqueda realizada por tecnica secuenncial.")
            return usuario
    print("Usuario no encontrado.")
    return None

def buscar_usuario_binaria(usuarios, username):
    izquierda, derecha = 0, len(usuarios) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].username == username:
            print("Busqueda realizada por tecnica binaria.")
            return usuarios[medio]
        elif usuarios[medio].username < username:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("usuario no encontrado.")
    return None
