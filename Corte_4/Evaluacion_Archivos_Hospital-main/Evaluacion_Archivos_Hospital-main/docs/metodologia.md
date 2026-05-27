# Metodología experimental

## Descripción de la metodología

Para el desarrollo del proyecto se utilizó una metodología experimental, debido a que se compararon dos organizaciones de archivos: CSV y JSON. El objetivo fue medir su comportamiento al almacenar, leer y procesar datos simulados de un sistema hospitalario.

El sistema fue desarrollado en Python y se dividió en diferentes módulos para organizar mejor el trabajo. Cada módulo cumple una función específica dentro del proyecto.

## Generación de datos

La generación de datos se realizó mediante el archivo `src/generar_datos.py`.

Este programa permite crear registros simulados de pacientes con los siguientes campos:

- ID del paciente.
- Nombre.
- Edad.
- Temperatura.
- Presión arterial.
- Medicamento recetado.
- Especialidad médica.
- Enfermedad.

Los datos se generan en dos formatos:

- CSV.
- JSON.

El formato CSV almacena la información de manera tabular, usando filas y columnas. El formato JSON almacena la información con una estructura jerárquica, permitiendo agrupar los datos de consulta dentro de cada paciente.

## Implementación del sistema

La implementación principal se realizó en los archivos `src/sistema.py` y `src/main.py`.

El sistema permite:

- Leer archivos CSV y JSON.
- Buscar pacientes por ID o nombre.
- Agregar nuevos pacientes en archivos CSV.
- Generar reportes de búsqueda.
- Mostrar estadísticas básicas.

Para comprobar el funcionamiento inicial, se utilizó un conjunto de prueba de 1000 registros.

## Experimentación

La experimentación se realizó mediante el archivo `src/experimentacion.py`.

En esta fase se compararon los formatos CSV y JSON mediante las siguientes métricas:

- Tiempo de escritura.
- Tiempo de lectura.
- Tamaño del archivo.
- Registros leídos.
- Facilidad de procesamiento.
- Facilidad de visualización.
- Flexibilidad para almacenar información compleja.

Los resultados de la experimentación se guardaron en el archivo:

`reportes/resultados_experimentacion.csv`

## Visualización de datos

La visualización de datos se realizó mediante el archivo `src/visualizacion.py`.

El sistema genera gráficas para facilitar la interpretación de la información. Las gráficas creadas fueron:

- Gráfica de barras de pacientes por rango de edad.
- Gráfica circular de medicamentos más recetados.
- Gráfica de líneas de temperatura promedio por especialidad.
- Histograma de distribución de edades.
- Gráfica comparativa de tiempo de lectura entre CSV y JSON.

Las imágenes generadas se guardaron en la carpeta `graficas/`.

## Análisis de datos

El análisis de datos se realizó mediante el archivo `src/analisis.py`.

En esta fase se obtuvieron:

- Promedios.
- Máximos.
- Mínimos.
- Frecuencias.
- Distribución de pacientes por edad.
- Medicamentos más utilizados.
- Especialidades más frecuentes.
- Enfermedades más frecuentes.

Los reportes generados se guardaron en la carpeta `reportes/`.

## Herramientas utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:

- Python.
- Pandas.
- Matplotlib.
- Faker.
- ijson.
- Visual Studio Code.
- Git y GitHub.
- Windows.