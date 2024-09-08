# Archivo principal para ejecutar la aplicación

import re
import random
from aritmetica import sumar, restar, dividir, multiplicar

usuarios = [] # Diccionario para almacenar los usuarios registrados


def mostrar_bienvenida():
    print("¡Bienvenido a la aplicacion!")
    print("1.Iniciar sesion.")
    print("2.Registrar nuevo usuario.")
    print("3.Olvido su contraseña.")
    print("4.Salir.")


def registrar_usuario():
    print("\n--- Registro de usuario ---")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")

    if dni in [u['dni'] for u in usuarios.values()]:
        print("Error: El DNI ya esta resgistrado.")
        return

    email = input("Ingrese su correo electronico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")
    nombre_usuario = input("Ingrese su nombre de usuario (6-12 caracteres): ")


    if len(nombre_usuario) < 6 or len(nombre_usuario) > 12 or nombre_usuario in usuarios:
        print("Error: El nombre de usuario no es valido o ya existe.")
        return

    clave = input("Ingrese su contraseña (minimo 8 caracteres, incluyendo mayusculas, minusculas, numeros y especiales): ")


    if not validar_contraseña(clave):
        print("Error: La contraseña no cumple con las condiciones.")
        return


    if validar_captcha():
        usuarios[nombre_usuario] = {
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni,
            'email': email,
            'fecha_nacimiento': fecha_nacimiento,
            'clave': clave
        }
        with open("usuariosCreados.txt", "a") as file:
            file.write(f"Usuario: {nombre_usuario}, DNI: {dni}, Registrado correctamente.\n")
        print("Usuario registrado correctamente.\n")
    else:
        print("Captcha incorrecto. No se registro el usuario.\n")


def validar_contraseña(clave):
    return (len(clave) >= 8 and
            re.search(r"[a-z]", clave) and
            re.search(r"[A-Z]", clave) and
            re.search(r"\d", clave) and
            re.search(r"\W", clave))


def validar_captcha():
    operaciones = [sumar,restar,dividir,multiplicar]
    op = random.choice(operaciones)
    a, b = round(random.uniform(1, 100), 2), round(random.uniform(1, 100), 2)
    resultado = op(a, b)
    print(f"Resuelva la operacion: {op.__name__}({a}, {b}) = ?")
    respuesta = input("ingrese el resultado con dos decimales: ")
    return float(respuesta) == resultado


def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("Usuario no resgistrado.")
        return

    intentos = 0
    while intentos < 4:
        clave = input("Ingrese su clave: ")
        if clave == usuarios[nombre_usuario]['clave']:
            print(f"Acceso concedido. Bienvenido {nombre_usuario}.\n")
            with open("ingresos.txt", "a") as file:
                file.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: ahora().\n")
            return
        else:
            intentos +=1
            print(f"Clave incorrecta. Intento {intentos}/4.")
            if intentos == 4:
                print("Usuario bloqueado por intentos fallidos.")
                with open("log.txt", "a") as file:
                    file.write(f"Usuario bloqueado: {nombre_usuario}.\n")


def main():
    while True:
        mostrar_bienvenida()
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Funcion 'Olvido su contraseña' aun no implementada.")
        elif opcion == '4':
            print("Gracias por usar la aplicacion. Adios.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()


