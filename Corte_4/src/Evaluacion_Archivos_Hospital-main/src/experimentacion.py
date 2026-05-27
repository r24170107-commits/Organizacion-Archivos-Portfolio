import csv
import os
import time
import argparse
import ijson

from generar_datos import crear_carpetas, generar_csv, generar_json


def medir_tamano_mb(ruta):
    return os.path.getsize(ruta) / (1024 * 1024)


def medir_lectura_csv(ruta):
    inicio = time.time()
    total = 0

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for _ in lector:
            total += 1

    fin = time.time()
    return fin - inicio, total


def medir_lectura_json(ruta):
    inicio = time.time()
    total = 0

    with open(ruta, "r", encoding="utf-8") as archivo:
        for _ in ijson.items(archivo, "pacientes.item"):
            total += 1

    fin = time.time()
    return fin - inicio, total


def guardar_resultados(resultados):
    os.makedirs("reportes", exist_ok=True)

    ruta = "reportes/resultados_experimentacion.csv"

    campos = [
        "cantidad",
        "formato",
        "tiempo_escritura_segundos",
        "tiempo_lectura_segundos",
        "tamano_mb",
        "registros_leidos",
        "facilidad_procesamiento",
        "facilidad_visualizacion",
        "flexibilidad"
    ]

    existe = os.path.exists(ruta)

    with open(ruta, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        if not existe:
            escritor.writeheader()

        for resultado in resultados:
            escritor.writerow(resultado)

    print(f"Resultados guardados en: {ruta}")


def experimentar(cantidad):
    crear_carpetas()
    resultados = []

    print("\n===== EXPERIMENTO CSV =====")
    inicio = time.time()
    generar_csv(cantidad)
    tiempo_escritura_csv = time.time() - inicio

    ruta_csv = f"datos/csv/pacientes_{cantidad}.csv"

    tiempo_lectura_csv, total_csv = medir_lectura_csv(ruta_csv)
    tamano_csv = medir_tamano_mb(ruta_csv)

    resultados.append({
        "cantidad": cantidad,
        "formato": "CSV",
        "tiempo_escritura_segundos": round(tiempo_escritura_csv, 2),
        "tiempo_lectura_segundos": round(tiempo_lectura_csv, 2),
        "tamano_mb": round(tamano_csv, 2),
        "registros_leidos": total_csv,
        "facilidad_procesamiento": "Alta",
        "facilidad_visualizacion": "Alta",
        "flexibilidad": "Media"
    })

    print("\n===== EXPERIMENTO JSON =====")
    inicio = time.time()
    generar_json(cantidad)
    tiempo_escritura_json = time.time() - inicio

    ruta_json = f"datos/json/pacientes_{cantidad}.json"

    tiempo_lectura_json, total_json = medir_lectura_json(ruta_json)
    tamano_json = medir_tamano_mb(ruta_json)

    resultados.append({
        "cantidad": cantidad,
        "formato": "JSON",
        "tiempo_escritura_segundos": round(tiempo_escritura_json, 2),
        "tiempo_lectura_segundos": round(tiempo_lectura_json, 2),
        "tamano_mb": round(tamano_json, 2),
        "registros_leidos": total_json,
        "facilidad_procesamiento": "Media",
        "facilidad_visualizacion": "Media",
        "flexibilidad": "Alta"
    })

    guardar_resultados(resultados)

    print("\n===== RESUMEN DEL EXPERIMENTO =====")
    for resultado in resultados:
        print(resultado)


def main():
    parser = argparse.ArgumentParser(description="Experimentacion CSV vs JSON")
    parser.add_argument("--cantidad", type=int, required=True, help="Cantidad de registros")

    args = parser.parse_args()

    experimentar(args.cantidad)


if __name__ == "__main__":
    main()