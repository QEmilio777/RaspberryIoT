from pymodbus.client import ModbusTcpClient
import time

IP = "192.168.6.30"
PORT = 502
UNIT_ID = 1 # cuando se trabaja con TCP es 1

client = ModbusTcpClient(IP, port=PORT)
client.connect()

try:
    while True:
        rr = client.read_holding_registers(address=0, count=3, device_id=UNIT_ID)
        if rr.isError():
            print("Lectura erronea")
        else:
            dist_mm = rr.registers[0]
            relay_state = rr.registers[1]
            auto_mode = rr.registers[2]
            
            dist_cm = dist_mm / 10.
            modo = "AUTOMATICO" if auto_mode == 1 else "MANUAL"
            print(f"Distancia (cm) {dist_cm:6.1f} | Relevador:  {relay_state} | Modo: {modo}")
        
        time.sleep(.5)
except KeyboardInterrupt:
    print("Finalizado desde el teclado")
finally:
    client.close()
    print("Programa terminado")
            
