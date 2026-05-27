import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt


def crear_carpetas():
    os.makedirs("graficas", exist_ok=True)


def grafica_pacientes_por_edad(ruta_csv):
    df = pd.read_csv(ruta_csv)

    rangos = pd.cut(
        df["edad"],
        bins=[0, 18, 30, 45, 60, 100],
        labels=["0-18", "19-30", "31-45", "46-60", "61+"]
    )

    conteo = rangos.value_counts().sort_index()

    plt.figure()
    conteo.plot(kind="bar")
    plt.title("Pacientes por rango de edad")
    plt.xlabel("Rango de edad")
    plt.ylabel("Cantidad de pacientes")
    plt.tight_layout()
    plt.savefig("graficas/pacientes_por_rango_edad.png")
    plt.close()

    print("Grafica generada: graficas/pacientes_por_rango_edad.png")


def grafica_medicamentos_mas_recetados(ruta_csv):
    df = pd.read_csv(ruta_csv)

    conteo = df["medicamento"].value_counts().head(10)

    plt.figure()
    conteo.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Medicamentos mas recetados")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("graficas/medicamentos_mas_recetados.png")
    plt.close()

    print("Grafica generada: graficas/medicamentos_mas_recetados.png")


def grafica_temperatura_promedio(ruta_csv):
    df = pd.read_csv(ruta_csv)

    promedio = df.groupby("especialidad")["temperatura"].mean()

    plt.figure()
    promedio.plot(kind="line", marker="o")
    plt.title("Temperatura promedio por especialidad")
    plt.xlabel("Especialidad")
    plt.ylabel("Temperatura promedio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficas/temperatura_promedio_especialidad.png")
    plt.close()

    print("Grafica generada: graficas/temperatura_promedio_especialidad.png")


def histograma_edades(ruta_csv):
    df = pd.read_csv(ruta_csv)

    plt.figure()
    df["edad"].plot(kind="hist", bins=20)
    plt.title("Distribucion de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("graficas/histograma_edades.png")
    plt.close()

    print("Grafica generada: graficas/histograma_edades.png")


def grafica_comparacion_csv_json(ruta_resultados):
    if not os.path.exists(ruta_resultados):
        print("No se encontro el archivo de resultados de experimentacion.")
        return

    df = pd.read_csv(ruta_resultados)

    pivot = df.pivot_table(
        index="cantidad",
        columns="formato",
        values="tiempo_lectura_segundos",
        aggfunc="mean"
    )

    plt.figure()
    pivot.plot(kind="bar")
    plt.title("Comparacion de tiempo de lectura CSV vs JSON")
    plt.xlabel("Cantidad de registros")
    plt.ylabel("Tiempo de lectura en segundos")
    plt.tight_layout()
    plt.savefig("graficas/comparacion_tiempo_lectura.png")
    plt.close()

    print("Grafica generada: graficas/comparacion_tiempo_lectura.png")


def main():
    parser = argparse.ArgumentParser(description="Generador de graficas hospitalarias")
    parser.add_argument("--csv", required=True, help="Ruta del archivo CSV")
    parser.add_argument(
        "--resultados",
        default="reportes/resultados_experimentacion.csv",
        help="Ruta del archivo de resultados de experimentacion"
    )

    args = parser.parse_args()

    crear_carpetas()

    grafica_pacientes_por_edad(args.csv)
    grafica_medicamentos_mas_recetados(args.csv)
    grafica_temperatura_promedio(args.csv)
    histograma_edades(args.csv)
    grafica_comparacion_csv_json(args.resultados)

    print("Visualizacion de datos finalizada.")


if __name__ == "__main__":
    main()