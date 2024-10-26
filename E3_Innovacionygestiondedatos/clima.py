# clima.py
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
import os

# generar registros pluviales aleatorios
def generar_registros_aleatorios():
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    registros_anuales = []

    for dias in dias_por_mes:
        # generar una lista de registros pluviales aleatorios para cada mes
        registros_mes = [random.randint(0, 100) for _ in range(dias)]
        registros_anuales.append(registros_mes)

    return registros_anuales

# guardar registros pluviales en un archivo CSV
def guardar_registros_csv(registros_anuales, anio):
    nombre_archivo = f"registroPluvial{anio}.csv"

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)

        # escribir encabezado de los meses
        encabezados = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        escritor.writerow(encabezados)

        # rellenar filas para cada dia del año
        for dia in range(31): # maximo 31 dias
            fila = [(registros_anuales[mes][dia] if dia < len(registros_anuales[mes]) else "") for mes in range(12)]
            escritor.writerow(fila)

    print(f"Archivo CSV '{nombre_archivo}' creado exitosamente.")

# cargar o generar datos pluviales de un año
def cargar_o_generar_registros(anio):
    nombre_archivo = f"registroPluvial{anio}.csv"

    if os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' ya existe. Leyendo datos...")
        registros_anuales = []

        # leer los datos del CSV
        with open(nombre_archivo, mode='r') as archivo_csv:
            lector = csv.reader(archivo_csv)
            next(lector) # saltar encabezado
            for fila in lector:
                registros_anuales.append([int(valor) if valor else None for valor in fila])

    else:
        print(f"El archivo '{nombre_archivo}' no existe. Generando registros aleatorios...")
        registros_anuales = generar_registros_aleatorios()
        guardar_registros_csv(registros_anuales, anio)

    return registros_anuales

# seleccionar y mostrar registros del mes
def mostrar_registros_mes(registros_anuales, mes):
    nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    if 1 <= mes <= 12:
        registros_mes = registros_anuales[mes - 1]
        print(f"Registros pluviales para {nombre_mes[mes - 1]}: {registros_mes}")
    else:
        print("Mes invalido. Debe estar entre 1 y 12.")

# grafico de barras: lluvias totales por mes
def graficar_lluvias_mensuales(registros_anuales):
    nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # calcular lluvia total de cada mes
    lluvias_mensuales = [sum(mes) for mes in registros_anuales]

    plt.figure(figsize=(10,6))
    plt.bar(nombre_meses, lluvias_mensuales, color="skyblue")
    plt.title("Lluvias totales por mes")
    plt.xlabel("Mes")
    plt.ylabel("Luvia total (mm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# grafico de dispersion: lluvias diarias por mes
def graficar_lluvias_diarias(registros_anuales):
    nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    plt.figure(figsize=(10, 6))

    for mes_idx, registros_mes in enumerate(registros_anuales):
        dias = list(range(1, len(registros_mes) + 1))
        plt.scatter([mes_idx + 1] * len(dias), dias, s=10, c=registros_mes, cmap="viridis", label=nombre_meses[mes_idx])

    plt.colorbar(label="Lluvia (mm)")
    plt.xticks(range(1, 13), nombre_meses, rotation=45)
    plt.title("Lluvias Diarias (Dispersión)")
    plt.xlabel("Mes")
    plt.ylabel("Día")
    plt.tight_layout()
    plt.show()

# grafico circular: proporcion de lluvias por mes
def graficar_proporcion_lluvias_mensuales(registros_anuales):
    nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    lluvias_mensuales = [sum(mes) for mes in registros_anuales]
    plt.figure(figsize=(8, 8))
    plt.pie(lluvias_mensuales, labels=nombre_meses, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Proporción de Lluvias por Mes")
    plt.show()
