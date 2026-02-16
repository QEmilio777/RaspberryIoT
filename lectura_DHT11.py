# librerias
from pymodbus.client import ModbusTcpClient
import time


# Datos para la conexion
IP = "192.168.173.30"
PORT = 502

#definir registros
REG_TEMP = 0;
REG_HUM = 1;

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("Conexion con el ESP-32 no establecida")
    exit()

print("Conexion establecida, leyendo cada 3 segundos\n")

try:
    
    while True:
        rr = client.read_holding_registers(REG_TEMP, count=2, device_id=1)
        
        if rr.isError():
            print("Error en la lectura")
        else:
            temp = rr.registers[0]
            hum = rr.registers[1]
            
            print(f"Temperatura: {temp/100.0:.2f} || Humedad: {hum/100.0:.2f}")
        
        time.sleep(3)
            
            
        
except KeyboardInterrupt:
    print("Ctrl c ejecutado")
finally:
    client.close()
    print("Programa finalizado")
    