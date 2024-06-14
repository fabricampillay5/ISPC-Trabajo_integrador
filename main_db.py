# MENU DE OPCIONES
# script principal donde se manejara un menu de opciones para que el usuario interactue con la base de datos utilizando las funciones definidas.

from operaciones_db import listar_proveedores, buscar_cliente, inner_join_ordenes, inner_join_orden_compra_proveedor

def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1.Listar proveedores")
        print("2.Buscar cliente por DNI")
        print("3.Consulta con INNER JOIN de ordenes de despacho y productos")
        print("4.Consulta con INNER JOIN de órdenes de compra y proveedores")
        print("5.Salir")

        opcion = input("Ingrese una opción:")

        if opcion == "1":
            listar_proveedores()
        elif opcion == "2":
            dni = input("Ingrese el DNI del cliente a buscar: ")
            buscar_cliente(dni)
        elif opcion == "3":
            inner_join_ordenes()
        elif opcion == "4":
            inner_join_orden_compra_proveedor()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
