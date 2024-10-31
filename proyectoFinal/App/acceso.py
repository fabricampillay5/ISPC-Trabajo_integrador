# acceso.py
from datetime import datetime


class Acceso:
    def __init__(self, id, fecha_ingreso=None, fecha_salida=None, usuario_logueado=None):
        self.__id = id
        self.__fecha_ingreso = fecha_ingreso or datetime.now()
        self.__fecha_salida = fecha_salida
        self.__usuario_logueado = usuario_logueado

    # Getters
    def get_id(self):
        return self.__id

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def get_fecha_salida(self):
        return self.__fecha_salida

    def get_usuario_logueado(self):
        return self.__usuario_logueado

    # Setters
    def set_fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    def set_usuario_logueado(self, usuario_logueado):
        self.__usuario_logueado = usuario_logueado

    # Representación en cadena para almacenamiento en archivos
    def __str__(self):
        return f"{self.__id}, {self.__fecha_ingreso}, {self.__fecha_salida}, {self.__usuario_logueado}"