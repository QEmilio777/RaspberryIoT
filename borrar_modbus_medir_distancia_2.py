# este programa tiene el proposito de cambiar el estado del registro auto_mode
# el registro puede cambiar a manual como tambien automatico
# solo el como un simple toggle

from pymodbus.client import ModbusTcpClient
from time import sleep

IP = "192.168.6.30"
PORT = 502
UNIT_ID = 1

client = ModbusTcpClient(IP, port=PORT)
client.connect()

try:
    rr = client.read_holding_registers(address=2, count=1, device_id=UNIT_ID)
    auto_mode = rr.registers[0] if not rr.isError() else None
    print("Modo: " "Automatico" if auto_mode else "Manual")
    
    client.write_register(address=3, value=1, device_id=UNIT_ID)
    sleep(0.5)
    
    rr = client.write_register(address=2, count=1, device_id=UNIT_ID)
    auto_mode = rr.registers[0] if not rr.isError() else None
    print("Modo: " "Automatico" if auto_mode else "Manual")


except Exception as e:
    print("Errro: ", e)
finally:
    client.close()
    print("Programa finalizado")