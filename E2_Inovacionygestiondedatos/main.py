# main.py
from crud import agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios
from acceso import ingresar_sistema
from clases import Usuario

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos Los Usuarios")
        print("6. Ingresar al Sistema")
        print("7.  Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_usuario = input("Ingrese ID del usuario: ")
            username = input("Ingrese Username: ")
            password = input("Ingrese Password: ")
            email = input("Ingrese Email: ")
            usuario = Usuario(id=id_usuario, username=username, password=password, email=email)
            agregar_usuario(usuario)
            print("Usuario Agregado Correctamente.")

        elif opcion == "2":
            username = input("Ingrese el Username del usuario a modificar: ")
            nuevo_email = input("Ingrese nuevo Email (deje vacio para no modificar): ")
            nueva_password = input("Ingrese nueva Password (deje vacio para no modificar): ")
            modificar_usuario(username, nuevo_email, nueva_password)
            print("usuario modificado correctamente.")

        elif opcion == "3":
            username = input("Ingrese Username del usuario a eliminar: ")
            eliminar_usuario(username)
            print("Usuario eliminado correctamente.")

        elif opcion == "4":
            username = input("Ingrese el Username del usuario a buscar: ")
            usuario = buscar_usuario(username=username)
            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")

        elif opcion == "5":
            mostrar_usuarios()

        elif opcion == "6":
            username = input("Ingrese Username: ")
            password = input("Ingrese Password: ")
            ingresar_sistema(username, password)

        elif opcion == "7":
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion no válida.")

if __name__ == "__main__":
    menu_principal()
