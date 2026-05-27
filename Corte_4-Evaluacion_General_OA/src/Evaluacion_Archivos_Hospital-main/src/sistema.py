import csv
import json
import os


def leer_csv(ruta):
    pacientes = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            pacientes.append(fila)

    return pacientes


def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos["pacientes"]


def buscar_paciente_csv(ruta, busqueda):
    encontrados = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            if fila["id"] == busqueda or busqueda.lower() in fila["nombre"].lower():
                encontrados.append(fila)

    return encontrados


def buscar_paciente_json(ruta, busqueda):
    encontrados = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for paciente in datos["pacientes"]:
        if str(paciente["id"]) == busqueda or busqueda.lower() in paciente["nombre"].lower():
            encontrados.append(paciente)

    return encontrados


def agregar_paciente_csv(ruta):
    nuevo = {
        "id": input("ID del paciente: "),
        "nombre": input("Nombre: "),
        "edad": input("Edad: "),
        "temperatura": input("Temperatura: "),
        "presion": input("Presion arterial: "),
        "medicamento": input("Medicamento: "),
        "especialidad": input("Especialidad: "),
        "enfermedad": input("Enfermedad: ")
    }

    campos = [
        "id",
        "nombre",
        "edad",
        "temperatura",
        "presion",
        "medicamento",
        "especialidad",
        "enfermedad"
    ]

    existe = os.path.exists(ruta)

    with open(ruta, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        if not existe:
            escritor.writeheader()

        escritor.writerow(nuevo)

    print("Paciente agregado correctamente en CSV.")


def mostrar_estadisticas_csv(ruta):
    total = 0
    suma_edad = 0
    suma_temperatura = 0

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            total += 1
            suma_edad += int(fila["edad"])
            suma_temperatura += float(fila["temperatura"])

    if total == 0:
        print("No hay datos para mostrar.")
        return

    print("\n===== ESTADISTICAS BASICAS =====")
    print(f"Total de pacientes: {total}")
    print(f"Edad promedio: {suma_edad / total:.2f}")
    print(f"Temperatura promedio: {suma_temperatura / total:.2f}")


def generar_reporte_busqueda(resultados):
    os.makedirs("reportes", exist_ok=True)

    ruta_reporte = "reportes/reporte_busqueda.txt"

    with open(ruta_reporte, "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE BUSQUEDA DE PACIENTES\n")
        archivo.write("=" * 45 + "\n\n")

        if not resultados:
            archivo.write("No se encontraron pacientes.\n")
        else:
            for paciente in resultados:
                archivo.write(str(paciente))
                archivo.write("\n\n")

    print(f"Reporte generado en: {ruta_reporte}")