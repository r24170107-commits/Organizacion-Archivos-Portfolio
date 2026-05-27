# generador.py
# Genera datos de prueba para maestro.txt.

from pathlib import Path
import random

BASE = Path(__file__).resolve().parent
archivo_maestro = BASE / "maestro.txt"

sensores = ["A1", "B2", "C3", "D4", "E5"]
tipos = ["Temperatura", "Humedad", "NivelAgua"]

def generar_valor(tipo):
    if tipo == "Temperatura":
        return random.randint(15, 42)
    if tipo == "Humedad":
        return random.randint(20, 95)
    if tipo == "NivelAgua":
        return random.randint(0, 100)
    return 0

def generar_estado(tipo, valor):
    if tipo == "NivelAgua" and valor <= 10:
        return "0%"
    if tipo == "Temperatura" and (valor < 18 or valor > 35):
        return "0%"
    if tipo == "Humedad" and (valor < 30 or valor > 85):
        return "0%"
    return random.choice(["ON", "ON", "ON", "OFF"])

def main(cantidad=1000):
    lineas = []

    for _ in range(cantidad):
        sensor = random.choice(sensores)
        tipo = random.choice(tipos)
        valor = generar_valor(tipo)
        estado = generar_estado(tipo, valor)
        lineas.append(f"{sensor},{tipo},{valor},{estado}")

    archivo_maestro.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"Se generaron {cantidad} registros en maestro.txt")

if __name__ == "__main__":
    main()