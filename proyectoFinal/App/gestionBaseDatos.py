# gestionBaseDatos.py
import mysql.connector
from mysql.connector import Error

class GestionBaseDatos:
    def __init__(self, host='localhost', database='nutricion_animal', user='root', password='fabriciocampillay5'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("[INFO] Conexión a la base de datos exitosa.")
        except Error as e:
            print(f"[ERROR] Fallo en la conexión: {e}. Configurar datos de conexión.")

    def ejecutar_consulta(self, consulta_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as e:
            print(f"[ERROR] Error al ejecutar consulta: {e}")
            return []

    def cerrar_conexion(self):
        if self.connection.is_connected():
            self.connection.close()
            print("[INFO] Conexión a la base de datos cerrada.")