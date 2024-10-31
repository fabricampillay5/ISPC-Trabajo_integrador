# gestionUsuario.py
import pickle
from usuario import Usuario
import os


class GestionUsuario:
    FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.ispc")

    @staticmethod
    def agregar_usuario(usuario):
        usuarios = GestionUsuario.leer_usuarios()
        usuarios.append(usuario)
        usuarios.sort(key=lambda u: u.get_dni())  # Orden por DNI
        with open(GestionUsuario.FILE_PATH, 'wb') as file:
            pickle.dump(usuarios, file)

    @staticmethod
    def leer_usuarios():
        if not os.path.exists(GestionUsuario.FILE_PATH):
            return []
        with open(GestionUsuario.FILE_PATH, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def modificar_usuario(dni, nuevo_username=None, nuevo_email=None):
        usuarios = GestionUsuario.leer_usuarios()
        for usuario in usuarios:
            if usuario.get_dni() == dni:
                if nuevo_username:
                    usuario.set_username(nuevo_username)
                if nuevo_email:
                    usuario.set_email(nuevo_email)
        with open(GestionUsuario.FILE_PATH, 'wb') as file:
            pickle.dump(usuarios, file)

    @staticmethod
    def eliminar_usuario(dni):
        usuarios = GestionUsuario.leer_usuarios()
        usuarios = [u for u in usuarios if u.get_dni() != dni]
        with open(GestionUsuario.FILE_PATH, 'wb') as file:
            pickle.dump(usuarios, file)