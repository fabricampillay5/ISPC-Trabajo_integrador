import pickle
from clases import Usuario
def cargar_usuario():
    try:
        with open('usuarios.ispc', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def guardar_usuario(usuarios):
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

def agregar_usuario():
    usuarios = cargar_usuario()
    id_usuario = len(usuarios) + 1
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    email = input("Ingrese el email:")

    nuevo_usuario = Usuario(id_usuario, username, password, email)
    usuarios.append(nuevo_usuario)
    guardar_usuario(usuarios)
    print("Usuario agregado correctamente.")

def modificar_usuario():
    usuarios = cargar_usuario()
    username = input("Ingrese su nombre de usuario a modificar: ")
    usuario = next((u for u in usuarios if u.username == username), None)

    if usuario:
        usuario.email = input(f"Ingrese nuevo email (actual: {usuario.email}): ")
        guardar_usuario(usuarios)
        print("Usuario modificado correctamente.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    usuarios = cargar_usuario()
    username = input("Ingrese el nombre de usuario a eliminar: ")
    usuarios = [u for u in usuarios if u.username != username]
    guardar_usuario(usuarios)
    print("Usuario eliminado correctamente.")

def buscar_usuario():
    usuarios = cargar_usuario()
    username = input("Ingrese el nombre de usuario a buscar: ")
    usuario = next((u for u in usuarios if u.username == username), None)

    if usuario:
        print(f"Usuario encontrado: {usuario-username}, Email: {usuario.email}")
    else:
        print("usuario no encontrado.")

def mostrar_usuarios():
    usuarios = cargar_usuario()
    for u in usuarios:
        print(f"ID: {u.id}, Username: {u.username}, Email: {u.email}")
