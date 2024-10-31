# gestionBusqueda.py
import pickle
import os


class GestionBusqueda:
    ORDENADO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuariosOrdenadosPorUsername.ispc")

    @staticmethod
    def ordenar_por_username(usuarios):
        # Algoritmo de ordenamiento burbuja
        for i in range(len(usuarios) - 1):
            for j in range(len(usuarios) - 1 - i):
                if usuarios[j].get_username() > usuarios[j + 1].get_username():
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]

        # Guardamos el archivo ordenado
        with open(GestionBusqueda.ORDENADO_PATH, 'wb') as file:
            pickle.dump(usuarios, file)
        print("[INFO] Usuarios ordenados por username y guardados en 'usuariosOrdenadosPorUsername.ispc'.")

    @staticmethod
    def leer_usuarios_ordenados():
        # Comprobamos si el archivo ordenado existe
        if not os.path.exists(GestionBusqueda.ORDENADO_PATH):
            print("[INFO] No existe el archivo de usuarios ordenados. Por favor, ordénelos primero.")
            return []

        # Leemos el archivo de usuarios ordenados
        with open(GestionBusqueda.ORDENADO_PATH, 'rb') as file:
            usuarios_ordenados = pickle.load(file)
        return usuarios_ordenados

    @staticmethod
    def buscar_por_dni(dni, usuarios):
        left, right = 0, len(usuarios) - 1
        while left <= right:
            mid = (left + right) // 2
            if usuarios[mid].get_dni() == dni:
                return usuarios[mid]
            elif usuarios[mid].get_dni() < dni:
                left = mid + 1
            else:
                right = mid - 1
        return None

    @staticmethod
    def buscar_por_username(username, usuarios):
        for index, usuario in enumerate(usuarios):
            print(f"Intento {index + 1}: {username} comparado con {usuario.get_username()}")
            if usuario.get_username() == username:
                return usuario
        return None