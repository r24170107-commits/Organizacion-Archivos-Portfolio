<?php
// receptor.php
// Recibe datos desde una Raspberry Pi o navegador mediante GET.
// Ejemplo:
// receptor.php?dato=A1,Temperatura,28,ON

if (isset($_GET["dato"])) {
    $dato = trim($_GET["dato"]);

    if ($dato === "") {
        http_response_code(400);
        echo "ERROR: el parámetro dato está vacío.";
        exit;
    }

    file_put_contents("maestro.txt", $dato . PHP_EOL, FILE_APPEND);

    echo "OK: dato guardado correctamente -> " . htmlspecialchars($dato, ENT_QUOTES, "UTF-8");
} else {
    http_response_code(400);
    echo "ERROR: falta el parámetro dato. Ejemplo: receptor.php?dato=A1,Temperatura,28,ON";
}
?>