<?php
// persistencia.php
// Versión PHP del filtrado.
// Lee busqueda.txt, filtra maestro.txt y guarda los resultados en filtrado.txt.

$archivo_busqueda = "busqueda.txt";
$archivo_maestro = "maestro.txt";
$archivo_filtrado = "filtrado.txt";

$buscar = "";

if (file_exists($archivo_busqueda)) {
    $buscar = trim(file_get_contents($archivo_busqueda));
}

if (!file_exists($archivo_maestro)) {
    file_put_contents($archivo_maestro, "");
}

$lineas = file($archivo_maestro, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$resultados = [];

foreach ($lineas as $renglon) {
    if ($buscar === "" || stripos($renglon, $buscar) !== false) {
        $resultados[] = $renglon;
    }
}

file_put_contents($archivo_filtrado, implode(PHP_EOL, $resultados));

header("Location: tabla.php");
exit;
?>