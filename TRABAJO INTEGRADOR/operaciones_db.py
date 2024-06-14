# FUNCIONES PARA EL CRUD Y CONSULTAS SQL
# creando funciones para realizar las operaciones CRUD (crear, leer, actualizar, eliminar) y consultas SQL especificas
import mysql.connector

from db_connection import conectar

def listar_proveedores():
    try:
        mybd = conectar()
        if mybd:
            cursor = mybd.cursor()
            sql = "SELECT * FROM `proveedor`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except mysql.connector.Error as err:
        print(f"Error al listar proveedores:{err}")
    finally:
        if mybd and mybd.is_connected():
            cursor.close()
            mybd.close()


def buscar_cliente(dni):
    try:
        mybd = conectar()
        if mybd:
            cursor = mybd.cursor()
            sql = "SELECT * FROM `clientes` WHERE DNI = %S"
            cursor.execute(sql, (dni,))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print("Cliente no encontrado.")
    except mysql.connector.Error as err:
        print(f"Error al buscar cliente: {err}")
    finally:
        if mybd and mybd.is_connected():
            cursor.close()
            mybd.close()


def inner_join_ordenes():
    try:
        mybd = conectar()
        if mybd:
            cursor = mybd.cursor()
            sql = """
            SELECT od.NUM_DESPACHO, od.NOMBRE_PRODUCTO, od.CANT_DESPACHO, p.`NOMBRE_PRODUCTO`, p.`FECHA_VENCIMIENTO`
            FROM `orden de despacho` od
            INNER JOIN `producto` P ON od.NOMBRE_PRODUCTO = P.`NOMBRE_PRODUCTO`
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except mysql.connector.Error as err:
        print(f"Error en inner join de ordenes: {err}")
    finally:
        if mybd and mybd.is_connected():
            cursor.close()
            mybd.close()

def inner_join_orden_compra_proveedor():
    try:
        mybd = conectar()
        if mybd:
            cursor = mybd.cursor()
            sql = """
            SELECT oc.NRO_ORDEN, oc.NOMBRE_PRODUCTO, oc.CANT_ORDEN, oc.TIPO_PRODUCTO, p.`RAZON SOCIAL`
            FROM `orden de compra` oc
            INNER JOIN `proveedor` p ON oc.PROVEEDOR_ID = p.ID
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except mysql.connector.Error as err:
        print(f"Error en inner join de órdenes de compra y proveedores: {err}")
    finally:
        if mybd and mybd.is_connected():
            cursor.close()
            mybd.close()
