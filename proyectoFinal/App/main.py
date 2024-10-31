# main.py
from gestionUsuario import GestionUsuario
from gestionAcceso import GestionAcceso
from gestionBaseDatos import GestionBaseDatos
from gestionBusqueda import GestionBusqueda
from analisisDatos import AnalisisDatos
from usuario import Usuario


def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema con los datos de usuario")
        print("3. Análisis de datos")
        print("4. Gestion Base de Datos")
        print("5. Salir de la aplicación")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_usuarios_y_accesos()
        elif opcion == '2':
            menu_ingresar_sistema()
        elif opcion == '3':
            menu_analisis_datos()
        elif opcion == '4':
            menu_gestion_base_datos()
        elif opcion == '5':
            print("Gracias por usar la aplicación.")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")


def menu_usuarios_y_accesos():
    while True:
        print("\n--- Usuarios y Accesos de la Aplicación ---")
        print("a) Acceder al CRUD de los Usuarios en POO")
        print("b) Mostrar los datos de Accesos")
        print("c) Ordenamiento y Búsqueda de Usuarios")
        print("d) Volver al Menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            menu_crud_usuarios()
        elif opcion == 'b':
            menu_datos_accesos()
        elif opcion == 'c':
            menu_ordenamiento_busqueda()
        elif opcion == 'd':
            break
        else:
            print("Opción inválida, intente de nuevo.")


def menu_crud_usuarios():
    while True:
        print("\n--- CRUD de Usuarios ---")
        print("a) Agregar un nuevo usuario")
        print("b) Modificar un usuario")
        print("c) Eliminar un usuario (dado su DNI)")
        print("d) Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            id = input("ID: ")
            username = input("Username: ")
            dni = int(input("DNI: "))
            password = input("Password: ")
            email = input("Email: ")
            usuario = Usuario(id=id, username=username, dni=dni, password=password, email=email)
            GestionUsuario.agregar_usuario(usuario)
            print("Usuario agregado con éxito.")

        elif opcion == 'b':
            dni = int(input("Ingrese el DNI del usuario a modificar: "))
            nuevo_username = input("Nuevo Username (dejar vacío para no cambiar): ")
            nuevo_email = input("Nuevo Email (dejar vacío para no cambiar): ")
            GestionUsuario.modificar_usuario(dni, nuevo_username or None, nuevo_email or None)
            print("Usuario modificado con éxito.")

        elif opcion == 'c':
            dni = int(input("Ingrese el DNI del usuario a eliminar: "))
            GestionUsuario.eliminar_usuario(dni)
            print("Usuario eliminado con éxito.")

        elif opcion == 'd':
            break
        else:
            print("Opción inválida, intente de nuevo.")


def menu_datos_accesos():
    while True:
        print("\n--- Datos de Accesos ---")
        print("a) Mostrar los Accesos")
        print("b) Mostrar los logs de intentos fallidos")
        print("c) Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            accesos = GestionAcceso.leer_accesos()
            for acceso in accesos:
                print(acceso)

        elif opcion == 'b':
            GestionAcceso.mostrar_logs()

        elif opcion == 'c':
            break
        else:
            print("Opción inválida, intente de nuevo.")


def menu_ordenamiento_busqueda():
    while True:
        print("\n--- Ordenamiento y Búsqueda de Usuarios ---")
        print("a) Ordenar los Usuarios por Username")
        print("b) Buscar los Usuarios")
        print("c) Mostrar los Usuarios")
        print("d) Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            usuarios = GestionUsuario.leer_usuarios()
            GestionBusqueda.ordenar_por_username(usuarios)

        elif opcion == 'b':
            metodo_busqueda()

        elif opcion == 'c':
            mostrar_usuarios()

        elif opcion == 'd':
            break
        else:
            print("Opción inválida, intente de nuevo.")


def metodo_busqueda():
    print("\n--- Métodos de Búsqueda de Usuarios ---")
    print("1) Buscar por DNI (búsqueda binaria)")
    print("2) Buscar por Username (búsqueda secuencial)")
    print("3) Buscar por Email (búsqueda secuencial)")

    opcion = input("Seleccione un método de búsqueda: ")
    usuarios = GestionUsuario.leer_usuarios()

    if opcion == '1':
        dni = int(input("Ingrese el DNI: "))
        usuario = GestionBusqueda.buscar_por_dni(dni, usuarios)
        if usuario:
            print("Usuario encontrado:", usuario)
        else:
            print("Usuario no encontrado.")

    elif opcion == '2':
        username = input("Ingrese el Username: ")
        usuario = GestionBusqueda.buscar_por_username(username, usuarios)
        if usuario:
            print("Usuario encontrado:", usuario)
        else:
            print("Usuario no encontrado.")

    elif opcion == '3':
        email = input("Ingrese el Email: ")
        usuario = next((u for u in usuarios if u.get_email() == email), None)
        if usuario:
            print("Usuario encontrado:", usuario)
        else:
            print("Usuario no encontrado.")
    else:
        print("Opción inválida.")


def mostrar_usuarios():
    print("\n--- Mostrar Usuarios ---")
    print("1) Mostrar usuarios del archivo 'usuarios.ispc'")
    print("2) Mostrar usuarios ordenados por Username")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        usuarios = GestionUsuario.leer_usuarios()
    elif opcion == '2':
        usuarios = GestionBusqueda.leer_usuarios_ordenados()
    else:
        print("Opción inválida.")
        return

    for usuario in usuarios:
        print(usuario)


def menu_ingresar_sistema():
    print("\n--- Iniciar Sesión ---")
    username = input("Username: ")
    password = input("Password: ")

    usuarios = GestionUsuario.leer_usuarios()
    usuario = next((u for u in usuarios if u.get_username() == username and u.get_password() == password), None)

    if usuario:
        GestionAcceso.registrar_acceso(usuario.get_id(), username)
        print("Bienvenido, ha ingresado al sistema.")
    else:
        GestionAcceso.registrar_fallo(username, password)
        print("Credenciales incorrectas.")


def menu_analisis_datos():
    print("\n--- Análisis de Datos Pluviales ---")
    año = input("Ingrese el año de análisis (ejemplo: 2023): ")
    df = AnalisisDatos.crear_registro_pluvial(año)
    AnalisisDatos.analizar_registro(año)




def menu_gestion_base_datos():
    db = GestionBaseDatos(user='root', password='fabriciocampillay5')
    db.conectar()

    while True:
        print("\n--- Gestión de Base de Datos ---")
        print("a) Cantidad despachada por Juan Perez")
        print("b) Productos cuya cantidad está por debajo del promedio")
        print("c) Proveedores con total de cantidad superior a 200")
        print("d) Productos con fecha de vencimiento posterior a una fecha específica")
        print("e) Productos con cantidades menores a 100 y fecha de vencimiento anterior a una fecha específica")
        print("f) Clasificación de productos en niveles de stock")
        print("g) Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            consulta = """
            select c.nombre as nombre_cliente, o.num_despacho, p.nombre_producto, pod.cantidad
            from orden_despacho o
            join clientes c on o.cliente_dni = c.DNI
            join producto_orden_despacho pod on o.num_despacho = pod.orden_despacho_id
            join producto p on pod.producto_id = p.id
            where c.DNI = 12345678;
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'b':
            consulta = """
            select nombre_producto, cantidad
            from producto
            where cantidad < (select avg(cantidad) from producto);
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'c':
            consulta = """
            select proveedor_id, sum(cantidad) as total_cantidad
            from producto
            group by proveedor_id
            having sum(cantidad) > 200;
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'd':
            fecha = input("Ingrese una fecha en formato YYYY-MM-DD: ")
            consulta = f"""
            with ProductosRecientes as (
                select id, nombre_producto, fecha_vencimiento
                from producto
                where fecha_vencimiento > '{fecha}'
            )
            select nombre_producto, fecha_vencimiento
            from ProductosRecientes
            order by fecha_vencimiento;
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'e':
            fecha = input("Ingrese una fecha en formato YYYY-MM-DD: ")
            consulta = f"""
            select nombre_producto, cantidad
            from producto
            where cantidad < 100 
            union 
            select nombre_producto, cantidad
            from producto
            where fecha_vencimiento < '{fecha}';
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'f':
            consulta = """
            select nombre_producto, cantidad,
                case
                    when cantidad < 110 then 'BAJO'
                    when cantidad between 110 and 180 then 'MODERADO'
                    else 'ALTO'
                end AS nivel_stock
            from producto;
            """
            resultados = db.ejecutar_consulta(consulta)
            for resultado in resultados:
                print(resultado)

        elif opcion == 'g':
            db.cerrar_conexion()
            break

        else:
            print("Opción inválida, intente de nuevo.")



# Ejecución del menú principal
if __name__ == "__main__":
    menu_principal()