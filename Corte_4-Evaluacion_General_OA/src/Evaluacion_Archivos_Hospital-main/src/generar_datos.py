import csv
import json
import random
import os
import argparse
import time
from faker import Faker


fake = Faker("es_MX")

MEDICAMENTOS = [
    "Paracetamol", "Ibuprofeno", "Amoxicilina", "Loratadina",
    "Omeprazol", "Metformina", "Losartan", "Aspirina",
    "Salbutamol", "Naproxeno"
]

ESPECIALIDADES = [
    "Medicina General", "Cardiologia", "Pediatria", "Traumatologia",
    "Neurologia", "Dermatologia", "Ginecologia", "Urgencias",
    "Oftalmologia", "Endocrinologia"
]

ENFERMEDADES = [
    "Gripe", "Diabetes", "Hipertension", "Gastritis", "Asma",
    "Migrana", "Fractura", "Infeccion respiratoria", "Alergia", "Bronquitis"
]


def crear_carpetas():
    os.makedirs("datos/csv", exist_ok=True)
    os.makedirs("datos/json", exist_ok=True)
    os.makedirs("reportes", exist_ok=True)
    os.makedirs("graficas", exist_ok=True)


def generar_paciente(id_paciente):
    sistolica = random.randint(100, 160)
    diastolica = random.randint(60, 100)

    return {
        "id": id_paciente,
        "nombre": fake.name(),
        "edad": random.randint(1, 95),
        "temperatura": round(random.uniform(36.0, 40.5), 1),
        "presion": f"{sistolica}/{diastolica}",
        "medicamento": random.choice(MEDICAMENTOS),
        "especialidad": random.choice(ESPECIALIDADES),
        "enfermedad": random.choice(ENFERMEDADES)
    }


def generar_csv(cantidad):
    ruta = f"datos/csv/pacientes_{cantidad}.csv"

    campos = [
        "id", "nombre", "edad", "temperatura", "presion",
        "medicamento", "especialidad", "enfermedad"
    ]

    inicio = time.time()

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for i in range(1, cantidad + 1):
            escritor.writerow(generar_paciente(i))

            if i % 100000 == 0:
                print(f"CSV: {i} registros generados...")

    fin = time.time()
    print(f"Archivo CSV generado: {ruta}")
    print(f"Tiempo CSV: {fin - inicio:.2f} segundos")


def generar_json(cantidad):
    ruta = f"datos/json/pacientes_{cantidad}.json"

    inicio = time.time()

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write('{"pacientes":[\n')

        for i in range(1, cantidad + 1):
            paciente = generar_paciente(i)

            paciente_json = {
                "id": paciente["id"],
                "nombre": paciente["nombre"],
                "edad": paciente["edad"],
                "consulta": {
                    "temperatura": paciente["temperatura"],
                    "presion": paciente["presion"],
                    "medicamento": paciente["medicamento"],
                    "especialidad": paciente["especialidad"],
                    "enfermedad": paciente["enfermedad"]
                }
            }

            json.dump(paciente_json, archivo, ensure_ascii=False)

            if i < cantidad:
                archivo.write(",\n")
            else:
                archivo.write("\n")

            if i % 100000 == 0:
                print(f"JSON: {i} registros generados...")

        archivo.write("]}")

    fin = time.time()
    print(f"Archivo JSON generado: {ruta}")
    print(f"Tiempo JSON: {fin - inicio:.2f} segundos")


def main():
    parser = argparse.ArgumentParser(description="Generador de datos hospitalarios")
    parser.add_argument("--cantidad", type=int, required=True, help="Cantidad de registros")
    parser.add_argument("--formato", choices=["csv", "json", "ambos"], default="ambos")

    args = parser.parse_args()

    crear_carpetas()

    if args.formato in ["csv", "ambos"]:
        generar_csv(args.cantidad)

    if args.formato in ["json", "ambos"]:
        generar_json(args.cantidad)

    print("Generacion de datos finalizada.")


if __name__ == "__main__":
    main()