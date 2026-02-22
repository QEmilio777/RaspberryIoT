from pymodbus.client import ModbusTcpClient
import time

IP = "192.168.6.30"
PORT = 502
UNIT_ID = 1 # cuando se trabaja con TCP es 1

client = ModbusTcpClient(IP, port=PORT)
client.connect()

try:
    rr = client.read_holding_registers(address=2, count=1, device_id=UNIT_ID)
    modo = rr.registers[0] if not rr.isError() else None
    print("Modo: ", "ATOMATICO" if modo == 1 else "MANUAL")
        
    client.write_register(address=4, value=1, device_id=UNIT_ID)
    time.sleep(.5)
        
    rr = client.read_holding_registers(address=2, count=1, device_id=UNIT_ID)
    modo = rr.registers[0] if not rr.isError() else None
    print("Modo: ", "ATOMATICO" if modo == 1 else "MANUAL")
except:
    print("Ocurrio un error")
finally:
    client.close