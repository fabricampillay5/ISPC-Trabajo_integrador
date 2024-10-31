# GRUPO 20 

## Descripcion 

Esta es una aplicacion de escritotio desarrollada en Python para la gestion de usuarios y accesos, conexion a la base de datos y analisis de datos pluviales.
La aplicacion esta diseñada para registrar usuarios y accesos, almacenar datos en archivos binarios y de texto y permite realizar una serie de consultas SQL predeterminadas en la base de datos 'nutricion_animal'.
Tambien incluye una funcionalidad de analisis de precipitaciones con visualizaciones graficas.

## Funcionalidades 

La aplicacion ofrece las siguientes funcionalidades:

1. GESTION DE USUARIOS Y ACCESOS:
  A) CRUD de usuarios con almacenamiento en un archivo binario `usuarios.ispc`.
  B) Registro de accesos y logs de intentos fallidos.
  C) Ordenamiento y búsqueda de usuarios (por `DNI`, `username`, o `email`).

2. CONEXION A LA BASE DE DATOS:
   A) Consultas SQL en la base de datos `nutricion_animal` para:
      1) Mostrar la cantidad despachada por un cliente específico.
      2) Listar productos con cantidad por debajo del promedio.
      3) Consultar proveedores con cantidades superiores a un umbral.
      4) Filtrar productos por fechas de vencimiento específicas y nivel de stock.

  3. ANALISIS DE DATOS PLUVIALES:
     A) Generación y análisis de datos de precipitaciones.
     B) Creación de archivos CSV para registros de precipitaciones anuales.
     C) Visualización de datos pluviales mediante gráficos de barras, dispersión y gráficos circulares.

## estructura del proyecto:

1. Main.py --> Archivo principal de ejecución de la aplicación
2. usuario.py --> Clase Usuario
3. acceso.py --> Clase Acceso
4. gestionUsuario.py --> Módulo de gestión de usuarios (CRUD)
5. gestionAcceso.py --> Módulo de gestión de accesos y logs de intentos fallidos
6. gestionBaseDatos.py --> Módulo de conexión y consultas a la base de datos
7. gestionBusqueda.py --> Módulo de ordenamiento y búsqueda de usuarios
8. analisisDatos.py --> Módulo de análisis de datos pluviales
9. usuarios.ispc --> Archivo binario para almacenar usuarios
10. accesos.ispc --> Archivo binario para almacenar accesos
11. logs.txt --> Archivo de logs de intentos fallidos de acceso
12. datosAnalizados/ --> Carpeta para archivos de datos pluviales y gráficos generados

## Requisitos: 
- Python 3.x
- Paquetes necesarios:
  - mysql-connector-python
  - pandas
  - numpy
  - matplotlib

## Configuracion de la base de datos 

1. Crea la base de datos nutricion_animal y las tablas utilizando el siguiente script SQL:

   CREATE DATABASE IF NOT EXISTS nutricion_animal;
USE nutricion_animal;

CREATE TABLE clientes (
    DNI INT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    activo TINYINT(1) DEFAULT 1
);

CREATE TABLE proveedor (
    id INT PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    tipo_producto VARCHAR(45),
    telefono VARCHAR(15)
);

CREATE TABLE producto (
    id INT PRIMARY KEY,
    nombre_producto VARCHAR(45) NOT NULL,
    cantidad INT DEFAULT 0,
    fecha_vencimiento DATE,
    proveedor_id INT,
    FOREIGN KEY (proveedor_id) REFERENCES proveedor(id) ON DELETE SET NULL
);

CREATE TABLE orden_compra (
    nro_orden INT PRIMARY KEY,
    fecha DATE NOT NULL,
    proveedor_id INT,
    FOREIGN KEY (proveedor_id) REFERENCES proveedor(id) ON DELETE CASCADE
);

CREATE TABLE producto_orden_compra (
    orden_compra_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (orden_compra_id, producto_id),
    FOREIGN KEY (orden_compra_id) REFERENCES orden_compra(nro_orden) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES producto(id) ON DELETE CASCADE
);

CREATE TABLE orden_despacho (
    num_despacho INT PRIMARY KEY,
    fecha DATE NOT NULL,
    cliente_dni INT,
    FOREIGN KEY (cliente_dni) REFERENCES clientes(DNI) ON DELETE CASCADE
);

CREATE TABLE producto_orden_despacho (
    orden_despacho_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (orden_despacho_id, producto_id),
    FOREIGN KEY (orden_despacho_id) REFERENCES orden_despacho(num_despacho) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES producto(id) ON DELETE CASCADE
);

2. Configuración de Conexión a la Base de Datos: En el archivo gestionBaseDatos.py, define tu user y password para la conexión a la base de datos.

## Ejecucion

Ejecuta el archivo main.py para iniciar la aplicación

## Funcionalidades Detalladas 
## Menu principal
1. Usuarios y Accesos de la Aplicación: Gestiona el CRUD de usuarios, muestra accesos y logs de fallos, realiza ordenamiento y búsqueda de usuarios.
2. Ingresar al Sistema: Inicia sesión con username y password, registra accesos exitosos y fallidos.
3. Análisis de Datos: Permite analizar precipitaciones anuales, creando archivos CSV y visualizando los datos.
4. Gestión de Base de Datos: Ejecuta consultas SQL sobre nutricion_animal, con opciones para filtrado y clasificación de productos.
5. Salir de la Aplicación: Finaliza el programa.

## Notas
1. El archivo usuariosOrdenadosPorUsername.ispc se genera automáticamente al realizar el ordenamiento por username.
