<?php
// Recibir datos en formato JSON (la Pico los manda con POST)
$data = json_decode(file_get_contents("php://input"), true);

// Revisar si llegaron datos
if ($data) {
    // Crear línea con fecha, temperatura y estado del ventilador
    $line = date("Y-m-d H:i:s") . " - Temp:" . $data['temperatura'] . "°C - " . $data['rele'] . "\n";

    // Guardar en auditoria.txt (se agrega al final)
    file_put_contents("auditoria.txt", $line, FILE_APPEND);

    // Responder a la Pico que todo salió bien
    http_response_code(200);
    echo "OK";
} else {
    // Si no llegaron datos válidos, mandar error
    http_response_code(400);
    echo "Error: datos inválidos";
}
?>