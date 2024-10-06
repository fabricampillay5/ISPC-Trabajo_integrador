
class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

class Acceso:
    def __init__(self, id, fecha_ingreso, fecha_salida, usuario_Logueado):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.usuario_Logueado = usuario_Logueado
