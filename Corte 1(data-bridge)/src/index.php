<?php
// index.php
// Interfaz principal del Sistema Smart Greenhouse.
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Smart Greenhouse - Búsqueda</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            padding: 20px;
        }

        .card {
            width: 100%;
            max-width: 720px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 22px;
            padding: 35px;
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
            text-align: center;
        }

        h1 {
            margin: 0 0 10px;
            font-size: 38px;
        }

        p {
            color: #d7fbe8;
            line-height: 1.6;
        }

        .formulario {
            margin-top: 25px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        input[type="text"] {
            flex: 1;
            min-width: 240px;
            padding: 15px;
            border: none;
            border-radius: 12px;
            font-size: 17px;
            outline: none;
        }

        button, .btn {
            padding: 15px 22px;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            cursor: pointer;
            background: #38ef7d;
            color: #062b16;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
        }

        button:hover, .btn:hover {
            background: #2fd46d;
        }

        .opciones {
            margin-top: 25px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .chip {
            background: rgba(255,255,255,0.18);
            border: 1px solid rgba(255,255,255,0.22);
            padding: 8px 12px;
            border-radius: 999px;
            color: white;
            text-decoration: none;
            font-size: 14px;
        }

        .acciones {
            margin-top: 25px;
        }

        @media (max-width: 600px) {
            h1 { font-size: 28px; }
            .formulario { flex-direction: column; }
        }
    </style>
</head>
<body>
    <main class="card">
        <h1>🌱 Smart Greenhouse</h1>
        <p>
            Sistema de monitoreo para invernadero inteligente.
            Busca datos por sensor, tipo de medición o estado operativo.
        </p>

        <form class="formulario" action="procesar.php" method="POST">
            <input
                type="text"
                name="criterio"
                placeholder="Ejemplo: A1, Temperatura, ON, OFF, Alerta..."
                required
            >
            <button type="submit">Buscar Datos</button>
        </form>

        <div class="opciones">
            <a class="chip" href="procesar.php?criterio=A1">Sensor A1</a>
            <a class="chip" href="procesar.php?criterio=Temperatura">Temperatura</a>
            <a class="chip" href="procesar.php?criterio=Humedad">Humedad</a>
            <a class="chip" href="procesar.php?criterio=NivelAgua">NivelAgua</a>
            <a class="chip" href="procesar.php?criterio=ON">ON</a>
            <a class="chip" href="procesar.php?criterio=OFF">OFF</a>
            <a class="chip" href="procesar.php?criterio=0%">0%</a>
        </div>

        <div class="acciones">
            <a class="btn" href="tabla.php">Ver últimos resultados</a>
        </div>
    </main>
</body>
</html>