## Proyecto 4: Evaluacion-General-OA

## Descripcion

Sistema completo de gestión, análisis y benchmarking de datos hospitalarios. Genera registros sintéticos de pacientes con Faker (es_MX), los almacena en CSV y JSON, expone un menú interactivo de búsqueda y gestión, realiza análisis estadístico descriptivo, ejecuta pruebas de rendimiento comparando ambos formatos a diferentes escalas (hasta 20,000,000 de registros) y genera cinco gráficas de comportamiento del sistema.

## Objetivo

Evaluar de manera general los sistemas basados en archivos desarrollados durante el semestre, aplicando los temas finales de la materia: estimación de uso, escalabilidad, análisis de rendimiento y análisis costo-beneficio entre CSV y JSON, en el contexto de un sistema hospitalario real.

## Tecnologias Utilizadas

- **Python 3** — lenguaje principal de todos los módulos
- **Pandas** — análisis estadístico y generación de reportes CSV
- **Matplotlib** — generación de 5 gráficas de comportamiento del sistema
- **ijson** — lectura eficiente en streaming de archivos JSON de gran volumen
- **Faker (es_MX)** — generación de datos sintéticos en español mexicano

## Formatos de Archivos

| Archivo                          | Formato | Operación principal                                      | Justificación técnica                                                                                                                                                                                                       |
| -------------------------------- | ------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pacientes_N.csv`                | CSV     | Escritura secuencial / lectura con `csv.DictReader`      | Formato tabular de alta compatibilidad. Acceso columnar por nombre sin cargar el archivo completo en RAM. Más eficiente en almacenamiento: 75.7 MB vs 198.73 MB para 1,000,000 registros. Facilidad de procesamiento: Alta. |
| `pacientes_N.json`               | JSON    | Escritura incremental / lectura con `ijson` en streaming | Estructura jerárquica que anida los datos de consulta dentro de cada paciente. Se usa `ijson` para iterar registro a registro sin cargar el archivo completo en memoria. Flexibilidad: Alta.                                |
| `resultados_experimentacion.csv` | CSV     | Escritura con append (`'a'`)                             | Acumula resultados de múltiples corridas de benchmarking sin sobreescribir datos anteriores, permitiendo comparar pruebas con distintas cantidades de registros.                                                            |
| `reporte_busqueda.txt`           | TXT     | Escritura completa (`'w'`)                               | Reporte legible por humanos del resultado de la última búsqueda de paciente.                                                                                                                                                |
| `interpretacion_resultados.txt`  | TXT     | Escritura con f-strings (`'w'`)                          | Informe textual generado dinámicamente con estadísticas calculadas del CSV analizado.                                                                                                                                       |

## Estructura del Proyecto

```text
Corte_4-Evaluacion_General_OA/
├── src/
│   └── Evaluacion_Archivos_Hospital-main/
│       ├── src/
│       │   ├── main.py             ← Menú interactivo del sistema hospitalario
│       │   ├── sistema.py          ← CRUD: buscar, agregar, estadísticas, reportes
│       │   ├── analisis.py         ← Análisis estadístico descriptivo con Pandas
│       │   ├── experimentacion.py  ← Benchmarking: tiempo y tamaño CSV vs JSON
│       │   ├── generar_datos.py    ← Generador de datos sintéticos con Faker (es_MX)
│       │   └── visualizacion.py    ← 5 gráficas con Matplotlib
│       ├── reportes/               ← CSVs y TXTs generados por analisis.py
│       ├── graficas/               ← PNGs generados por visualizacion.py
│       ├── docs/
│       │   ├── introduccion.md
│       │   ├── metodologia.md
│       │   ├── resultados.md
│       │   └── conclusiones.md
│       └── requirements.txt
└── README.md
```

## Enlaces de los Repositorios Del Portafolio De Arquitectura y Organizacion De Datos

| Proyectos                              | Tecnologías                              | Formatos de Archivo | Enlace Directo                                                                                                      |
| -------------------------------------- | ---------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Proyecto-Corte-1-Data-bridge           | Python, PHP, HTML                        | .txt                | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_1-Data-bridge)           |
| Proyecto-Corte-2-Control de acceso     | MicroPython, PHP, HTML/CSS/JS            | .json, .txt         | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_2-Control%20de%20acceso) |
| Proyecto-Corte-3-Actividad-integradora | Python, Pandas, Matplotlib               | .csv, .png          | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_3-Actividad-Integradora) |
| Proyecto-Corte-4-Evaluacion_General_OA | Python, Pandas, Matplotlib, ijson, Faker | .csv, .json, .txt   | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_4-Evaluacion_General_OA) |
