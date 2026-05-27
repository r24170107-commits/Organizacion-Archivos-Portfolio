# Resultados, gráficas y comparaciones

## Resultados de la experimentación

Durante la prueba experimental se generaron 1,000,000 de registros simulados de pacientes en los formatos CSV y JSON. Posteriormente, se midieron el tiempo de escritura, tiempo de lectura, tamaño del archivo y cantidad de registros leídos.

Los resultados obtenidos fueron los siguientes:

| Formato | Tiempo de escritura | Tiempo de lectura | Tamaño del archivo | Registros leídos |
|---|---:|---:|---:|---:|
| CSV | 15.36 segundos | 1.91 segundos | 75.7 MB | 1,000,000 |
| JSON | 29.85 segundos | 3.19 segundos | 198.73 MB | 1,000,000 |

## Comparación de resultados

Con base en los resultados obtenidos con 1,000,000 de registros, el formato CSV presentó un mejor desempeño en escritura, lectura y almacenamiento.

El archivo CSV ocupó 75.7 MB, mientras que el archivo JSON ocupó 198.73 MB. Esto muestra que CSV consume menos espacio de almacenamiento.

También se observó que el tiempo de escritura fue menor en CSV, con 15.36 segundos, mientras que JSON tardó 29.85 segundos. En lectura, CSV tardó 1.91 segundos y JSON tardó 3.19 segundos.

Esto se debe a que CSV utiliza una estructura simple basada en filas y columnas, mientras que JSON utiliza una estructura jerárquica con etiquetas y datos anidados.

Sin embargo, JSON ofrece mayor flexibilidad para representar información compleja, como los datos de una consulta médica dentro de cada paciente.

## Gráficas generadas

Durante la fase de visualización se generaron las siguientes gráficas:

1. `graficas/pacientes_por_rango_edad.png`

Esta gráfica muestra la cantidad de pacientes agrupados por rangos de edad. Permite identificar la distribución general de los pacientes dentro del conjunto de datos.

2. `graficas/medicamentos_mas_recetados.png`

Esta gráfica circular muestra los medicamentos más recetados dentro de los registros simulados. Permite observar rápidamente qué medicamentos aparecen con mayor frecuencia.

3. `graficas/temperatura_promedio_especialidad.png`

Esta gráfica de líneas muestra la temperatura promedio de los pacientes agrupada por especialidad médica. Permite comparar el comportamiento de la temperatura entre diferentes áreas médicas.

4. `graficas/histograma_edades.png`

El histograma permite observar la distribución de edades de los pacientes. Esta gráfica ayuda a identificar si los pacientes se concentran en ciertos rangos de edad.

5. `graficas/comparacion_tiempo_lectura.png`

Esta gráfica compara el tiempo de lectura entre CSV y JSON. Sirve para visualizar cuál formato fue más rápido durante la fase experimental.

## Análisis descriptivo

El análisis descriptivo permitió obtener información básica del conjunto de datos, como:

- Total de pacientes.
- Edad promedio.
- Edad máxima.
- Edad mínima.
- Temperatura promedio.
- Temperatura máxima.
- Temperatura mínima.

Los resultados fueron guardados en:

`reportes/analisis_descriptivo.csv`

## Frecuencias encontradas

También se generaron reportes de frecuencia para identificar los elementos más repetidos dentro del conjunto de datos.

Los reportes generados fueron:

- `reportes/frecuencia_medicamentos.csv`
- `reportes/frecuencia_especialidades.csv`
- `reportes/frecuencia_enfermedades.csv`
- `reportes/distribucion_edades.csv`

Estos archivos permiten identificar medicamentos más utilizados, especialidades más frecuentes, enfermedades comunes y distribución de pacientes por rango de edad.

## Interpretación de resultados

A partir de los datos simulados, se identificaron patrones relacionados con la distribución de pacientes, medicamentos recetados, enfermedades frecuentes y especialidades médicas con mayor presencia.

El formato CSV resultó más adecuado para el análisis tabular y estadístico, mientras que JSON resultó más adecuado para representar información estructurada y jerárquica.

## Comparación general CSV vs JSON

| Criterio | CSV | JSON |
|---|---|---|
| Tiempo de escritura | Más rápido: 15.36 segundos | Más lento: 29.85 segundos |
| Tiempo de lectura | Más rápido: 1.91 segundos | Más lento: 3.19 segundos |
| Tamaño del archivo | Menor tamaño: 75.7 MB | Mayor tamaño: 198.73 MB |
| Procesamiento con Pandas | Más directo | Requiere más transformación |
| Visualización | Más sencilla | Requiere adaptar datos |
| Flexibilidad | Media | Alta |
| Estructura | Tabular | Jerárquica |

## Resultado general

En la prueba con 1,000,000 de registros, CSV fue más eficiente en almacenamiento, escritura y lectura.

JSON fue menos eficiente en tamaño y tiempo, pero presentó mayor flexibilidad para representar información compleja y estructurada.

Por esta razón, CSV se considera más útil para análisis estadístico, generación de reportes y manejo de datos tabulares, mientras que JSON se considera más útil cuando se requiere almacenar datos con estructura más detallada.

Durante la prueba experimental se generaron 20,000,000 de registros simulados de pacientes en los formatos CSV y JSON. Posteriormente, se midieron el tiempo de escritura, tiempo de lectura, tamaño del archivo y cantidad de registros leídos.

Los resultados obtenidos fueron los siguientes:

| Formato | Tiempo de escritura | Tiempo de lectura | Tamaño del archivo | Registros leídos |
|---|---:|---:|---:|---:|
| CSV | 305.99 segundos | 37.17 segundos | 1543.72 MB | 20,000,000 |
| JSON | 624.33 segundos | 67.23 segundos | 4004.19 MB | 20,000,000 |