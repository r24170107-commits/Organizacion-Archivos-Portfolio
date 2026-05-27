<?php
// tabla.php
// Muestra el contenido de filtrado.txt en una tabla HTML.

$nombre_archivo = "filtrado.txt";
$busqueda_archivo = "busqueda.txt";
$criterio = file_exists($busqueda_archivo) ? trim(file_get_contents($busqueda_archivo)) : "";

$lineas = [];

if (file_exists($nombre_archivo)) {
    $lineas = file($nombre_archivo, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $lineas = array_reverse($lineas);
}

function limpiar($valor) {
    return htmlspecialchars(trim($valor), ENT_QUOTES, "UTF-8");
}

function clase_estado($estado) {
    $estado_limpio = strtoupper(trim($estado));

    if ($estado_limpio === "ON" || $estado_limpio === "ACTIVO") {
        return "activo";
    }

    if ($estado_limpio === "OFF" || $estado_limpio === "INACTIVO") {
        return "inactivo";
    }

    if ($estado_limpio === "0%" || $estado_limpio === "ALERTA") {
        return "alerta";
    }

    return "normal";
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Smart Greenhouse - Resultados</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #eef7f0;
            color: #1b2e22;
            padding: 30px;
        }

        .contenedor {
            max-width: 1100px;
            margin: auto;
        }

        .header {
            background: white;
            border-radius: 18px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            margin-bottom: 22px;
        }

        h1 {
            margin: 0 0 8px;
        }

        .acciones {
            margin-top: 18px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        a, button {
            background: #1f8f4d;
            color: white;
            padding: 11px 16px;
            border-radius: 10px;
            text-decoration: none;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }

        a:hover, button:hover {
            background: #176c3a;
        }

        .tabla-card {
            overflow-x: auto;
            background: white;
            border-radius: 18px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 700px;
        }

        th, td {
            padding: 14px;
            text-align: left;
            border-bottom: 1px solid #e4e4e4;
        }

        th {
            background: #1f8f4d;
            color: white;
        }

        tr.activo {
            border-left: 8px solid #18a558;
            background: #ecfff3;
        }

        tr.inactivo {
            border-left: 8px solid #d93636;
            background: #fff1f1;
        }

        tr.alerta {
            border-left: 8px solid #f3b51b;
            background: #fff8e1;
        }

        tr.normal {
            border-left: 8px solid #7c8a99;
        }

        .vacio {
            background: white;
            border-radius: 18px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }

        .contador {
            display: inline-block;
            background: #e1f5e8;
            color: #176c3a;
            padding: 8px 12px;
            border-radius: 999px;
            font-weight: bold;
        }

        .estado {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <main class="contenedor">
        <section class="header">
            <h1>📊 Resultados del Smart Greenhouse</h1>
            <p>
                Criterio buscado:
                <strong><?php echo limpiar($criterio !== "" ? $criterio : "Sin criterio"); ?></strong>
            </p>
            <span class="contador">Registros encontrados: <?php echo count($lineas); ?></span>

            <div class="acciones">
                <a href="index.php">Nueva búsqueda</a>
                <a href="maestro.txt" target="_blank">Ver maestro.txt</a>
                <a href="filtrado.txt" target="_blank">Ver filtrado.txt</a>
            </div>
        </section>

        <?php if (count($lineas) === 0): ?>
            <section class="vacio">
                <h2>No se encontraron resultados</h2>
                <p>Prueba buscar por A1, B2, Temperatura, Humedad, NivelAgua, ON, OFF o 0%.</p>
            </section>
        <?php else: ?>
            <section class="tabla-card">
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Sensor</th>
                            <th>Tipo</th>
                            <th>Valor</th>
                            <th>Estado / Bomba</th>
                        </tr>
                    </thead>
                    <tbody>
                    <?php foreach ($lineas as $indice => $linea): ?>
                        <?php
                            $partes = array_map("trim", explode(",", $linea));
                            $sensor = $partes[0] ?? "Sin dato";
                            $tipo = $partes[1] ?? "Sin dato";
                            $valor = $partes[2] ?? "Sin dato";
                            $estado = $partes[3] ?? "Sin dato";
                            $clase = clase_estado($estado);
                        ?>
                        <tr class="<?php echo $clase; ?>">
                            <td><?php echo $indice + 1; ?></td>
                            <td><?php echo limpiar($sensor); ?></td>
                            <td><?php echo limpiar($tipo); ?></td>
                            <td><?php echo limpiar($valor); ?></td>
                            <td class="estado"><?php echo limpiar($estado); ?></td>
                        </tr>
                    <?php endforeach; ?>
                    </tbody>
                </table>
            </section>
        <?php endif; ?>
    </main>
</body>
</html>