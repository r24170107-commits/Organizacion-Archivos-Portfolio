<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Proyecto Héctor</title>
    <!-- Librerías externas -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.rawgit.com/Mikhus/canvas-gauges/master/gauge.min.js"></script>
    
    <style>
        body { background:#2b2b2b; color:#d1d1d1; font-family:'Segoe UI'; text-align:center; }
        .panel { background:#3c3c3c; border:3px inset #555; padding:20px; display:inline-block; margin:10px; border-radius:5px; vertical-align:top; }
        .titulo-labview { color:#f1c40f; text-transform:uppercase; border-bottom:2px solid #f1c40f; padding:10px; margin-bottom:20px; }
        .display-digital { background:#000; color:#ff0000; font-family:'Courier New'; padding:10px; border:2px solid #555; font-size:2.5rem; margin-top:10px; }
        .status-rele { margin-top:15px; font-weight:bold; border:1px solid #555; padding:5px; }
        .fan { width:120px; height:120px; margin:20px auto; background:url("ventilador.png") no-repeat center; background-size:contain; }
        .fan.spin { animation: rotateFan 0.25s linear infinite; }
        @keyframes rotateFan { from { transform:rotate(0deg);} to { transform:rotate(360deg);} }
    </style>
</head>
<body>
    <h2 class="titulo-labview">Sistema de Temperatura</h2>

    <div style="display:flex; flex-wrap:wrap; justify-content:center;">
        <!-- Panel Temperatura -->
        <div class="panel">
            <h3>TEMPERATURA °C</h3>
            <canvas id="gauge-temp"></canvas>
            <div id="digital-reading" class="display-digital">00.00</div>
            <div id="rele-status" class="status-rele">Ventilador: <span id="rele-txt">---</span></div>
            <div id="ventilador" class="fan"></div>
        </div>

        <!-- Panel Historial -->
        <div class="panel">
            <h3>HISTORIAL</h3>
            <canvas id="trendChart" width="500" height="340"></canvas>
        </div>
    </div>

    <script>
        // Configuración del gauge
        var gauge = new RadialGauge({
            renderTo:'gauge-temp', width:300, height:300,
            units:"°C", minValue:0, maxValue:50,
            majorTicks:["0","5","10","15","20","25","30","35","40","45","50"],
            highlights:[{ "from":30, "to":50, "color":"rgba(200,50,50,.75)" }],
            colorPlate:"#222", colorNumbers:"#eee",
            needleType:"arrow", needleWidth:3,
            animationDuration:500, animationRule:"linear"
        }).draw();

        // Configuración de la gráfica
        const ctx = document.getElementById('trendChart').getContext('2d');
        const chart = new Chart(ctx, {
            type:'line',
            data:{ labels:[], datasets:[{ label:'Grafica', data:[], borderColor:'#f1c40f', backgroundColor:'rgba(241,196,15,0.1)', fill:true }] },
            options:{ responsive:false, scales:{ y:{ min:15, max:45, grid:{ color:"#555" } } } }
        });

        // Función para traer datos desde lecturas.php
        async function fetchData() {
            try {
                const response = await fetch('lecturas.php'); // PHP devuelve JSON
                const data = await response.json();
                if (data.length > 0) {
                    const latest = data[data.length - 1]; // último registro
                    const val = parseFloat(latest.temperatura);

                    // Actualizar gauge y display digital
                    gauge.value = val;
                    document.getElementById('digital-reading').innerText = val.toFixed(2);

                    // Actualizar estado del ventilador (más limpio)
                    const txtRele = document.getElementById('rele-txt');
                    if (latest.rele === "VENTILADOR ENCENDIDO") {
                        txtRele.innerText = "Encendido";
                        txtRele.style.color = "#2ecc71"; // verde
                    } else {
                        txtRele.innerText = "Apagado";
                        txtRele.style.color = "#e74c3c"; // rojo
                    }

                    // Animación del ventilador
                    const ventilador = document.getElementById('ventilador');
                    if (latest.rele === "VENTILADOR ENCENDIDO") { ventilador.classList.add("spin"); }
                    else { ventilador.classList.remove("spin"); }

                    // Actualizar gráfica
                    if (chart.data.labels.length > 15) {
                        chart.data.labels.shift();
                        chart.data.datasets[0].data.shift();
                    }
                    chart.data.labels.push(latest.fecha);
                    chart.data.datasets[0].data.push(val);
                    chart.update('none');
                }
            } catch (e) { console.log("Buscando datos..."); }
        }
        setInterval(fetchData, 1000); // actualizar cada segundo
    </script>
</body>
</html>