# Proyecto 2: Control de Acceso — Monitor de Temperatura con Raspberry Pi Pico W

## Descripcion

Este proyecto corresponde al Proyecto Corte 2 de la Unidad 3: Organización de Archivos Actuales. Su propósito es implementar un sistema embebido de Internet de las Cosas (IoT) que mide temperatura ambiental con un sensor DS18B20 conectado a una Raspberry Pi Pico W. El sistema controla automáticamente un ventilador de 12V mediante un relé y transmite los datos a un servidor PHP, donde se almacenan en un archivo de log y se visualizan en un dashboard en tiempo real inspirado en LabVIEW.

## Objetivo

Integrar un sistema embebido en MicroPython con un servidor web en PHP utilizando JSON como formato de transmisión y configuración, y archivo de texto plano como bitácora secuencial de lecturas, aplicando la selección correcta del formato según el patrón de acceso de cada capa del sistema.

## Tecnologias Utilizadas

- **MicroPython** — firmware de la Raspberry Pi Pico W (sensor, relé, WiFi, HTTP)
- **PHP** — receptor de datos y API interna de lecturas
- **HTML / CSS / JavaScript** — dashboard con gauge, display digital y gráfica en tiempo real
- **Chart.js** — gráfica de historial de temperatura
- **Canvas Gauges** — velocímetro analógico estilo LabVIEW

## Formatos de Archivos

| Archivo         | Formato                    | Operación principal                         | Justificación técnica                                                                                                                                                                                          |
| --------------- | -------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config.json`   | JSON                       | Lectura única al arrancar con `json.load()` | JSON permite acceso jerárquico mediante diccionarios, ideal para parámetros de configuración (pines GPIO, umbral de temperatura, credenciales WiFi, ID de sensor) que se modifican sin tocar el código fuente. |
| `auditoria.txt` | TXT plano (log secuencial) | Escritura con `FILE_APPEND`                 | El modo append registra cada evento sin leer el archivo previo, garantizando escritura O(1) en disco. Óptimo para bitácoras de IoT que escriben cada segundo de forma cíclica.                                 |

## Estructura del Proyecto

```text
Corte_2-Control de acceso/
├── src/
│   ├── main.py           ← Firmware MicroPython para Raspberry Pi Pico W
│   ├── Config.json       ← Configuración: WiFi, pines GPIO, umbral de temperatura
│   ├── Guardar_Datos.php ← Receptor HTTP: parsea JSON y hace append a auditoria.txt
│   ├── Index.php         ← Dashboard: gauge, display digital, gráfica en tiempo real
│   ├── Lecturas.php      ← API interna: sirve últimas 20 lecturas en JSON
│   ├── auditoria.txt     ← Bitácora secuencial de temperatura y estado del relé
│   └── ventilador.png    ← Imagen para animación CSS del ventilador
└── README.md
```

## Enlaces de los Repositorios Del Portafolio De Arquitectura y Organizacion De Datos

| Proyectos                              | Tecnologías                              | Formatos de Archivo | Enlace Directo                                                                                                      |
| -------------------------------------- | ---------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Proyecto-Corte-1-Data-bridge           | Python, PHP, HTML                        | .txt                | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_1-Data-bridge)           |
| Proyecto-Corte-2-Control de acceso     | MicroPython, PHP, HTML/CSS/JS            | .json, .txt         | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_2-Control%20de%20acceso) |
| Proyecto-Corte-3-Actividad-integradora | Python, Pandas, Matplotlib               | .csv, .png          | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_3-Actividad-Integradora) |
| Proyecto-Corte-4-Evaluacion_General_OA | Python, Pandas, Matplotlib, ijson, Faker | .csv, .json, .txt   | [Ver](https://github.com/r24170107-commits/Organizacion-Archivos-Portfolio/tree/main/Corte_4-Evaluacion_General_OA) |
