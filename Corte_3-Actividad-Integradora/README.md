# Proyecto 3: Actividad-Integradora

## Descripcion

Sistema de análisis de datos de ventas de una tienda de tecnología. Lee un archivo CSV con registros de tres productos (Laptop, Mouse, Teclado) durante seis meses, calcula estadísticas agregadas por producto y por mes, genera tres gráficas de visualización exportadas en PNG y muestra un resumen de datos clave en consola

## Objetivo

Demostrar el uso de archivos CSV como fuente de datos estructurados para análisis estadístico, aplicando lectura, transformación y visualización sin intervención de bases de datos. Evaluar CSV como formato adecuado para datos tabulares de análisis comercial.

## Tecnologias Utilizadas

- **Python 3** — lenguaje principal
- **Pandas** — lectura de CSV, agrupaciones y cálculos estadísticos
- **Matplotlib** — generación de 3 gráficas (barras, líneas y pastel)

## Formatos de Archivos

| Archivo                 | Formato | Operación principal                  | Justificación técnica                                                                                                                                                                                                                               |
| ----------------------- | ------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ventas_tecnologia.csv` | CSV     | Lectura completa con `pd.read_csv()` | CSV es el estándar para datos tabulares de análisis. Su estructura de columnas facilita la carga directa en DataFrame con soporte nativo en Pandas para agrupaciones, ordenamiento categórico y cálculos estadísticos sin transformaciones previas. |
| `graficas_ventas.png`   | PNG     | Escritura con `plt.savefig(dpi=150)` | Formato de imagen sin pérdida, adecuado para reportes con gráficas de alta resolución. El parámetro `dpi=150` garantiza calidad para presentaciones.                                                                                                |

## Estructura del Proyecto

```text
Corte_3-Actividad-Integradora/
├── src/
│   ├── analisis_ventas.py       ← Script principal: análisis y generación de gráficas
│   ├── ventas_tecnologia.csv    ← Fuente de datos: 18 registros (3 productos × 6 meses)
│   └── graficas_ventas.png      ← Las 3 gráficas exportadas en un solo archivo PNG
└── README.md
```

## Enlace del Repositorio Inicial del proyecto

https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio

## Enlaces de los Repositorios Del Portafolio De Arquitectura y Organizacion De Datos

| Proyectos                              | Tecnologías                              | Formatos de Archivo | Enlace Directo                                                                                                      |
| -------------------------------------- | ---------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Proyecto-Corte-1-Data-bridge           | Python, PHP, HTML                        | .txt                | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_1-Data-bridge)           |
| Proyecto-Corte-2-Control de acceso     | MicroPython, PHP, HTML/CSS/JS            | .json, .txt         | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_2-Control%20de%20acceso) |
| Proyecto-Corte-3-Actividad-integradora | Python, Pandas, Matplotlib               | .csv, .png          | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_3-Actividad-Integradora) |
| Proyecto-Corte-4-Evaluacion_General_OA | Python, Pandas, Matplotlib, ijson, Faker | .csv, .json, .txt   | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_4-Evaluacion_General_OA) |
