from pymodbus.client import ModbusTcpClient
from time import sleep

IP = "192.168.214.78"
PORT = 502

temp_reg = 0
humid_reg = 1

UNIT_ID = 1

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("Error en la conexion en el puerto: " + IP)
    exit()

try:
    while True:
        rr = client.read_holding_registers(0, count=2, device_id=UNIT_ID)
        
        if rr.isError():
            print("Error en los datos")
        else:
            temp = rr.registers[0]
            humid = rr.registers[1]
            
            print(f"Temperatura: {temp / 100} || Humedad: {humid / 100}")
        
        sleep(3)


except KeyboardInterrupt:
    print("\nCTRL C ejecutado")
finally:
    client.close()
    print("Programa finalizado")