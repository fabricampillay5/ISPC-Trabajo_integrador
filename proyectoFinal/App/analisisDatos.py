# analisisDatos.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class AnalisisDatos:
    @staticmethod
    def crear_registro_pluvial(año):
        # Definir la ruta y crear el directorio si no existe
        path = os.path.join("datosAnalizados", f"registroPluvial{año}.csv")
        if not os.path.exists("datosAnalizados"):
            os.makedirs("datosAnalizados")  # Crea el directorio si no existe

        # Generar los datos aleatorios si el archivo no existe
        if not os.path.exists(path):
            data = np.random.rand(31, 12) * 100  # Precipitaciones aleatorias de 0 a 100
            df = pd.DataFrame(data, columns=[
                'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
            ])
            df.to_csv(path, index=False)
            print(f"[INFO] Archivo de registro pluvial '{path}' creado.")
        else:
            print(f"[INFO] Archivo '{path}' ya existe. Leyendo datos.")
        return pd.read_csv(path)

    @staticmethod
    def analizar_registro(año):
        df = AnalisisDatos.crear_registro_pluvial(año)
        print("Análisis del año", año)
        print("Máxima precipitación:", df.values.max())
        print("Mínima precipitación:", df.values.min())
        print("Promedio de precipitación:", df.values.mean())

        # Gráfico de barras
        df.sum().plot(kind='bar', title="Lluvias anuales")
        plt.show()

        # Gráfico de dispersión
        plt.scatter(x=np.repeat(range(1, 13), 31), y=np.tile(range(1, 32), 12), c=df.values.flatten())
        plt.colorbar(label="Precipitación")
        plt.title("Dispersión de lluvias anuales")
        plt.xlabel("Mes")
        plt.ylabel("Día")
        plt.show()

        # Gráfico circular (pie chart)
        plt.pie(df.sum(), labels=df.columns, autopct='%1.1f%%')
        plt.title("Distribución mensual de precipitaciones")
        plt.show()