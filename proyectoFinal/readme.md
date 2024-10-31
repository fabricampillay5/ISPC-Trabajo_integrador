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
