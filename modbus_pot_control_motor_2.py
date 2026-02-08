from pymodbus.client import ModbusTcpClient
import RPi.GPIO as GPIO
from time import sleep
import MCP3008_simple as MCP

pot_val = None

IP = "192.168.47.30"
PORT = 502
REG_NUM = 0

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("No hay conexión")
    exit()

print("Conexión establecida")
print("\nEste programa usa un pot para enviar pwm al esp-32\n")

try:
    while True:
        
        pot_val = MCP.getResult(0, 12)
        
        client.write_register(REG_NUM, pot_val)
        
except KeyboardInterrupt:
    print("Control C ejecutado")

finally:
    sleep(0.1)
    print("Fin del programa")
    client.write_register(REG_NUM, 0)
    client.close()