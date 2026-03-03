# este programa trae tres valores y los muestra en pantalla


from pymodbus.client import ModbusTcpClient
from time import sleep

IP = "192.168.6.30"
PORT = 502
UNIT_ID = 1

client = ModbusTcpClient(IP, port=PORT)
client.connect()

try:
    while True:
        rr = client.read_holding_registers(address=0, count=3, device_id=UNIT_ID)
        if rr.isError():
            print("Hubo un error")
        else:
            distancia_mm = rr.registers[0]
            relay_state = rr.registers[1]
            auto_mode = rr.registers[2]
            
            distancia_cm = f"{distancia_mm:6.2f}"
            modo = "Automatico" if auto_mode == 1 else "Manual"
            
            print(f"Distancia: {distancia_cm} | Estado: {relay_state} | Modo: {modo}")
        
        sleep(0.5)

except KeyboardInterrupt:
    print("\nCRTL c ejecutado\n")
finally:
    client.close()
    print("Programa finalizado")