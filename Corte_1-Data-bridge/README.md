# Proyecto 1: Data Bridge — Smart Greenhouse

## Descripcion del Proyecto

Sistema de monitoreo para invernadero inteligente que simula sensores físicos (temperatura, humedad y nivel de agua), persiste los datos en archivos de texto plano y expone una interfaz web en PHP para búsqueda y visualización de registros en tiempo real con diseño glassmorphism.

## Objetivo

Aplicar operaciones fundamentales de manejo de archivos — escritura completa, lectura y filtrado por criterio — sin depender de ningún motor de base de datos, usando el sistema de archivos del servidor como único medio de persistencia.

## Tecnologías Utilizadas

- **Python** — generación de datos simulados y filtrado de registros
- **PHP** — servidor web, recepción de datos externos y renderizado HTML
- **HTML / CSS** — interfaz de usuario responsive con diseño glassmorphism

## Formatos de Archivo

| Archivo        | Formato                                  | Operación principal               | Justificación técnica                                                                                                                                                                                                                                     |
| -------------- | ---------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `maestro.txt`  | TXT plano (registros separados por coma) | Escritura completa (`write_text`) | Registro masivo de datos de sensores simulados. TXT secuencial es el formato más liviano para escritura de alta frecuencia sin estructura compleja. El modo append en `receptor.php` permite recibir datos de sensores reales sin leer el archivo previo. |
| `busqueda.txt` | TXT plano                                | Escritura completa / lectura      | Canal de comunicación entre PHP (`procesar.php`) y Python (`persistencia.py`). Al contener un único valor de criterio, TXT es el formato más simple y eficiente.                                                                                          |
| `filtrado.txt` | TXT plano                                | Escritura completa / lectura      | Almacena los resultados del último filtrado para ser consumidos por `tabla.php` sin necesidad de re-procesar el archivo maestro.                                                                                                                          |

## Estructura del Proyecto

```text
Corte_1-Data-bridge/
├── src/
│   ├── generador.py      ← Genera 1000 registros simulados en maestro.txt
│   ├── persistencia.py   ← Filtra maestro.txt → filtrado.txt (Python)
│   ├── persistencia.php  ← Misma lógica de filtrado implementada en PHP
│   ├── procesar.php      ← Orquestador: guarda criterio y ejecuta persistencia.py
│   ├── receptor.php      ← Endpoint GET para recibir datos de sensores reales
│   ├── tabla.php         ← Vista de resultados con tabla HTML coloreada por estado
│   ├── index.php         ← Interfaz principal de búsqueda (glassmorphism)
│   ├── maestro.txt       ← Base de datos plana con todos los registros
│   ├── busqueda.txt      ← Canal de comunicación PHP → Python
│   └── filtrado.txt      ← Resultados del último filtrado
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
