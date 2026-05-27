import network, urequests, time, machine, json, onewire, ds18x20

# 1. Cargar configuración desde config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# 2. Configurar hardware (sensor y relé)
ds_pin = machine.Pin(config['pines']['sensor_temperatura'])
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
rele = machine.Pin(config['pines']['rele_ventilador'], machine.Pin.OUT)

# 3. Conectar WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config['wifi_ssid'], config['wifi_pass'])
while not wlan.isconnected():
    print("Conectando WiFi...")
    time.sleep(1)
print("Conectado:", wlan.ifconfig())

# 4. Ciclo principal
while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        estado = "VENTILADOR ENCENDIDO" if temp > config['umbral_temp'] else "VENTILADOR APAGADO"
        rele.value(1 if estado == "VENTILADOR ENCENDIDO" else 0)

        # Preparar datos para enviar a guardar.php
        payload = {
            "sensor_id": config['sensor_id'],
            "temperatura": temp,
            "rele": estado,
            "umbral_config": config['umbral_temp']
        }

        try:
            # Mandar datos al servidor PHP
            res = urequests.post(
                "http://172.16.36.201/SALAS/Guardar_Datos.php",
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
            print("Respuesta servidor:", res.status_code)
            res.close()
        except Exception as e:
            print("Error red:", e)

    time.sleep(1)