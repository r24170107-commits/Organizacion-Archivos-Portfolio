# persistencia.py
# Lee busqueda.txt, filtra maestro.txt y guarda coincidencias en filtrado.txt.

from pathlib import Path

BASE = Path(__file__).resolve().parent

archivo_busqueda = BASE / "busqueda.txt"
archivo_maestro = BASE / "maestro.txt"
archivo_filtrado = BASE / "filtrado.txt"

def normalizar(texto):
    return texto.strip().lower()

def main():
    if not archivo_busqueda.exists():
        archivo_filtrado.write_text("", encoding="utf-8")
        return

    criterio = normalizar(archivo_busqueda.read_text(encoding="utf-8"))

    if not archivo_maestro.exists():
        archivo_maestro.write_text("", encoding="utf-8")

    lineas = archivo_maestro.read_text(encoding="utf-8").splitlines()

    if criterio == "":
        resultados = lineas
    else:
        resultados = [
            linea for linea in lineas
            if criterio in normalizar(linea)
        ]

    archivo_filtrado.write_text(
        "\n".join(resultados) + ("\n" if resultados else ""),
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()