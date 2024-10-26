# clases.py
class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

    def __str__(self):
        return (f"ID Acceso: {self.id}, Usuario: {self.usuarioLogueado}, Ingreso: {self.fechaIngreso}, Salida: {self.fechaSalida}")

