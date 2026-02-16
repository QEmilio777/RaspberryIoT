from pymodbus.client import ModbusTcpClient
import time


# datos del internet
IP = "192.168.173.30"
PORT = 502

# creacion del cliente
client = ModbusTcpClient(IP, port=PORT)

# variables del registro
HREG_TEMP = 0
HREG_HUM = 1

# verificar conexion del cliente
if not client.connect():
    print("Error en la conexion")
    exit()

print("Lectura de sensor cada 3 segundos\n")

try:
    while True:
        datos = client.read_holding_registers(HREG_TEMP, count=2, id=1)
        
        if datos.isError():
            print("Error en la lectura")
        else:
            temp = datos[0]
            hum = datos[1]
        
            print(f"Temperatura: {temp/100:.2f} || Humedad: {hum/100:.2f}")
        
        time.sleep(3)
        
        
except KeyboardInterrupt:
    print("Ctrl c ejecutado")
finally:
    client.close()
    print("Programa finalizado")