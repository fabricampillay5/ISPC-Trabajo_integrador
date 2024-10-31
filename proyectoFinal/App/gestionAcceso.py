# gestionAcceso.py
import pickle
import os
from acceso import Acceso
from datetime import datetime

class GestionAcceso:
    ACCESO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accesos.ispc")
    LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs.txt")

    @staticmethod
    def registrar_acceso(usuario_id, username):
        acceso = Acceso(id=usuario_id, usuario_logueado=username, fecha_ingreso=datetime.now())
        accesos = GestionAcceso.leer_accesos()
        accesos.append(acceso)
        with open(GestionAcceso.ACCESO_PATH, 'wb') as file:
            pickle.dump(accesos, file)
        print(f"[INFO] Usuario '{username}' accedió correctamente.")

    @staticmethod
    def registrar_fallo(username, password):
        with open(GestionAcceso.LOG_PATH, 'a') as log_file:
            log_file.write(f"{datetime.now()}: Fallo de ingreso para Username: {username}, Password: {password}\n")
        print("[ERROR] Intento fallido de ingreso registrado en logs.txt.")

    @staticmethod
    def leer_accesos():
        if not os.path.exists(GestionAcceso.ACCESO_PATH):
            return []
        with open(GestionAcceso.ACCESO_PATH, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def mostrar_logs():
        if not os.path.exists(GestionAcceso.LOG_PATH):
            print("[INFO] No se encontraron registros de fallos.")
            return
        with open(GestionAcceso.LOG_PATH, 'r') as file:
            logs = file.readlines()
            for log in logs:
                print(log.strip())