import os
import argparse
import pandas as pd


def crear_carpetas():
    os.makedirs("reportes", exist_ok=True)


def analisis_descriptivo(ruta_csv):
    df = pd.read_csv(ruta_csv)

    resultados = {
        "total_pacientes": len(df),
        "promedio_edad": round(df["edad"].mean(), 2),
        "edad_maxima": df["edad"].max(),
        "edad_minima": df["edad"].min(),
        "temperatura_promedio": round(df["temperatura"].mean(), 2),
        "temperatura_maxima": df["temperatura"].max(),
        "temperatura_minima": df["temperatura"].min()
    }

    reporte = pd.DataFrame([resultados])
    reporte.to_csv("reportes/analisis_descriptivo.csv", index=False)

    print("Reporte generado: reportes/analisis_descriptivo.csv")


def frecuencia_medicamentos(ruta_csv):
    df = pd.read_csv(ruta_csv)

    frecuencia = df["medicamento"].value_counts()
    frecuencia.to_csv("reportes/frecuencia_medicamentos.csv", header=["frecuencia"])

    print("Reporte generado: reportes/frecuencia_medicamentos.csv")


def frecuencia_especialidades(ruta_csv):
    df = pd.read_csv(ruta_csv)

    frecuencia = df["especialidad"].value_counts()
    frecuencia.to_csv("reportes/frecuencia_especialidades.csv", header=["frecuencia"])

    print("Reporte generado: reportes/frecuencia_especialidades.csv")


def frecuencia_enfermedades(ruta_csv):
    df = pd.read_csv(ruta_csv)

    frecuencia = df["enfermedad"].value_counts()
    frecuencia.to_csv("reportes/frecuencia_enfermedades.csv", header=["frecuencia"])

    print("Reporte generado: reportes/frecuencia_enfermedades.csv")


def distribucion_edades(ruta_csv):
    df = pd.read_csv(ruta_csv)

    rangos = pd.cut(
        df["edad"],
        bins=[0, 18, 30, 45, 60, 100],
        labels=["0-18", "19-30", "31-45", "46-60", "61+"]
    )

    distribucion = rangos.value_counts().sort_index()
    distribucion.to_csv("reportes/distribucion_edades.csv", header=["cantidad"])

    print("Reporte generado: reportes/distribucion_edades.csv")


def interpretar_resultados(ruta_csv):
    df = pd.read_csv(ruta_csv)

    medicamento_top = df["medicamento"].value_counts().idxmax()
    especialidad_top = df["especialidad"].value_counts().idxmax()
    enfermedad_top = df["enfermedad"].value_counts().idxmax()
    temperatura_promedio = round(df["temperatura"].mean(), 2)
    edad_promedio = round(df["edad"].mean(), 2)

    texto = f"""
INTERPRETACION DE RESULTADOS

1. Tendencia encontrada:
La edad promedio de los pacientes fue de {edad_promedio} años, lo que permite observar una distribución general de pacientes de diferentes edades.

2. Patrones de consultas:
La especialidad médica con mayor frecuencia fue {especialidad_top}, lo que indica que esta área tuvo mayor cantidad de consultas dentro de los datos simulados.

3. Distribución de pacientes:
La distribución por rangos de edad se encuentra registrada en el archivo reportes/distribucion_edades.csv.

4. Medicamento más utilizado:
El medicamento más recetado fue {medicamento_top}, lo que permite identificar uno de los tratamientos más frecuentes.

5. Enfermedad más frecuente:
La enfermedad con mayor frecuencia fue {enfermedad_top}, por lo que puede considerarse como una de las condiciones más comunes en el conjunto de datos.

6. Temperatura promedio:
La temperatura promedio registrada fue de {temperatura_promedio} °C.
"""

    with open("reportes/interpretacion_resultados.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print("Reporte generado: reportes/interpretacion_resultados.txt")


def main():
    parser = argparse.ArgumentParser(description="Analisis de datos hospitalarios")
    parser.add_argument("--csv", required=True, help="Ruta del archivo CSV")

    args = parser.parse_args()

    crear_carpetas()

    analisis_descriptivo(args.csv)
    frecuencia_medicamentos(args.csv)
    frecuencia_especialidades(args.csv)
    frecuencia_enfermedades(args.csv)
    distribucion_edades(args.csv)
    interpretar_resultados(args.csv)

    print("Analisis de datos finalizado.")


if __name__ == "__main__":
    main()