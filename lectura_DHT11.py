# librerias
from pymodbus.client import ModbusTcpClient
import time
from datetime import datetime
import csv


# Datos para la conexion
IP = "192.168.214.30"
PORT = 502

#definir registros
REG_TEMP = 0;
REG_HUM = 1;

filename = "lectura_DHT.csv"
fields = ['Temperatura', 'Humedad', 'Fecha']

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("Conexion con el ESP-32 no establecida")
    exit()

print("Conexion establecida, leyendo cada 3 segundos\n")

try:
    
    while True:
        # leer los registros
        rr = client.read_holding_registers(REG_TEMP, count=2, device_id=1)
        
        if rr.isError():
            print("Error en la lectura")
        else:
            temp = rr.registers[0]
            hum = rr.registers[1]
            
            datos = [{
                "Temperatura": f"{temp/100.0:.2f}",
                "Humedad": f"{hum/100.0:.2f}",
                "Fecha":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },]
            
            print(f"Temperatura: {temp/100.0:.2f} || Humedad: {hum/100.0:.2f}")
            
            with open(filename, 'a') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)

                # writing headers (field names)
                # writer.writeheader()

                # writing data rows
                writer.writerows(datos)
        
        time.sleep(3)
            
            
        
except KeyboardInterrupt:
    print("Ctrl c ejecutado")
finally:
    client.close()
    print("Programa finalizado")
    