# Conclusiones y evaluación del sistema

## Evaluación del sistema

Después de realizar las pruebas experimentales con archivos CSV y JSON, se compararon aspectos como el tiempo de escritura, tiempo de lectura, tamaño del archivo, facilidad de procesamiento, facilidad de visualización y flexibilidad para almacenar información compleja.

Con una prueba inicial de 1000 registros se obtuvieron los siguientes resultados:

| Formato | Tiempo de escritura | Tiempo de lectura | Tamaño del archivo |
|---|---:|---:|---:|
| CSV | 0.02 segundos | 0.01 segundos | 0.07 MB |
| JSON | 0.03 segundos | 0.01 segundos | 0.20 MB |

## 1. ¿Qué organización fue más eficiente?

La organización de archivos CSV fue más eficiente en la prueba inicial, debido a que presentó menor tiempo de escritura y menor tamaño de archivo en comparación con JSON.

CSV es un formato más simple y tabular, por lo que resulta adecuado para manejar grandes cantidades de registros cuando la información tiene una estructura plana.

## 2. ¿Cuál fue más flexible?

JSON fue el formato más flexible, ya que permite almacenar información con una estructura jerárquica o anidada.

En este proyecto, JSON permitió guardar los datos de la consulta médica dentro de una estructura interna, incluyendo temperatura, presión, medicamento, especialidad y enfermedad.

## 3. ¿Cuál facilita más el análisis de datos?

CSV facilita más el análisis de datos cuando se usan herramientas como Python y Pandas, porque los datos están organizados en columnas y filas.

Esto permite calcular promedios, máximos, mínimos, frecuencias y generar gráficas de forma más directa.

## 4. ¿Cuál consume menos almacenamiento?

CSV consume menos almacenamiento. En la prueba inicial con 1000 registros, el archivo CSV ocupó aproximadamente 0.07 MB, mientras que el archivo JSON ocupó aproximadamente 0.20 MB.

Esto indica que JSON requiere más espacio debido a que almacena etiquetas y estructuras adicionales.

## 5. ¿Qué formato se recomendaría para hospitales reales?

Para un hospital real, se podría recomendar el uso de una combinación de ambos formatos dependiendo de la necesidad.

CSV sería recomendable para reportes tabulares, análisis estadístico y exportación de datos.

JSON sería recomendable para almacenar información más compleja, como historial clínico, consultas anidadas, medicamentos, diagnósticos y datos relacionados con cada paciente.

Sin embargo, para un sistema hospitalario real, lo más adecuado sería utilizar una base de datos, ya que ofrece mayor seguridad, control, consultas avanzadas y manejo eficiente de grandes volúmenes de información.

## Conclusión general

El proyecto permitió comprobar que la organización de archivos influye directamente en el rendimiento, el tamaño de almacenamiento y la facilidad de procesamiento de los datos.

CSV mostró mejores resultados en eficiencia y almacenamiento, mientras que JSON presentó mayor flexibilidad para representar información compleja.

Con base en los resultados iniciales, CSV es más conveniente para análisis rápido y reportes, mientras que JSON es más útil cuando se requiere representar estructuras más completas.

