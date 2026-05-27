<?php
// Leer el archivo auditoria.txt
$lines = file("auditoria.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// Tomar las últimas 20 líneas (historial corto)
$last = array_slice($lines, -20);

// Crear arreglo para guardar datos
$result = [];

// Recorrer cada línea y sacar temperatura y estado
foreach ($last as $line) {
    // Ejemplo de línea: "2026-04-12 01:45:12 - Temp:29.5°C - VENTILADOR ENCENDIDO"
    preg_match("/Temp:(.*?)°C - (.*)/", $line, $matches);

    // Guardar en formato JSON
    $result[] = [
        "fecha" => substr($line,0,19),   // fecha y hora
        "temperatura" => floatval($matches[1]), // valor numérico
        "rele" => $matches[2]            // estado del ventilador
    ];
}

// Mandar respuesta en JSON
header('Content-Type: application/json');
echo json_encode($result);
?>