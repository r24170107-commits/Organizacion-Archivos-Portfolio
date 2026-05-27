<?php
// procesar.php
// Recibe el criterio de búsqueda, lo guarda en busqueda.txt y ejecuta persistencia.py.

$criterio = "";

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["criterio"])) {
    $criterio = trim($_POST["criterio"]);
} elseif (isset($_GET["criterio"])) {
    $criterio = trim($_GET["criterio"]);
}

if ($criterio === "") {
    header("Location: index.php?error=vacio");
    exit;
}

file_put_contents("busqueda.txt", $criterio);

$python = "python3";
$script = "persistencia.py";

$comando = escapeshellcmd($python) . " " . escapeshellarg($script);

$salida = [];
$codigo = 0;
exec($comando, $salida, $codigo);

if ($codigo !== 0) {
    echo "<h2>Error al ejecutar persistencia.py</h2>";
    echo "<p>Verifica que Python 3 esté instalado y que el archivo persistencia.py exista.</p>";
    echo "<pre>" . htmlspecialchars(implode("\n", $salida)) . "</pre>";
    echo '<p><a href="index.php">Volver</a></p>';
    exit;
}

header("Location: tabla.php");
exit;
?>