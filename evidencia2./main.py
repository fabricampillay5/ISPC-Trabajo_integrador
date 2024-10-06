# menu principal
from crud import cargar_usuario, guardar_usuario,agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios
from acceso import iniciar_sesion, registrar_acceso
from clases import Usuario

def mostrar_menu():
    print("""
    1. Iniciar sesion
    2. Agregar usuario
    3. Modificar usuario
    4. Eliminar usuario
    5. Buscar usuario
    6. Mostrar todos los usuarios
    7. Salir
    """)
    
def main():
    # Cargar usuarios desde el archivo binario
    usuarios = cargar_usuario()


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            # iniciar sesion
            iniciar_sesion(usuarios)
        elif opcion == "2":
            # agreagar usuario
            agregar_usuario(usuarios) # pasar lista de usuarios
            guardar_usuario(usuarios) # guardar los cambios
        elif opcion == "3":
            # modificar usuario
            modificar_usuario(usuarios) # pasar la lista de usuarios
            guardar_usuario(usuarios) # guardar los cambios
        elif opcion == "4":
            # eliminar usuario
            eliminar_usuario(usuarios) # pasar la lista de usuarios
            guardar_usuario(usuarios) # guardar los cambios
        elif opcion == "5":
            # buscar usuario
            buscar_usuario(usuarios)
        elif opcion == "6":
            # mostarar todos los usuarios
            mostrar_usuarios(usuarios)
        elif opcion == "7":
            print("Saliendo del sistema. . .")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

# Esto garantiza que el programa inicie en el menú cuando se ejecute este archivo
if __name__ == "__main__":
    main()  # Llamada al menú principal
