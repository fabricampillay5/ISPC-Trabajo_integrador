# usuario.py
class Usuario:
    def __init__(self, id, username, dni, password, email):
        self.__id = id
        self.__username = username
        self.__dni = dni
        self.__password = password
        self.__email = email

    # Getters
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_dni(self):
        return self.__dni

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    # Setters
    def set_username(self, username):
        self.__username = username

    def set_dni(self, dni):
        self.__dni = dni

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    # Representación en cadena para almacenamiento en archivos
    def __str__(self):
        return f"{self.__id}, {self.__username}, {self.__dni},{self.__email}"